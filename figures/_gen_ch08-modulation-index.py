"""Generate figures/ch08-modulation-index.svg — FM carrier/sidebands vs index.

Canon (accuracy-canon §2.14, pool 2024–2028 subelement E8B):
- Modulation index = frequency deviation ÷ modulating frequency; the pool's
  two index calculations both key to 3: 3000/1000 = 3 (E8B03) and
  6000/2000 = 3 (E8B04). A phase-modulated emission's index does not depend
  on the RF carrier frequency (E8B02).
- Deviation ratio = MAXIMUM carrier deviation ÷ HIGHEST modulating frequency
  (the worst-case sibling of the index, E8B09): 5 kHz/3 kHz = 1.67 (E8B05)
  and 7.5 kHz/3.5 kHz = 2.14 (E8B06).
- Every calculation question offers the inverted ratio as a distractor —
  divide deviation BY modulating frequency, never the reverse (canon §2.14).
- The physics drawn here (single-tone FM line spectra, Bessel amplitudes
  J_n(index), significant sidebands reaching about ±(index+1)·f_mod) is
  standard FM theory, drawn at the pool's own values.

Single-color (black) on transparent, then post-processed:
#000000 -> currentColor, plus fill=currentColor seeded on the root <svg>
(series hardening: matplotlib emits glyph <use> elements and alpha patches
with no fill attribute, which otherwise silently inherit SVG initial black).
"""

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from scipy.special import jv

INK = "black"

fig = plt.figure(figsize=(7.8, 9.2))
gs = fig.add_gridspec(2, 1, height_ratios=[1.12, 1.0], hspace=0.50,
                      top=0.875, bottom=0.20, left=0.105, right=0.965)

fig.suptitle("FM Modulation Index — Where the Carrier's Power Goes",
             fontsize=14, fontweight="bold", color=INK, y=0.970)
fig.text(0.5, 0.938, "index = deviation ÷ modulating frequency"
         " · deviation ratio = the worst-case version",
         fontsize=10.5, color=INK, ha="center")

# ---- panel A: Bessel amplitudes vs modulation index -------------------------
a = fig.add_subplot(gs[0])

beta = np.linspace(0, 4.3, 500)
styles = [
    (0, dict(linewidth=2.4, linestyle="solid")),
    (1, dict(linewidth=1.8, linestyle=(0, (6, 3)))),
    (2, dict(linewidth=1.8, linestyle=(0, (6, 2, 1.5, 2)))),
    (3, dict(linewidth=2.2, linestyle=(0, (1.5, 2)))),
    (4, dict(linewidth=1.2, linestyle="solid")),
]
for n, kw in styles:
    a.plot(beta, jv(n, beta), color=INK, **kw)

a.set_xlim(0, 4.3)
a.set_ylim(-0.55, 1.05)
a.axhline(0, color=INK, linewidth=0.8, alpha=0.45)

# direct curve labels (positions verified against the rendered PNG)
a.annotate("carrier J₀", xy=(0.90, 0.94), fontsize=9, color=INK,
           ha="center", fontweight="bold")
a.annotate("1st sideband pair J₁", xy=(1.22, 0.60), fontsize=9, color=INK,
           ha="center")
a.annotate("2nd pair J₂", xy=(3.38, 0.53), fontsize=9, color=INK,
           ha="center")
a.annotate("3rd pair J₃", xy=(3.98, 0.485), fontsize=9, color=INK,
           ha="center")
a.annotate("4th pair J₄", xy=(4.02, 0.205), fontsize=9, color=INK,
           ha="center")

# the pool's values
for x, lab in [(1.67, "1.67"), (2.14, "2.14"), (3.0, "3")]:
    a.axvline(x, color=INK, linewidth=1.1, linestyle=(0, (4, 3)), alpha=0.75)
    a.annotate(lab, xy=(x, 0.985), fontsize=9, fontweight="bold", color=INK,
               ha="center", va="top")

a.set_xlabel("modulation index", fontsize=9.5, color=INK)
a.set_ylabel("relative amplitude", fontsize=9.5, color=INK)
a.set_title("carrier and sideband-pair amplitudes vs index"
            " — the pool's numbers dashed", fontsize=11, color=INK)
a.grid(True, which="major", color=INK, alpha=0.15, linewidth=0.7)
for side in ("top", "right"):
    a.spines[side].set_visible(False)
for side in ("left", "bottom"):
    a.spines[side].set_color(INK)
a.tick_params(colors=INK, labelsize=9)

# ---- panel B: the line spectrum at index 3 ----------------------------------
b = fig.add_subplot(gs[1])

n = np.arange(-5, 6)
amp = np.abs(jv(n, 3.0))
b.vlines(n, 0, amp, color=INK, linewidth=1.8)
b.plot(n, amp, "o", color=INK, markersize=4.5)
b.axhline(0, color=INK, linewidth=1.0)

for ni, ai in zip(n, amp):
    if ni == 0:
        b.annotate("carrier: 0.26", xy=(ni, ai + 0.022), fontsize=8,
                   fontweight="bold", color=INK, ha="center")
    else:
        b.annotate(f"{ai:.2f}", xy=(ni, ai + 0.022), fontsize=7.5, color=INK,
                   ha="center")

b.set_xlim(-5.7, 5.7)
b.set_ylim(0, 0.72)
b.set_xticks([-4, -2, 0, 2, 4])
b.set_xticklabels(["fc − 4fm", "fc − 2fm", "fc", "fc + 2fm", "fc + 4fm"])

# spacing dimension between adjacent lines
b.annotate("", xy=(1, 0.575), xytext=(0, 0.575),
           arrowprops=dict(arrowstyle="<->", color=INK, lw=1.1))
b.annotate("line spacing = f_mod", xy=(0.5, 0.585), fontsize=8.5, color=INK,
           ha="center", va="bottom")
# significant-sideband reach
b.annotate("", xy=(4, 0.665), xytext=(-4, 0.665),
           arrowprops=dict(arrowstyle="<->", color=INK, lw=1.1))
b.annotate("the significant sidebands reach about ±(index + 1) · f_mod",
           xy=(0, 0.675), fontsize=8.5, color=INK, ha="center", va="bottom")

b.set_xlabel("spectrum lines at fc ± n·fm — spaced by the modulating"
             " frequency", fontsize=9, color=INK)
b.set_ylabel("relative amplitude", fontsize=9.5, color=INK)
b.set_title("the spectrum at index 3 — both pool index calculations"
            " land here", fontsize=11, color=INK)
b.grid(True, which="major", axis="y", color=INK, alpha=0.15, linewidth=0.7)
for side in ("top", "right"):
    b.spines[side].set_visible(False)
for side in ("left", "bottom"):
    b.spines[side].set_color(INK)
b.tick_params(colors=INK, labelsize=9)

# ---- footers: the pool's arithmetic (kept short enough to fit the width) -----
fig.text(0.5, 0.128, "modulation index = deviation ÷ modulating frequency"
         " — E8B03: 3000 ÷ 1000 = 3 · E8B04: 6000 ÷ 2000 = 3",
         fontsize=8.5, color=INK, ha="center", va="bottom")
fig.text(0.5, 0.105, "deviation ratio = MAXIMUM deviation ÷ HIGHEST"
         " modulating frequency (E8B09)",
         fontsize=8.5, color=INK, ha="center", va="bottom")
fig.text(0.5, 0.082, "pool: E8B05 = 5 kHz ÷ 3 kHz = 1.67 · E8B06 = 7.5"
         " kHz ÷ 3.5 kHz = 2.14",
         fontsize=8.5, color=INK, ha="center", va="bottom")
fig.text(0.5, 0.059, "the inverted ratio is always a distractor — divide"
         " deviation BY the modulating frequency, never the reverse",
         fontsize=8.5, color=INK, ha="center", va="bottom")
fig.text(0.5, 0.036, "a phase-modulated emission's index does not depend on"
         " the RF carrier frequency (E8B02)",
         fontsize=8.5, color=INK, ha="center", va="bottom")
fig.text(0.5, 0.013, "amplitudes are Bessel Jn(index) — a negative carrier"
         " lobe is a phase reversal; power is the square",
         fontsize=8.5, color=INK, ha="center", va="bottom")

out = "figures/ch08-modulation-index.svg"
fig.savefig(out, transparent=True)

# theme-able: black -> currentColor; seed fill=currentColor at the root so
# fill-less glyph <use> elements inherit the theme color instead of black.
with open(out, encoding="utf-8") as fh:
    svg = fh.read()
svg = svg.replace("#000000", "currentColor")
svg = svg.replace("<svg xmlns:xlink", '<svg fill="currentColor" xmlns:xlink', 1)
with open(out, "w", encoding="utf-8") as fh:
    fh.write(svg)
print("wrote", out)
print("index-3 amplitudes |J_n(3)|, n=0..5:",
      " ".join(f"{abs(jv(i, 3.0)):.4f}" for i in range(6)))
