# Writer Spec — Appendix B. Glossary & Formulas

**Output file:** `appendices/glossary-and-formulas.md` (this exact filename — the builder includes it by name)
**Target length:** reference material, excluded from the prose target; the glossary alone is 502 entries × one line.
**Pool coverage:** none — no pool quotes required here. Content comes from canon §4 (glossary) and canon §3 (notation & units, the Extra formula set), which are binding.

## 1. Purpose

The upgrading ham's back-of-book reference: every term the book uses, defined plainly in one line, plus the Extra course's formula set — each formula with a plain statement and a worked micro-example using the pool's own numbers. Not narrated in the audiobook (chapters 00–10 only).

## 2. Structure

- First line: `## Appendix B: Glossary & Formulas` (appendices are exempt from the chapter format laws — the audit's `check_format_laws` only applies to `chNN` stems — but keep the `## Appendix …` heading shape for the TOC; the colon form mirrors the series' shipped appendices).
- One short intro paragraph: how to use the appendix (definitions match the chapters; formulas carry micro-examples with the pool's own numbers).
- `### Glossary` — the full table from canon §4.
- `### Formulas` — the canon §3 Extra formula set with micro-examples (§4 below).
- `### Notation & Units` — the short note block (§5 below).

## 3. The glossary (`### Glossary`)

- **Source is canon §4 and only canon §4.** It carries **502 terms** as `| Term | Definition |` — consolidate them into this appendix **byte-exact**, terms alphabetical as published (the canon table is already A→Z, running "100% tie-off" through "Zepp antenna").
- Keep the canon's one-line definitions verbatim — they are binding (canon §4: "a chapter may expand a definition but must not contradict it"; series law: shared terms carry Book 2/3's definitions verbatim). Do not add terms of your own, do not drop any, do not reword.
- Format: a two-column markdown table (`| Term | Definition |` with the `|---|---|` separator) mirrors the canon and renders cleanly in the build (the builder has markdown pipe-table support). Group-letter subheadings (A, B, C …) are optional; if used, they are plain bold lines, not `####` headings, so the TOC stays flat.
- Sanity check before finishing: the row count is exactly 502 and a `diff` of the two tables shows no wording drift (mechanical copy, not retype — watch the µ in "µV" entries, the en dashes in ranges, the curly apostrophes, and "100% tie-off" at the top).

## 4. The formulas (`### Formulas`)

Present each relation from canon §3's Extra formula set with a one-line plain statement and a worked micro-example using the pool's own numbers. Cover exactly these (the book's complete formula set — nothing more, nothing less). The canon §3 table is the binding source; the groupings below mirror it.

**Carry-overs (series staples, kept for completeness — one line each):**

| Formula | Plain statement | Micro-example (pool numbers) |
|---|---|---|
| **V = I × R** (Ohm's law) | Voltage equals current times resistance; rearranged I = V / R, R = V / I. | 12 V across a resistor with 1.5 A through it: R = 12 ÷ 1.5 = 8 Ω. |
| **P = V × I = I² × R = V² / R** | The three DC power forms. | 1 A through 100 Ω: I²R = 100 W — and the j100 Ω of reactance in series adds zero real watts (E5D11). |
| **λ(m) = 300 / f(MHz)** | Wavelength in meters equals 300 divided by frequency in megahertz — the pool's own approximation of λ = c / f with c ≈ 3×10⁸ m/s, never an exact identity. | 300 ÷ 14.10 ≈ 21.3 m — the number behind E9F06's line length. |
| **Prefix ladder** | pico (10⁻¹²) → nano (10⁻⁹) → micro (10⁻⁶) → milli (10⁻³) → base → kilo (10³) → mega (10⁶) → giga (10⁹); toward a smaller unit multiply, toward a larger unit divide. | The E5C figure questions are the pool's own drill: 38 pF at 14 MHz, 18 µH at 3.505 MHz. |
| **dB = 10·log₁₀(P₂/P₁)** | The decibel definition — first-class exam math in this book. | ×2 ≈ 3 dB; a 1 dB loss leaves 0.794 of the power; net +2.8 dB ≈ ×1.9 (E9A02's step). |

**Reactance, resonance, Q, and bandwidth:**

| Formula | Plain statement | Micro-example (pool numbers) |
|---|---|---|
| **X_L = 2πfL** | Inductive reactance rises with frequency. | 18 µH at 3.505 MHz ≈ 400 Ω (E5C11's step to Point 3). |
| **X_C = 1/(2πfC)** | Capacitive reactance falls with frequency. | 38 pF at 14 MHz ≈ 300 Ω (E5C10); 19 pF at 21.2 MHz ≈ 400 Ω (E5C12). |
| **f₀ = 1/(2π√(LC))** | Resonant frequency of an LC combination; R never enters it. | 50 µH + 40 pF → 3.56 MHz (E5A02); 50 µH + 10 pF → 7.12 MHz (E5A10). |
| **X_L = X_C at resonance** | The reactances cancel: series RLC → minimum impedance; parallel → maximum. | E5A03–E5A08 (concept row — no numbers). |
| **BW = f₀ / Q** | Half-power bandwidth of a resonant circuit. | 7.1 MHz / 150 = 47.3 kHz (E5A11); 3.7 MHz / 118 = 31.4 kHz (E5A12); inverse Q = f / BW (E4B08). |
| **series Q = X / R; parallel Q = R / X** | Circuit Q from reactance and resistance. | Definition (E5A09); loaded Q always runs lower than unloaded. |
| **V_L = V_C ≈ Q × V_applied** | Resonant voltage magnification in a series circuit. | With E5A02's numbers: Q ≈ 51, so 10 V applied → ≈ 510 V across the coil (E5A01, E5A13). |

**Complex impedance (rectangular/polar), phase, admittance:**

| Formula | Plain statement | Micro-example (pool numbers) |
|---|---|---|
| **Z = R ± jX** | Rectangular impedance: resistance plus signed reactance, +j inductive and −j capacitive. | Pure capacitive 100 Ω = 0 − j100 (E5C01); 50 − j25 = 50 Ω + 25 Ω capacitive (E5C06). |
| **\|Z\| = √(R² + X²); θ = atan(X/R)** | Rectangular → polar. | 50 − j25 → 55.9 ∠−26.6° Ω (E5C06). |
| **R = \|Z\|cos θ; X = \|Z\|sin θ** | Polar → rectangular. | Same family (concept row). |
| **θ = atan((X_L − X_C)/R)** | Series RLC phase angle; positive = inductive = voltage leads. | −14.0° lags (E5B07); −63° lags (E5B08); +27° leads (E5B11). |
| **Y = 1/Z = G + jB; \|Y\| = 1/\|Z\|, ∠Y = −∠Z** | Admittance mirrors impedance in siemens, angle negated. | 50 − j25 Ω → ≈ 17.9 mS ∠+26.6° (E5B03's rule; E5B02/B05/B06/B12). |
| **P_real = I²R = VI·cos θ; Q = VI·sin θ** | Only resistance consumes real power; reactance stores and returns. | 1 A × 100 Ω → 100 W; the j100 term adds zero (E5D11). |
| **τ = R × C; τ = L/R** | Time constant: 63.2% charge / 36.8% discharge per τ. | 440 µF × 500 kΩ = 220 s (E5B04). |

**Reflection, SWR, and power bookkeeping:**

| Formula | Plain statement | Micro-example (pool numbers) |
|---|---|---|
| **Γ = (Z_L − Z₀)/(Z_L + Z₀); \|Γ\| = √(P_r/P_f)** | Reflection coefficient from impedances or wattmeter powers. | √(25/100) = 0.5 (E4B06's numbers). |
| **SWR = (1 + \|Γ\|)/(1 − \|Γ\|)** | SWR from Γ; always ≥ 1, larger number first. | 0.5 → 3:1. |
| **return loss = −20·log₁₀\|Γ\|** | Return loss in dB (amplitudes use 20·log). | 0.5 → ≈ 6.0 dB. |
| **P_load = P_fwd − P_refl** | Absorbed power is forward minus reflected. | 100 − 25 = 75 W (E4B06). |
| **ΔdB = 10·log₁₀(BW₂/BW₁)** | Noise floor scales with bandwidth. | 50 Hz → 1,000 Hz = 13 dB (E4C06). |
| **P(W) = 10^((dBm−30)/10)** | dBm ↔ watts (0 dBm = 1 mW; 30 dBm = 1 W). | −100 dBm = 10⁻¹³ W = 0.1 pW (E4D14). |

**Link budgets and ERP/EIRP:**

| Formula | Plain statement | Micro-example (pool numbers) |
|---|---|---|
| **P_rx = P_tx + G_tx + G_rx − losses − path loss** | Link budget as pure dB bookkeeping. | 40 + 6 + 3 − 100 = −51 dBm (E4D13). |
| **margin = P_rx − MDS − required SNR** | Link margin after the noise floor and the SNR reserve. | −89 − (−103) − 6 = +8 dB (E4D12). |
| **ERP = TPO × 10^((gains − losses)/10)** | ERP (with dBd) / EIRP (with dBi): sign discipline first. | 286 W (E9A02); 317 W (E9A06); 252 W EIRP (E9A07). |
| **dBd = dBi − 2.15** | Gain referenced to a dipole vs isotropic. | 6 dBi = 3.85 dBd (E9A12). |
| **Z_in = (Ω/V) × full-scale voltage** | Voltmeter input impedance from its ohms-per-volt rating. | 20 kΩ/V × 10 V = 200 kΩ (E4B02). |

**Transmission lines, stubs, and the λ/4 transformer:**

| Formula | Plain statement | Micro-example (pool numbers) |
|---|---|---|
| **L(λ/2, m) ≈ 150 × VF / f(MHz)** | Physical line length; velocity factor divides. | 10.6 m at 14.10 MHz, air VF ≈ 1.0 (E9F06). |
| **λ/2 repeats, λ/4 inverts, λ/8 converts** | The transformation table: a λ/2 line repeats its termination; a λ/4 line inverts it (short↔open); a λ/8 line becomes a reactance (shorted → inductive, open → capacitive). | E9F04, E9F09–E9F12 (the table row — worked with any shorted λ/4 stub). |
| **Z₀ = √(Z_line × Z_load)** | Quarter-wave Q-section: the geometric mean. | √(50 × 100) = 70.7 → 75 Ω line (E9E06). |

**Circuits, conversion, and signal arithmetic:**

| Formula | Plain statement | Micro-example (pool numbers) |
|---|---|---|
| **Av = −RF/R1; Vout = −(RF/R1)·Vin** | Inverting op-amp gain law (the pool's best return-on-formula). | 47 (E7G07); −2.3 V (E7G09); ≈38 (E7G10); ≈14 (E7G11). |
| **P = (V_in − V_out) × I_out** | Series-regulator dissipation. | (25 − 12) V × 1 A = 13 W (E7D13). |
| **operating time = amp-hours ÷ average current** | Battery time. | 10 Ah at 2 A = 5 h (E7D09). |
| **n bits → 2ⁿ levels** | ADC resolution. | 8 bits = 256 levels (E8A09); 1 V at 1 mV → 10 bits (E7F06). |
| **sample rate ≥ 2 × highest component** | Nyquist rate. | ≥ 30 kHz for a 15 kHz signal (E7F05). |
| **index = Δf / f_mod; deviation ratio = max Δf / max f_mod** | Modulation index and its worst-case sibling. | 3000/1000 = 3 (E8B03); 6000/2000 = 3 (E8B04); 5/3 = 1.67 (E8B05); 7.5/3.5 = 2.14 (E8B06). |
| **BW ≈ 4 × WPM** | CW bandwidth from keying speed. | 13 WPM ≈ 52 Hz (E8C05). |
| **BW ≈ (1.2 × shift) + baud** | FSK/data bandwidth. | 1.2 × 4800 + 9600 = 15.36 kHz (E8C07). |

**MPE (flagged as enrichment — no E0A question requires it):**

| Formula | Plain statement | Micro-example |
|---|---|---|
| **S = ERP / (4πR²)** | Far-field power density — the shape of an MPE evaluation. | 100 W ERP at 10 m ≈ 0.08 mW/cm² (enrichment only — flag exactly as ch10 does). |

## 5. The notation block (`### Notation & Units`)

A short note block carrying the canon §3 laws a reader will meet in the pool and the book:

- This book's prose uses **V** for voltage and **×** for multiplication (V = I × R), exactly as Books 2 and 3 do. The 2024–2028 Extra pool states electrical quantities in **words** ("a 400-ohm resistor and a 38-picofarad capacitor") and prints complex impedances and angles in ASCII ("0 - j100", "90 degrees") — verbatim pool quotes always keep the pool's typography, so quotes never conflict with the prose convention.
- **Complex-number conventions (new at Extra depth):** impedance is written rectangular (Z = R ± jX: +j inductive, −j capacitive) or polar (|Z| ∠θ, degrees always). The book uses the engineering j, never i; the house minus sign with the j attached to the number ("400 − j300 Ω"); polar with the angle marker ("55.9 ∠−26.6° Ω"). Admittance mirrors it in siemens (Y = G + jB) with the angle negated.
- Unit case is load-bearing: **kHz** (lowercase k), **MHz**/**GHz** (capital M/G), always capital H; **mA**, **µV**, **pF**, **nF**, **kV** follow the same prefix case rules. Subscripts are set as subscripts: X_L, X_C, f₀, Z₀, P_fwd, P_refl, S21, S11.
- c = 3×10⁸ m/s = 300,000 km/s is the working value; f = 1/T; dBm is decibels relative to 1 milliwatt (0 dBm = 1 mW); amplitude ratios use 20·log₁₀, power ratios 10·log₁₀.
- The hobby's customary units: antenna lengths in feet (468/f-style, approximate), transmission-line lengths in meters (the pool's E9F06 unit), propagation paths in miles, coax loss in dB per 100 feet, gains in dBi or dBd with the reference always named; SWR is always written larger-number-first ("3:1").
- Inline math uses the same `$…$` style as the chapters — at most one `$…$` span per paragraph; the renderer supports subscripts, Greek letters ($\Gamma$, $\tau$, $\omega$), $\pi$, $\sqrt{}$, and fractions — the whole formula set above.

## 6. Integrity notes

- Appendices are exempt from the chapter format laws (no Exam Focus, no Key Takeaways, no FACT-line requirement) — but banned phrases still apply nowhere ("little did they know", "in that moment", "a testament to").
- Everything here traces to canon §3/§4 or to pool numbers already pinned in the canon — introduce no new facts, no new terms, no new formulas.
- Alphabetization, spelling, and punctuation of terms match the canon byte-exactly; the formula micro-examples use the pool's own numbers exactly as pinned in canon §3's formula table; the MPE formula keeps its enrichment flag verbatim.
