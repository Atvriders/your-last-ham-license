# R3 Teaching Notes — Extra Pool Subelements E1–E5

Researcher: R3. Scope: E1 (rules), E2 (operating), E3 (propagation), E4 (amateur practices & test equipment), E5 (electrical principles) — 279
questions (E1:68, E2:60, E3:39, E4:63, E5:49). Every question was read in full from `canon/pool-extra.json`; `[97.xxx]` tags are the pool's own
published references from the ID lines in `canon/pool-extra.txt` (66 tagged questions, all in E1). Untagged items are standard textbook knowledge
unless noted.

Audience model: peer-level with an experienced General. Assume HF operating fluency, Ohm's-law algebra, and General-level rules; teach only the delta
the Extra exam demands.

Errata watch: E2A13 deleted (errata 2, 2024-11-08 — E2A ends at E2A12); E4D05 deleted (errata 4, 2026-02-04 — E4D runs D01–D04, D06–D14). Gaps are
intentional; never renumber.

---

## E1 — Commission's Rules (68 questions, E1A–E1F)

E1 is pure Part 97. The Extra delta over General: (a) band-edge arithmetic for wide signals, (b) the special bands (60 m, 630 m, 2200 m), (c)
space/telemetry/telecommand vocabulary, (d) the VE system, (e) pinned numeric limits. Distractors are plausible-but-wrong numbers and swapped
definitions.

### E1A — Bandwidth vs. band edges, special bands, ships & aircraft (11)

- **Inventory:** signal-at-band-edge arithmetic (4: E1A01–E1A04); vessels/aircraft (3: E1A05, E1A10, E1A11); special allocations (3: E1A06, E1A07, E1A09); forwarding
  accountability (1: E1A08).
- **Teach:** the displayed SSB "carrier frequency" sits at the band-edge side of the signal; legality is judged on where sideband energy falls, not the dial [97.305,
  97.307(b)]. USB occupies carrier→carrier+BW; LSB carrier−BW→carrier. E1A01: USB at 14.348 MHz puts energy to 14.351 — the upper 1 kHz is out of band. E1A02: lowest
  legal LSB display = lower edge + 3 kHz [97.301, 97.305]. E1A03: 20 m ends at 14.350, so a 2.8 kHz USB data signal's highest carrier is 14.350 − 0.0028 = 14.1472 MHz
  [97.305, 97.307(b)]. E1A04: LSB at 3.601 MHz reaches ≈3.598, below the 3.600 Extra phone edge — illegal [97.301, 97.305]. Aboard US-documented craft any FCC amateur
  licensee (or alien reciprocal) may be control operator (E1A05, E1A11 [97.5]) but needs the master's/pilot's approval (E1A10 [97.11]). 60 m CW goes at the channel
  *center* (E1A06 [97.303(h)(1)]). 2200 m = 1 W EIRP (E1A07 [97.313(k)]); 630 m = 5 W EIRP except parts of Alaska (E1A09 [97.313(l)]) — EIRP, antenna gain counts.
  Message-forwarding violations belong to the *originating* station's control operator (E1A08 [97.219]).
- **Confusions:** "14.348 is outside the band" — carrier is inside, the sideband is not; 1 W (2200 m) vs. 5 W (630 m) are cross-paired as distractors, with 50/100 W
  PEP tempting HF habits.
- **Vocab:** necessary bandwidth, carrier frequency, EIRP, channelized operation, message forwarding system, control operator.
- **FACT:** 2200 m = 1 W EIRP; 630 m = 5 W EIRP; 60 m CW = channel center; 20 m top = 14.350 MHz; 75 m Extra phone bottom = 3.600 MHz.

### E1B — Spurious emissions, protected zones, antenna structures, RACES (11)

- **Inventory:** emissions & interference (3: E1B01, E1B02, E1B08); protected places (3: E1B03, E1B04, E1B05); antenna regulation (3: E1B06, E1B07, E1B11); RACES (2:
  E1B09, E1B10).
- **Teach:** spurious emission = emission outside the necessary bandwidth that can be reduced or eliminated without affecting the information (E1B01 [97.3]) — memorize
  cold. On HF, 3 kHz is an acceptable bandwidth for digital voice or SSTV (E1B02 [97.307(f)(2)]). Protect FCC monitoring facilities within 1 mile (E1B03 [97.13]); a 70
  cm repeater interfering with radiolocation must cease or mitigate (E1B04 [97.303(b)]) — 70 cm is secondary to government radiolocation. The National Radio Quiet Zone
  surrounds the National Radio Astronomy Observatory, Green Bank WV (E1B05 [97.3]). Towers near public-use airports may need FAA notification + FCC registration under
  Part 17 (E1B06 [97.15]). PRB-1 binds *state and local zoning* only and requires "reasonable accommodation" (E1B07, E1B11 [97.15]) — not HOAs. Interference to
  good-design broadcast receivers → quiet hours on offending frequencies, not shutdown (E1B08 [97.121]). RACES = any FCC-licensed station certified by the responsible
  civil defense organization (E1B09), on all frequencies authorized to the control operator (E1B10) [97.407].
- **Confusions:** NRQZ distractors (Laurel MD, White Sands, Cape Canaveral) are real sites, wrong facility; "HOAs" is the classic PRB-1 trap; RACES distractors ("club
  stations", "all but Technician") misstate the certification requirement.
- **Vocab:** spurious emission, necessary bandwidth, harmful interference, National Radio Quiet Zone, PRB-1, reasonable accommodation, RACES, HAAT, NOTAM.
- **FACT:** 1 mile FCC-facility protection; HF digital voice/SSTV = 3 kHz.

### E1C — International, MF notification, control links, emission limits (12)

- **Inventory:** international/reciprocal (4: E1C02, E1C04, E1C06, E1C11); 2200/630 m procedure (3: E1C03, E1C07, E1C12); automatic/remote control (2: E1C05, E1C08);
  emission standards (3: E1C01, E1C09, E1C10).
- - **Teach:** 60 m data max = 2.8 kHz (E1C01 [97.303]); phone is permitted across the *entire* 630 m band (E1C12 [97.305(c)]) — surprising, pin it. Foreign contacts
  limited to amateur-service remarks of a personal nature (E1C02 [97.117]). CEPT = European reciprocal, carry FCC Public Notice DA 16-1048 (E1C06, E1C11 [97.5]); IARP
  = Inter-American permit for certain countries of the Americas (E1C04). Map: CEPT→Europe, IARP→Americas. 2200/630 m access is notification, not licensing: notify the
  Utilities Technology Council with call sign + coordinates (E1C07 [97.303(g)]), operate after 30 days unless told you're within 1 km of PLC (power-line carrier)
  systems (E1C03 [97.303(g)]) — utilities were there first. Automatic control may carry third-party traffic only in RTTY/data emissions (E1C05
  [97.221(c)(1), 97.115(c)]); a failed remote-control link must kill transmissions within 3 minutes (E1C08 [97.213]). Angle modulation below 29.0 MHz: modulation index
  ≤ 1.0 at the highest modulating frequency (E1C09 [97.307]) — effectively narrowband-only on HF. Spurious emissions below 30 MHz: mean power ≥ 43 dB below the
  fundamental (E1C10 [97.307]).
- **Confusions:** UTC is a utilities body, not FCC/NTIA — distractors file with the wrong agency; 30 days / 3 min / 43 dB / 1.0 come as look-alike number ladders.
- **Vocab:** CEPT, IARP, third-party communications, automatic control, remote control, UTC, power-line carrier (PLC), modulation index, angle modulation, mean power.
- **FACT:** 60 m data = 2.8 kHz; UTC = 30 days / 1 km PLC; control-link failure = 3 min; index 1.0 below 29 MHz; HF spurious = −43 dB.

### E1D — Space, telemetry, telecommand, beacons, one-way rules (12)

- **Inventory:** definitions (3: E1D01, E1D03, E1D12); encryption & authority (3: E1D02, E1D10, E1D11); ID/posting/power (3: E1D04, E1D05, E1D06); space allocations
  (3: E1D07, E1D08, E1D09).
- **Teach:** telemetry = *one-way* transmission of measurements at a distance (E1D01 [97.3]); the "initiates/modifies/terminates a device" distractor is the definition
  of *telecommand* — the pool swaps them deliberately. Space telecommand station = station transmitting to initiate, modify, or terminate space-station functions
  (E1D03 [97.3(a)(45)]); encrypted messages are allowed *only* for space telecommand (E1D02 [97.211(b)]) — the one encryption exception worth pinning. Balloon
  telemetry ID = call sign only (E1D04 [97.119(a)]). A telecommanded station on/within 50 km of Earth posts all three: license photocopy, licensee label,
  control-operator label (E1D05 [97.213(d)] — an all-of-the-above). Model-craft telecommand max = 1 W (E1D06 [97.215(c)]). Space-station allocations [97.207]: HF
  40/20/15/ 10 m only — WARC bands excluded (E1D07); VHF = 2 m only (E1D08); UHF = 70 cm and 13 cm (E1D09). Eligibility: any station designated by the space-station
  licensee may telecommand (E1D10 [97.211]); any amateur per operator privileges may be an Earth station (E1D11 [97.209]). One-way transmissions belong to space,
  beacon, and telecommand stations (E1D12 [97.207(e), 97.203(g)]).
- **Confusions:** telemetry/telecommand swap; "30/17/10 m" adds WARC bands; "6 m and 2 m" feels right to VHF ops and is wrong; invented AMSAT/ITU approval bodies in
  E1D10/E1D11.
- **Vocab:** telemetry, telecommand, space telecommand station, Earth station, space station, beacon station, one-way communication, model craft.
- **FACT:** model-craft telecommand = 1 W; space bands: HF 40/20/15/10 m, VHF 2 m, UHF 70+13 cm.

### E1E — Volunteer examiner system (11)

- **Inventory:** roles & accreditation (4: E1E02, E1E03, E1E04, E1E06); session conduct (3: E1E05, E1E07, E1E08); paperwork & penalties (4: E1E01, E1E09, E1E10, E1E11).
- **Teach:** VEC = an *organization* with an FCC agreement to coordinate, prepare, and administer exams (E1E03 [97.521]); the VECs maintain the question pools (E1E02
  [97.523]) — not the FCC, not "the ARRL" (a VEC, not *the* VEC). VE accreditation = a VEC confirming FCC qualifications (E1E04 [97.509, 97.525]); each administering
  VE is responsible for conduct and supervision (E1E06 [97.509]). Failed candidate → return the application to the examinee (E1E05 [97.509(j)]); candidate ignores
  instructions → immediately terminate that candidate's exam (E1E07 [97.509, 97.511]); no exams for relatives listed in the rules (E1E08 [97.509]). Passing → three VEs
  certify qualification and compliance (E1E11 [97.509(i)]); documents go to the coordinating VEC per its instructions (E1E10 [97.509(m)]) — VEs never issue licenses
  nor file with the FCC directly. Reimbursement only for out-of-pocket costs of preparing, processing, administering, coordinating exams (E1E01 [97.527]) — teaching a
  course doesn't count. Fraudulent administration → revocation of station grant + suspension of operator grant (E1E09 [97.509]).
- **Confusions:** the pool tests VE-vs-VEC-vs-FCC job assignment; teach the flow candidate → VE team → VEC → FCC. Employees and friends may be examined; only listed
  relatives are barred. Fine/prison distractors are criminal penalties that don't apply.
- **Vocab:** VE, VEC, accreditation, administering VE, CSCE, examination element.
- **FACT:** 3 VEs certify; VECs maintain the question pools.

### E1F — Spread spectrum, reciprocal, amplifiers, Line A, business, aux (11)

- **Inventory:** novel emissions (2: E1F01, E1F09); foreign licensees (1: E1F02); amplifiers (2: E1F03, E1F11); geography (2: E1F04, E1F05); prohibited communications
  (2: E1F07, E1F08); STA & auxiliary (2: E1F06, E1F10).
- **Teach:** spread spectrum only above 222 MHz (E1F01 [97.305]). Canadian licensees operate on their home license's terms, capped at US Extra privileges (E1F02
  [97.107]). Amplifiers: a dealer may sell a non-certificated below-144 MHz amplifier only if built or modified by an amateur for amateur use (E1F03 [97.315]);
  certification requires meeting spurious standards at the lesser of 1500 W or full output (E1F11 [97.317]). Line A runs roughly parallel to and *south* of the US–Canada border
  (E1F04 [97.3]); contiguous-48 stations north of Line A may not transmit 420–430 MHz (E1F05 [97.303]) — protects Canadian systems. Business traffic is fine when
  neither the amateur nor their employer has a pecuniary interest (E1F07 [97.113]); communications for hire or material compensation are prohibited (E1F08
  [97.113(c)]); encoding to obscure meaning is barred even on mesh (E1F09). STA = Special Temporary Authority, e.g. for experimental amateur communications (E1F06).
  Auxiliary-station control operator: Technician or higher (E1F10 [97.201]).
- **Confusions:** the 50/144/222/420 ladder in E1F01; "$25/$50" invented thresholds in E1F07 (the rule is zero pecuniary interest); "General or higher" trap in E1F10 —
  Technicians qualify.
- **Vocab:** spread spectrum, Line A, STA, external RF power amplifier, FCC certification, pecuniary interest, auxiliary station, mesh network.
- **FACT:** SS above 222 MHz only; north of Line A: no 420–430 MHz; amp test = lesser of 1500 W / full output.

---

## E2 — Operating (60 questions, E2A–E2E)

Operating craft, not rules. Almost no math; wins come from precise vocabulary (satellite modes, TV standards, WSJT mode names, APRS frames).
Distractors recycle real-but-wrong terms from neighboring topics.

### E2A — Amateur satellites (12)

- **Inventory:** orbits & passes (4: E2A01, E2A06, E2A10, E2A11); transponders (4: E2A02, E2A03, E2A07, E2A08); mode designators (3: E2A04, E2A05, E2A09);
  store-and-forward (1: E2A12).
- **Teach:** ascending pass = south→north (crossing the equator going up) (E2A01); Keplerian elements = the orbit-defining parameter set tracking software eats
  (E2A06); geostationary = appears fixed (E2A10). A linear transponder is a bent-pipe translator: uplink mixed with a local oscillator, difference product
  retransmitted (E2A03); being linear it relays any mode — FM, CW, SSB, SSTV, PSK, packet (E2A07). In an inverting transponder all three hold: USB↔ LSB swap, band
  position reversed, Doppler partially cancels (E2A02 — all-of-the-above). Downlink power is shared; excessive uplink ERP captures the transponder's AGC and steals
  downlink power from everyone (E2A08). "Mode" = the uplink/downlink band pair (E2A04); the mode letters specify uplink and downlink frequency ranges, uplink first
  (E2A05). L band = 23 cm, S band = 13 cm (E2A09) — microwave letters, not "long/short". Circular polarization at the ground station mitigates spin modulation and
  Faraday rotation (E2A11). Store-and-forward = orbiting mailbox holds digital messages for later download (E2A12).
- **Confusions:** "mode" ≠ FM-vs-SSB and ≠ LEO-vs-GEO; ascending/descending is latitude direction, not altitude; E2A02's sub-facts appear singly as distractors elsewhere.
- **Vocab:** ascending/descending pass, Keplerian elements, LEO/HEO/geostationary, linear transponder, inverting transponder, mode designator, L/S band, spin
  modulation, Faraday rotation, store-and-forward, ERP.
- **FACT:** L band = 23 cm; S band = 13 cm.

### E2B — Television: fast-scan ATV, SSTV, digital TV (12)

- **Inventory:** NTSC/fast-scan (4: E2B02, E2B03, E2B05, E2B08); vestigial sideband (1: E2B06); SSTV (5: E2B04, E2B09, E2B10, E2B11, E2B12); digital TV (2: E2B01, E2B07).
- **Teach:** NTSC = 525 lines per frame, interlaced — odd lines one field, even lines the next (E2B02, E2B03). VSB = AM with one full sideband plus a vestige of the
  other — cuts bandwidth while preserving low-frequency video fidelity (E2B05, E2B06). Analog SSTV: brightness is encoded by tone *frequency* (E2B10); color is sent as
  sequential color lines (E2B04); the VIS code announces the SSTV mode so software auto-selects (E2B11); specific tone frequencies trigger each new line (E2B12);
  DRM-protocol SSTV is receivable on an ordinary SSB receiver (E2B09). Digital TV: coding rate 3/4 means 25% of transmitted data is forward-error- correction overhead
  (E2B01); amateur DVB-T uses QAM and QPSK (E2B07). 70 cm fast-scan ATV is watchable on analog cable-ready TVs by using frequencies shared with cable channels (E2B08).
- **Confusions:** 525 vs. 30/60 (frame/field rates) vs. 1080 (HD); VIS identifies the *mode*, not the station, and isn't vertical sync despite the name; VSB ≠ "one
  sideband inverted".
- **Vocab:** NTSC, interlaced scanning, field/frame, vestigial sideband, chroma, SSTV, VIS code, DRM, DVB-T, QAM, QPSK, coding rate, FEC.
- **FACT:** NTSC = 525 lines; coding rate 3/4 = 25% FEC.

### E2C — Contesting, DX, logging, mesh, remote operation (12)

- **Inventory:** contest/DX practice (5: E2C03, E2C05, E2C06, E2C10, E2C11); log formats (3: E2C02, E2C07, E2C08); mesh (2: E2C04, E2C09); remote control (2: E2C01,
  E2C12).
- **Teach:** contest-free by convention: 30 m (E2C03); VHF/UHF contest SSB/CW clusters in the weak-signal segment near the calling frequency (E2C06). Split operation
  serves all three purposes: keeps callers off the DX frequency, improves efficiency, lets stations call where licensed (E2C10 — all-of-the-above). In a pileup send
  your full call sign once or twice (E2C11). QSL manager handles a DX station's confirmations (E2C05). ADIF = log-data exchange; Cabrillo = contest-log submission
  (E2C02, E2C07); LoTW confirms special-event, DX, and WAS contacts alike (E2C08). Mesh runs on channels shared with unlicensed Part 15 data services using wireless
  routers with custom firmware, e.g. AREDN (E2C04, E2C09). Remote operation of a US transmitter needs *no additional ID indicator* (E2C01) — pin this. Latency = delay
  between control action and the change in the transmitted signal (E2C12).
- **Confusions:** ADIF vs. Cabrillo swapped in distractors; latency distractors (jitter, hang time, anti-VOX) are real terms with other meanings; "last two letters of
  your call" is a real (bad) pileup habit.
- **Vocab:** split operation, pileup, QSL manager, LoTW, ADIF, Cabrillo, weak-signal segment, calling frequency, mesh network, AREDN, latency.
- **FACT:** no contests on 30 m; remote control needs no special indicator.

### E2D — Digital modes in the field: WSJT, APRS, EME/meteor tools (11)

- **Inventory:** mode-to-job (4: E2D01, E2D03, E2D04, E2D05); WSJT detail (2: E2D02, E2D09); EME technique (1: E2D06); APRS internals (4: E2D07, E2D08, E2D10, E2D11).
- **Teach:** pin the mode→job map: MSK144 → meteor scatter (E2D01); Q65 → EME (E2D03); APRS → real-time balloon tracking (E2D04); JT65 → decodes very-low-SNR signals
  (E2D05) using multitone AFSK (E2D09). FT8/FT4 in a VHF contest exchange grid square in place of the SNR report (E2D02). EME runs on time-synchronous transmit/receive
  alternation (E2D06) — the discipline WSJT automates. APRS = AX.25 (E2D07); beacons use Unnumbered Information (UI) frames — connectionless, no ack (E2D08); relays
  are packet digipeaters (E2D11); WIDE3-1 = three hops requested, one remaining — the counter decrements per digipeater (E2D10).
- **Confusions:** MSK144/Q65/JT65 is the most-shuffled triplet in E2D — anchor by purpose (meteor pings are milliseconds → fast short bursts; EME needs long
  averaging); WIDE3-1's "3-1" is "of 3, 1 left", not stations or subcarriers; JT65's 65 is the tone count, not bandwidth or baud.
- **Vocab:** MSK144, Q65, JT65, FT8/FT4, WSPR, APRS, AX.25, UI frame, digipeater, WIDE path, grid square, EME, meteor scatter, multitone AFSK.
- **FACT:** MSK144 = meteor scatter; Q65 = EME; APRS = AX.25 UI frames.

### E2E — Digital mode characteristics & mechanics (13)

- **Inventory:** WSJT-X internals (6: E2E02, E2E03, E2E04, E2E06, E2E07, E2E10); keyboard modes & files (3: E2E05, E2E08, E2E09); modulation mechanics (2: E2E01,
  E2E11); ALE & throughput (2: E2E12, E2E13).
- **Teach:** below 30 MHz data emissions use FSK (E2E01); direct FSK shifts the transmitter VFO itself, AFSK feeds audio tones into an SSB rig (E2E11). WSJT-X timing =
  synchronized computer clocks (E2E02); FT8 cycle = 15 s (E2E06); FT4's "4" = four-tone continuous-phase FSK (E2E03); FST4 = four-tone Gaussian FSK with variable T/R
  periods and seven tone spacings (E2E04 — all-of-the-above); Q65 averages multiple receive cycles where JT65 doesn't (E2E07). WSPR is beacon-only — no
  keyboard-to-keyboard (E2E05). PSK31 uses variable-length varicode — common letters get short codes (E2E09). PACTOR transfers binary files on HF (E2E08); PACTOR IV
  has the highest throughput of the listed modes in clear conditions (E2E13); FT8 has the narrowest bandwidth of the listed modes, ~50 Hz (E2E10). ALE constantly scans
  a frequency list and activates on the designated call sign (E2E12).
- **Confusions:** narrowest-bandwidth (FT8) vs. highest-throughput (PACTOR IV) are separate questions with swapped option sets (E2E10/E2E13); FST4's all-true clauses
  reappear as lone distractors.
- **Vocab:** FSK vs. AFSK, direct FSK, continuous phase, GFSK, varicode, WSPR beacon, ALE, PACTOR, throughput, T/R cycle.
- **FACT:** FT8 cycle = 15 s; FT8 narrowest listed; PACTOR IV fastest listed.

---

## E3 — Propagation (39 questions, E3A–E3C)

No math. A taxonomy subelement: know each exotic mode's cause, frequency range, geometry, and time pattern. Distractors attach right numbers to wrong
modes.

### E3A — EME, aurora, meteor scatter, ducts, EM-wave fundamentals (14)

- **Inventory:** EME (3: E3A01, E3A02, E3A03); EM-wave physics (4: E3A04, E3A05, E3A10, E3A14); tropospheric ducts (2: E3A07, E3A11); meteor scatter (2: E3A08, E3A09);
  aurora (2: E3A12, E3A13); MUF at night (1: E3A06).
- **Teach:** EME stations can be at most ~12,000 miles apart with the moon mutually visible (E3A01); least path loss at perigee (E3A03); libration fading = fluttery,
  irregular fading from multipath off the moon's rough, wobbling face (E3A02). EM anatomy: E and H fields at right angles to each other, propagation at right angles to
  both (E3A04, E3A05); speed through a medium is set by its index of refraction (E3A10); circular polarization = fields rotating as the wave advances (E3A14) — links
  to E2A11. MUF falls after dark → move to a lower HF band (E3A06). Microwave ducts form over large bodies of water, typical range 100–300 miles (E3A07, E3A11). Meteor
  trails ionize at E-region height; best scatter 28–148 MHz (E3A08, E3A09) — pairs with MSK144 (E2D01). Auroral propagation follows severe geomagnetic storms; signals
  arrive phase-distorted, so CW is the most usable mode (E3A12, E3A13).
- **Confusions:** perigee vs. apogee vs. full moon (bright ≠ close); "90° out of phase" vs. "at right angles" in E3A05 — the fields are in time-phase but spatially
  perpendicular, and the exam wants the geometry; meteor scatter is E region, not the reflexive F2.
- **Vocab:** EME, perigee/apogee, libration fading, tropospheric duct, meteor scatter, E region, auroral propagation, MUF, index of refraction, circular polarization.
- **FACT:** EME max ≈ 12,000 mi; meteor scatter 28–148 MHz, E region; ducts 100–300 mi over water.

### E3B — Transequatorial, long path, chordal hop, sporadic E, ground wave (13)

- **Inventory:** TEP (3: E3B01, E3B02, E3B03); wave splitting (1: E3B04); darkness & long path (3: E3B05, E3B06, E3B07); ground wave (2: E3B08, E3B13); sporadic E (2:
  E3B09, E3B11); chordal hop (2: E3B10, E3B12).
- **Teach:** TEP: stations 2,000–3,000 miles apart on a path perpendicular to the geomagnetic equator (E3B01); max range ~5,000 miles (E3B02); most likely
  afternoon/early evening (E3B03); mechanism is field-aligned ducting between equatorial anomalies. The ionosphere splits waves into independently propagating,
  elliptically polarized ordinary and extraordinary waves (E3B04). 160 m long-haul needs a path entirely in darkness — D-region absorption kills sunlit paths (E3B05);
  long path is most frequent on 40 and 20 m (E3B06); lower takeoff angle → longer hops (E3B07). Ground wave: vertical polarization only (E3B13), max range decreases as
  frequency rises (E3B08) — why 160 m ground wave outreaches 10 m. Sporadic E peaks around the solstices, especially the summer solstice (E3B09), and is a daytime mode
  — between sunrise and sunset (E3B11). Chordal hop = successive ionospheric refractions without intermediate ground reflection (E3B12); skipping the lossy ground
  bounce means less loss than ordinary multi-hop (E3B10).
- **Confusions:** TEP runs *across* the geomagnetic equator, not along it; station separation (2,000–3,000 mi) vs. max path (5,000 mi) are two numbers in two
  questions; E3B11's "sunset–midnight" distractor tempts 6 m ops who work evening Es — pool answer is sunrise-to-sunset.
- **Vocab:** transequatorial propagation (TEP), geomagnetic equator, ordinary/extraordinary waves, long path, takeoff angle, ground wave, sporadic E (Es), chordal hop,
  multi-hop.
- **FACT:** TEP 2,000–3,000 mi / 5,000 mi max / afternoon–early evening; Es = solstices (summer) + sunrise-to-sunset; ground wave = vertical, range falls with frequency.

### E3C — Space weather & propagation tools (12)

- **Inventory:** indices & events (6: E3C01, E3C02, E3C03, E3C07, E3C08, E3C12); IMF (2: E3C04, E3C05); radio horizon (1: E3C06); data & tools (3: E3C09, E3C10, E3C11).
- **Teach:** sudden short-term HF blackouts = solar flares (X-rays ionize the sunlit D region) (E3C01); a sudden broadband rise in HF background noise likewise means a
  flare or CME impact (E3C12). Rising A- or K-index = increasing geomagnetic disturbance (E3C02); elevated indices hammer paths through the auroral oval with
  absorption (E3C03). Bz = the north–south component of the interplanetary magnetic field (E3C04); *southward* Bz couples solar-wind energy into the magnetosphere →
  disturbed conditions (E3C05). Flare classes ascend A→B→C→M→X, X strongest (E3C07); geomagnetic storms use the G scale, G5 = extreme (E3C08) — two scales, two top
  letters. VHF/UHF radio horizon ≈ 15% farther than the geographic horizon via atmospheric refraction (E3C06). Reporting networks (PSK Reporter, WSPRNet, RBN) report
  digital-mode and CW sightings (E3C09); the 304A index measures UV at 304 angstroms, correlated to solar flux (E3C10); VOACAP models HF propagation (E3C11).
- **Confusions:** three scales interleaved — flare letters (X>M>C>B>A), G-scale (G5 top), K-index (0–9); "north-oriented IMF" is the calm condition, E3C05 tests the
  inversion; 304A is angstroms of UV, not GHz or degrees.
- **Vocab:** A-index, K-index, Bz, interplanetary magnetic field, flare classes, CME, G-scale storm, sudden ionospheric disturbance, radio horizon, 304A, VOACAP,
  reporting network.
- **FACT:** radio horizon +15%; X strongest flare; G5 extreme storm; southward Bz = disturbed.

---

## E4 — Amateur Practices & Test Equipment (63 questions, E4A–E4E)

The workbench subelement: instruments, receiver specs, RFI hunting. Light but real math (dB bookkeeping, one wattmeter subtraction, one bandwidth
ratio) — see the E4 math handbook.

### E4A — Oscilloscope, spectrum analyzer, counter, antenna analyzer (11)

- **Inventory:** oscilloscopes (5: E4A01, E4A04, E4A06, E4A09, E4A10); spectrum analysis (2: E4A02, E4A03); frequency counter (1: E4A05); antenna analysis/SWR (3:
  E4A07, E4A08, E4A11).
- **Teach:** a digital scope's highest accurate frequency is set by the ADC sampling rate; undersampling produces aliasing — a false, jittery low-frequency copy
  (E4A01, E4A06). Compensate a ×10 probe on the calibrator square wave until the flat tops are flat (E4A04); keep the probe ground lead short (E4A09); line triggering
  locks to the AC line and is the stable choice for power-supply ripple (E4A10). Spectrum analyzer = amplitude (vertical) vs. frequency (horizontal) — the tool for
  transmitter spurs and intermod products (E4A02, E4A03); a scope is amplitude vs. time. A prescaler divides high frequencies into the counter's range (E4A05). An
  antenna analyzer computes SWR and impedance directly and can measure velocity factor, cable length, and tuned-circuit resonance (E4A07, E4A11); SWR is measurable by
  directional wattmeter, VNA, or antenna analyzer — all three (E4A08).
- **Confusions:** time-domain vs. frequency-domain axes swapped; prescaler divides (the "multiply" distractor inverts it); aliasing is a sampling artifact, not a
  calibration error.
- **Vocab:** sampling rate, aliasing, probe compensation, trigger modes (line/edge/single- shot), spectrum analyzer, prescaler, antenna analyzer, directional wattmeter.
- **FACT:** line trigger for ripple; spectrum analyzer = amplitude vs. frequency.

### E4B — Accuracy, S parameters, VNA, power, IMD testing (11)

- **Inventory:** instrument accuracy (2: E4B01, E4B02); S parameters & VNA (6: E4B03, E4B04, E4B05, E4B07, E4B09, E4B11); power & Q measurement (2: E4B06, E4B08); IMD
  method (1: E4B10).
- **Teach:** counter accuracy is dominated by time-base accuracy (E4B01); a meter's Ω/V rating × full-scale voltage = its input impedance (E4B02: 20 kΩ/V × 10 V = 200
  kΩ). S parameters describe a two-port; subscripts name the ports measured (E4B07); S21 = forward gain (E4B03); S11 = input return loss/reflection coefficient,
  equivalent to VSWR (E4B04); a two-port VNA measures filter frequency response, input/output impedance, reflection coefficient (E4B09, E4B11); VNA calibration uses
  short, open, and 50 Ω loads (E4B05). Absorbed power = forward − reflected: E4B06's 100 W − 25 W = 75 W. Q of a series-tuned circuit comes from the bandwidth of its
  frequency response, Q = f/BW (E4B08) — bridges to E5A11/E5A12. Transmitter IMD test: two non-harmonically related *audio* tones into the mic input, RF output
  observed on a spectrum analyzer (E4B10).
- **Confusions:** S11 vs. S21 numbering — port 1 in, port 2 out, read S21 as "into 2 from 1"; E4B06 distractors add (125 W) instead of subtracting; the RF-tones IMD
  distractor describes a receiver test — transmitter IMD uses AF tones.
- **Vocab:** time base, ohms-per-volt, S parameters (S11/S21/S12/S22), return loss, reflection coefficient, VNA, SOL calibration, forward/reflected power, two-tone IMD
  test.
- **FACT:** VNA cal = short/open/50 Ω; S21 = forward gain; S11 = return loss.

### E4C — Receiver noise, selectivity, phase noise, overload (14)

- **Inventory:** noise theory (4: E4C04, E4C05, E4C06, E4C07); overload & phase noise (4: E4C01, E4C08, E4C11, E4C13); selectivity architecture (5: E4C02, E4C09,
  E4C10, E4C12, E4C14); FM capture (1: E4C03).
- **Teach:** noise figure = dB ratio of receiver noise to the theoretical minimum (E4C04); reference floor −174 dBm in 1 Hz at room temperature (E4C05); noise scales
  with bandwidth — E4C06: 50→1000 Hz = 10·log10(20) = 13 dB; MDS = minimum discernible signal (E4C07). Reciprocal mixing: LO phase noise mixes with strong adjacent
  signals and dumps noise onto the desired signal (E4C13); the same mechanism makes SDR master-clock phase noise dangerous (E4C01). SDR overload = input peaks
  exceeding the ADC reference voltage (E4C08). A high first IF eases image rejection (E4C09); a front-end filter/preselector removes strong out-of-band signals before
  they can intermod (E4C02); selectable bandwidths match the mode for best SNR (E4C10); a narrow roofing filter improves blocking dynamic range by attenuating strong
  close-in signals early (E4C12); IF Shift slides the passband away from adjacent interference (E4C14). On low HF bands, attenuation costs almost nothing because
  atmospheric noise still exceeds internal noise (E4C11). Capture effect: in FM the stronger co-channel signal suppresses the weaker (E4C03).
- **Confusions:** reciprocal mixing (phase noise × one strong signal) vs. IMD (nonlinearity × two signals) — E4C13's distractor defines IMD; noise figure / noise floor
  / MDS are three distinct terms, and −174 dBm is physics, not a spec; roofing filter narrows early, IF Shift moves late.
- **Vocab:** noise figure, noise floor, MDS, thermal noise, phase noise, reciprocal mixing, capture effect, blocking dynamic range, roofing filter, preselector, image
  response, IF Shift, ADC reference voltage, overload.
- **FACT:** −174 dBm/Hz floor; 50→1000 Hz = +13 dB.

### E4D — Dynamic range, intermodulation, link budgets (13; E4D05 deleted)

- **Inventory:** dynamic range & desense (4: E4D01, E4D02, E4D06, E4D07); intermod mechanics (5: E4D03, E4D04, E4D08, E4D09, E4D11); intercept point (1: E4D10);
  link-budget math (3: E4D12, E4D13, E4D14).
- **Teach:** blocking dynamic range = dB from noise floor to the level causing 1 dB gain compression (E4D01); poor dynamic range shows up as cross-modulation and
  desensitization from strong adjacent signals (E4D02); desensitization = sensitivity loss from a strong nearby signal (E4D06), tamed by attenuation before the first
  RF stage (E4D07). Intermod is born in nonlinear circuits (E4D08); two close repeaters intermod when signals mix in a final amplifier (E4D03); a properly terminated
  circulator on the transmitter output isolates it (E4D04); a preselector raises out-of-band rejection (E4D09). Odd-order products matter because two in-band signals
  yield odd-order products that also land in-band, e.g. 2f1−f2 (E4D11). IP3 of 40 dBm = the extrapolated point where two 40 dBm inputs would produce third-order
  products equal to the inputs — an extrapolation, not a working level (E4D10). Link budgets are pure dB bookkeeping: E4D12 = +8 dB margin, E4D13 = −51 dBm received,
  E4D14 = −100 dBm = 0.1 pW (worked below).
- **Confusions:** blocking DR (one signal, compression) vs. IMD DR (two signals, third-order) — E4D01's distractors define the IMD version; circulator fixes energy
  coming *back into* the transmitter, the band-pass distractor treats the wrong path.
- **Vocab:** blocking dynamic range, 1 dB compression, desensitization, cross-modulation, intermodulation, IP3, circulator, preselector, link margin, path loss, MDS.
- **FACT:** odd-order products fall in-band; E4D05 deleted by errata 4 — do not renumber.

### E4E — Noise tools, RFI sources & cures, grounding (14)

- **Inventory:** DSP noise tools (4: E4E01, E4E02, E4E03, E4E09); RFI signatures (4: E4E06, E4E10, E4E11, E4E12); RFI cures (2: E4E04, E4E05); common-mode (2: E4E07,
  E4E08); grounding (2: E4E13, E4E14).
- **Teach:** tool-to-noise map: noise blanker → impulse noise (ignition, power-line) (E4E03); DSP noise reduction → broadband white, ignition, and power-line noise
  (E4E02 — all-of-the- above); a blanker can distort strong signals so they *appear* to cause spurious emissions (E4E09); an automatic notch filter hunting a carrier
  can notch out your own CW signal (E4E01). Cures: alternator/charging noise → ferrite chokes on the charging leads (E4E04); AC-motor RFI → brute-force AC-line filter
  in series with the motor leads (E4E05). Signatures: network equipment → unstable modulated/unmodulated signals at specific frequencies (E4E06); switch-mode supplies
  → carriers at regular intervals across a wide range (E4E12); arcing thermostats, doorbell transformers, flickering displays → intermittent roaring/buzzing (E4E10 —
  all three); corroded metal joints near broadcast sites mix and re-radiate signals — the rusty-bolt effect (E4E11). Common-mode current flows equally on all
  conductors (E4E08) and is what makes shielded cables radiate or pick up interference (E4E07); chokes kill common-mode without touching the differential signal. Surge
  protectors mount on the single point ground panel (E4E13), whose job is ensuring all lightning protectors fire simultaneously, preventing lethal chassis-to-chassis
  potentials (E4E14).
- **Confusions:** blanker (impulse) vs. DNR (broadband) vs. ANF (steady tones) boundaries; common- vs. differential-mode inverted in distractors; series-choke-good /
  series-capacitor- bad placement shuffles in E4E04/E4E05.
- **Vocab:** noise blanker, DNR, ANF, impulse noise, brute-force line filter, ferrite choke, common-/differential-mode current, switch-mode power supply, rusty-bolt
  effect, single point ground panel, surge protector.
- **FACT:** SMPS = evenly spaced carriers; surge protector on the SPGP.

### E4 math handbook (pool-number-verified)

1. **Absorbed power** — P_load = P_fwd − P_refl. E4B06: 100 − 25 = 75 W.
2. **Noise floor vs. bandwidth** — ΔdB = 10·log10(BW2/BW1). E4C06: 10·log10(1000/50) = 13 dB.
3. **dBm ↔ watts** — P(W) = 10^((dBm−30)/10). E4D14: −100 dBm → 10⁻¹³ W = 0.1 pW.
4. **Link budget** — P_rx = P_tx + G_tx + G_rx − losses − path loss. E4D13: 40+6+3−100 = −51 dBm (each distractor omits exactly one gain: −54, −57, −60).
5. **Link margin** — margin = P_rx − MDS − required SNR. E4D12: P_rx = 40+10−3−136 = −89 dBm; −89−(−103) = 14 dB over MDS; 14−6 = +8 dB. Sign-flip distractors (−8,
   ±14) punish skipping the SNR reserve.
6. **Voltmeter input Z** — Z_in = Ω/V × full-scale (E4B02): 20 kΩ/V × 10 V = 200 kΩ.

---

## E5 — Electrical Principles (49 questions, E5A–E5D)

The only heavily mathematical subelement in R3's scope. Teach complex arithmetic as a *plotting* skill — three of the hardest questions (E5C10–E5C12)
are plotting exercises on Figure E5-1.

### E5A — Resonance and Q (13)

- **Inventory:** resonance phenomena (6: E5A01, E5A03, E5A04, E5A06, E5A07, E5A08); frequency calculations (2: E5A02, E5A10); Q definitions & effects (5: E5A05, E5A09,
  E5A11, E5A12, E5A13).
- **Teach:** at resonance X_L = X_C and cancels. Series RLC: |Z| ≈ R (minimum), line current maximum, V and I in phase (E5A03, E5A08). Parallel RLC: |Z| ≈ R (maximum —
  the pool's "approximately equal to circuit resistance" assumes the parallel-R model), input current minimum, but *circulating* current inside the L–C loop maximum
  (E5A04, E5A06, E5A07) — keep "circulating" vs. "input" straight; that word swap is the E5A06/E5A07 trap. Resonant rise: series voltages across L and C can each
  exceed the applied voltage by ≈ Q (E5A01); raising series Q raises internal voltages (E5A13) — why tank capacitors arc. Q: series Q = X/R, parallel Q = R/X (E5A09);
  higher Q in a matching network → narrower matching bandwidth (E5A05); half-power BW = f0/Q (E5A11, E5A12).
- **Confusions:** series vs. parallel behaviors are mirror images and the pool asks both directions; R never enters the resonance formula — E5A02/E5A10 hand you a
  resistor as bait.
- **Vocab:** resonance, resonant frequency, half-power bandwidth, Q, loaded/unloaded Q, circulating current, resonant voltage rise, matching network.
- **FACT:** f0 = 1/(2π√(LC)); BW = f0/Q; series Q = X/R, parallel Q = R/X.

### E5B — Time constants, admittance/susceptance, phase angles (12)

- **Inventory:** RC time constants (2: E5B01, E5B04); admittance/susceptance (5: E5B02, E5B03, E5B05, E5B06, E5B12); ELI/ICE phase rules (2: E5B09, E5B10); phase-angle
  calcs (3: E5B07, E5B08, E5B11).
- **Teach:** one time constant τ = RC (or L/R): charge to 63.2% of applied or discharge to 36.8% of initial in one τ (E5B01). Combine components first: E5B04's two
  parallel 220 µF = 440 µF, two parallel 1 MΩ = 500 kΩ, τ = 220 s. Admittance Y = 1/Z = G + jB in siemens — conductance G real, susceptance B imaginary, letter B
  (E5B02, E5B06, E5B12); polar conversion: |Y| = 1/|Z| and negate the angle (E5B03); pure reactance → susceptance of reciprocal magnitude (E5B05). Phase rules: ELI —
  in an inductor voltage (E) leads current (I) by 90° (E5B10); ICE — in a capacitor current leads voltage by 90° (E5B09). Series RLC angle θ = atan((X_L−X_C)/R):
  positive = net inductive = voltage leads, negative = capacitive = voltage lags — E5B07 = −14.0° lags, E5B08 = −63° lags, E5B11 = +27° leads (worked below).
- **Confusions:** each question offers both angles × both directions — e.g. E5B08's 27° distractor is atan(R/X); compute X_L−X_C first, then divide by R; lead/lag
  wording ("voltage leads" = inductive) is where sign-perfect solvers still lose points.
- **Vocab:** time constant τ, admittance, conductance, susceptance, siemens, ELI/ICE, phase angle, charge/discharge curve.
- **FACT:** 63.2% charge / 36.8% discharge per τ; susceptance = B.

### E5C — Complex impedance: rectangular/polar notation, Figure E5-1 (12)

- **Inventory:** notation & diagrams (9: E5C01–E5C09); Figure E5-1 plotting (3: E5C10–E5C12).
- **Teach:** rectangular Z = R ± jX: +j inductive, −j capacitive. Pure capacitive 100 Ω = 0 − j100 (E5C01); 50 − j25 = 50 Ω resistance in series with 25 Ω capacitive
  reactance (E5C06). Polar = magnitude and phase angle (E5C02); pure inductance = +90° (E5C03), pure capacitance = −90°. On rectangular impedance coordinates the X
  axis is *resistance*, Y axis *reactance* (E5C09); pure resistance plots on the horizontal axis (E5C07); polar coordinates display magnitude/phase directly (E5C08); a
  phasor diagram shows phase relationships among impedances at one frequency (E5C05); frequency-response graphs use a logarithmic Y axis (E5C04). Figure method:
  compute X_L = 2πfL or X_C = 1/(2πfC), pair with R, plot. E5C10: 400 Ω + 38 pF @ 14 MHz → X_C ≈ 300 → 400−j300 = Point 4. E5C11: 300 Ω + 18 µH @ 3.505 MHz → X_L ≈ 400
  → 300+j400 = Point 3. E5C12: 300 Ω + 19 pF @ 21.2 MHz → X_C ≈ 400 → 300−j400 = Point 1.
- **Confusions:** the figure's axis tips are labeled "+X/−X/+Y/−Y" (coordinate axes), which collides with "X = reactance" notation — the horizontal axis is resistance;
  capacitive points plot in the *lower* half; Points 5/7 have negative resistance, impossible for passive series circuits, so any answer naming them is auto-wrong.
- **Vocab:** rectangular/polar coordinates, j-operator, real/imaginary parts, magnitude, phase angle, phasor diagram, logarithmic scale.
- **FACT:** +j inductive / −j capacitive; pure L = +90°, pure C = −90°; X axis = R.

#### Figure E5-1 — precise redraw specification (E5C10–E5C12)

Verified three ways: `canon/source/e4_2024-svgs.zip → E5-1.svg` (authoritative vector, viewBox 276×277; chart origin at SVG (138.2, 146.9); scale ≈
0.164 units/ohm horizontal, 0.160 vertical), page 1 of `Extra_Figures_2024-2028-1.pdf`, and Diagrams_Page_1.jpg (visual match).

- **What it is:** a rectangular-coordinate impedance graph — *not* a circuit schematic (the brief's "R-L-C circuit" framing is a misnomer; the R, L, C live in the
  questions, the figure is the plane on which the computed impedance is plotted).
- **Frame:** square plot box; bold X and Y axes through the origin extending slightly past the box; axis tips labeled "+X" (right), "−X" (left), "+Y" (top), "−Y"
  (bottom); title "Figure E5-1" centered above.
- **Scales:** both axes −600 to +600 ohms; numeric tick labels every 100 Ω (X below the horizontal axis, Y left of the vertical axis); light gridlines every 200 Ω.
  Horizontal = resistance R, vertical = reactance jX (per E5C09; the figure itself carries only ±X/±Y tip labels, no R/jX titles).
- **Eight points** (small filled dots, each labeled "Point N"): Point 1 (+300, −400); Point 2 (+400, +300); Point 3 (+300, +400); Point 4 (+400, −300); Point 5 (−400,
  −300); Point 6 (+400, ≈0 — dot on the +X axis, SVG puts it a hair below at ≈ −10 Ω); Point 7 (−300, −400); Point 8 (+300, ≈0 — dot on the +X axis, SVG puts it a hair
  above at ≈ +30 Ω).
- **Answer mapping:** E5C10 → Point 4 (400−j300); E5C11 → Point 3 (300+j400); E5C12 → Point 1 (300−j400). All keyed points sit in the right half-plane; the negative-R
  points (5, 7) and on-axis points (6, 8) exist purely as distractors.

### E5D — Skin effect, parasitics, real vs. reactive power (12)

- **Inventory:** conductor behavior vs. frequency (3: E5D01, E5D02, E5D04); parasitics & self-resonance (4: E5D05, E5D06, E5D07, E5D08); power fundamentals (4: E5D03,
  E5D09, E5D11, E5D12); electrical length (1: E5D10).
- **Teach:** skin effect crowds RF current toward the conductor surface, so resistance rises with frequency (E5D01); it is also the primary RF loss in film capacitors
  (E5D08). Leads are parasitic inductance: keep VHF+ leads short to minimize inductive reactance (E5D02); at microwave frequencies short connections also reduce phase
  shift (E5D04). A conductor's electrical length *increases* with diameter (E5D10) — counterintuitive, pin it. Electrolytics carry too much series inductance for RF
  (E5D05); an inductor's inter-turn capacitance creates self-resonance (E5D06); self-resonance generally = nominal + parasitic reactances combining (E5D07); above
  self-resonance an inductor turns capacitive (builder context). Reactive power: V and I 90° out of phase (E5D03); ideal L/C store energy in fields and return it —
  nothing is dissipated (E5D09); hence "wattless, nonproductive power" (E5D12). Only resistance consumes real power: E5D11's 1 A through 100 Ω + j100 Ω dissipates I²R
  = 100 W, not 141 or 200 W.
- **Confusions:** E5D11 distractors use |Z| = 141 Ω (141.4 W) or 200-style arithmetic — real power touches R only; skin effect raises resistance (decrease/temperature
  distractors); E5D10 defies intuition — larger diameter = longer electrical length.
- **Vocab:** skin effect, parasitic inductance/capacitance, self-resonance, inter-turn capacitance, dielectric loss, electrical length, real/reactive/apparent power,
  power factor.
- **FACT:** real power = I²R only; electrolytics fail at RF from inductance.

### E5 math handbook (every example uses pool numbers; script-verified)

1. **Resonant frequency** — f0 = 1/(2π√(LC)). E5A02: L = 50 µH, C = 40 pF → √(LC) = 4.472×10⁻⁸ → f0 = 3.56 MHz. E5A10: L = 50 µH, C = 10 pF → 7.12 MHz. R is a decoy
   both times (E5A02's 22.36 MHz distractor = 2π × f0 — forgetting to divide by 2π).
2. **Half-power bandwidth** — BW = f0/Q. E5A11: 7.1 MHz/150 = 47.3 kHz. E5A12: 3.7 MHz/118 = 31.4 kHz. Inverse (E4B08): measure BW, get Q = f0/BW.
3. **Circuit Q** — series Q = X_L/R = X_C/R; parallel Q = R/X (E5A09). Component Q = reactance/series resistance of the part; loaded Q includes the external load and
   is always lower than unloaded Q (standard textbook knowledge).
4. **Resonant voltage magnification** — at series resonance V_L = V_C ≈ Q × V_applied (E5A01, E5A13). With E5A02's numbers: X_L at 3.56 MHz ≈ 1.12 kΩ, Q ≈ 1118/22 ≈
   51, so 10 V applied → ≈ 510 V across coil or capacitor.
5. **RC/RL time constant** — τ = RC; τ = L/R. Charge V(t) = V(1−e^(−t/τ)): 63.2% at τ, ≈99.3% at 5τ. Discharge V(t) = V0·e^(−t/τ): 36.8% at τ (E5B01). E5B04: (220+220
   µF) × (1 MΩ ∥ 1 MΩ) = 440 µF × 500 kΩ = 220 s; distractors are the three wrong combinations (110, 440, 55 s).
6. **Reactance** — X_L = 2πfL; X_C = 1/(2πfC). E5C11: 2π × 3.505 MHz × 18 µH ≈ 396 ≈ 400 Ω → Point 3. E5C10: 1/(2π × 14 MHz × 38 pF) ≈ 299 ≈ 300 Ω → Point 4. E5C12:
   1/(2π × 21.2 MHz × 19 pF) ≈ 395 ≈ 400 Ω → Point 1.
7. **Rectangular ↔ polar** — |Z| = √(R²+X²); θ = atan(X/R); back: R = |Z|cosθ, X = |Z|sinθ. With E5C06's value: 50−j25 → |Z| = √(50²+25²) = 55.9 Ω, θ = atan(−25/50) =
   −26.6°, i.e. 55.9 ∠−26.6° Ω. The j-operator rotates 90°: ×(+j) = +90° inductive, ×(−j) = −90° capacitive (E5C01, E5C03).
8. **Series RLC phase angle** — θ = atan((X_L−X_C)/R); θ>0 voltage leads (inductive), θ<0 voltage lags. E5B07: atan((250−500)/1000) = −14.0° lags. E5B08:
   atan((100−300)/100) = −63.4° lags. E5B11: atan((75−25)/100) = +26.6 ≈ 27° leads.
9. **Admittance & susceptance** — Y = 1/Z = G + jB (siemens); polar: |Y| = 1/|Z|, ∠Y = −∠Z (E5B03); pure X → B = 1/X in magnitude (E5B05). With E5C06's Z = 50−j25: Y =
   (16+j8) mS; polar 17.9 mS ∠+26.6° — note the angle sign flip.
10. **Real vs. reactive power** — P = I²R = VI·cosθ (watts); Q = VI·sinθ (vars); ideal L/C dissipate nothing (E5D03, E5D09, E5D12). E5D11: P = 1² × 100 = 100 W; the
    j100 reactance adds zero real watts.
11. **Reflection coefficient & SWR** — Γ = (Z_L−Z_0)/(Z_L+Z_0); |Γ| = √(P_refl/P_fwd); SWR = (1+|Γ|)/(1−|Γ|); return loss = −20·log10|Γ|. With E4B06's wattmeter
    numbers (the pool's SWR hook, via E4B04's S11↔VSWR equivalence): |Γ| = √(25/100) = 0.5 → SWR = 3:1; return loss ≈ 6.0 dB; delivered power = 100−25 = 75 W.
12. **Skin effect** (qualitative) — AC resistance rises with √f as current confines to the surface (E5D01); concept only, no pool calculation.

---

## Cross-subelement distractor patterns (writer's summary)

- **Number ladders:** E1 limits always appear as 4-rung ladders (1/2/5/100 W; 30 s/3/5/10 min; −43/−53/−63/−73 dB; 50/144/222/420 MHz) — teach the exact rung.
- **Swapped definitions:** telemetry vs. telecommand (E1D01/E1D03); ADIF vs. Cabrillo (E2C02/E2C07); blanker vs. DNR vs. ANF targets (E4E01–E4E03); time- vs.
  frequency-domain axes (E4A01/E4A02).
- **All-of-the-above keyed answers:** E1D05, E2A02, E2C08, E2C10, E2E04, E4A08, E4A11, E4B11, E4E02, E4E10 — legitimate because each clause is independently true; warn
  readers not to use it as a guessing heuristic elsewhere.
- **Mirror traps:** series vs. parallel resonance (E5A03–E5A07); lead vs. lag (E5B07–E5B11); perigee vs. apogee (E3A03); northward vs. southward Bz (E3C05); narrowest
  bandwidth vs. highest throughput (E2E10/E2E13).

## Ambiguous / surprising items for chapter writers

- E4D05 (errata 4) and E2A13 (errata 2) deleted — numbering gaps intentional; do not fix.
- E1C12: phone permitted on the *entire* 630 m band — defies HF band-plan intuition.
- E2C01: no special identifier for US remote-control operation — many Generals remember otherwise.
- E2C03: 30 m contest exclusion is convention, not FCC rule ("generally excluded").
- E3B11: sporadic E keyed to "between sunrise and sunset" despite evening-Es operating lore — teach the pool answer with the solar-ionization mechanism.
- E5A04: parallel-resonance |Z| "approximately equal to circuit resistance" assumes the parallel-R model; series/parallel model swap confuses strong readers — flag it.
- E5D10: larger conductor diameter → *increased* electrical length — counterintuitive FACT.
- Figure E5-1 is a coordinate chart, not an R-L-C schematic; Points 5/7 (negative R) and on-axis Points 6/8 are pure distractors.

## Coverage

E1A 11, E1B 11, E1C 12, E1D 12, E1E 11, E1F 11; E2A 12, E2B 12, E2C 12, E2D 11, E2E 13; E3A 14, E3B 13, E3C 12; E4A 11, E4B 11, E4C 14, E4D 13, E4E
14; E5A 13, E5B 12, E5C 12, E5D 12 = 279 questions — every ID cited above, script-verified.
