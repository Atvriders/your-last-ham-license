"""Generate figures/ch07-active-filters.svg — active filter responses vs passive shapes.

Canon (accuracy-canon 2.13, pool 2024-2028 subelements E7C and E7G):
- Book 3 (General) showed the passive shapes; the Extra adds active filters
  built around op-amps: gain in the passband, sharper skirts (each reactive
  section adds 6 dB/octave, so a two-pole active stage rolls off at
  40 dB/decade where a passive RC manages 20), and Q-controlled peaking at
  the corner. Three panels: low-pass, high-pass, band-pass, each with the
  passive prototype against two active 2nd-order stages (Q = 0.7, flat;
  Q = 4, peaking).
- Pool anchors in the footer: the filter-family ladder Butterworth
  (maximally flat) / Chebyshev (passband ripple, sharper) / elliptical
  (sharpest, stop-band notches) — E7C05/E7C06; shape factor measures
  adjacent-channel rejection (E7C11); a capacitor across RF in Figure E7-3
  turns the inverting stage into a low-pass (E7G02).

Shapes (r = f/f0, all normalized to unity reference so the shapes compare):
- passive LP/HP: first-order RC, 20 dB/decade skirts, -3 dB at r = 1.
- active 2nd-order LP: |H| = 1/sqrt((1-r^2)^2 + (r/Q)^2)  (peaks for Q > 0.707)
- active 2nd-order HP: |H| = r^2/sqrt((1-r^2)^2 + (r/Q)^2)
- active 2nd-order BP: |H| = (r/Q)/sqrt((1-r^2)^2 + (r/Q)^2) (0 dB peak, BW = f0/Q)
- passive BP: single-tuned hump |H| = 1/sqrt(1 + (Q*u)^2), u = r - 1/r, Q = 2.

Single-color (black) matplotlib output on a transparent background, then
post-processed: #000000 -> currentColor, plus fill="currentColor" seeded on
the root <svg> so no glyph can silently inherit SVG-initial black
(established series pattern from Books 2 and 3, hardened here).
"""

import re

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

INK = "black"

r = np.logspace(-1, 1, 4000)          # f/f0 from 0.1 to 10
u = r - 1.0 / r                        # normalized detuning (band-pass panel)

def db(x):
    return 20 * np.log10(x)

# curve definitions -------------------------------------------------------
Q_FLAT, Q_PEAK, Q_PASS_BP = 0.7, 4.0, 2.0

passive_lp = 1.0 / np.sqrt(1 + r ** 2)
passive_hp = r / np.sqrt(1 + r ** 2)
passive_bp = 1.0 / np.sqrt(1 + (Q_PASS_BP * u) ** 2)

def active_lp(Q):
    return 1.0 / np.sqrt((1 - r ** 2) ** 2 + (r / Q) ** 2)

def active_hp(Q):
    return r ** 2 / np.sqrt((1 - r ** 2) ** 2 + (r / Q) ** 2)

def active_bp(Q):
    return (r / Q) / np.sqrt((1 - r ** 2) ** 2 + (r / Q) ** 2)

PANELS = [
    ("LOW-PASS", passive_lp, active_lp, None),
    ("HIGH-PASS", passive_hp, active_hp,
     "mirror image of the low-pass"),
    ("BAND-PASS", passive_bp, active_bp,
     "higher Q, narrower window: BW = $f_0$/Q"),
]

STYLES = [
    ("passive (Book 3 basics)", (0, (2, 2.5)), 1.7),
    ("active, Q = 0.7 (flat)", (0, (6, 2, 1.5, 2)), 1.8),
    ("active, Q = 4 (peaking)", "solid", 2.5),
]

fig, axes = plt.subplots(1, 3, figsize=(9.6, 4.3), sharey=True)

for ax, (name, pas, act, note) in zip(axes, PANELS):
    curves = [pas, act(Q_FLAT), act(Q_PEAK)]
    for (label, ls, lw), y in zip(STYLES, curves):
        ax.semilogx(r, db(y), color=INK, linewidth=lw, linestyle=ls,
                    solid_capstyle="round", label=label)
    ax.axhline(-3.01, color=INK, linewidth=0.9, linestyle=(0, (2, 3)), alpha=0.5)
    ax.axhline(0, color=INK, linewidth=0.9, linestyle=(0, (2, 3)), alpha=0.5)
    ax.axvline(1, color=INK, linewidth=0.9, linestyle=(0, (2, 3)), alpha=0.5)
    ax.set_xlim(0.1, 10)
    ax.set_ylim(-46, 20)
    ax.set_xticks([0.1, 0.5, 1, 2, 10])
    ax.set_xticklabels(["0.1", "0.5", "1", "2", "10"])
    ax.set_title(name, fontsize=12, fontweight="bold", color=INK)
    ax.set_xlabel("frequency  $f/f_0$", fontsize=10, color=INK)
    for side in ("top", "right"):
        ax.spines[side].set_visible(False)
    for side in ("left", "bottom"):
        ax.spines[side].set_color(INK)
    ax.tick_params(colors=INK, labelsize=9)
    ax.grid(axis="y", color=INK, alpha=0.12, linewidth=0.7)
    if note is not None:
        ax.text(0.115, 17.8, note, fontsize=8.5, color=INK, va="top")

axes[0].set_ylabel("relative response (dB)", fontsize=10, color=INK)
axes[0].text(0.62, -2.6, "0 dB", fontsize=8.5, color=INK)
axes[0].text(0.62, -6.0, "\u22123 dB", fontsize=8.5, color=INK)

# peaking callouts
axes[0].annotate("peaking: Q lifts the corner above 0 dB",
                 xy=(0.97, 12.5), xytext=(0.115, 14.6), fontsize=8.5, color=INK,
                 arrowprops=dict(arrowstyle="->", color=INK, lw=1.0))
axes[0].annotate("passive RC:\ngentle skirt", xy=(3.2, -20.4), xytext=(0.28, -33),
                 fontsize=8.5, color=INK,
                 arrowprops=dict(arrowstyle="->", color=INK, lw=1.0))
axes[0].annotate("active: 40 dB/decade,\ntwice the skirt", xy=(3.05, -31.5),
                 xytext=(1.6, -44), fontsize=8.5, color=INK,
                 arrowprops=dict(arrowstyle="->", color=INK, lw=1.0))
axes[2].annotate("passive single-tuned:\nbroad hump", xy=(0.55, -9.6),
                 xytext=(0.13, -33), fontsize=8.5, color=INK,
                 arrowprops=dict(arrowstyle="->", color=INK, lw=1.0))

handles, labels = axes[0].get_legend_handles_labels()
fig.legend(handles, labels, loc="upper center", ncol=3, fontsize=9.5,
           frameon=False, bbox_to_anchor=(0.5, 0.995))

fig.suptitle("Active Filters — Gain, Sharper Skirts, and Q Peaking vs the Passive Shapes",
             fontsize=13.5, fontweight="bold", color=INK, y=1.04)

fig.text(0.5, -0.035,
         "the pool's filter ladder: Butterworth = maximally flat (E7C05) \u00b7 "
         "Chebyshev = passband ripple, sharper cutoff \u00b7 elliptical = sharpest + "
         "stop-band notches (E7C06)\nshape factor measures adjacent-channel "
         "rejection (E7C11) \u00b7 a capacitor across $R_F$ in Figure E7-3 makes a "
         "low-pass (E7G02) \u00b7 curves normalized so the shapes compare",
         fontsize=8.5, color=INK, ha="center", va="top", style="italic")

fig.tight_layout(rect=[0, 0.02, 1, 0.93])

out = "figures/ch07-active-filters.svg"
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
