# Figure Plan — Your Last Ham License (Extra)

39 figures: 29 originals + 10 pool-figure redraws. Canon is law (`accuracy-canon.md`); redraws follow canon §1.4's binding specs.

## Conventions (binding — identical to the series)

- **Themeable:** `currentColor` for strokes/fills/text; no hardcoded black/white; transparent background; `viewBox`; legible at ~600–800 px.
- **Hand-authored SVG** for diagrams/schematics; **matplotlib→SVG** for plots/grids (generator at `figures/_gen_<id>.py`, black→`currentColor` post-process).
- Ground symbols in redraws: three slanted strokes of decreasing length (canon §1.4 style).
- Metadata: `figures/fragments/<id>.json` — exactly `{"id", "chapter": <INT 0–10>, "caption", "kind": "original", "source", "spoken"}`; redraws carry `source: "redrawn from NCVEC pool figure E#-#"`.
- Pool-facing numbers from canon/pool only. Numbering by **first-reference order** per chapter.
- Self-check: XML-parse, chrome-headless render to PNG, view with ReadMediaFile, fix defects. **Every redraw additionally: side-by-side content comparison against the official figure (files in `canon/source/`) and a per-question cross-check** (each keyed answer's component/point sits where your figure puts it).

## Original figures

| # | id | ch | type | content |
|---|---|---|---|---|
| 1 | ch00-what-extra-opens | 00 | SVG | General vs Extra: the Extra-only HF slices lighting up (80/75, 40, 20, 15 m) + "everything else" note |
| 2 | ch00-upgrade-journey-ae | 00 | SVG | Pass Element 4 → CSCE + Form 605 → operate immediately signing /AE (§97.9(b) + §97.119(f)(3)) → ULS shows Extra → drop /AE |
| 3 | ch01-extra-band-chart | 01 | plot | Extra privileges by band with the Extra-only slices distinct vs General (canon §2.1 exact edges) |
| 4 | ch01-cept-carry | 01 | SVG | CEPT operating: the three documents to carry (license, passport, FCC public notice) + full-privileges note for Extra/Advanced |
| 5 | ch02-satellite-modes | 02 | SVG | Satellite mode designators: uplink band letter FIRST, downlink second (V/U/L/S/X per canon); one worked example |
| 6 | ch02-linear-transponder | 02 | SVG | Linear (bent-pipe) transponder: uplink passband → downlink passband; inverting vs non-inverting; Doppler on both legs |
| 7 | ch02-eme-path | 02 | SVG | Earth-Moon-Earth: stations, ~2.5 s round-trip delay, huge path loss (~252 dB), antenna gain + low noise as the answer |
| 8 | ch03-aurora-geometry | 03 | SVG | Auroral propagation: station beams NORTH at the auroral curtain, signal scattered back; fluttery CW/SSB quality note |
| 9 | ch03-meteor-scatter | 03 | SVG | Meteor scatter: meteor trail ionization, brief pings/bursts on a timeline, MSK144's fast handshake riding them |
| 10 | ch03-transequatorial | 03 | SVG | Transequatorial (TE): north-south paths crossing the geomagnetic equator, afternoon/evening enhancement, long reach |
| 11 | ch03-ducting | 03 | SVG | Tropospheric ducting: inversion layer traps VHF/UHF, long over-water/over-land paths, "lift" weather |
| 12 | ch04-receiver-performance | 04 | SVG | Receiver performance trio: sensitivity (MDS), dynamic range (IMD3/free of overload), selectivity — what each number means |
| 13 | ch04-link-budget | 04 | SVG | Link budget chain: TX power → gains → path loss → RX sensitivity, margin; dB arithmetic on a real pool example |
| 13a | ch04-noise-cascade | 04 | SVG | Receiver noise chain: antenna noise, preamp gain/NF, first stage sets system noise figure (Friis concept, no derivation) |
| 14 | ch05-complex-plane | 05 | SVG | Rectangular/polar complex impedance: 50 − j25 → 55.9∠−26.6° worked example (pool value); j-operator rotation |
| 15 | ch05-q-bandwidth | 05 | plot | Resonance BW = f₀/Q: same f₀, several Q curves; pool worked numbers (3.56 MHz, 47.3 kHz) |
| 16 | ch05-time-constants-e | 05 | plot | RC/RL charge/discharge with 63.2%/36.8% at 1τ and the pool's specific percentages/values |
| 17 | ch05-swr-gamma | 05 | plot | Reflection coefficient Γ vs load; SWR = (1+|Γ|)/(1−|Γ|) curve with the Γ=0.5 → 3:1 pool point |
| 18 | ch06-depletion-region | 06 | SVG | PN junction: depletion region, forward/reverse bias at the physics level the pool tests |
| 19 | ch07-active-filters | 07 | plot | Active filter responses: Sallen-Key-style LP/HP/BP with Q/peaking vs the passive shapes from Book 3 |
| 20 | ch07-pll-block | 07 | SVG | PLL: reference → phase detector → loop filter → VCO → ÷N feedback → out; DDS contrast note |
| 21 | ch07-sdr-iq | 07 | SVG | SDR architecture: antenna → LNA → quadrature mixers (I/Q) → ADC → DSP; sampling/aliasing note |
| 22 | ch08-modulation-index | 08 | plot | FM modulation index/deviation visual: carrier + sidebands vs index; the pool's index values marked |
| 23 | ch08-sampling-aliasing | 08 | plot | Sampling & Nyquist: signal, sample rate, aliased fold-back below Nyquist/2 |
| 24 | ch08-spread-spectrum | 08 | SVG | Spread spectrum: DSSS (code spreading) vs FHSS (hopping) concept panels |
| 25 | ch09-stub-matching | 09 | SVG | Matching with lines: λ/4 transformer (Z' = Z₀²/Z) + open/shorted stubs as reactances; worked pool numbers |
| 26 | ch09-phased-array | 09 | SVG | Phased verticals: two elements, drive phase, pattern steering concept |
| 27 | ch09-eirp-erp-chain | 09 | SVG | ERP/EIRP chain: TX power − line loss × antenna gain (dBd vs dBi) → ERP/EIRP; pool worked values |
| 28 | ch10-mpe-math | 10 | plot | MPE evaluation at depth: power × duty × averaging vs MPE limits curve (30–300 MHz most restrictive) |

## Pool-figure redraws (canon §1.4 binding specs; official files in `canon/source/`)

| # | id | ch | figure | questions |
|---|---|---|---|---|
| 29 | ch05-pool-fig-e51 | 05 | E5-1 impedance-coordinate chart (axes ±600 Ω, points P1–P8) | E5C10–E5C12 |
| 30 | ch06-pool-fig-e61 | 06 | E6-1: six FET symbols | E6A10, E6A11 |
| 31 | ch06-pool-fig-e62 | 06 | E6-2: eight diode symbols | E6B10 |
| 32 | ch06-pool-fig-e63 | 06 | E6-3: six logic gates | E6C08, E6C10, E6C11 |
| 33 | ch07-pool-fig-e71 | 07 | E7-1: common-emitter NPN bias (R1–R4) | E7B10–E7B12 |
| 34 | ch07-pool-fig-e72 | 07 | E7-2: linear regulator (Q1, D1, C2) | E7D06–E7D08 |
| 35 | ch07-pool-fig-e73 | 07 | E7-3: inverting op-amp (gain = −R_F/R_1) | E7G02, E7G07, E7G09–E7G11 |
| 36 | ch09-pool-fig-e91 | 09 | E9-1: azimuth "Free-Space Pattern" polar plot | E9B01–E9B03 |
| 37 | ch09-pool-fig-e92 | 09 | E9-2: elevation "Over Real Ground" semicircle | E9B04–E9B06 |
| 38 | ch09-pool-fig-e93 | 09 | E9-3: **Smith chart, infinity RIGHT** (rotated per errata #1; no wavelength scales) | E9G06, E9G07 |

**Smith-chart discipline:** E9-3 is the only Smith figure — geometrically faithful (constant-R circles tangent at infinity on the RIGHT, reactance arcs, axis labels per the official). No invented wavelength scales (the published figure has none).

**Merging:** assembler merges fragments → `figures/figures.json` (first-reference numbering per chapter), `figreg.validate()` empty, all 39 XML-parse, renders ≥10 incl. ALL 10 redraws to PNG, side-by-side vs officials.
