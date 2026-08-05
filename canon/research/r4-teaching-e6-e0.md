# R4 teaching notes — Extra pool subelements E6–E0 (2024–2028)

Researcher: R4. Source: `canon/pool-extra.json` (599 questions; verified). Coverage: E6 (68), E7 (99), E8 (48), E9 (93), E0 (12) = 320 questions, every one read. Figures: E6-1, E6-2, E6-3, E7-1, E7-2, E7-3, E9-1, E9-2, E9-3 (9 of the pool's 10; E5-1 is R3's). Every figure was rendered from `canon/source/Extra_Figures_2024-2028-1.pdf` (300 dpi crops) and cross-checked against the SVG set in `canon/source/e4_2024-svgs.zip`; every keyed answer on a figure question was re-derived from the drawing itself.

Exam weight: the Extra exam is 50 questions, one from each of the 50 groups. Subelements E6–E0 supply 30 of the 50 — E6:6, E7:8, E8:4, E9:8, E0:1 — so this material is 60% of the exam, and E7+E9 alone are 16 questions. Group-level balance means no topic below can be skipped: every group is guaranteed exactly one seat on every exam.

Group map (each group = exactly one exam question):

| Group | Qs | Theme | Group | Qs | Theme |
|---|---:|---|---|---:|---|
| E6A | 12 | Semiconductors: BJT/FET | E8A | 11 | Waveforms, sampling, PEP |
| E6B | 11 | Diodes: Zener/Schottky/varactor/PIN | E8B | 11 | Modulation index, multiplexing |
| E6C | 11 | Digital ICs, logic families, gates | E8C | 15 | Digital modes, codes, bandwidths |
| E6D | 11 | Cores, toroids, crystals (no 07) | E8D | 11 | Spread spectrum, keying, codes |
| E6E | 12 | MMICs, packages, SMT | E9A | 12 | Gain, ERP/EIRP, efficiency |
| E6F | 11 | Optical devices | E9B | 11 | Patterns, modeling; Figs E9-1/2 |
| E7A | 11 | Flip-flops, counters, gates | E9C | 14 | Wire antennas, phased arrays |
| E7B | 12 | Amplifier classes; Fig E7-1 | E9D | 12 | Yagis, dishes, loading |
| E7C | 11 | Filters, matching networks | E9E | 10 | Matching systems (no 10) |
| E7D | 15 | Power supplies; Fig E7-2 | E9F | 12 | Transmission lines, stubs |
| E7E | 11 | Modulation/demodulation | E9G | 11 | Smith chart; Fig E9-3 |
| E7F | 14 | DSP, SDR | E9H | 11 | Receiving/DF antennas |
| E7G | 12 | Op-amps; Fig E7-3 | E0A | 12 | RF exposure, tower safety |
| E7H | 13 | Oscillators, PLL, DDS | | | |

Numbering quirks (script-verified against the pool): **E6D07 does not exist** (E6D runs 01–06, 08–12; 11 questions) and **E9E10 does not exist** (E9E runs 01–09, 11; 10 questions). These are gaps in the published numbering, not ingestion losses. All other groups are contiguous from 01. Subelement totals reconcile exactly: E6 = 12+11+11+11+12+11 = 68; E7 = 11+12+11+15+11+14+12+13 = 99; E8 = 11+11+15+11 = 48; E9 = 12+11+14+12+10+12+11+11 = 93; E0 = 12.

---

## Subelement E6 — Circuit components (68 questions, 6 groups, 6 exam seats)

### E6A (12) — Semiconductor materials and devices: BJT, FET
- Topic inventory: N/P-type doping (E6A02, E6A04), PN-junction reverse bias (E6A03), GaAs use (E6A01), FET vs BJT input impedance (E6A05), beta definition (E6A06), Si NPN bias voltage (E6A07), alpha cutoff frequency (E6A08), depletion-mode FET (E6A09), MOSFET gate-protection Zeners (E6A12), schematic symbols ×2 (E6A10–11, Figure E6-1).
- Must understand: donor impurities add free electrons (N-type), acceptor impurities add holes (P-type); reverse bias pulls holes and electrons away from the junction and widens the depletion region, so no current flows; a FET gate is insulated (MOSFET) or reverse-biased (JFET), so its DC input impedance is far higher than a BJT base; beta = ΔIc/ΔIb (current gain); a forward-biased silicon base-emitter junction drops ≈0.6–0.7 V; a depletion-mode FET conducts source-to-drain with zero gate voltage (an enhancement-mode device does not).
- Confusions: E6A07 distractors swap units and magnitude — 6–7 *volts* and 0.6–0.7/6–7 *ohms*; keyed is 0.6–0.7 V. E6A08: "alpha cutoff" (grounded-BASE current gain down to 0.7 of its 1 kHz value) vs the invented "beta cutoff frequency" distractor. E6A04: acceptor (adds holes) vs donor (adds electrons) — the pair is swapped in the distractors. E6A12: the gate Zeners protect against **static damage**, not overheating or bias referencing. E6A09: depletion-mode = conducts at zero gate bias; the "no current at zero gate" distractor describes enhancement-mode.
- Vocab: acceptor impurity, donor impurity, depletion region, depletion-mode/enhancement-mode FET, beta (β), alpha cutoff frequency, N-channel/P-channel, dual-gate MOSFET.
- Math: none beyond recognizing 0.6–0.7 V junction drop.
- FACT: Si B-E junction ≈0.6–0.7 V (E6A07); GaAs → microwave circuits (E6A01); N-type = excess free electrons (E6A02); MOSFET gate Zeners = static protection (E6A12).

### E6B (11) — Diodes: Zener, Schottky, varactor, PIN, point-contact
- Topic inventory: Zener characteristic (E6B01), Schottky forward drop and construction (E6B02, E6B08), LED forward voltage (E6B03), varactor (E6B04), PIN diode RF switching/attenuation (E6B05, E6B11), Schottky uses (E6B06), thermal failure (E6B07), point-contact (E6B09), Schottky symbol (E6B10, Figure E6-2).
- Must understand: a Zener holds a constant voltage drop across varying current (reference/regulator use); a Schottky is a metal-semiconductor junction — low forward drop, fast recovery, good as a VHF/UHF mixer/detector and as an efficient power-supply rectifier; LED forward drop is set by the semiconductor band gap; a varactor is a voltage-controlled capacitor; a PIN diode's RF resistance is set by forward DC bias current and its low junction capacitance makes it a good RF switch; junction diodes fail from excessive junction temperature (current kills via heat).
- Confusions: varactor vs tunnel vs SCR vs Zener (E6B04 — the phrase "voltage-controlled capacitor" is the tell); Schottky rectifier advantage is lower forward drop, NOT higher reverse breakdown (E6B02); PIN attenuation is controlled by forward DC bias current, not by reverse voltage or a reference voltage (E6B11); point-contact diodes are RF detectors, not high-voltage rectifiers (E6B09).
- Vocab: Schottky barrier diode, metal-semiconductor junction, varactor, PIN diode, point-contact diode, band gap, junction capacitance.
- FACT: point-contact diode → RF detector (E6B09); Schottky → VHF/UHF mixer/detector (E6B06).

### E6C (11) — Digital ICs: logic families, comparators, symbols
- Topic inventory: comparator hysteresis and threshold (E6C01–02), tri-state logic (E6C03), BiCMOS (E6C04), CMOS power/noise immunity (E6C05–06), pull-up/pull-down (E6C07), FPGA design entry (E6C09), gate symbols ×3 (E6C08, E6C10, E6C11, Figure E6-3).
- Must understand: hysteresis stops input noise from chattering the output; a comparator flips its output state when the input crosses the threshold voltage; tri-state = 0, 1, and high-impedance output states (for bus sharing); CMOS has the lowest power consumption of the listed families and its input switches at about HALF the supply voltage (hence wide noise margins); a pull-up/pull-down resistor establishes a defined voltage on an input or output that would otherwise be open-circuit; FPGAs are configured in a hardware description language (HDL).
- Confusions: E6C06 — the switching threshold is about HALF the supply; the distractor says "twice the power supply voltage." E6C03 — tri-state is about the third (high-impedance) output state, not ternary math or three selectable impedances. BiCMOS = CMOS high input impedance + bipolar low output impedance (E6C04) — not cheaper, not ESD-immune. CMOS beats Schottky TTL, ECL, and NMOS on power (E6C05).
- Vocab: hysteresis, comparator, threshold voltage, tri-state logic, BiCMOS, CMOS, pull-up/pull-down resistor, FPGA, hardware description language (HDL).

### E6D (11) — Toroids, cores, crystals (note: no E6D07)
- Topic inventory: piezoelectricity (E6D01, E6D03), crystal equivalent circuit (E6D02), laminated cores (E6D04), ferrite vs powdered iron (E6D05, E6D08), permeability (E6D06), ferrite beads (E6D09), toroid advantage (E6D10), brass slug (E6D11), saturation (E6D12).
- Must understand: piezoelectricity is two-way — generate a voltage when stressed AND flex when a voltage is applied (both E6D01 and E6D03 ride on this); a quartz crystal models as a series RLC (motional arm) in parallel with a shunt C (electrode + stray capacitance); laminations reduce eddy-current power loss; core permeability determines inductance; ferrite needs fewer turns for a given inductance than powdered iron, but powdered iron has the better temperature stability; a toroid confines most of its magnetic field inside the core (less stray coupling, less pickup); inserting brass into a coil DECREASES inductance; saturation = operation at excessive magnetic flux.
- Confusions: ferrite wins on turns count/permeability, powdered iron wins on temperature stability — the pool tests both directions (E6D05 vs E6D08), and the distractors trade the two materials' strengths. Brass and aluminum are both non-ferromagnetic, but only brass is keyed as decreasing inductance (E6D11); aluminum appears as a distractor in both E6D08 and E6D11. Toroid distractors promise easier coupling and higher hysteresis — the keyed property is field confinement (E6D10).
- Vocab: piezoelectricity, motional arm (series RLC), shunt/electrode capacitance, permeability, eddy currents, lamination, ferrite bead, saturation, toroid, slug tuning.
- FACT: ferrite beads = VHF/UHF parasitic suppressors at transistor amp terminals (E6D09); powdered iron = most temperature-stable magnetic material listed (E6D08).

### E6E (12) — MMICs, device packages, SMT
- Topic inventory: GaAs electron mobility (E6E01), through-hole package ID (E6E02), MMIC material/frequency (E6E03), MMIC impedance (E6E04), LNA noise figure (E6E05), MMIC characteristics (E6E06), microstrip (E6E07), MMIC bias feed (E6E08), SMT parasitics (E6E09–10), DIP package facts (E6E11–12).
- Must understand: GaAs's higher electron mobility suits UHF and above; GaN supports the highest MMIC operating frequency of the listed materials; MMICs are 50-ohm-in/50-ohm-out blocks with controlled gain, low noise figure, and constant input/output impedance over their specified range; bias is supplied through a resistor and/or RF choke on the OUTPUT lead; microstrip is the usual MMIC interconnect; surface-mount parts have the least parasitic inductance/capacitance above HF, and SMT's RF advantages compound (smaller area, shorter traces, less parasitics — "All these choices are correct"); DIP = dual in-line package, two rows of pins on opposite sides, and its lead length is why it disappears at UHF+.
- Confusions: E6E05 distractors mix units — 0.5 dB is the typical low-noise UHF preamp noise figure; -10 dB / 44 dBm / -20 dBm are not noise figures at all. E6E02: DIP is the only through-hole part among PLCC/BGA/SOT. E6E12: DIP fails at UHF from excessive LEAD LENGTH, not dielectric loss. E6E08: bias enters at the output lead, not the input lead (distractor A swaps them).
- Vocab: MMIC, GaAs, GaN, microstrip, noise figure, DIP (dual in-line package), PLCC, BGA, SOT, surface-mount technology (SMT), parasitic inductance/capacitance.
- FACT: MMIC input/output impedance = 50 ohms (E6E04); typical low-noise UHF preamp NF = 0.5 dB (E6E05).

### E6F (11) — Optical devices
- Topic inventory: photon absorption (E6F01), photoconductive response (E6F02), optoisolator construction (E6F03), photovoltaic effect (E6F04), shaft encoder (E6F05), photoconductive material (E6F06), solid-state relay (E6F07), isolation purpose (E6F08), PV efficiency (E6F09), PV material (E6F10), PV cell voltage (E6F11).
- Must understand: photons are the particles absorbed in a photovoltaic cell; light DECREASES the resistance of photoconductive material; an optoisolator is an LED + phototransistor pair giving electrical (galvanic) isolation between a control circuit and a 120 VAC switched circuit; the photovoltaic effect converts light to electrical energy; PV efficiency = the fraction of light converted to current; a shaft encoder detects rotation by interrupting a light source with a patterned wheel; crystalline semiconductor is the common photoconductive material.
- Confusions: photovoltaic (generates) vs photoconductive (changes resistance) — E6F01/04/09 vs E6F02/06; an SSR is a semiconductor implementation of relay functions, not a transistor driving a mechanical coil (E6F07 distractor A); optoisolators provide ISOLATION, not impedance matching or a low-impedance link (E6F08).
- Vocab: photovoltaic cell/effect, photoconductive, optoisolator/optocoupler, phototransistor, solid-state relay (SSR), optical shaft encoder.
- FACT: fully illuminated silicon PV cell ≈ 0.5 V open-circuit (E6F11); silicon is the common power-generating PV material (E6F10).

---

## Subelement E7 — Practical circuits (99 questions, 8 groups, 8 exam seats)

### E7A (11) — Digital circuits: flip-flops, counters, gates
- Topic inventory: bistable element (E7A01), decade counter (E7A02), ÷2 and ÷16 by flip-flops (E7A03–04), astable/monostable (E7A05–06), NAND/OR/XNOR truth (E7A07–09), truth table (E7A10), positive logic (E7A11).
- Must understand: a flip-flop is bistable (two stable states) and one stage divides a pulse train by 2 — N cascaded stages divide by 2^N; a decade counter emits one output pulse per 10 input pulses; an astable multivibrator free-runs between two states with no clock; a monostable flips to its alternate state for a set time then returns; NAND = 0 only when ALL inputs are 1; OR = 1 if ANY input is 1; XNOR = 0 when exactly one input is 1 (an equality detector); positive logic: high voltage = 1, low = 0.
- Math: ÷16 needs log2(16) = **4 flip-flops** (E7A04; distractors 6/8/16 punish guessing powers other than 2^4).
- Confusions: XNOR vs XOR wording — the keyed XNOR produces 0 when one and only one input is 1 (E7A09; option D is the XOR truth); a decade counter COUNTS, it does not decode for 7-segment displays (both decoder distractors, E7A02); monostable vs astable — "temporarily switches for a set time" vs "continuously alternates" (E7A05 vs E7A06).
- Vocab: bistable/monostable/astable multivibrator, flip-flop, J-K/T flip-flop, decade counter, truth table, positive logic.

### E7B (12) — Amplifier classes and Figure E7-1
- Topic inventory: Class AB conduction angle (E7B01), Class D (E7B02, E7B08), output filtering (E7B03), Class A operating point (E7B04), parasitic oscillation cures (E7B05), grounded-grid (E7B06), Class C on SSB (E7B07), emitter follower (E7B09), Figure E7-1 bias/circuit ID ×3 (E7B10–12).
- Must understand — the conduction-angle ladder (the group's core discrimination):
  - Class A: conducts the entire 360°; operating point about halfway between saturation and cutoff.
  - Class AB: each push-pull device conducts MORE than 180° but LESS than 360°.
  - Class B: exactly 180° (distractor value in E7B01).
  - Class C: less than 180° — high efficiency, nonlinear; using it on SSB gives signal distortion and excessive bandwidth.
  - Class D: switching amplifier; efficient because the device sits at saturation or cutoff most of the time; requires an output filter to remove harmonic content.
- Also: kill unwanted RF power-amp oscillation with parasitic suppressors and/or neutralization (E7B05); grounded-grid = LOW input impedance (E7B06); emitter follower (common collector) keeps input and output in phase (E7B09).
- Confusions: the 180°/AB/C ladder above is exactly what E7B01's options enumerate; switching-amp efficiency comes from saturation/cutoff operation, not higher voltage or push-pull topology (E7B08); Class C is fine for FM/CW but the keyed result on SSB is distortion + excessive bandwidth, not reduced intermod (E7B07).
- Vocab: push-pull, Class A/AB/B/C/D, saturation, cutoff, operating point, neutralization, parasitic suppressor, grounded-grid, emitter follower (common collector).
- FACT: grounded-grid → low input impedance (E7B06); emitter follower → input/output in phase (E7B09).

### E7C (11) — Filters and impedance matching networks
- Topic inventory: low-pass Pi-network topology (E7C01), T-network response (E7C02), Pi-L purpose and description (E7C03, E7C07), matching principle (E7C04), Chebyshev (E7C05), elliptical (E7C06), helical (E7C08), crystal lattice (E7C09), cavity (E7C10), shape factor (E7C11).
- Must understand: a low-pass Pi-network = shunt C at input and output with a series L between them (E7C01's four options permute the L/C positions — draw it once); a T-network with SERIES capacitors and a SHUNT inductor passes highs (high-pass, E7C02); a Pi-L adds a series output inductor to a Pi for greater harmonic suppression (E7C03) and is literally "a Pi-network with an additional output series inductor" (E7C07); a matching network cancels the reactive part of an impedance and transforms the resistive part to the desired value (E7C04); Chebyshev = passband ripple + sharp cutoff; elliptical = extremely sharp cutoff WITH one or more stop-band notches; helical filters are the common VHF/UHF band-pass/notch filters; cavity filters serve repeater duplexers; shape factor measures adjacent-channel rejection.
- Confusions: the filter-family ladder — Butterworth (maximally flat, no ripple) vs Chebyshev (passband ripple, sharp) vs elliptical (sharpest, stop-band notches) — is the tested three-way discrimination (E7C05–06); a crystal lattice filter is for LOW-LEVEL signals made with quartz crystals, not a power-supply or audio device (E7C09); duplexer = cavity filter at 2 m, not crystal/DSP/L-C (E7C10).
- Vocab: Pi-network, Pi-L network, T-network, Chebyshev, Butterworth, elliptical filter, helical filter, crystal lattice filter, cavity filter, duplexer, shape factor, passband ripple.

### E7D (15) — Power supplies and regulators; Figure E7-2
- Topic inventory: linear vs switchmode regulation (E7D01–02), Zener reference (E7D03), three-terminal series regulator (E7D04), shunt regulator (E7D05), Figure E7-2 ×3 (E7D06–08), battery time (E7D09), switchmode weight/cost (E7D10), solar inverter (E7D11), dropout voltage (E7D12), regulator dissipation (E7D13), equalizing/bleeder resistors (E7D14), step-start (E7D15).
- Must understand: a linear regulator varies the conduction of a control element to hold output constant; a switcher varies the DUTY CYCLE of pulses fed to a filter; a Zener is the stable voltage reference; a three-terminal regulator is a SERIES regulator; a shunt regulator loads the unregulated source; high-frequency switching uses much smaller transformers and filter components for the same power (hence lighter/cheaper); a solar-panel inverter converts DC to AC; dropout voltage = minimum input-to-output differential needed to stay in regulation; equal-value resistors across series filter capacitors equalize voltage AND discharge the caps AND provide a minimum load ("All these choices are correct"); a step-start circuit lets filter capacitors charge gradually.
- Math: battery operating time = amp-hour capacity ÷ average current (E7D09) — e.g., 10 Ah at 2 A = 5 h. Series-regulator dissipation P = (Vin − Vout) × Iout (E7D13) — using Figure E7-2's numbers, (25 − 12) V × 1 A = 13 W dissipated in Q1.
- Confusions: "varies conduction" (linear) vs "varies duty cycle" (switchmode) — the two stems are near-twins and the distractors cross-quote them (E7D01 vs E7D02); dropout is an input-MINUS-output figure, not an absolute minimum input and not an output sag (E7D12); regulator dissipation uses the voltage DIFFERENCE, not input or output voltage alone (E7D13).
- Vocab: pass element, series/shunt regulator, switchmode, duty cycle, dropout voltage, step-start circuit, bleeder/equalizing resistor, inverter, brute-force filter.

### E7E (11) — Modulation and demodulation circuits
- Topic inventory: FM generation by reactance modulator (E7E01–02), discriminator (E7E03), SSB by balanced modulator + filter (E7E04), pre-/de-emphasis (E7E05–06), baseband (E7E07), mixer products (E7E08), mixer overload (E7E09), envelope detector (E7E10), product detector (E7E11).
- Must understand: FM phone is generated by reactance modulation of a local oscillator; a reactance modulator makes PM/FM by varying a capacitance; a discriminator detects FM; SSB = balanced modulator (cancels carrier) followed by a filter (removes one sideband); pre-emphasis boosts the higher audio frequencies at the TRANSMITTER; de-emphasis in the RECEIVER restores response and keeps compatibility with phase modulation; baseband = the frequency range the message occupies before modulation; a mixer outputs the two input frequencies plus their sum and difference; overdriven mixer inputs generate spurious mixer products; an AM envelope detector works by rectification and filtering of the RF; SSB demodulation needs a product detector.
- Confusions: the three-detector sort — product detector (SSB) vs discriminator (FM) vs envelope detector (AM) — is tested at E7E03/10/11; pre-emphasis is TX-side, de-emphasis RX-side (E7E05 vs E7E06); "reactance modulator of the FINAL amplifier" is the E7E01 trap — modulation happens at the oscillator.
- Vocab: reactance modulator, frequency discriminator, balanced modulator, product detector, envelope detector, pre-emphasis, de-emphasis, baseband, mixer products.

### E7F (14) — DSP and SDR
- Topic inventory: direct sampling (E7F01), adaptive noise filter (E7F02), Hilbert-transform SSB (E7F03–04), Nyquist (E7F05), ADC resolution bits (E7F06), FFT (E7F07), decimation and anti-alias (E7F08–09), sample rate vs bandwidth (E7F10), minimum detectable signal (E7F11), FIR properties (E7F12), taps (E7F13–14).
- Must understand: direct sampling digitizes incoming RF with an ADC — no local oscillator, no mixer; an adaptive filter removes unwanted noise from a received SSB signal; the Hilbert-transform (phasing) method generates SSB by combining signals in quadrature phase relationship; Nyquist: sample at ≥2× the highest frequency component; the FFT converts time domain → frequency domain; decimation reduces the effective sample rate by removing samples, and an anti-alias low-pass must remove high-frequency components first (else they reappear as false low-frequency components); sample RATE sets maximum receive bandwidth, while reference voltage + sample width in bits sets the minimum detectable signal; FIR filters can delay all frequency components equally (linear phase/constant group delay); taps provide the incremental delays, and more taps give a sharper filter.
- Math: 1 V range at 1 mV resolution needs 1000 codes; 2^10 = 1024 ≥ 1000 → **10 bits** (E7F06; 8 bits = 256 codes is the trap). Nyquist example: to reproduce a signal with components to 15 kHz, sample at ≥30 kHz. Decimation example: keeping every 4th sample of a 1 MS/s stream yields 250 kS/s effective — and anything above 125 kHz must be filtered out first.
- Confusions: bandwidth ↔ sample rate, sensitivity ↔ bits + reference voltage (E7F10 vs E7F11 — the distractors swap the two parameters); "adaptive" removes noise, "Hilbert" generates SSB (E7F02 vs E7F03); anti-aliasing is needed BEFORE decimation, not to notch the sampling frequency (E7F09).
- Vocab: direct sampling, SDR, adaptive filter, Hilbert transform, quadrature, Nyquist rate, FFT, time/frequency domain, decimation, anti-aliasing filter, FIR, tap, group delay.

### E7G (12) — Op-amps; Figure E7-3
- Topic inventory: output/input impedance (E7G01, E7G03), feedback-capacitor response (E7G02, Fig E7-3), input offset voltage (E7G04), ringing prevention (E7G05), gain-bandwidth (E7G06), gain/output calcs ×4 (E7G07, E7G09–11, Fig E7-3), ideal-amp gain vs frequency (E7G08), op-amp definition (E7G12).
- Must understand: an op-amp is a high-gain, direct-coupled differential amplifier with very high input impedance and very low output impedance; input offset voltage = the differential input voltage needed to bring the open-loop output to zero; gain-bandwidth = the frequency at which the open-loop gain falls to one; an IDEAL op-amp's gain does not vary with frequency; ringing/instability in an op-amp audio filter is prevented by restricting BOTH gain and Q.
- Math (inverting amplifier, Figure E7-3): **Av = −RF/R1; Vout = −(RF/R1)·Vin**. Worked with the pool's own numbers: E7G07: 470/10 = **47**; E7G09: −(10000/1000) × 0.23 V = **−2.3 V**; E7G10: 68000/1800 = 37.8 ≈ **38**; E7G11: 47000/3300 = 14.2 ≈ **14**. Add a capacitor across RF and the feedback impedance falls as frequency rises → **low-pass filter** (E7G02).
- Confusions: sign — only E7G09 asks for output voltage (negative, −2.3 V, with +2.3 V as distractor); the other three ask "absolute voltage gain" (positive). Distractor patterns: 24 ≈ (R1+RF)/20-ish averaging, 4700 = RF×10, 76 = 2×38, 28 = 2×14 — all punish arithmetic slips, so compute RF/R1 exactly. E7G02's stem prints "in E7-3" (no "Figure") and E7G07's prints "Figure E73" (missing hyphen) — published typos, preserve them in quotes.
- Vocab: operational amplifier, inverting/non-inverting input, input offset voltage, gain-bandwidth product, open-loop vs closed-loop gain, feedback resistor.

### E7H (13) — Oscillators and frequency synthesis
- Topic inventory: oscillator circuit names (E7H01), microphonics (E7H02, E7H07), PLL definition and uses (E7H03, E7H06), Colpitts/Pierce feedback paths (E7H04–05), thermal drift (E7H08), DDS architecture/lookup/spurs (E7H09–11), crystal load capacitance (E7H12), microwave stability references (E7H13).
- Must understand: the three common oscillators are Colpitts, Hartley, and Pierce (the Taft/Fenner/Beane distractor names are invented); Colpitts feedback = capacitive divider; Pierce feedback = through a quartz crystal; a PLL is an electronic servo loop = phase detector + low-pass filter + VCO + stable reference oscillator, and it can perform frequency synthesis and FM demodulation; a DDS = phase accumulator + lookup table (amplitude values representing the desired waveform) + DAC + low-pass anti-alias filter; DDS spectral impurities are spurious signals at discrete frequencies; microphonics = oscillator frequency changes caused by mechanical vibration, reduced by mechanically isolating the circuit from its enclosure; NP0 capacitors reduce thermal drift; a crystal runs on its specified frequency when given the specified parallel (load) capacitance; GPS reference, rubidium reference, and temperature-controlled dielectric resonators all serve microwave stability ("All these choices are correct").
- Confusions: Colpitts = capacitive divider vs Hartley = tapped coil — the pool tests Colpitts with "tapped coil" as distractor (E7H04); DDS spurs are discrete-frequency, not broadband noise (E7H11); the two drift cures stay separate — NP0 for THERMAL drift (E7H08), mechanical isolation for MICROPHONICS (E7H07; its distractor "use NP0 capacitors" raids E7H08).
- Vocab: Colpitts, Hartley, Pierce, phase-locked loop (PLL), VCO, phase detector, direct digital synthesizer (DDS), phase accumulator, lookup table, NP0/C0G, microphonic, load capacitance, dielectric resonator.

---

## Subelement E8 — Signals and emissions (48 questions, 4 groups, 4 exam seats)

### E8A (11) — AC waveforms, sampling, PEP
- Topic inventory: Fourier analysis of a square wave (E8A01), successive approximation (E8A02), time domain (E8A03), dither (E8A04), true-RMS (E8A05), PEP:average ratio (E8A06–07), flash ADCs in SDRs (E8A08), 8-bit levels (E8A09), DAC reconstruction filter (E8A10), ADC quality metric (E8A11).
- Must understand: Fourier analysis shows a square wave is a sine plus its odd harmonics; successive approximation is a type of analog-to-digital conversion; time domain = amplitude at different times; dither = a small amount of noise added to the input to reduce quantization noise; a true-RMS meter measures RMS for sinusoidal AND non-sinusoidal signals; unprocessed SSB phone PEP:average ≈ 2.5:1 and is determined by speech characteristics; flash/direct converters are used in SDRs because their very high speed allows digitizing high frequencies; the DAC output low-pass removes spurious sampling artifacts; total harmonic distortion measures ADC quality.
- Math: an 8-bit ADC encodes 2^8 = **256** input levels (E8A09; distractor 8 confuses bits with levels).
- Confusions: PEP ratio is 2.5:1, not 25:1 (E8A06); the ratio depends on speech characteristics, not carrier suppression or amplifier gain (E8A07); THD is the ADC quality measure — PEP, reciprocal mixing, and power factor are borrowed RF terms (E8A11).
- Vocab: Fourier analysis, successive approximation, flash/direct conversion, dither, quantization noise, true RMS, total harmonic distortion (THD), peak envelope power (PEP).

### E8B (11) — Modulation index, deviation ratio, multiplexing
- Topic inventory: modulation index definition (E8B01), PM index vs carrier frequency (E8B02), index calculations (E8B03–04), deviation ratio (E8B05–06, definition E8B09), OFDM (E8B07–08), FDM (E8B10), TDM (E8B11).
- Must understand: modulation index = frequency deviation ÷ modulating frequency; a phase-modulated emission's index does not depend on the RF carrier frequency; deviation ratio = MAXIMUM carrier deviation ÷ HIGHEST modulating frequency (the worst-case sibling of the index); OFDM = a digital modulation using subcarriers at frequencies chosen to avoid intersymbol interference, used for amateur digital modes; FDM divides the transmitted signal into separate frequency bands each carrying a different data stream; digital TDM gives two or more signals discrete time slots of one transmission.
- Math: index = Δf / f_mod → E8B03: 3000/1000 = **3**; E8B04: 6000/2000 = **3**. Deviation ratio = max Δf / max f_mod → E8B05: 5 kHz / 3 kHz = **1.67**; E8B06: 7.5 kHz / 3.5 kHz = **2.14**.
- Confusions: index vs deviation ratio (same formula shape, different numerator/denominator scope — E8B01 vs E8B09); every calc question offers the inverted ratio as a distractor (0.3, 0.6, 0.167, 0.47) — divide deviation BY modulating frequency, never the reverse; E8B03 and E8B04 BOTH key to 3.
- Vocab: modulation index, deviation ratio, OFDM, subcarrier, intersymbol interference, frequency-division multiplexing (FDM), time-division multiplexing (TDM).

### E8C (15) — Digital modes, codes, bandwidths
- Topic inventory: QAM (E8C01), symbol rate (E8C02, E8C11), PSK zero-crossing switching (E8C03), PSK31 pulse shaping (E8C04), CW bandwidth (E8C05, E8C12), FT8 bandwidth (E8C06), FSK bandwidth calc (E8C07), ARQ (E8C08), Gray code (E8C09), data rate vs bandwidth (E8C10), constellation diagrams (E8C13), mesh networking (E8C14–15).
- Must understand: QAM transmits data by modulating the amplitude of two carriers of the same frequency 90° out of phase; symbol rate = the rate at which the waveform changes to convey information, and symbol rate and baud are THE SAME; changing PSK phase at the RF zero crossing minimizes bandwidth; PSK31 uses sinusoidal data pulses for the same reason; CW bandwidth is set by keying speed and rise/fall shape; ARQ corrects errors by requesting retransmission when errors are detected; Gray code changes only one bit between sequential code values; a more efficient digital code raises data rate without more bandwidth; a constellation diagram shows the possible phase and amplitude states for each symbol; mesh nodes have IP addresses and form the network via discovery and link-establishment protocols.
- Math: CW bandwidth ≈ 4 × WPM → 13 WPM ≈ **52 Hz** (E8C05; distractors halve/double it). FSK/data bandwidth = (1.2 × frequency shift) + baud → E8C07: 1.2 × 4800 + 9600 = 5760 + 9600 = **15.36 kHz** (distractors are the raw shift and baud values). FT8 = **50 Hz** (E8C06, FACT).
- Confusions: "symbol rate = baud" against two halving/doubling distractors (E8C11); ARQ = retransmission on detection, not redundant substitution or polynomial self-correction (E8C08); mesh nodes are NOT store-and-forward digipeaters — discovery/link establishment is keyed (E8C15); CW bandwidth does not depend on power or mod index (E8C12).
- Vocab: QAM, QPSK, symbol rate, baud, constellation diagram, PSK31, sinusoidal data pulses, ARQ, Gray code, FT8, mesh network, link establishment.
- FACT: 13 WPM CW ≈ 52 Hz (E8C05); FT8 bandwidth = 50 Hz (E8C06).

### E8D (11) — Spread spectrum, keying, codes
- Topic inventory: SS interference resistance (E8D01), direct sequence (E8D02), frequency hopping (E8D03), key clicks (E8D04–05), parity (E8D06), AFSK overmodulation and IMD (E8D07–09), Baudot vs ASCII (E8D10), ASCII advantage (E8D11).
- Must understand: spread-spectrum receivers suppress signals not using the spreading algorithm (hence interference resistance); direct sequence uses a high-speed binary bit stream to shift the phase of an RF carrier; frequency hopping rapidly varies the carrier frequency per a pseudorandom sequence; extremely short rise/fall times on CW generate key clicks — the cure is INCREASING rise and fall times; parity bits let some error types be DETECTED (not corrected); the common cause of AFSK overmodulation is excessive transmit audio level, evaluated as intermodulation distortion; acceptable maximum IMD for an idling PSK signal ≈ −30 dB; Baudot = 5 data bits/character with 2 letters-figures shift codes, ASCII = 7 or 8 bits with no shift codes; ASCII can transmit both upper- and lowercase text.
- Confusions: the direct-sequence and frequency-hopping definitions appear swapped in each other's distractors (E8D02 vs E8D03) — "phase" = DS, "frequency" = FH; key-click cure is LONGER rise/fall time, not shorter, and not output filters (E8D05); the IMD limit is NEGATIVE (−30 dB) against +5/+10/+15 dB distractors (E8D09); Baudot bit-count distractors (4/6/7 bits) surround the keyed 5 (E8D10).
- Vocab: spread spectrum, direct sequence, frequency hopping, pseudorandom sequence, key clicks, parity bit, AFSK, intermodulation distortion (IMD), Baudot, ASCII, letters/figures shift.
- FACT: idle PSK IMD max ≈ −30 dB (E8D09); Baudot 5 bits with 2 shift codes, ASCII 7/8 bits (E8D10).

---

## Subelement E9 — Antennas and transmission lines (93 questions, 8 groups, 8 exam seats)

### E9A (12) — Antenna basics, gain, ERP/EIRP
- Topic inventory: isotropic radiator (E9A01), ERP calcs (E9A02, E9A06), EIRP calc (E9A07), ERP definition (E9A03), feed-point impedance factors (E9A04), ground gain (E9A05), Fresnel zone (E9A08), efficiency (E9A09), vertical ground system (E9A10–11), dBi↔dBd conversion (E9A12).
- Must understand: the isotropic radiator is a hypothetical, lossless antenna with equal radiation in all directions — the reference for gain; ERP is the total radiated-power figure that accounts for ALL gains and losses; antenna height affects feed-point impedance (line length, tuner settings, and power level do not); ground gain = increased signal strength from ground reflections near the antenna; efficiency = radiation resistance ÷ TOTAL resistance; a ground radial system improves a ground-mounted λ/4 vertical; soil conductivity determines HF vertical ground losses; the higher the frequency, the smaller the first Fresnel zone (5.8 GHz is smallest of the listed bands).
- Math: ERP = TPO × 10^((gains − losses)/10), worked with the pool's numbers — E9A02: 150 W, −2 dB feedline, −2.2 dB duplexer, +7 dBd → net +2.8 dB → 150 × 10^0.28 = 150 × 1.905 ≈ **286 W**. E9A06: 200 W, −4 −3.2 −0.8 dB, +10 dBd → net +2 dB → 200 × 1.585 ≈ **317 W**. E9A07 (asks EIRP, gain given in dBi): 200 W, −2 −2.8 −1.2 dB, +7 dBi → net +1 dB → 200 × 1.259 ≈ **252 W**. dBd = dBi − 2.15 → E9A12: 6 − 2.15 = **3.85 dB**. dB arithmetic primer for the chapter: +3 dB ≈ ×2, +10 dB = ×10, so +2.8 dB ≈ ×1.9.
- Confusions: ERP pairs with dBd, EIRP with dBi — E9A07 says EIRP and gives dBi, E9A02/06 say ERP and give dBd; sign discipline (subtract losses, add gain) — distractor 469 W in E9A02 comes from ADDING the losses, 78.7 W from deeper sign errors; E9A06's 2000 W distractor punishes treating 10 dB as ×10 in dB-space. Efficiency divides radiation resistance by TOTAL resistance, not by "transmission resistance" and never the inverse (E9A09).
- Vocab: isotropic radiator, ERP, EIRP, dBd, dBi, ground gain, radiation resistance, antenna efficiency, first Fresnel zone.
- FACT: half-wave dipole = 2.15 dB over isotropic (underlies E9A12); 5.8 GHz → smallest first Fresnel zone (E9A08).

### E9B (11) — Radiation patterns; Figures E9-1 and E9-2
- Topic inventory: Figure E9-1 azimuth reads ×3 (E9B01–03), Figure E9-2 elevation reads ×3 (E9B04–06), gain vs total power (E9B07), far field (E9B08), Method of Moments (E9B09–11).
- Must understand: directivity redirects power, it does not create it — a lossless gain antenna and an isotropic radiator driven by the same power radiate the SAME total power (E9B07); the far field is the region where the pattern shape no longer varies with distance; antenna modeling commonly uses the Method of Moments: a wire is modeled as a series of segments each carrying a uniform current, and dropping below ~10 segments per half-wavelength can make the computed feed-point impedance wrong.
- Reading the figures (full redraw specs below): E9-1 is an azimuth free-space polar plot, 0 dB outer ring with −3/−6/−12/−24 dB rings — main lobe at 0°, −3 dB crossings at ±25° → **50° beamwidth** (E9B01); 180° response ≈ −18 dB → **F/B 18 dB** (E9B02); 90° response ≈ −14 dB → **F/S 14 dB** (E9B03). E9-2 is an elevation semicircle "Over Real Ground", −10/−20/−30/−40 dB arcs — pattern type **elevation** (E9B05), peak at **7.5° elevation** (E9B06), rear ≈ −28 dB → **F/B 28 dB** (E9B04). Stem-typo ledger: E9B04 prints "Figure E92".
- Confusions: beamwidth is measured between the −3 dB points, not between nulls (75°/30°/25° distractors in E9B01 come from reading the wrong reference); front-to-side reads the 90° value (−14 dB), not the sidelobe peaks near ±55° (−12 dB is the trap in E9B03).
- Vocab: beamwidth (−3 dB points), front-to-back ratio, front-to-side ratio, elevation/azimuth pattern, far field, Method of Moments, wire segment.
- Math: none beyond reading dB differences off the polar grids (18 dB, 14 dB, 28 dB above).

### E9C (14) — Wire antennas and phased arrays
- Topic inventory: two-vertical phased patterns (E9C01–03), long-wire behavior (E9C04), OCFD (E9C05), terminating resistor (E9C06), folded dipole (E9C07–08), G5RV (E9C09), Zepp (E9C10), seawater effect (E9C11), extended double Zepp (E9C12), height vs takeoff angle (E9C13), slope effect (E9C14).
- Must understand — the phased-array table (tested as a set):
  - Two λ/4 verticals spaced λ/2, fed 180° out of phase → figure-eight oriented ALONG the array axis (end-fire).
  - Two λ/4 verticals spaced λ/4, fed 90° out of phase → cardioid.
  - Two λ/4 verticals spaced λ/2, fed IN phase → figure-eight BROADSIDE to the array axis.
- Also: lengthening an unterminated long wire forms additional lobes that align increasingly with the wire axis; a terminating resistor makes a rhombic/long-wire pattern UNIDIRECTIONAL (bidirectional otherwise); an OCFD is fed off-center to create a similar feed-point impedance on multiple bands; a folded dipole is a λ/2 dipole with an additional parallel wire connecting its ends, ≈300 Ω feed impedance; a G5RV is a center-fed wire through a specific length of open-wire line to a balun and coax; a Zepp is an end-fed half-wavelength antenna; an extended double Zepp is a center-fed 1.25λ antenna; mounting over seawater increases low-angle radiation vs soil; raising a horizontally polarized antenna LOWERS the lowest-lobe takeoff angle; a long downhill slope lowers the main-lobe takeoff angle in the downhill direction.
- Confusions: Zepp (end-fed λ/2) vs extended double Zepp (center-fed 1.25λ) vs G5RV (open-wire matching section + balun) — E9C09/10/12 raid each other's answer text verbatim; "in phase vs 180°" swaps broadside and end-fire in E9C01/03 (the phase and the pattern orientation move together: in-phase broadside, out-of-phase end-fire, at λ/2 spacing).
- Vocab: phased array, end-fire, broadside, cardioid, OCFD (off-center-fed dipole), folded dipole, G5RV, Zepp, extended double Zepp (EDZ), terminating resistor, takeoff angle, long-wire/rhombic.
- FACT: folded dipole ≈ 300 Ω (E9C07); EDZ = center-fed 1.25 λ (E9C12).

### E9D (12) — Yagis, dishes, loading
- Topic inventory: dish gain vs frequency (E9D01), circular polarization from Yagis (E9D02), loading-coil placement (E9D03), coil reactance:resistance ratio (E9D04), driven-element length (E9D05), loading vs SWR bandwidth (E9D06), top loading (E9D07), antenna Q (E9D08), loading-coil function (E9D09), radiation resistance below resonance (E9D10), reflector vs director (E9D11), parasitic element tuning (E9D12).
- Must understand: doubling the operating frequency increases an ideal parabolic reflector's gain by 6 dB (the dish is twice as many wavelengths across); circular polarization from linear Yagis = two Yagis on the SAME axis, perpendicular to each other, driven elements at the same point on the boom, fed 90° out of phase; the most efficient loading-coil location on a short whip is near the CENTER of the radiator; loading coils should have a high reactance-to-resistance ratio to maximize efficiency; a loading coil cancels the short antenna's capacitive reactance to resonate it — but Q rises and SWR bandwidth DECREASES; top loading improves radiation efficiency; below resonance a base-fed whip's radiation resistance decreases; two-element Yagis favor a reflector over a director because it gives higher gain; parasitic elements are made longer/shorter than resonance to control phase shift.
- Confusions: higher antenna Q → SWR bandwidth DECREASES (E9D08 — the "increases" option is the trap, and it pairs with E9D06's keyed "decreased"); driven element ≈ λ/2 — the 234/f and 1005/f distractors are wire-length formulas in feet, not the element's electrical fraction (E9D05); the E9D02 distractors offer parallel-plane stacking and 180° feeding — the keyed recipe is same-axis/perpendicular/same-boom-point/90°.
- Vocab: parabolic reflector, circular polarization, loading coil, top loading, radiation efficiency, radiation resistance, reflector, director, driven element, parasitic element.
- FACT: dish gain +6 dB per frequency doubling (E9D01); Yagi driven element ≈ 1/2 wavelength (E9D05).

### E9E (10) — Matching systems (note: no E9E10)
- Topic inventory: beta/hairpin insulation (E9E01), gamma match (E9E02, E9E09), stub match (E9E03), gamma series capacitor (E9E04), beta feed impedance (E9E05), Q-section (E9E06), reflection coefficient (E9E07), Wilkinson divider (E9E08), phasing lines (E9E11).
- Must understand: a gamma match connects the coax shield to the element center and the center conductor (through a series capacitor) to a point a fraction of a wavelength off-center — it is also the match used to shunt-feed a grounded tower at its base; the gamma series capacitor cancels the unwanted inductive reactance of the gamma section; a beta/hairpin match needs a driven element electrically SHORTER than λ/2 (capacitive feed-point impedance) and requires the element insulated from the boom; a stub match is a short length of transmission line in parallel with the feed line at or near the feed point; the reflection coefficient describes the interaction of a load and a transmission line; a Wilkinson divider splits power equally between two 50-Ω loads while maintaining a 50-Ω input impedance; multiple driven elements connected through phasing lines control the antenna's radiation pattern.
- Math: quarter-wave Q-section Z0 = √(Zline × Zload) → E9E06: √(50 × 100) = 70.7 Ω → **75 Ω** line is the suitable choice among {50, 62, 75, 90}.
- Confusions: gamma = series tap off-center, beta = shunt inductor at the feed point (needs a capacitive element), stub = parallel line section — the three descriptions are dealt across E9E02/03/05's options; "insulated from the boom" belongs to beta/hairpin, not gamma (E9E01); the Q-section answer is the geometric mean, not the arithmetic mean (62 Ω distractor ≈ halfway between 50 and 75... note 75 is keyed, not 62).
- Vocab: gamma match, beta/hairpin match, stub match, Q-section (quarter-wave transformer), delta match, T-match, shunt feed, Wilkinson divider, reflection coefficient, phasing lines.

### E9F (12) — Transmission lines
- Topic inventory: velocity factor definition/cause (E9F01–03), λ/2 shorted line (E9F04), microstrip (E9F05), physical length calc (E9F06), parallel line vs coax (E9F07), foam vs solid dielectric (E9F08), λ/4 and λ/8 transformations (E9F09–12).
- Must understand: velocity factor = wave velocity in the line ÷ velocity of light in a vacuum; the dielectric insulating material has the biggest effect on VF; electrical length exceeds physical length because waves move slower in the line; open-wire parallel line has LOWER loss than plastic-dielectric coax; foam vs solid dielectric coax (all else equal): lower safe operating voltage AND lower loss per length AND higher VF — "All these choices are correct"; microstrip = precision PCB conductors above a ground plane giving constant-impedance interconnects at microwave frequencies.
- The transformation table (the group's core, six questions ride on it):
  - λ/2 line REPEATS its termination: shorted far end → very low impedance at the input (E9F04).
  - λ/4 line INVERTS its termination: shorted → very high impedance (E9F09); open → very low impedance (E9F12).
  - λ/8 line converts to reactance: shorted → inductive reactance (E9F10); open → capacitive reactance (E9F11).
- Math: physical length of a λ/2 air-insulated parallel line at 14.10 MHz: λ = 300/14.10 = 21.28 m; λ/2 ≈ **10.6 m** (E9F06; air VF ≈ 1.0). General: L(λ/2, meters) ≈ 150 × VF / f(MHz); distractors 7.0/8.5/13.3 m correspond to wrong VF or λ/3-vs-λ/2 slips.
- Confusions: the λ/4 vs λ/2 shorted-line answers are mirror images (very high vs very low) and both are tested (E9F04 vs E9F09); λ/8 shorted = INDUCTIVE, open = CAPACITIVE (E9F10 vs E9F11 — teach "short→L" via the stub-tuner intuition); VF DIVIDES the speed of light, the distractor multiplies (E9F01).
- Vocab: velocity factor, electrical length vs physical length, characteristic impedance, microstrip, dielectric, open-wire/ladder line, foam dielectric.

### E9G (11) — Smith chart; Figure E9-3
- Topic inventory: Smith chart uses (E9G01, E9G03, E9G05), coordinate families (E9G02, E9G04, E9G10), reactance axis and resistance axis on Figure E9-3 (E9G06–07), normalization (E9G08), SWR circles (E9G09), wavelength scales (E9G11).
- Must understand: a Smith chart plots normalized impedance on a coordinate system of resistance CIRCLES and reactance ARCS (the two families); it is used to calculate impedance along transmission lines and impedance/SWR values, and its classic use is determining the length and position of an impedance-matching stub; normalizing = reassigning the prime center's impedance value to the system impedance (e.g., 1.0 = 50 Ω); a third family — constant-SWR circles centered on the prime center — is added during matching-network design; the rim's wavelength scales are calibrated in fractions of transmission-line electrical wavelength; the arcs are points of constant reactance, the circles points of constant resistance.
- Reading Figure E9-3 (full redraw spec below): resistance circles strung along the horizontal axis from 0 (left, short circuit) to ∞ (right, open circuit), marked 0.2/0.5/1.0/2.0/5.0/20; reactance arcs ±0.2/±0.5/±1.0/±2.0/±5.0, upper half inductive (+jX), lower half capacitive (−jX); prime center at 1.0. Keyed: the large outer circle on which the reactance arcs terminate = **reactance axis** (E9G06); the only straight line = **resistance axis** (E9G07).
- Stub-matching procedure for the chapter (what E9G05 means in practice): (1) normalize the load and plot it; (2) draw the constant-SWR circle through it; (3) travel along the line (rim scale, toward the generator) until the circle crosses the 1.0 resistance circle; (4) the distance traveled sets the stub position, and the reactance read there sets the stub length needed to cancel it.
- Confusions: "resistance axis" vs "reactance axis" naming is the tested discrimination and the two questions share an option pool (E9G06 vs E9G07); arcs = constant REACTANCE, circles = constant resistance (E9G10 inverts them in distractors); normalization reassigns the PRIME CENTER's impedance, not an axis (E9G08).
- Vocab: Smith chart, resistance circle, reactance arc, prime center, normalized impedance, constant-SWR circle, reactance axis, resistance axis, wavelength scale.

### E9H (11) — Receiving and DF antennas
- Topic inventory: Beverage design (E9H01), 160/80 m receiving reality (E9H02), RDF (E9H03), DF-loop electrostatic shield (E9H04), small-loop DF challenge (E9H05), Beverage termination (E9H06–07), sense antenna (E9H08), pennant loop pattern (E9H09), multiturn loop output (E9H10), cardioid null for DF (E9H11).
- Must understand: a Beverage should be at least one wavelength long; on 160/80 m, atmospheric noise is so high that DIRECTIVITY matters far more than losses in a receiving antenna; receiving directivity factor (RDF) = peak antenna gain compared to average gain over the hemisphere around and above the antenna; a Beverage's terminating resistor absorbs signals arriving from the reverse direction, and the correct value is indicated by minimum SWR variation over the desired frequency range; an electrostatic shield around a small DF loop eliminates unbalanced capacitive coupling to the surroundings, improving null depth; a small wire loop's DF challenge is its bidirectional null pattern (180° ambiguity); a sense antenna modifies the DF pattern to provide a null in only one direction; a terminated single-turn loop such as a pennant is cardioid; more turns and/or more enclosed area increases a multiturn loop's output voltage.
- Confusions: RDF is NOT front-to-back ratio and not dBi/dBd (E9H03 distractors); the cardioid's DF value is its SINGLE null, not a sharp peak or high angle (E9H11); correct Beverage termination shows flat SWR across the band — not maximum DC current or minimum front-to-back (E9H06).
- Vocab: Beverage antenna, receiving directivity factor (RDF), sense antenna, pennant antenna, electrostatic shield, cardioid pattern, direction finding (DF), bidirectional null.

---

## Subelement E0 — Safety (12 questions, 1 group, 1 exam seat)

### E0A (12) — RF exposure, grounding, tower climbing
- Topic inventory: ground-rod purpose (E0A01), neighbor exposure evaluation (E0A02), most restrictive MPE range (E0A03), multi-transmitter responsibility (E0A04), microwave hazard (E0A05), separate E/H limits (E0A06), 100% tie-off (E0A07), SAR (E0A08), evaluation exemptions (E0A09), 80 m evaluation (E0A10), lanyard attachment (E0A11–12).
- Must understand: the primary function of an external earth connection/ground rod is lightning charge dissipation; a neighbor's home is general-population territory, so the station's signals there must meet the UNCONTROLLED MPE limits; MPE limits are most restrictive at 30–300 MHz (the body-resonance region); at a multi-transmitter site, every transmitter producing 5% or more of its MPE limit in an area where the total limit is exceeded shares responsibility for mitigation; the microwave hazard is that the commonly used high-gain antennas can produce high exposure levels; below 300 MHz separate E- and H-field limits exist because the body reacts to both fields AND their intensity peaks can occur at different locations ("All these choices are correct"); SAR measures the rate at which RF energy is absorbed by the body; on 80 meters an RF exposure evaluation must ALWAYS be performed; 100% tie-off means at least one lanyard is attached to the tower at all times; lanyards attach to tower LEGS; a shock-absorbing lanyard anchors ABOVE the climber's head level.
- Math: the pool requires NO MPE computation — all 12 questions are conceptual/regulatory. For chapter enrichment only: far-field power density S = ERP / (4πR²) — e.g., 100 W ERP at 10 m gives 100/(4π·10²) ≈ 0.08 mW/cm², the shape of an MPE check. Flag clearly in the text that no E0A question requires this calculation.
- Confusions: controlled vs uncontrolled MPE (neighbors = uncontrolled, E0A02 — and the distractor pair swaps "exposure" for "emission"); the 5% vs 20% contribution threshold (5% keyed, E0A04); exempt equipment — hand-held transceivers sold before May 3, 2021 are exempt (E0A09), NOT "any transceiver under 7 W" or "dishes under 1 m"; E0A10's "always evaluate" beats the power/mode-conditional distractors.
- Vocab: MPE (maximum permissible exposure), controlled/uncontrolled exposure limits, SAR (specific absorption rate), E-field/H-field limits, RF exposure evaluation, 100% tie-off, shock-absorbing lanyard, fall arrest.
- FACT: 30–300 MHz most restrictive (E0A03); 5% contribution rule (E0A04); HTs sold before May 3, 2021 exempt (E0A09); 80 m → evaluation always required (E0A10); lanyard to tower legs (E0A11), anchor above head level (E0A12).

---

## Pool figure redraw specs (R4's 9 figures)

Method: PDF pages rendered at 300 dpi (`pdftoppm`), every symbol and label verified on close-up crops; the SVGs in `canon/source/e4_2024-svgs.zip` were used to confirm structure and label text. Redraw rule (as for G7-1 in the General book): the book redraws each figure as an original SVG conveying exactly the official content — same components, same labels, same numbered positions — and never copies the published graphic. All pool figures are black line-art on white; each figure title "Figure EX-N" is centered above its drawing. In the published art the ground symbols are classic three-stroke shrinking horizontal lines (the book may substitute its slanted-stroke house style — content-neutral).

### Figure E6-1 — six FET schematic symbols (2 questions: E6A10, E6A11)
**Overall:** grid of 6 circled transistor symbols, 2 rows × 3 columns, each numbered beneath (top row 1, 2, 3; bottom row 4, 5, 6). Gate lead(s) enter from the left labeled G (or G2 over G1 on the dual-gate parts); drain lead exits top-right labeled D; source lead exits bottom-right labeled S. Every symbol: a circle enclosing a vertical channel bar; D and S connect to the top and bottom of that bar.
- **1** — JFET: single gate line from G ending in a filled arrowhead pointing AWAY from the channel (arrow points left, out of the device) = **P-channel junction FET**.
- **2** — MOSFET: gate separated from the channel bar by a gap (insulated gate; the L-shaped gate line runs parallel to the bar without touching); internal arrow on the substrate/source connection points IN toward the channel; a connection dot ties the internal source node to the S lead = **N-channel single-gate MOSFET**.
- **3** — same construction as 2 but the internal arrow points OUT (away from the channel) = **P-channel single-gate MOSFET**.
- **4** — like 2 but with TWO insulated gate lines on the left labeled G2 (top) and G1 (bottom); internal arrow points IN = **N-channel dual-gate MOSFET**.
- **5** — like 4 (G2 over G1) with the internal arrow pointing OUT = **P-channel dual-gate MOSFET**.
- **6** — JFET: single gate line with a filled arrowhead pointing INTO the channel (arrow points right) = **N-channel junction FET**.
**Question→position map:** E6A10 (N-channel dual-gate MOSFET) → **4** ✓; E6A11 (P-channel junction FET) → **1** ✓. Option pools: E6A10 {2, 4, 5, 6}; E6A11 {1, 2, 3, 6}.
**Teaching strategy:** drill the three independent discriminators: (1) JFET vs MOSFET — the JFET's arrow sits ON the gate lead (1, 6); the MOSFET's gate is insulated and the arrow is internal on the source/substrate (2–5); (2) arrow-in = N-channel, arrow-out = P-channel; (3) dual-gate = G1/G2 labels (4, 5). With those three rules every option in both questions resolves mechanically.

### Figure E6-2 — eight diode symbols (1 question: E6B10)
**Overall:** grid of 8 symbols, 2 rows × 4 columns, numbered beneath (top row 1–4, bottom row 5–8). All are horizontal two-lead devices: a filled triangle against a cathode bar unless noted.
- **1** — diode with a separate curved (bowed) line sweeping across the triangle near the cathode, like a second capacitor plate (varactor-style symbol).
- **2** — two diode triangles point-to-point sharing a central T-shaped double bar (bidirectional / back-to-back pair).
- **3** — diode whose cathode bar carries angled hooks bent at BOTH ends (the "Z" wings) = Zener-style symbol.
- **4** — plain junction diode (triangle + straight bar).
- **5** — diode with two small arrows pointing away, upward-right (light leaving) = LED.
- **6** — diode whose cathode-bar ends bend back in squared S-hooks (a hook at each end curling back toward the bar) = **Schottky diode**.
- **7** — diode inside a circle, with an angled external lead ("whisker") entering the circle from the upper right and touching the cathode region.
- **8** — circle enclosing TWO opposed diodes (one triangle up, one down, sharing the central bar) plus the same angled whisker lead at upper right.
**Question→position map:** E6B10 (Schottky) → **6** ✓. Options {1, 2, 3, 6}. Only 6 is exam-relevant; 7 and 8 (circled, whiskered — point-contact-style devices) are described structurally because no pool question names them. The distractor set is well chosen: 1 (varactor-style bow), 2 (back-to-back pair), and 3 (Zener wings) all have "something extra on the cathode bar" — the Schottky's tell is the pair of squared S-hooks at both bar ends.

### Figure E6-3 — six logic gate symbols (3 questions: E6C08, E6C10, E6C11)
**Overall:** grid of 6 gate symbols, 2 rows × 3 columns, numbered beneath (top row 1–3, bottom row 4–6). Two inputs enter from the left (single input on 5 and 6), one output exits right.
- **1** — flat-left, round-right "D" body, no output bubble = **AND**.
- **2** — same D body WITH a small output bubble = **NAND**.
- **3** — curved-input, pointed-output body, no bubble = **OR**.
- **4** — OR body WITH output bubble = **NOR**.
- **5** — triangle WITH output bubble = **NOT (inverter)**.
- **6** — triangle without bubble (swept sides) = **buffer**.
**Question→position map:** E6C08 (NAND) → **2** ✓; E6C10 (NOR) → **4** ✓; E6C11 (NOT) → **5** ✓. Option pools: E6C08 {1, 2, 3, 4}; E6C10 {1, 2, 3, 4}; E6C11 {2, 4, 5, 6}.
**Teaching strategy:** the 2×2 matrix — D-shape = AND family, curved-input = OR family; bubble = negation; triangle = buffer/inverter decided by the bubble. E6C11's options deliberately mix bubbles from both families (2, 4) with the triangle pair (5, 6).

### Figure E7-1 — transistor amplifier stage (3 questions: E7B10, E7B11, E7B12)
**Overall:** single NPN transistor in a circle (emitter arrow pointing outward, down-right — "Not Pointing iN" = NPN). Positive supply rail across the top to an open-circle terminal "+"; signal enters at open-circle "IN" (left) and leaves at open-circle "OUT" (right).
- **C1** — series coupling capacitor from IN to the base node.
- **R1** — from the + rail down to the base node.
- **R2** — from the base node to ground.
- (unlabeled resistor) — from the + rail to the collector (collector load).
- **C2** — series coupling capacitor from the collector to OUT.
- **R3** — from the emitter to ground.
- **C3** — in parallel with R3 (emitter bypass capacitor, drawn to the right of R3, both tying the emitter node to ground).
Three ground symbols (bottoms of R2, R3, C3).
**Question→position map:** E7B10 (purpose of R1 and R2) → **voltage divider bias** ✓; E7B11 (purpose of R3) → **self bias** ✓ (R3 carries the full emitter current, giving emitter-degeneration self bias; C3 bypasses it for AC only); E7B12 (circuit type) → **common emitter** ✓ (input at base, output at collector, emitter common to both). Options: E7B10 {load resistors, voltage divider bias, self bias, feedback}; E7B11 {fixed bias, emitter bypass, output load resistor, self bias}; E7B12 {common base, common collector, common emitter, emitter follower}. Note E7B11's distractor "emitter bypass" names C3's job, not R3's — the classic misread to warn about.

### Figure E7-2 — linear voltage regulator (3 questions: E7D06, E7D07, E7D08)
**Overall:** left-to-right DC regulator schematic. Open-circle input terminal "+25" (top left); open-circle output terminal "+12" (top right).
- **C1** — labeled "4000" (electrolytic, one straight one curved plate), input rail to ground (input/brute-force filter).
- **R1** — from the +25 rail down to the base node.
- **Q1** — NPN series-pass transistor in a circle: collector to the +25 rail, emitter to the +12 output rail, base straight down to the base node.
- **C2** — labeled "4000" (electrolytic), from the base node to ground.
- **D1** — Zener diode in a circle (cathode bar with the "Z" wings, pointing up), from the base node to ground; C2 and D1 are in PARALLEL from the base node to ground.
- **C3** — labeled "0.01", output rail to ground.
- **R2** — output rail to ground (the load).
Ground symbols under C1, C2, D1, C3, R2.
**Question→position map:** E7D06 (purpose of Q1) → **it controls the current to keep the output voltage constant** ✓ (series-pass element, NOT a chopper — that's the switching-regulator distractor); E7D07 (purpose of C2) → **it bypasses rectifier-output ripple around D1** ✓ (C2 parallels D1, keeping the Zener reference clean); E7D08 (circuit type) → **linear voltage regulator** ✓. Circuit story for the caption: D1 holds the base at its Zener voltage; Q1's emitter follows one B-E drop below it (+12); R1 feeds the Zener from the raw +25; C1/C2 are 4000 (µF implied) electrolytics; C3 0.01 kills output transients; R2 is the load.

### Figure E7-3 — inverting op-amp (5 questions: E7G02, E7G07, E7G09, E7G10, E7G11)
**Overall:** op-amp triangle pointing right. **R1** from the open-circle input terminal (left) to the inverting (−) input; **RF** feedback resistor from the output back to the − input, drawn across the top; non-inverting (+) input grounded; output to an open-circle terminal at the right; a separate ground symbol sits near the output terminal.
**Question→position map and math:** gain law Av = −RF/R1. E7G07: RF 470 / R1 10 = **47** ✓. E7G09: −(10,000/1,000) × 0.23 V = **−2.3 V** ✓ (sign matters; +2.3 V is the distractor). E7G10: 68 k/1.8 k = 37.8 ≈ **38** ✓. E7G11: 47 k/3.3 k = 14.2 ≈ **14** ✓. E7G02: a capacitor added across RF makes feedback impedance fall with frequency → **low-pass filter** ✓. All four numeric answers recompute exactly from the drawing's topology.
**Teaching strategy:** one formula answers five questions — the best return-on-formula in the whole pool. Watch the stem typos: E7G02 prints "in E7-3" (no "Figure"); E7G07 prints "Figure E73" (missing hyphen). Preserve both byte-exact in quotes.

### Figure E9-1 — azimuth radiation pattern, "Free-Space Pattern" (3 questions: E9B01, E9B02, E9B03)
**Overall:** full-circle polar plot. Angular labels: 0° at right, 30 and 60 upper right, 120 and 150 upper left, 180° at left, −150 and −120 lower left, −60 and −30 lower right (radial spokes every 15°; the top/bottom spokes carry no numerals). Concentric dB rings labeled outer→in: −3, −6, −12, −24; the outer circle is the 0 dB reference. Caption text "Free-Space Pattern" at upper right. A single heavy trace shows the antenna pattern.
**Trace:** main lobe centered on 0°, touching the outer ring and crossing the −3 dB ring at ≈ ±25°; sidelobes near ±50–60° at ≈ −12 dB; deep nulls (below −24 dB) near ±70–80° and flanking the rear; rear lobe at 180° at ≈ −18 dB; trace level at ±90° ≈ −14 dB.
**Question→position map:** E9B01 (3 dB beamwidth) → 2 × 25° = **50°** ✓; E9B02 (front-to-back) → 0 − (−18) = **18 dB** ✓; E9B03 (front-to-side) → **14 dB** ✓. Distractor anatomy: 75°/30°/25° in E9B01 come from reading null-to-null or one-sided widths; 12 dB in E9B03 is the sidelobe level, not the 90° level.
**Redraw checklist:** 15° spoke spacing; ring labels −3/−6/−12/−24 stacked near the top; 0° reference at right; the trace's five features (main lobe, two sidelobes, two null pairs, rear lobe) at the bearings above.

### Figure E9-2 — elevation radiation pattern, "Over Real Ground" (3 questions: E9B04, E9B05, E9B06)
**Overall:** semicircular polar plot above a horizontal baseline (the ground). Baseline runs 180° (left) to 0° (right); 90° at zenith; labeled radials 0, 30, 60, 90, 120, 150, 180 with finer subdivision spokes (7.5° spacing visible). Concentric dB arcs labeled along the baseline right of center, outer→in: −10, −20, −30, −40; the outer semicircle is 0 dB. Caption text "Over Real Ground" at upper right.
**Trace:** largest lobe hugs the horizon, peaking at ≈ 7.5° elevation and reaching the outer arc; successively smaller lobes at ≈ 22°, ≈ 38°, ≈ 52°; a cluster of small rear lobes toward 150–180° down ≈ −28 to −40 dB.
**Question→position map:** E9B04 (front-to-back) → main lobe 0 dB vs rear ≈ −28 dB = **28 dB** ✓; E9B05 (pattern type) → **elevation** ✓ (the semicircle-above-ground format is the tell; "azimuth" is the distractor); E9B06 (peak elevation angle) → **7.5°** ✓ (distractors 45/75/25 read the wrong lobes). Stem-typo ledger: E9B04 prints "Figure E92" (missing hyphen).
**Redraw checklist:** semicircle + baseline; radial labels 0/30/60/90/120/150/180; dB arc labels −40/−30/−20/−10 along the baseline (note the published order prints "-40 -30 -20 -10" left to right toward the 0° end); four forward lobes decreasing with angle; small rear-lobe cluster.

### Figure E9-3 — Smith chart (2 questions: E9G06, E9G07)
**Overall:** a simplified normalized Smith chart — one large circle, no peripheral wavelength scales. **Infinity (∞) is at the RIGHT end of the horizontal diameter** (the open-circuit point); **0 is at the LEFT end** (short circuit). The horizontal diameter is the chart's only straight line and carries the resistance-circle labels 0, 0.2, 0.5, 1.0, 2.0, 5.0, 20 left→right; the 1.0 point at mid-chart is the prime center (the normalized system impedance, e.g., 50 Ω). Constant-resistance circles are all tangent at the ∞ point, bulging left. Constant-reactance arcs sweep from the rim into the ∞ point, labeled 0.2, 0.5, 1.0, 2.0, 5.0 above the axis (inductive, +jX) and the same magnitudes (0.5, 1.0, 2.0, …) below (capacitive, −jX); every reactance arc terminates on the large outer circle.
**Question→position map:** E9G06 (name of the large outer circle on which the reactance arcs terminate) → **reactance axis** ✓; E9G07 (the only straight line) → **resistance axis** ✓. The two questions share an option pool ({prime axis, reactance axis, impedance axis, polar axis} / {reactance axis, current axis, voltage axis, resistance axis}), so "reactance axis" is correct in one and a distractor in the other — the naming pair is the whole lesson.
**Redraw checklist (the tested features are mandatory):** ∞ at right, 0 at left; resistance labels 0.2–20 ascending left→right along the single straight horizontal axis; reactance arcs terminating on the outer circle with matching +/− magnitudes above/below; prime center at 1.0. Wavelength scales are absent in the published figure — do not invent them.

---

## Consolidated watch-item (FACT) index — pure-memorization values to pin as FACT lines

E6:
- Silicon base-emitter junction: 0.6–0.7 V when biased on (E6A07).
- Gallium arsenide: used in microwave circuits; higher electron mobility (E6A01, E6E01).
- Gallium nitride: highest frequency of operation in MMICs (E6E03).
- MMIC input and output impedance: 50 ohms (E6E04).
- Typical low-noise UHF preamplifier noise figure: 0.5 dB (E6E05).
- Silicon photovoltaic cell, fully illuminated: ≈0.5 V open-circuit (E6F10–11).
- Powdered iron: highest temperature stability of the listed core materials (E6D08).
- Ferrite beads: VHF/UHF parasitic suppressors (E6D09).

E7:
- ÷16 frequency division requires 4 flip-flops (E7A04).
- Three common oscillator circuits: Colpitts, Hartley, Pierce (E7H01).
- Class AB conduction: more than 180°, less than 360° (E7B01).
- Nyquist: sample at least twice the highest frequency component (E7F05).
- 1 V at 1 mV resolution needs 10 bits (E7F06); 8 bits = 256 levels (E8A09).
- Inverting op-amp gain: Av = −RF/R1 (E7G07/09/10/11).

E8:
- Unprocessed SSB PEP-to-average power ratio: ≈2.5:1 (E8A06).
- 13 WPM Morse bandwidth: ≈52 Hz (E8C05); FT8 bandwidth: 50 Hz (E8C06).
- Acceptable maximum IMD for an idling PSK signal: −30 dB (E8D09).
- Baudot: 5 data bits, 2 letters/figures shift codes; ASCII: 7 or 8 bits (E8D10).
- Symbol rate and baud are the same (E8C11).

E9:
- Half-wave dipole gain over isotropic: 2.15 dB (so 6 dBi = 3.85 dBd, E9A12).
- Folded dipole feed-point impedance: ≈300 ohms (E9C07).
- Extended double Zepp: center-fed 1.25-wavelength antenna (E9C12).
- Parabolic reflector: +6 dB gain when frequency doubles (E9D01).
- Yagi driven element: ≈1/2 wavelength (E9D05).
- Smallest first Fresnel zone of the listed bands: 5.8 GHz (E9A08).
- λ/2 line repeats its termination; λ/4 line inverts it; λ/8 shorted = inductive, λ/8 open = capacitive (E9F04, E9F09–12).
- Beverage antenna: at least one wavelength long (E9H01).

E0:
- Most restrictive MPE frequency range: 30–300 MHz (E0A03).
- Multi-transmitter mitigation threshold: 5% of MPE limit (E0A04).
- Exempt equipment: hand-held transceivers sold before May 3, 2021 (E0A09).
- 80 meters: RF exposure evaluation must always be performed (E0A10).
- Lanyards attach to tower legs; shock-absorbing lanyard anchors above head level (E0A11–12).

---

## Distractor pattern catalog (cross-subelement)

- **Unit/magnitude swaps:** 0.6–0.7 V vs 6–7 V vs ohms (E6A07); noise figure 0.5 dB vs dBm values (E6E05); −30 dB vs +5/+10/+15 dB (E8D09).
- **Inverted ratios:** modulation index/deviation ratio questions all offer the reciprocal (0.3, 0.167, 0.47, 0.214) alongside the keyed value (E8B03–06); inverted voltage-divider and gain arithmetic in E7G distractors (24, 76, 28).
- **Definition swaps within a pair:** direct sequence vs frequency hopping (E8D02/03); linear vs switchmode regulator stem wording (E7D01/02); sample rate vs bit width (E7F10/11); pre- vs de-emphasis (E7E05/06); adaptive vs Hilbert filters (E7F02/03).
- **Family-ladder confusions:** Butterworth/Chebyshev/elliptical (E7C05–06); Class A/AB/B/C conduction angles (E7B01); product detector/discriminator/envelope detector (E7E03/10/11); gamma/beta/stub match descriptions (E9E01–05).
- **"All these choices are correct" is the keyed answer** in E6E10, E7D14, E7H13, E9F08, E0A06 — and a wrong decoy elsewhere (E6C04, E8A08, E8C03, E8C12, E9A10, E9H05, E9H10, E6F06); never teach "all of the above" as a guess heuristic.
- **ERP/EIRP sign and reference traps:** adding instead of subtracting losses (469 W, E9A02); treating dB as a linear multiplier (2000 W, E9A06); dBd/dBi pairing (E9A07).
- **Published typo stems to preserve byte-exact in quotes:** E7G02 "in E7-3", E7G07 "Figure E73", E9B04 "Figure E92".

---

## Verification ledger

- All 320 owned questions read from `canon/pool-extra.json` (E6–E0 dumped with answers marked; group inventories cross-counted by script: E6A 12, E6B 11, E6C 11, E6D 11 [no 07], E6E 12, E6F 11; E7A 11, E7B 12, E7C 11, E7D 15, E7E 11, E7F 14, E7G 12, E7H 13; E8A 11, E8B 11, E8C 15, E8D 11; E9A 12, E9B 11, E9C 14, E9D 12, E9E 10 [no 10], E9F 12, E9G 11, E9H 11; E0A 12).
- Figure→question map from the JSON `figure` fields matches the assignment exactly: E6-1→E6A10/11; E6-2→E6B10; E6-3→E6C08/10/11; E7-1→E7B10/11/12; E7-2→E7D06/07/08; E7-3→E7G02/07/09/10/11; E9-1→E9B01/02/03; E9-2→E9B04/05/06; E9-3→E9G06/07. 28 figure questions total; every keyed answer re-derived from the rendered figure (✓ marks above).
- Every question ID cited in this file was script-checked against `canon/pool-extra.json` — all resolve, except the two intentionally cited non-existent IDs E6D07 and E9E10 (documented numbering gaps).
- Every quoted numeric answer was recomputed: E7G07/09/10/11 (47, −2.3 V, 38, 14), E8B03–06 (3, 3, 1.67, 2.14), E8C05/07 (52 Hz, 15.36 kHz), E9A02/06/07/12 (286 W, 317 W, 252 W, 3.85 dB), E9E06 (75 Ω), E9F06 (10.6 m), E7F06 (10 bits), E8A09 (256).
- Published stem typos preserved for the quoting discipline: E7G07 "Figure E73", E9B04 "Figure E92", E7G02 "in E7-3".
- No other canon files, tools, or tests were modified; this file is the only artifact created.
