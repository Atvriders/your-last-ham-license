"""Generate figures/ch05-q-bandwidth.svg — half-power bandwidth BW = f0/Q.

Canon (accuracy-canon 2.11, pool 2024-2028 subelement E5A):
- BW = f0/Q. Pool worked values: E5A11 7.1 MHz/150 = 47.3 kHz; E5A12
  3.7 MHz/118 = 31.4 kHz. Drawn here at one shared f0 = 3.56 MHz (E5A02's
  own resonance, 50 uH + 40 pF), so the same law shows three Qs side by
  side: Q = 35.6 -> 100 kHz, Q = 75.3 -> 47.3 kHz, Q = 113.4 -> 31.4 kHz.
  Higher Q, narrower passband — Q is selectivity.

Curve: single-tuned-circuit relative response |H| = 1/sqrt(1 + (Q*u)^2)
with u = f/f0 - f0/f, in dB. The -3 dB (half-power) points sit at Q*u = +/-1,
so the -3 dB width is exactly f0/Q.

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

F0 = 3.56e6                       # E5A02: 50 uH + 40 pF -> 3.56 MHz
off = np.linspace(-62e3, 62e3, 4000)
f = F0 + off
u = f / F0 - F0 / f               # normalized detuning

# (Q, BW label, linestyle, linewidth) — BW = f0/Q exactly at the -3 dB points
CURVES = [
    (35.6, "100 kHz", (0, (6, 2, 1.5, 2)), 1.8),
    (75.3, "47.3 kHz", (0, (5, 3)), 2.0),
    (113.4, "31.4 kHz", "solid", 2.4),
]

fig, ax = plt.subplots(figsize=(8.6, 5.4))

for Q, bw, ls, lw in CURVES:
    ax.plot(off / 1e3, 20 * np.log10(1.0 / np.sqrt(1 + (Q * u) ** 2)),
            color=INK, linewidth=lw, linestyle=ls, solid_capstyle="round")

# half-power reference and f0 marker
ax.axhline(-3.01, color=INK, linewidth=1.0, linestyle=(0, (2, 3)), alpha=0.55)
ax.text(-61, -0.5, "half power (\u22123 dB)", fontsize=9.5, color=INK)
ax.text(0.8, 0.4, "$f_0$ = 3.56 MHz", fontsize=10, color=INK)

# width double-arrows at staggered heights, each spanning its -3 dB width
ax.annotate("", xy=(50, -5.2), xytext=(-50, -5.2),
            arrowprops=dict(arrowstyle="<->", color=INK, lw=1.3))
ax.text(53.5, -5.2, "BW = 100 kHz \u00b7 Q = 35.6", fontsize=10, color=INK,
        va="center")
for Q, bw, y in ((75.3, "47.3 kHz", -8.6), (113.4, "31.4 kHz", -12.0)):
    half = (F0 / Q) / 2 / 1e3     # kHz
    ax.annotate("", xy=(half, y), xytext=(-half, y),
                arrowprops=dict(arrowstyle="<->", color=INK, lw=1.3))
    ax.text(0, y - 1.6, f"BW = {bw} \u00b7 Q = {Q}", fontsize=10, color=INK,
            ha="center", va="top")

ax.annotate("higher Q, narrower passband —\nthe same $f_0$, a tighter window",
            xy=(20, -17), xytext=(30, -20), fontsize=10, color=INK,
            arrowprops=dict(arrowstyle="->", color=INK, lw=1.1))
ax.annotate("lower Q, wider passband", xy=(-48, -6.5), xytext=(-61, -16),
            fontsize=10, color=INK,
            arrowprops=dict(arrowstyle="->", color=INK, lw=1.1))

ax.set_xlim(-62, 62)
ax.set_ylim(-26, 2)
ax.set_xlabel("frequency offset from $f_0$ (kHz)", fontsize=10.5, color=INK)
ax.set_ylabel("relative response (dB)", fontsize=10.5, color=INK)
ax.set_title("Bandwidth $= f_0/Q$ — Same Resonance, Different Q",
             fontsize=14, fontweight="bold", color=INK, pad=10)

for side in ("top", "right"):
    ax.spines[side].set_visible(False)
for side in ("left", "bottom"):
    ax.spines[side].set_color(INK)
ax.tick_params(colors=INK, labelsize=9.5)
ax.grid(axis="y", color=INK, alpha=0.15, linewidth=0.7)

fig.text(0.5, 0.018,
         "the pool\u2019s own computations: E5A11: 7.1 MHz/150 = 47.3 kHz \u00b7 "
         "E5A12: 3.7 MHz/118 = 31.4 kHz \u00b7 drawn at E5A02\u2019s $f_0$ = 3.56 MHz",
         fontsize=9, color=INK, ha="center", va="bottom", style="italic")

fig.tight_layout(rect=[0, 0.05, 1, 1])

out = "figures/ch05-q-bandwidth.svg"
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
