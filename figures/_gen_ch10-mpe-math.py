"""Generate figures/ch10-mpe-math.svg — MPE limits, duty factor, and the averaging window.

Canon (accuracy-canon §2.16, pool 2024–2028 subelement E0A):
- FCC MPE limits are most restrictive over 30–300 MHz — the body-resonance
  region (E0A03); a neighbor's home is general-population territory, so the
  UNCONTROLLED limits apply there (E0A02); below 300 MHz separate E- and
  H-field limits exist (E0A06), plotted here as equivalent power density.
- The pool requires NO MPE computation — all 12 E0A questions are
  conceptual/regulatory. The S = ERP/(4πR²) illustration is enrichment
  (research note r4 §E0A) and the figure says so.
- Limit values per FCC OET Bulletin 65 (the canon's own source for E0A):
  uncontrolled 100 mW/cm² below 1.34 MHz, 180/f² (f in MHz) 1.34–30 MHz,
  0.2 flat 30–300 MHz, f/1500 300–1500 MHz, 1.0 above 1500 MHz; controlled
  runs 5× higher (900/f² over 3–30 MHz, 1.0 flat 30–300 MHz, f/300
  300–1500 MHz, 5.0 above 1500 MHz).
- Worked enrichment example (r4 §E0A; units and window resolved per
  accuracy-canon §7.12): 100 W ERP at 10 m gives
  S = 100/(4π·10²) ≈ 0.08 W/m² peak (= 0.008 mW/cm² — the mW/cm² form is
  10× smaller; the draft's "0.08 mW/cm²" was a unit error). With
  series-typical duty factors (SSB voice ≈ 0.2 while keyed, key down half
  the window — Book 3 ch10) the window average is 10 % of peak:
  ≈ 0.008 W/m². The 2 W/m² (= 0.2 mW/cm²) uncontrolled floor that applies
  on 2 meters sits ≈ 25× above the peak (≈ 250× above the average).
- Averaging windows per OET 65: 6 minutes CONTROLLED, 30 minutes
  UNCONTROLLED. This scenario is the neighbor's lot line — uncontrolled
  (E0A02) — so panel B spans one 30-minute window (canon §7.12).

Single-color (black) on transparent, then post-processed:
#000000 -> currentColor (established book pattern).
"""

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
import numpy as np

INK = "black"

fig = plt.figure(figsize=(7.6, 7.6))
gs = fig.add_gridspec(2, 1, height_ratios=[1.15, 1.0], hspace=0.55,
                      top=0.878, bottom=0.135, left=0.11, right=0.97)

fig.suptitle("MPE Math at Depth: The Limit Curve, Duty, and the Average",
             fontsize=14, fontweight="bold", color=INK, y=0.972)
fig.text(0.5, 0.938, "FCC exposure limits by band — and why duty factor rescues the average",
         fontsize=10.5, color=INK, ha="center")

# ---- panel A: the MPE limit curves ----------------------------------------
a = fig.add_subplot(gs[0])

def mpe_uncontrolled(f):
    f = np.asarray(f, dtype=float)
    return np.piecewise(f, [f < 1.34, (f >= 1.34) & (f < 30),
                            (f >= 30) & (f < 300), (f >= 300) & (f < 1500),
                            f >= 1500],
                        [100.0, lambda x: 180.0 / x**2, 0.2,
                         lambda x: x / 1500.0, 1.0])

def mpe_controlled(f):
    f = np.asarray(f, dtype=float)
    return np.piecewise(f, [f < 3, (f >= 3) & (f < 30), (f >= 30) & (f < 300),
                            (f >= 300) & (f < 1500), f >= 1500],
                        [100.0, lambda x: 900.0 / x**2, 1.0,
                         lambda x: x / 300.0, 5.0])

segs = [np.logspace(np.log10(lo), np.log10(hi), 60)
        for lo, hi in [(1, 1.34), (1.34, 30), (30, 300), (300, 1500), (1500, 3000)]]
for s in segs:
    a.plot(s, mpe_uncontrolled(s), color=INK, linewidth=2.5)
    a.plot(s, mpe_controlled(s), color=INK, linewidth=1.6, linestyle=(0, (5, 3)))

a.set_xscale("log")
a.set_yscale("log")
a.set_xlim(1, 3000)
a.set_ylim(0.08, 300)
a.set_xticks([1, 10, 100, 1000])
a.set_xticklabels(["1", "10", "100", "1,000"])
a.set_yticks([0.1, 1, 10, 100])
a.set_yticklabels(["0.1", "1", "10", "100"])

# the most-restrictive span (capped so the legend clears it)
a.axvspan(30, 300, color=INK, alpha=0.08, ymax=0.84)
a.annotate("MOST RESTRICTIVE\n30–300 MHz — the body-resonance region",
           xy=(95, 20), fontsize=9.5, fontweight="bold", color=INK,
           ha="center", va="center")

# amateur-band markers on the uncontrolled curve
bands = [(1.9, "160 m"), (3.7, "80 m"), (7.15, "40 m"), (14.2, "20 m"),
         (28.5, "10 m"), (52, "6 m"), (146, "2 m"), (440, "70 cm"),
         (1270, "23 cm")]
for i, (f, lab) in enumerate(bands):
    a.plot([f], [mpe_uncontrolled(f)], marker="o", markersize=4.5,
           color=INK, zorder=5)
    if i == 0:  # 160 m: label right of the dot, clear of the 100-flat line
        a.annotate(lab, xy=(f, mpe_uncontrolled(f)), xytext=(9, -3),
                   textcoords="offset points", fontsize=8, color=INK, ha="left")
    else:
        a.annotate(lab, xy=(f, mpe_uncontrolled(f)),
                   xytext=(0, 6 if i % 2 == 0 else 13),
                   textcoords="offset points", fontsize=8, color=INK,
                   ha="center")

# curve legend, clear of the band markers
handles = [Line2D([0], [0], color=INK, linewidth=2.5,
                  label="uncontrolled (general population)"),
           Line2D([0], [0], color=INK, linewidth=1.6, linestyle=(0, (5, 3)),
                  label="controlled")]
a.legend(handles=handles, loc="upper right", frameon=False, fontsize=9)

a.set_xlabel("frequency (MHz) — amateur bands marked", fontsize=9.5, color=INK)
a.set_ylabel("MPE limit (mW/cm²)", fontsize=9.5, color=INK)
a.set_title("the limits dip where the body absorbs RF best",
            fontsize=11, color=INK)
a.grid(True, which="major", color=INK, alpha=0.15, linewidth=0.7)
for side in ("top", "right"):
    a.spines[side].set_visible(False)
for side in ("left", "bottom"):
    a.spines[side].set_color(INK)
a.tick_params(colors=INK, labelsize=9)
a.text(0.02, 0.058, "uncontrolled = the limit that applies at a neighbor's home",
       transform=a.transAxes, fontsize=8, color=INK, va="bottom")
a.text(0.02, 0.018, "below 300 MHz the FCC also sets separate E- and H-field"
       " limits (plotted as equivalent power density)",
       transform=a.transAxes, fontsize=8, color=INK, va="bottom")

# ---- panel B: duty factor and the averaging window -------------------------
b = fig.add_subplot(gs[1])
b.set_yscale("log")
b.set_xlim(0, 30)
b.set_ylim(0.001, 5)
b.set_xticks([0, 7.5, 15, 22.5, 30])
b.set_xticklabels(["0", "7.5", "15", "22.5", "30"])

# the example station: 100 W ERP at 10 m → 0.08 W/m² peak; keyed SSB voice
b.plot([0, 30], [0.0012, 0.0012], color=INK, linewidth=1, alpha=0.4)
for t0, t1 in [(0, 7.5), (15, 22.5)]:
    b.plot([t0, t1], [0.016, 0.016], color=INK, linewidth=9,
           solid_capstyle="butt")
b.annotate("key down: 0.08 peak × 0.2 speech duty ≈ 0.016",
           xy=(0.75, 0.024), fontsize=8.5, color=INK, ha="left")

# the window average vs the limit
b.axhline(0.008, color=INK, linewidth=1.5, linestyle=(0, (5, 3)))
b.annotate("window average ≈ 0.008", xy=(8.5, 0.0105), fontsize=8.5,
           color=INK, ha="left")
b.axhline(2.0, color=INK, linewidth=2)
b.text(0.02, 0.868, "MPE limit (uncontrolled, 30–300 MHz): 2 W/m² (= 0.2 mW/cm²)",
       transform=b.transAxes, fontsize=8.5, color=INK, ha="left", va="top")
b.annotate("", xy=(26.5, 2.0), xytext=(26.5, 0.08),
           arrowprops=dict(arrowstyle="<->", color=INK, lw=1.3))
b.annotate("≈ 25×\nheadroom\n(peak)", xy=(27.3, 0.4), fontsize=9, color=INK,
           ha="left", va="center")

b.set_xlabel("one 30-minute averaging window (minutes) — uncontrolled, as at the lot line", fontsize=9.5, color=INK)
b.set_ylabel("power density (W/m²)", fontsize=9.5, color=INK)
b.set_title("the limit is judged against the time AVERAGE, not the peaks",
            fontsize=11, color=INK)
b.grid(True, which="major", axis="y", color=INK, alpha=0.15, linewidth=0.7)
for side in ("top", "right"):
    b.spines[side].set_visible(False)
for side in ("left", "bottom"):
    b.spines[side].set_color(INK)
b.tick_params(colors=INK, labelsize=9)
b.text(0.02, 0.965, "worked example: 100 W ERP on 2 m, 10 m away —"
       " peak S = ERP/(4πR²) ≈ 0.08 W/m² (0.008 mW/cm²)",
       transform=b.transAxes, fontsize=8.5, color=INK, va="top")

fig.text(0.5, 0.052, "Enrichment beyond the exam — every pool E0A question"
         " is conceptual; no MPE math is required.",
         fontsize=8.5, color=INK, ha="center", va="bottom")
fig.text(0.5, 0.02, "Limits per FCC OET Bulletin 65; duty factors"
         " series-typical (SSB ≈ 0.2 keyed, key down half the window).",
         fontsize=8.5, color=INK, ha="center", va="bottom")

out = "figures/ch10-mpe-math.svg"
fig.savefig(out, transparent=True)

# theme-able: black -> currentColor
with open(out, encoding="utf-8") as fh:
    svg = fh.read()
svg = svg.replace("#000000", "currentColor")
with open(out, "w", encoding="utf-8") as fh:
    fh.write(svg)
print("wrote", out)
