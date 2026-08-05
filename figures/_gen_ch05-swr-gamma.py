"""Generate figures/ch05-swr-gamma.svg — SWR and return loss vs |Gamma|.

Canon (accuracy-canon 2.11 and the E5 math set, pool 2024-2028):
- Gamma = (Z_L - Z_0)/(Z_L + Z_0); |Gamma| = sqrt(P_refl/P_fwd);
  SWR = (1 + |Gamma|)/(1 - |Gamma|); return loss = -20*log10|Gamma|.
- The marked pool point (E4B06's wattmeter numbers, via E4B04's
  S11<->VSWR equivalence): 100 W forward, 25 W reflected ->
  |Gamma| = sqrt(25/100) = 0.5 -> SWR = 3:1 and return loss ~= 6.0 dB.
- Landmark: |Gamma| = 1/3 -> SWR = 2:1 (the classic tuner threshold).

Left axis SWR (linear 1-10), right axis return loss in dB, both against
|Gamma| so the return-loss connection is visible on the same readout.

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

g = np.linspace(0.005, 0.849, 2000)
swr = (1 + g) / (1 - g)
rl = -20 * np.log10(g)

fig, ax = plt.subplots(figsize=(8.6, 5.2))
ax2 = ax.twinx()

# SWR curve (solid, left axis) and return loss (dashed, right axis)
ax.plot(g, swr, color=INK, linewidth=2.4, solid_capstyle="round")
ax2.plot(g, rl, color=INK, linewidth=2.0, linestyle=(0, (5, 3)),
         solid_capstyle="round")

# the pool point: |Gamma| = 0.5 -> SWR 3:1, return loss ~6 dB; the dashed
# return-loss curve passes through the very same dot (RL(0.5) = 6.02 dB)
ax.plot([0.5, 0.5], [1, 3], color=INK, linewidth=1.0,
        linestyle=(0, (2, 3)), alpha=0.55)
ax.plot([0, 0.5], [3, 3], color=INK, linewidth=1.0,
        linestyle=(0, (2, 3)), alpha=0.55)
ax.plot([0.5], [3], marker="o", markersize=7, color=INK)
ax.annotate("pool point: $|\\Gamma| = \\sqrt{25\\,\\mathrm{W}/100\\,"
            "\\mathrm{W}} = 0.5$\nSWR = $(1+|\\Gamma|)/(1-|\\Gamma|) = 3:1$\n"
            "return loss $= -20\\log_{10}|\\Gamma| \\approx 6$ dB\n"
            "— one dot on both curves",
            xy=(0.5, 3), xytext=(0.755, 8.3), fontsize=10.5, color=INK,
            ha="right", va="center",
            arrowprops=dict(arrowstyle="->", color=INK, lw=1.1))

# 2:1 landmark at |Gamma| = 1/3
ax.plot([1/3], [2], marker="o", markersize=6, color=INK)
ax.annotate("2:1 at $|\\Gamma| = 1/3$ — the classic\n"
            "\u201cgood enough\u201d tuner threshold",
            xy=(1/3, 2), xytext=(0.38, 1.55), fontsize=10, color=INK,
            ha="left",
            arrowprops=dict(arrowstyle="->", color=INK, lw=1.1))

# 1:1 at the origin
ax.plot([0], [1], marker="o", markersize=6, color=INK)
ax.annotate("perfect match: $\\Gamma = 0$ \u2192 1:1", xy=(0, 1),
            xytext=(0.045, 1.3), fontsize=10, color=INK,
            arrowprops=dict(arrowstyle="->", color=INK, lw=1.1))

ax2.text(0.135, 15.5, "return loss (dB)", fontsize=10, color=INK,
         ha="left", rotation=-38)

ax.set_xlim(0, 0.85)
ax.set_ylim(1, 10)
ax2.set_ylim(0, 27)
ax.set_xlabel("magnitude of the reflection coefficient $|\\Gamma|$",
              fontsize=10.5, color=INK)
ax.set_ylabel("SWR ($n$:1)", fontsize=10.5, color=INK)
ax2.set_ylabel("return loss (dB)", fontsize=10.5, color=INK)
ax.set_title("SWR $= (1+|\\Gamma|)\\,/\\,(1-|\\Gamma|)$ — and Its"
             " Return-Loss Twin", fontsize=14, fontweight="bold",
             color=INK, pad=10)

for side in ("top",):
    ax.spines[side].set_visible(False)
for side in ("left", "bottom", "right"):
    ax.spines[side].set_color(INK)
ax.tick_params(colors=INK, labelsize=9.5)
ax2.tick_params(colors=INK, labelsize=9.5)
ax.grid(axis="y", color=INK, alpha=0.15, linewidth=0.7)

fig.text(0.5, 0.018,
         "$\\Gamma = (Z_L - Z_0)\\,/\\,(Z_L + Z_0)$ \u00b7 "
         "$|\\Gamma| = \\sqrt{P_{refl}/P_{fwd}}$ — E4B06\u2019s wattmeter"
         " numbers drive the marked point",
         fontsize=9.5, color=INK, ha="center", va="bottom", style="italic")

fig.tight_layout(rect=[0, 0.045, 1, 1])

out = "figures/ch05-swr-gamma.svg"
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
