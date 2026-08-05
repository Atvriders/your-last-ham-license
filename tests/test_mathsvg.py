from tools.mathsvg import render

def test_render_returns_inline_svg():
    svg = render("E = IR")
    assert svg.strip().startswith("<svg") and "</svg>" in svg

def test_render_is_self_contained():
    svg = render("c = f\\lambda")
    # namespace decls (xmlns="http://www.w3.org/2000/svg") are fine; external RESOURCE refs are not:
    assert "<image" not in svg
    assert 'xlink:href="http' not in svg and 'href="http' not in svg.replace('xmlns', '')
    assert "@import" not in svg

def test_render_handles_subscripts_and_abs():
    svg = render("f_{IF} = |f_{RF} - f_{LO}|")
    assert svg.strip().startswith("<svg")


# --- The General formula set (Appendix B): every form the course teaches ---
# must render to inline SVG at build time (audit check #4 is the backstop).

def _renders_svg(expr):
    svg = render(expr)
    assert svg.strip().startswith("<svg") and "</svg>" in svg
    return svg

def test_render_inductive_reactance():
    _renders_svg("X_L = 2\\pi f L")

def test_render_capacitive_reactance_fraction():
    _renders_svg("X_C = \\frac{1}{2\\pi f C}")

def test_render_capacitive_reactance_paren_form():
    _renders_svg("X_C = 1/(2\\pi f C)")

def test_render_resonant_frequency():
    _renders_svg("f_r = \\frac{1}{2\\pi\\sqrt{LC}}")

def test_render_impedance_magnitude():
    _renders_svg("Z = \\sqrt{R^2 + X^2}")

def test_render_swr_gamma_form():
    _renders_svg("SWR = \\frac{1 + |\\Gamma|}{1 - |\\Gamma|}")

def test_render_swr_impedance_form():
    _renders_svg("SWR = \\frac{Z_{load}}{Z_0}")

def test_render_db_power_form():
    _renders_svg("dB = 10 \\log_{10}(P_1/P_0)")

def test_render_db_voltage_form():
    _renders_svg("dB = 20 \\log_{10}(V_1/V_0)")


# --- The Extra formula set (Appendix B additions): complex impedance in
# rectangular and polar forms, phase, time constants, reflection coefficient,
# and the heavier Greek letters the Extra course teaches. Every printed
# $...$ span must render to SVG at build time (audit check #4 backstop).

def test_render_complex_impedance_rectangular():
    _renders_svg("Z = R + jX")

def test_render_complex_impedance_magnitude():
    _renders_svg("|Z| = \\sqrt{R^2 + X^2}")

def test_render_complex_rectangular_values():
    _renders_svg("Z = 50 + j50")

def test_render_complex_polar_form():
    _renders_svg("Z = 70.7 \\angle 45^\\circ")

def test_render_rectangular_to_polar_equivalence():
    _renders_svg("50 + j50 = 70.7 \\angle 45^\\circ")

def test_render_phase_angle_arctan():
    _renders_svg("\\phi = \\arctan(X/R)")

def test_render_time_constant_rc():
    _renders_svg("\\tau = RC")

def test_render_time_constant_lr():
    _renders_svg("\\tau = L/R")

def test_render_reflection_coefficient():
    _renders_svg("\\Gamma = \\frac{Z_L - Z_0}{Z_L + Z_0}")

def test_render_swr_from_gamma_mathsrm():
    _renders_svg("\\mathrm{SWR} = \\frac{1 + |\\Gamma|}{1 - |\\Gamma|}")

def test_render_rho_as_gamma_magnitude():
    _renders_svg("\\rho = |\\Gamma|")

def test_render_angular_frequency():
    _renders_svg("\\omega = 2\\pi f")

def test_render_reactance_from_omega():
    _renders_svg("X_L = \\omega L")

def test_render_q_factor():
    _renders_svg("Q = \\frac{X_L}{R}")

def test_render_varphi_variant():
    _renders_svg("\\varphi")
