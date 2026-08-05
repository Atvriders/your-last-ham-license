"""Generate figures/ch01-extra-band-chart.svg — Amateur Extra HF privileges by band.

All edges come from this book's accuracy canon §2.1 / §2.2 / §7.1 (pinned
values only, ITU Region 2, §97.301(b) current text, emissions §97.305(c)(3)):
- 80/75 m: 3.500-3.600 CW+data, 3.600-4.000 phone+CW; Extra-only slices
  3.500-3.525 and 3.600-3.800 (canon §2.1 exact edges)
- 60 m: two parts per canon §7.1 — contiguous 5351.5-5366.5 kHz @ 9.15 W ERP
  plus four channels 5332/5348/5373/5405 kHz @ 100 W ERP, <= 2.8 kHz
  (identical for General)
- 40 m: 7.000-7.125 CW+data, 7.125-7.300 phone+CW; Extra-only slices
  7.000-7.025 and 7.125-7.175
- 30 m: 10.100-10.150 MHz, CW+data only, 200 W PEP (§97.313(c)(1)) —
  identical for General
- 20 m: 14.000-14.150 CW+data, 14.150-14.350 phone+CW; Extra-only slices
  14.000-14.025 and 14.150-14.225
- 17 m: 18.068-18.168 MHz entire band; 15 m: 21.000-21.200 CW+data and
  21.200-21.450 phone+CW, Extra-only slices 21.000-21.025 and 21.200-21.275
- 12 m: 24.890-24.990 MHz entire band; 10 m: 28.0-28.3 CW+data, 28.3-29.7
  phone+CW — 17, 12, and 10 m are identical for General
- 1.5 kW PEP elsewhere (§97.313(b)); CW permitted on every authorized
  frequency (§97.305(a)).
- VHF/UHF: all amateur bands 50 MHz and above, unchanged (§97.301(a)).

Each row is its own schematic bar (rows are NOT on a shared frequency axis);
numbers are printed on the segments. Hatched = CW + data, filled = phone +
CW, thick-outlined darker slice = Extra-only (General stops short), with the
exact slice edges printed in bold. Single-color (black) matplotlib output on
a transparent background, then post-processed: every #000000 becomes
currentColor (established pattern from the series' figures/_gen_*.py).
"""

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

W, H = 100.0, 108.0
BX0, BX1 = 17.0, 84.0          # bar region
BAR_H = 3.4

fig = plt.figure(figsize=(8.0, 8.64))
ax = fig.add_axes([0, 0, 1, 1])
ax.set_xlim(0, W)
ax.set_ylim(0, H)
ax.axis("off")

INK = "black"


def xpos(frac):
    return BX0 + frac * (BX1 - BX0)


def seg(f0, f1, y, kind):
    x0, x1 = xpos(f0), xpos(f1)
    if kind == "cw":
        ax.add_patch(Rectangle((x0, y - BAR_H / 2), x1 - x0, BAR_H,
                               fill=False, edgecolor=INK, hatch="////",
                               linewidth=1.2))
    else:  # phone (+CW)
        ax.add_patch(Rectangle((x0, y - BAR_H / 2), x1 - x0, BAR_H,
                               facecolor=INK, alpha=0.28, edgecolor=INK,
                               linewidth=1.4))


def extra_slice(f0, f1, y, label, ha="center"):
    """Extra-only slice: darker overlay + thick outline + bold edge label."""
    x0, x1 = xpos(f0), xpos(f1)
    ax.add_patch(Rectangle((x0, y - BAR_H / 2), x1 - x0, BAR_H,
                           facecolor=INK, alpha=0.18, edgecolor=INK,
                           linewidth=2.4))
    lx = x0 if ha == "left" else (x0 + x1) / 2
    ax.text(lx, y - 3.2, label, fontsize=7.2, fontweight="bold", ha=ha,
            va="center", color=INK)


def band(y, name, freq):
    ax.text(1.5, y, name, fontsize=11.5, fontweight="bold", ha="left",
            va="center", color=INK)
    ax.text(1.5, y - 3.5, freq, fontsize=7.4, ha="left", va="center",
            color=INK)


def mode(frac, y, label, fs=8.0):
    ax.text(xpos(frac), y + 2.6, label, fontsize=fs, ha="center",
            va="center", color=INK)


def edge(frac, y, label, ha="center"):
    ax.text(xpos(frac), y - 3.2, label, fontsize=7.2, ha=ha, va="center",
            color=INK)


def power(y, text, fs=8.0, bold=False):
    ax.text(86.0, y, text, fontsize=fs, fontweight=("bold" if bold else
            "normal"), ha="left", va="center", color=INK)


# ---- title ---------------------------------------------------------------
ax.text(50, 105, "AMATEUR EXTRA HF PRIVILEGES AT A GLANCE", fontsize=14.5,
        fontweight="bold", ha="center", va="center", color=INK)
ax.text(50, 101.6, "ITU Region 2 — segments per §97.301(b) / §97.305(c)(3), "
        "power per §97.313", fontsize=8.5, ha="center", va="center",
        color=INK)
ax.text(86.0, 99.0, "MAX POWER", fontsize=7, fontweight="bold", ha="left",
        va="center", color=INK)

# ---- 80/75 m -------------------------------------------------------------
y = 95.0
band(y, "80/75 m", "3.5–4.0 MHz band")
seg(0.0, 0.20, y, "cw")          # 3.500-3.600
seg(0.20, 1.00, y, "phone")      # 3.600-4.000
extra_slice(0.0, 0.05, y, "3.500–3.525", ha="left")
extra_slice(0.20, 0.60, y, "3.600–3.800")
mode(0.125, y, "CW + data", fs=7.5)
mode(0.80, y, "phone + CW")
edge(1.0, y, "4.000 MHz", ha="right")
power(y, "1.5 kW PEP")

# ---- 60 m (two parts, canon §7.1 — same as General) ----------------------
y = 86.0
band(y, "60 m", "5.3 MHz · same as General")
seg(0.0, 0.52, y, "phone")
mode(0.26, y, "USB phone · CW · data ≤ 2.8 kHz", fs=7.5)
edge(0.26, y, "5351.5–5366.5 kHz · 9.15 W ERP")
for f in (0.62, 0.72, 0.82, 0.92):
    ax.add_patch(Rectangle((xpos(f) - 1.0, y - BAR_H / 2), 2.0, BAR_H,
                           facecolor=INK, alpha=0.28, edgecolor=INK,
                           linewidth=1.4))
mode(0.77, y, "4 channels", fs=7.5)
edge(0.77, y, "5332 · 5348 · 5373 · 5405 kHz · 100 W ERP")
power(y + 1.4, "9.15 W ERP", fs=7.5)
power(y - 1.8, "100 W ERP", fs=7.5)

# ---- 40 m ----------------------------------------------------------------
y = 77.0
band(y, "40 m", "7.0–7.3 MHz band")
seg(0.0, 5 / 12, y, "cw")        # 7.000-7.125
seg(5 / 12, 1.0, y, "phone")     # 7.125-7.300
extra_slice(0.0, 1 / 12, y, "7.000–7.025", ha="left")
extra_slice(5 / 12, 7 / 12, y, "7.125–7.175")
mode(0.25, y, "CW + data")
mode(0.79, y, "phone + CW")
edge(1.0, y, "7.300 MHz", ha="right")
power(y, "1.5 kW PEP")

# ---- 30 m — THE 200 W PEP band (same as General) --------------------------
y = 68.0
band(y, "30 m", "10.100–10.150 MHz")
seg(0.0, 1.0, y, "cw")
mode(0.5, y, "CW + data only — no phone, no image")
edge(0.5, y, "same as General")
ax.add_patch(Rectangle((84.8, y - 2.8), 14.4, 5.6, fill=False,
                       edgecolor=INK, linewidth=1.4))
ax.text(92.0, y, "200 W PEP", fontsize=8, fontweight="bold", ha="center",
        va="center", color=INK)

# ---- 20 m ----------------------------------------------------------------
y = 59.0
band(y, "20 m", "14.0–14.35 MHz band")
seg(0.0, 6 / 14, y, "cw")        # 14.000-14.150
seg(6 / 14, 1.0, y, "phone")     # 14.150-14.350
extra_slice(0.0, 1 / 14, y, "14.000–14.025", ha="left")
extra_slice(6 / 14, 9 / 14, y, "14.150–14.225")
mode(0.25, y, "CW + data")
mode(0.82, y, "phone + CW")
edge(1.0, y, "14.350 MHz", ha="right")
power(y, "1.5 kW PEP")

# ---- 17 m (same as General) ----------------------------------------------
y = 50.0
band(y, "17 m", "18.068–18.168 MHz")
seg(0.0, 1.0, y, "phone")
mode(0.5, y, "CW + phone + data — entire band")
edge(0.5, y, "same as General")
power(y, "1.5 kW PEP")

# ---- 15 m ----------------------------------------------------------------
y = 41.0
band(y, "15 m", "21.0–21.45 MHz band")
seg(0.0, 8 / 18, y, "cw")        # 21.000-21.200
seg(8 / 18, 1.0, y, "phone")     # 21.200-21.450
extra_slice(0.0, 1 / 18, y, "21.000–21.025", ha="left")
extra_slice(8 / 18, 11 / 18, y, "21.200–21.275")
mode(0.25, y, "CW + data")
mode(0.80, y, "phone + CW")
edge(1.0, y, "21.450 MHz", ha="right")
power(y, "1.5 kW PEP")

# ---- 12 m (same as General) ----------------------------------------------
y = 32.0
band(y, "12 m", "24.890–24.990 MHz")
seg(0.0, 1.0, y, "phone")
mode(0.5, y, "CW + phone + data — entire band")
edge(0.5, y, "same as General")
power(y, "1.5 kW PEP")

# ---- 10 m (same as General) ----------------------------------------------
y = 23.0
band(y, "10 m", "28.0–29.7 MHz band")
seg(0.0, 0.3 / 1.7, y, "cw")     # 28.0-28.3
seg(0.3 / 1.7, 1.0, y, "phone")  # 28.3-29.7
mode(0.088, y, "CW + data", fs=7.5)
mode(0.59, y, "phone + CW")
edge(0.088, y, "28.0–28.3")
edge(0.59, y, "28.3–29.7 MHz · same as General")
power(y, "1.5 kW PEP")

# ---- VHF/UHF unchanged ----------------------------------------------------
y = 14.0
band(y, "VHF/UHF", "50 MHz and up")
ax.add_patch(Rectangle((BX0, y - BAR_H / 2), BX1 - BX0, BAR_H,
                       fill=False, edgecolor=INK, linewidth=1.6))
mode(0.5, y, "all bands · all modes — unchanged from General and Technician")
edge(0.5, y, "6 m · 2 m · 1.25 m · 70 cm · and all higher allocations")
power(y, "1.5 kW PEP")

# ---- legend ----------------------------------------------------------------
ly = 4.2
ax.add_patch(Rectangle((13, ly - 1.1), 4.2, 2.4, fill=False, edgecolor=INK,
                       hatch="////", linewidth=1.0))
ax.text(18.3, ly, "CW + data", fontsize=7.5, ha="left", va="center",
        color=INK)
ax.add_patch(Rectangle((30, ly - 1.1), 4.2, 2.4, facecolor=INK, alpha=0.28,
                       edgecolor=INK, linewidth=1.2))
ax.text(35.3, ly, "phone + CW", fontsize=7.5, ha="left", va="center",
        color=INK)
ax.add_patch(Rectangle((50, ly - 1.1), 4.2, 2.4, facecolor=INK, alpha=0.18,
                       edgecolor=INK, linewidth=2.2))
ax.text(55.3, ly, "Extra-only slice — General stops short (bold edges)",
        fontsize=7.5, ha="left", va="center", color=INK)
ax.text(50, 1.4, "CW is permitted on every authorized frequency "
        "(§97.305(a)) · rows are schematic, not to scale", fontsize=7.5,
        ha="center", va="center", style="italic", color=INK)

out = "figures/ch01-extra-band-chart.svg"
fig.savefig(out, transparent=True, bbox_inches="tight", pad_inches=0.05)

# theme-able: black -> currentColor; matplotlib emits glyph <use> elements
# and alpha patches with no fill attribute at all (they silently inherit the
# SVG initial black), so also seed fill=currentColor at the root — explicit
# fills (none, url(#hatch)) still override the inheritance.
with open(out, encoding="utf-8") as fh:
    svg = fh.read()
svg = svg.replace("#000000", "currentColor")
svg = svg.replace("<svg xmlns:xlink", '<svg fill="currentColor" xmlns:xlink', 1)
with open(out, "w", encoding="utf-8") as fh:
    fh.write(svg)
print("wrote", out)
