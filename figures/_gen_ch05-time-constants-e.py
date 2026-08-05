"""Generate figures/ch05-time-constants-e.svg — RC/RL charge & discharge.

Canon (accuracy-canon 2.11, pool 2024-2028 subelement E5B):
- One time constant tau = R*C (or L/R): a capacitor charges to 63.2% of the
  applied voltage, or discharges to 36.8% of its initial voltage, in one
  tau (E5B01). By 5 tau it is 99.3% — called fully charged.
- E5B04's worked value: two paralleled 220 uF = 440 uF, two paralleled
  1 Mohm = 500 kohm, tau = 440 uF x 500 kohm = 220 s. The top axis is
  scaled in seconds for exactly that circuit, so the 63.2% point lands at
  220 s.

Charge V = Vs*(1 - e^(-t/tau)); discharge V = V0*e^(-t/tau).

Single-color (black) matplotlib output on a transparent background, then
post-processed: #000000 -> currentColor, plus fill="currentColor" seeded on
the root <svg> so no glyph can silently inherit SVG-initial black.
"""

import re

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

INK = "black"
TAU_S = 220.0                     # E5B04: 440 uF x 500 kohm

t = np.linspace(0, 5, 2000)       # in units of tau

fig, ax = plt.subplots(figsize=(8.6, 5.2))

ax.plot(t, 100 * (1 - np.exp(-t)), color=INK, linewidth=2.4,
        solid_capstyle="round")
ax.plot(t, 100 * np.exp(-t), color=INK, linewidth=2.2,
        linestyle=(0, (5, 3)), solid_capstyle="round")

# the one-tau crosshairs and the two keyed percentages
ax.axvline(1, color=INK, linewidth=1.0, linestyle=(0, (2, 3)), alpha=0.55)
ax.plot([0, 1], [63.2, 63.2], color=INK, linewidth=1.0,
        linestyle=(0, (2, 3)), alpha=0.55)
ax.plot([0, 1], [36.8, 36.8], color=INK, linewidth=1.0,
        linestyle=(0, (2, 3)), alpha=0.55)
ax.plot([1, 1], [63.2, 36.8], marker="o", markersize=7, color=INK)

ax.annotate("charging: 63.2% of the source\nvoltage after one $\\tau$",
            xy=(1, 63.2), xytext=(2.3, 66), fontsize=10.5, color=INK,
            arrowprops=dict(arrowstyle="->", color=INK, lw=1.1))
ax.annotate("discharging: 36.8% of the initial\nvoltage remains after one $\\tau$",
            xy=(1, 36.8), xytext=(1.6, 47), fontsize=10.5, color=INK,
            arrowprops=dict(arrowstyle="->", color=INK, lw=1.1))
ax.text(1, 29.5, "$1\\tau$", fontsize=10.5, color=INK, ha="center")

# 5 tau: practically full
ax.plot([5], [100 * (1 - np.exp(-5))], marker="o", markersize=6, color=INK)
ax.annotate("99.3% at $5\\tau$ — called full", xy=(5, 99.3),
            xytext=(3.35, 92), fontsize=10, color=INK,
            arrowprops=dict(arrowstyle="->", color=INK, lw=1.1))

ax.text(3.3, 80, "charge: $V = V_S\\,(1 - e^{-t/\\tau})$", fontsize=10.5,
        color=INK, ha="center")
ax.text(2.6, 18, "discharge: $V = V_0\\,e^{-t/\\tau}$", fontsize=10.5,
        color=INK, ha="center")

ax.set_xlim(0, 5.15)
ax.set_ylim(0, 108)
ax.set_xticks([0, 1, 2, 3, 4, 5])
ax.set_xticklabels(["0", "$1\\tau$", "$2\\tau$", "$3\\tau$", "$4\\tau$",
                    "$5\\tau$"])
ax.set_xlabel("time in time constants ($\\tau = R \\times C$, or $L/R$)",
              fontsize=10.5, color=INK)
ax.set_ylabel("% of source / initial voltage", fontsize=10.5, color=INK)
ax.set_title("One Time Constant: 63.2% Charged, 36.8% Remaining",
             fontsize=14, fontweight="bold", color=INK, pad=34)

# top axis: seconds for E5B04's exact circuit (tau = 220 s)
top = ax.secondary_xaxis("top", functions=(lambda x: x * TAU_S,
                                           lambda x: x / TAU_S))
top.set_xticks([0, 220, 440, 660, 880, 1100])
top.set_xlabel("seconds for E5B04\u2019s circuit: 440 \u00b5F \u00d7 500 k\u03a9"
               " \u2192 $\\tau$ = 220 s", fontsize=9.5, color=INK)
top.tick_params(colors=INK, labelsize=9)

for side in ("left", "bottom"):
    ax.spines[side].set_color(INK)
ax.tick_params(colors=INK, labelsize=9.5)
ax.grid(axis="y", color=INK, alpha=0.15, linewidth=0.7)

fig.tight_layout()

out = "figures/ch05-time-constants-e.svg"
fig.savefig(out, transparent=True, bbox_inches="tight")

# theme-able: black -> currentColor, and seed the root <svg> fill so no
# glyph silently inherits SVG-initial black
with open(out, encoding="utf-8") as fh:
    svg = fh.read()
svg = svg.replace("#000000", "currentColor")
svg = re.sub(r"<svg ", '<svg fill="currentColor" ', svg, count=1)
with open(out, "w", encoding="utf-8") as fh:
    fh.write(svg)
print("wrote", out)
