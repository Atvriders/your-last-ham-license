"""Generate figures/ch08-sampling-aliasing.svg — Nyquist and aliasing.

Canon (accuracy-canon §2.14, pool 2024–2028 subelement E8A):
- The DAC output low-pass filter removes spurious sampling artifacts
  (E8A10) — the same copy-removal idea drawn here, in reverse.
- Flash (direct) converters serve SDRs because their very high speed allows
  digitizing high frequencies (E8A08).
- The Nyquist criterion itself (sample faster than twice the highest
  frequency, else the spectral copies overlap and fold back as aliases) is
  the standard teaching frame for those facts. The numbers on the axes
  (fs = 48 kHz, a 20 kHz / 30 kHz band, a tone folding 30 -> 18 kHz) are a
  worked teaching example, not pool values.

Single-color (black) on transparent, then post-processed:
#000000 -> currentColor, plus fill=currentColor seeded on the root <svg>
(series hardening: matplotlib emits glyph <use> elements and alpha patches
with no fill attribute, which otherwise silently inherit SVG initial black).
"""

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

INK = "black"

FS = 48.0          # sample rate (kHz) — teaching example
F_LO = 1.0         # band edge low (kHz)


def bump(f, f_lo, f_hi):
    """Smooth band-limited spectrum shape: sin^2 bump over [f_lo, f_hi]."""
    f = np.asarray(f, dtype=float)
    out = np.zeros_like(f)
    m = (f >= f_lo) & (f <= f_hi)
    out[m] = np.sin(np.pi * (f[m] - f_lo) / (f_hi - f_lo)) ** 2
    return out


f = np.linspace(0, 100, 4000)

fig = plt.figure(figsize=(7.8, 8.4))
gs = fig.add_gridspec(2, 1, height_ratios=[1, 1.12], hspace=0.55,
                      top=0.88, bottom=0.185, left=0.095, right=0.965)

fig.suptitle("Sampling and Nyquist — Sample Fast, or the Signal Folds Back",
             fontsize=14, fontweight="bold", color=INK, y=0.972)
fig.text(0.5, 0.938, "sampling copies the spectrum around every multiple"
         " of fs — at least twice the highest frequency",
         fontsize=10.5, color=INK, ha="center")


def style_axis(ax):
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 1.55)
    ax.set_xticks([0, 12, 24, 36, 48, 60, 72, 84, 96])
    ax.set_yticks([])
    for side in ("top", "right", "left"):
        ax.spines[side].set_visible(False)
    ax.spines["bottom"].set_color(INK)
    ax.tick_params(colors=INK, labelsize=9)
    ax.grid(True, which="major", axis="x", color=INK, alpha=0.12,
            linewidth=0.7)


# ---- panel A: sampled fast enough -------------------------------------------
a = fig.add_subplot(gs[0])

sig_a = bump(f, F_LO, 20)
a.fill_between(f, 0, sig_a, color=INK, alpha=0.22, linewidth=0)
a.plot(f, sig_a, color=INK, linewidth=2.2)

# copies around fs and 2fs — mirrored pairs make a bump on each side of n*fs
copy1 = bump(f, FS - 20, FS - F_LO) + bump(f, FS + F_LO, FS + 20)
copy2 = bump(f, 2 * FS - 20, 2 * FS - F_LO) + bump(f, 2 * FS + F_LO, 2 * FS + 20)
a.fill_between(f, 0, copy1, color=INK, alpha=0.10, linewidth=0)
a.plot(f, copy1, color=INK, linewidth=1.3, linestyle=(0, (5, 3)))
a.fill_between(f, 0, copy2, color=INK, alpha=0.10, linewidth=0)
a.plot(f, copy2, color=INK, linewidth=1.3, linestyle=(0, (5, 3)))

a.axvline(FS / 2, color=INK, linewidth=1.8)
a.axvline(FS, color=INK, linewidth=1.2, linestyle=(0, (4, 3)))
a.axvline(2 * FS, color=INK, linewidth=1.2, linestyle=(0, (4, 3)))

a.annotate("fs ÷ 2 = 24 kHz\nthe Nyquist limit", xy=(FS / 2, 1.48),
           fontsize=9, fontweight="bold", color=INK, ha="center", va="top")
a.annotate("sample rate\nfs = 48 kHz", xy=(FS, 1.48), fontsize=9,
           color=INK, ha="center", va="top")
a.annotate("2fs", xy=(2 * FS, 1.48), fontsize=9, color=INK, ha="center",
           va="top")

a.annotate("the signal: band-limited to 20 kHz", xy=(2, 1.07), fontsize=9,
           color=INK, ha="left", va="bottom")
a.annotate("the copies sit far away —\na low-pass filter lifts the original"
           " out", xy=(72, 1.26), fontsize=9, color=INK, ha="center",
           va="top")

a.set_ylabel("amplitude", fontsize=9.5, color=INK)
a.set_title("sampled right: fs = 48 kHz against a 20 kHz band"
            " — the copies stay clear", fontsize=11, color=INK)
style_axis(a)

# ---- panel B: sampled too slow — the fold-back -------------------------------
b = fig.add_subplot(gs[1])

sig_b = bump(f, F_LO, 30)
b.fill_between(f, 0, sig_b, color=INK, alpha=0.22, linewidth=0)
b.plot(f, sig_b, color=INK, linewidth=2.2)

# copy around fs now overlaps the baseband
copy_b = bump(f, FS - 30, FS - F_LO) + bump(f, FS + F_LO, FS + 30)
b.fill_between(f, 0, copy_b, color=INK, alpha=0.10, linewidth=0)
b.plot(f, copy_b, color=INK, linewidth=1.3, linestyle=(0, (5, 3)))

# overlap region: the copy reaches back inside the band (18–30 kHz)
overlap = np.minimum(sig_b, copy_b)
b.fill_between(f, 0, overlap, where=(overlap > 1e-3), color=INK, alpha=0.45,
               linewidth=0)
b.annotate("the copy folds back\nINSIDE the band", xy=(34, 0.06),
           fontsize=8.5, color=INK, ha="left", va="bottom", fontweight="bold")
b.annotate("", xy=(26.5, 0.05), xytext=(34, 0.14),
           arrowprops=dict(arrowstyle="->", color=INK, lw=1.0))

b.axvline(FS / 2, color=INK, linewidth=1.8)
b.annotate("fs ÷ 2 = 24 kHz", xy=(FS / 2, 1.48), fontsize=9,
           fontweight="bold", color=INK, ha="center", va="top")
b.annotate("anti-alias filter", xy=(10, 1.22), fontsize=8.5,
           fontstyle="italic", color=INK, ha="center", va="bottom")

# a discrete tone above fs/2 and its alias
b.vlines(30, 0, 0.82, color=INK, linewidth=2.0)
b.plot([30], [0.82], "o", color=INK, markersize=4.5)
b.annotate("a tone at 30 kHz", xy=(38, 1.30), fontsize=9, color=INK,
           ha="left", va="center")
b.annotate("", xy=(30.5, 0.87), xytext=(39, 1.24),
           arrowprops=dict(arrowstyle="->", color=INK, lw=1.0))
b.vlines(18, 0, 0.82, color=INK, linewidth=2.0, linestyle=(0, (4, 3)))
b.plot([18], [0.82], "o", color=INK, markersize=4.5, fillstyle="none")
b.annotate("alias: 48 − 30 = 18 kHz", xy=(2, 1.04), fontsize=9, color=INK,
           ha="left", va="bottom")
b.annotate("", xy=(17.8, 0.885), xytext=(14, 0.96),
           arrowprops=dict(arrowstyle="->", color=INK, lw=1.0))
b.annotate("", xy=(18.6, 0.70), xytext=(29.4, 0.70),
           arrowprops=dict(arrowstyle="->", color=INK, lw=1.3,
                           connectionstyle="arc3,rad=0.25"))

# the anti-alias filter: flat to 20 kHz, skirt to zero by fs/2
filt = np.piecewise(f, [f <= 20, (f > 20) & (f < FS / 2), f >= FS / 2],
                    [1.0, lambda x: (FS / 2 - x) / (FS / 2 - 20), 0.0])
b.plot(f, 1.20 * filt, color=INK, linewidth=1.6, linestyle=(0, (7, 3)))
b.annotate("the fix: an anti-alias filter BEFORE the sampler —\n"
           "cut everything above fs ÷ 2 first; after sampling,\n"
           "an alias can never be filtered out again",
           xy=(54, 1.05), fontsize=8.5, color=INK, ha="left", va="bottom")

b.set_xlabel("frequency (kHz) — worked example, fs = 48 kHz",
             fontsize=9.5, color=INK)
b.set_ylabel("amplitude", fontsize=9.5, color=INK)
b.set_title("sampled too slow: the copy folds back below fs ÷ 2"
            " — that is aliasing", fontsize=11, color=INK)
style_axis(b)

# ---- footers: the canon tie-in (kept short enough to fit the width) ----------
fig.text(0.5, 0.098, "Nyquist: sample at least twice the highest"
         " frequency — anything above fs ÷ 2 folds back into the band",
         fontsize=8.5, color=INK, ha="center", va="bottom")
fig.text(0.5, 0.074, "the anti-alias filter only works BEFORE sampling —"
         " afterward, signal and alias are inseparable",
         fontsize=8.5, color=INK, ha="center", va="bottom")
fig.text(0.5, 0.050, "after a DAC the same idea runs in reverse: the output"
         " low-pass removes spurious sampling artifacts (pool E8A10)",
         fontsize=8.5, color=INK, ha="center", va="bottom")
fig.text(0.5, 0.026, "flash (direct) converters serve SDRs because their"
         " very high speed digitizes high frequencies (E8A08)",
         fontsize=8.5, color=INK, ha="center", va="bottom")

out = "figures/ch08-sampling-aliasing.svg"
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
