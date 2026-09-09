# -*- coding: utf-8 -*-
import json
from sqlalchemy.orm import Session
from app.database.engine import SessionLocal
from app.database.models import Topic

with open('app/learning/theory_5to.json', 'r', encoding='utf-8') as f:
    t5 = json.load(f)
with open('app/learning/theory_6to.json', 'r', encoding='utf-8') as f:
    t6 = json.load(f)

def beautify(content):
    c = content
    # Cinemática
    c = c.replace('x(t) = x0 + v · (t - t0)', r'x(t) = x_0 + v \cdot (t - t_0)')
    c = c.replace('Δx = x_f - x_0 = v · Δt', r'\Delta x = x_f - x_0 = v \cdot \Delta t')
    c = c.replace('v(t) = v0 + a · t', r'v(t) = v_0 + a \cdot t')
    c = c.replace('x(t) = x0 + v0 · t + ½ a · t²', r'x(t) = x_0 + v_0 \cdot t + \frac{1}{2} a \cdot t^2')
    c = c.replace('vf² = v0² + 2 · a · Δx ⇔ Δx = (vf² - v0²) / (2a)', r'v_f^2 = v_0^2 + 2 a \Delta x \iff \Delta x = \frac{v_f^2 - v_0^2}{2a}')
    
    # Dinámica
    c = c.replace('Σ F_ext = 0 ⇔ v = constante ⇔ a = 0', r'\sum \vec{F}_{\text{ext}} = \vec{0} \iff \vec{v} = \text{constante} \iff \vec{a} = \vec{0}')
    c = c.replace('Σ F = m · a = dp/dt', r'\sum \vec{F} = m \cdot \vec{a} = \frac{d\vec{p}}{dt}')
    c = c.replace('F_AB = - F_BA', r'\vec{F}_{AB} = - \vec{F}_{BA}')
    c = c.replace('P = m · g', r'P = m \cdot g')
    c = c.replace('Fe = - k · Δx', r'F_e = - k \cdot \Delta x')
    c = c.replace('f_rc = μ_c · N', r'f_{rc} = \mu_c \cdot N')
    c = c.replace('Px = m · g · sen(α)', r'P_x = m \cdot g \cdot \sin\alpha')
    c = c.replace('Py = m · g · cos(α)', r'P_y = m \cdot g \cdot \cos\alpha')
    c = c.replace('tan(α_c) = μ_e ⇔ α_c = arctan(μ_e)', r'\tan\alpha_c = \mu_e \iff \alpha_c = \arctan(\mu_e)')
    c = c.replace('a = g · (sen(α) - μ_c · cos(α))', r'a = g \cdot (\sin\alpha - \mu_c \cdot \cos\alpha)')

    # Trabajo y Energía
    c = c.replace('W = F · d = F · d · cos(θ)', r'W = \vec{F} \cdot \vec{d} = F \cdot d \cdot \cos\theta')
    c = c.replace('Ek = ½ m · v²', r'E_k = \frac{1}{2} m \cdot v^2')
    c = c.replace('W_neto = ΔEk = Ek_final - Ek_inicial = ½ m · vf² - ½ m · v0²', r'W_{\text{neto}} = \Delta E_k = \frac{1}{2} m v_f^2 - \frac{1}{2} m v_0^2')
    c = c.replace('Epg = m · g · h', r'E_{pg} = m \cdot g \cdot h')
    c = c.replace('Epe = ½ k · x²', r'E_{pe} = \frac{1}{2} k \cdot x^2')
    c = c.replace('Em = Ek + Epg + Epe', r'E_m = E_k + E_{pg} + E_{pe}')
    c = c.replace('P = W / Δt', r'P = \frac{W}{\Delta t} = \vec{F} \cdot \vec{v}')

    # Cantidad de movimiento
    c = c.replace('p = m · v', r'\vec{p} = m \cdot \vec{v}')
    c = c.replace('I = F_media · Δt', r'\vec{I} = \vec{F}_{\text{media}} \cdot \Delta t = \Delta\vec{p}')
    c = c.replace('P_total,inicial = P_total,final', r'\sum m_i \vec{v}_{i,\text{inicial}} = \sum m_i \vec{v}_{i,\text{final}}')

    # Movimiento circular
    c = c.replace('ac = vt² / r = ω² · r', r'a_c = \frac{v_t^2}{r} = \omega^2 \cdot r')
    c = c.replace('Fc = m · ac = m · (vt² / r) = m · ω² · r', r'F_c = m \cdot a_c = m \frac{v_t^2}{r} = m \omega^2 r')
    c = c.replace('T = 2π / ω', r'T = \frac{2\pi}{\omega} = \frac{1}{f}')

    # Gravitación
    c = c.replace('F = G · (m1 · m2) / r²', r'F = G \frac{m_1 \cdot m_2}{r^2}')
    c = c.replace('g(r) = G · M / r²', r'g(r) = G \frac{M}{r^2}')
    c = c.replace('v_orb = √(G · M / r)', r'v_{\text{orb}} = \sqrt{\frac{G \cdot M}{r}}')
    c = c.replace('v_esc = √(2 · G · M / R) = √2 · v_orb', r'v_{\text{esc}} = \sqrt{\frac{2 G M}{R}} = \sqrt{2} \cdot v_{\text{orb}}')
    c = c.replace('T² / a³ = 4π² / (G · M_Sol) = constante', r'\frac{T^2}{a^3} = \frac{4\pi^2}{G \cdot M_{\odot}} = \text{constante}')

    # Estática
    c = c.replace('τ_O = r × F ⇒ ||τ|| = r · F · sen(θ) = F · d_brazo', r'\vec{\tau}_O = \vec{r} \times \vec{F} \implies \|\vec{\tau}\| = r \cdot F \cdot \sin\theta = F \cdot d_{\text{brazo}}')
    c = c.replace('Σ F_ext = 0 ⇔ Σ Fx = 0,  Σ Fy = 0,  Σ Fz = 0', r'\sum \vec{F}_{\text{ext}} = \vec{0} \quad \text{y} \quad \sum \vec{\tau}_O = \vec{0}')

    # Fluidos
    c = c.replace('ΔP = ρ · g · h', r'\Delta P = \rho \cdot g \cdot h')
    c = c.replace('F1 / A1 = F2 / A2 ⇒ F2 = F1 · (A2 / A1)', r'\frac{F_1}{A_1} = \\frac{F_2}{A_2} \implies F_2 = F_1 \left(\frac{A_2}{A_1}\right)')
    c = c.replace('E = m_fluido_desalojado · g = ρ_fluido · V_sumergido · g', r'E = \rho_{\text{fluido}} \cdot V_{\text{sumergido}} \cdot g')

    # Ondas
    c = c.replace('v = λ / T = λ · f', r'v = \frac{\lambda}{T} = \lambda \cdot f')
    c = c.replace('sen(θ1)/sen(θ2) = v1/v2 = λ1/λ2', r'\frac{\sin\theta_1}{\sin\theta_2} = \frac{v_1}{v_2} = \frac{\lambda_1}{\lambda_2}')

    # Electrostática 6to
    c = c.replace('F_12 = (1 / 4πε0) · (q1 · q2 / r²) · r̂_12 = ke · (q1 · q2 / r²) · r̂_12', r'\vec{F}_{12} = \frac{1}{4\pi\varepsilon_0} \frac{q_1 q_2}{r^2} \hat{r}_{12} = k_e \frac{q_1 q_2}{r^2} \hat{r}_{12}')
    c = c.replace('E(r) = lim (q0 → 0) [ F / q0 ]', r'\vec{E}(\vec{r}) = \lim_{q_0 \to 0} \frac{\vec{F}}{q_0} = k_e \frac{Q}{r^2} \hat{r}')
    c = c.replace('V(r) = U(r) / q = ke · Q / r', r'V(r) = \frac{U(r)}{q} = k_e \frac{Q}{r}')
    c = c.replace('|ΔV| = E · d ⇔ E = |ΔV| / d', r'|\Delta V| = E \cdot d \iff E = \frac{|\Delta V|}{d}')
    c = c.replace('R = ρ · (L / A)', r'R = \rho \frac{L}{A}')
    c = c.replace('V = I · R ⇔ I = V / R ⇔ R = V / I', r'V = I \cdot R \iff I = \frac{V}{R} \iff R = \frac{V}{I}')
    c = c.replace('P = V · I = I² · R = V² / R', r'P = V \cdot I = I^2 \cdot R = \frac{V^2}{R}')

    # Kirchhoff
    c = c.replace('Σ I_entrantes = Σ I_salientes ⇔ Σ I_k = 0', r'\sum I_{\text{entrantes}} = \sum I_{\text{salientes}} \iff \sum I_k = 0')
    c = c.replace('Σ ΔV_k = 0 ⇔ Σ E = Σ (I · R)', r'\sum \Delta V_k = 0 \iff \sum \mathcal{E} = \sum (I \cdot R)')

    # Magnetismo
    c = c.replace('F = q · (E + v × B)', r'\vec{F} = q (\vec{E} + \vec{v} \times \vec{B})')
    c = c.replace('F_m = q · (v × B) ⇒ ||F_m|| = |q| · v · B · sen(θ)', r'\vec{F}_m = q (\vec{v} \times \vec{B}) \implies \|\vec{F}_m\| = |q| v B \sin\theta')
    c = c.replace('F_m = I · (L × B) ⇒ ||F_m|| = I · L · B · sen(θ)', r'\vec{F}_m = I (\vec{L} \times \vec{B}) \implies \|\vec{F}_m\| = I L B \sin\theta')
    c = c.replace('Φ_B = ∫∫_S B · dA = B · A · cos(θ)', r'\Phi_B = \iint_S \vec{B} \cdot d\vec{A} = B \cdot A \cdot \cos\theta')
    c = c.replace('E = - dΦ_B / dt', r'\mathcal{E} = - \frac{d\Phi_B}{dt}')

    # Capacitores RC
    c = c.replace('C = Q / V', r'C = \frac{Q}{V}')
    c = c.replace('U = ½ C · V² = ½ Q · V = Q² / (2C)', r'U = \frac{1}{2} C V^2 = \frac{1}{2} Q V = \frac{Q^2}{2C}')
    c = c.replace('Constante de tiempo: τ = R · C', r'\tau = R \cdot C')
    c = c.replace('VC(t) = V0 · (1 - e^(-t / τ))', r'V_C(t) = V_0 \left(1 - e^{-\frac{t}{\tau}}\right)')
    c = c.replace('VC(t) = V0 · e^(-t / τ)', r'V_C(t) = V_0 \cdot e^{-\frac{t}{\tau}}')
    c = c.replace('I(t) = (V0 / R) · e^(-t / τ)', r'I(t) = \frac{V_0}{R} e^{-\frac{t}{\tau}}')

    # Cajas con clases elegantes
    c = c.replace("class='p-3 bg-slate-50 border-l-4 border-physics-500 font-mono text-xs my-2'", "class='formula-card'")
    c = c.replace("class='p-3 bg-slate-50 border-l-4 border-physics-500 text-xs my-2'", "class='formula-card'")
    c = c.replace("class='p-3 bg-rose-50 border-l-4 border-rose-500 text-xs text-rose-900 my-2'", "class='formula-card-warning'")
    return c

db = SessionLocal()
try:
    topics = db.query(Topic).all()
    count = 0
    for topic in topics:
        raw = None
        if topic.slug in t5:
            raw = t5[topic.slug]
        elif topic.slug in t6:
            raw = t6[topic.slug]

        if raw:
            topic.theory_content = beautify(raw)
            count += 1

    db.commit()
    print(f"{count} temas actualizados exitosamente con KaTeX y tarjetas de formulas.")
finally:
    db.close()
