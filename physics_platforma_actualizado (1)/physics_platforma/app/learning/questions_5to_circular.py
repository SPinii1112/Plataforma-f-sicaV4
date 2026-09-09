import json
import random
from app.learning.question_helper import make_mc

def generate_circular_questions():
    q = []
    # 20 preguntas de Movimiento Circular
    q.append(make_mc(
        'Un disco gira a 120 rpm (revoluciones por minuto). ¿Cuál es su velocidad angular ω en rad/s?',
        '12.57 rad/s (4π rad/s)', ['120.0 rad/s', '2.0 rad/s', '6.28 rad/s'],
        'ω = 120 rev/min * (2π rad / 1 rev) * (1 min / 60 s) = (120 * 2π) / 60 = 4π ≈ 12.57 rad/s.',
        'ω = (120 * 2 * 3.1416) / 60 = 12.57 rad/s.', 'basic', 1120
    ))
    q.append(make_mc(
        'Si el disco anterior tiene un radio r = 0.50 m, ¿cuál es la rapidez tangencial de un punto en el borde?',
        '6.28 m/s (2π m/s)', ['12.57 m/s', '3.14 m/s', '24.0 m/s'],
        'vt = ω * r = 4π rad/s * 0.50 m = 2π ≈ 6.28 m/s.', 'vt = 12.57 * 0.5 = 6.28 m/s.', 'basic', 1130
    ))
    q.append(make_mc(
        'Un cuerpo describe un MCU con rapidez tangencial v = 10 m/s en una circunferencia de radio r = 2.0 m. ¿Cuál es su aceleración centrípeta?',
        '50.0 m/s²', ['5.0 m/s²', '20.0 m/s²', '100.0 m/s²'],
        'ac = v² / r = (10)² / 2.0 = 100 / 2 = 50.0 m/s².', 'ac = 100 / 2 = 50 m/s².', 'basic', 1110
    ))
    q.append(make_mc(
        '¿Cuál es la función física de la fuerza centrípeta en el Movimiento Circular Uniforme?',
        'Modificar continuamente la dirección del vector velocidad sin alterar su rapidez escalar',
        ['Aumentar la rapidez lineal del móvil', 'Frenar el cuerpo hacia el centro', 'Compensar la fuerza centrífuga imaginaria'],
        'Como la aceleración centrípeta es perpendicular a la velocidad (ac ⊥ v), solo curva la trayectoria y no realiza trabajo.',
        'Fc ⊥ v ⇒ no altera el módulo de v, solo su dirección.', 'basic', 1120
    ))
    q.append(make_mc(
        'Un automóvil de 1200 kg toma una curva plana horizontal de radio r = 50 m a 20 m/s. ¿Qué fuerza de rozamiento centrípeta mínima requieren los neumáticos?',
        '9600 N', ['480 N', '24000 N', '12000 N'],
        'Fc = m * (v² / r) = 1200 * (400 / 50) = 1200 * 8 = 9600 N.',
        'Fc = 1200 * 400 / 50 = 9600 N.', 'intermediate', 1210
    ))
    q.append(make_mc(
        'Un satélite en órbita circular tiene un período orbital T = 90 minutos. ¿Cuál es su frecuencia en Hertz?',
        '1.85 × 10⁻⁴ Hz', ['0.011 Hz', '5400 Hz', '90 Hz'],
        'T = 90 min * 60 s/min = 5400 s. f = 1 / T = 1 / 5400 s ≈ 1.85 × 10⁻⁴ Hz.',
        'f = 1 / 5400 = 1.85x10⁻⁴ Hz.', 'basic', 1130
    ))
    q.append(make_mc(
        'Si el radio de una trayectoria circular se duplica manteniendo constante la rapidez tangencial, ¿cómo varía la aceleración centrípeta?',
        'Se reduce a la mitad (ac / 2)', ['Se duplica', 'Se cuadruplica', 'Permanece constante'],
        'ac = v² / r. Como r está en el denominador, al duplicar r con v fijo, ac se reduce a la mitad.',
        'ac2 = v² / (2r) = 0.5 * (v²/r) = ac1 / 2.', 'basic', 1140
    ))
    q.append(make_mc(
        'Si el radio se duplica manteniendo constante la velocidad angular ω, ¿cómo varía la aceleración centrípeta?',
        'Se duplica (2 · ac)', ['Se reduce a la mitad', 'Se cuadruplica', 'Se reduce a la cuarta parte'],
        'ac = ω² · r. Como r está en el numerador con exponente 1, al duplicar r con ω fijo, ac se duplica.',
        'ac = ω² * (2r) = 2 * (ω² r).', 'intermediate', 1180
    ))
    q.append(make_mc(
        'La fuerza centrífuga experimentada por un pasajero al girar un auto es:',
        'Una fuerza ficticia o de inercia percibida únicamente desde un sistema de referencia no inercial (acelerado)',
        ['Una fuerza real del tipo acción-reacción', 'La fuerza gravitatoria', 'La normal de la puerta'],
        'Desde un marco inercial terrestre no existe fuerza centrífuga; solo existe la fuerza centrípeta real que desvía el auto.',
        'Fuerza ficticia debida a la aceleración del sistema de referencia propio del vehículo.', 'intermediate', 1220
    ))
    q.append(make_mc(
        'Un objeto de 0.20 kg atado a una cuerda de 0.80 m gira en un plano vertical. En el punto más bajo viaja a 4.0 m/s. ¿Cuál es la tensión de la cuerda? (g = 9.8 m/s²).',
        '5.96 N', ['4.00 N', '1.96 N', '2.04 N'],
        'En el punto inferior: T - P = m * (v²/r) ⇒ T = m*g + m*(v²/r) = 0.2*9.8 + 0.2*(16/0.8) = 1.96 + 4.0 = 5.96 N.',
        'T = m*(g + v²/r) = 0.2 * (9.8 + 20) = 0.2 * 29.8 = 5.96 N.', 'advanced', 1280
    ))
    q.append(make_mc(
        '¿Cuál es la rapidez crítica mínima en la cúspide de un rizo vertical de radio r para que el cuerpo no se desprenda de la pista? (g = 9.8 m/s²).',
        'v_crítica = √(g · r)', ['v_crítica = √(2 · g · r)', 'v_crítica = g · r', 'v_crítica = 0'],
        'En el punto más alto, en el límite de desprendimiento la normal se anula (N = 0): P = Fc ⇒ m*g = m*v²/r ⇒ v = √(g*r).',
        'N = 0 ⇒ m*g = m*v²/r ⇒ v = √(g*r).', 'intermediate', 1240
    ))
    q.append(make_mc(
        'Una centrífuga de laboratorio gira a 3000 rpm con un radio de 0.10 m. ¿A cuántas "g" de aceleración centrípeta somete las muestras? (g = 9.8 m/s²).',
        '1006 g', ['100 g', '300 g', '30 g'],
        'ω = (3000 * 2π) / 60 = 100π ≈ 314.16 rad/s. ac = ω² * r = (314.16)² * 0.10 ≈ 98696 * 0.10 = 9869.6 m/s². En g: 9869.6 / 9.8 ≈ 1006 g.',
        'ac / g = (314.16² * 0.1) / 9.8 ≈ 1007 g.', 'advanced', 1290
    ))
    q.append(make_mc(
        'El ángulo de peralte óptimo θ de una curva en una autopista de radio r para velocidad v sin fricción cumple:',
        'tan(θ) = v² / (g · r)', ['sen(θ) = v² / (g · r)', 'cos(θ) = v² / (g · r)', 'tan(θ) = g · r / v²'],
        'N*sen(θ) = m*v²/r y N*cos(θ) = m*g. Dividiendo miembro a miembro: tan(θ) = v² / (g*r).',
        'tan(θ) = (v²/r) / g = v² / (g*r).', 'intermediate', 1230
    ))
    q.append(make_mc(
        'Un ventilador tarda 4.0 s en detenerse desde una velocidad de 20 rad/s con desaceleración angular constante. ¿Cuántas radianes gira hasta parar?',
        '40 rad', ['80 rad', '20 rad', '10 rad'],
        'Δθ = ½ (ω0 + ωf) * t = ½ (20 + 0) * 4.0 = 10 * 4 = 40 rad.',
        'Δθ = 0.5 * 20 * 4 = 40 rad.', 'intermediate', 1210
    ))
    q.append(make_mc(
        '¿Cuántas vueltas completas equivalen a 40 radianes?',
        '6.37 vueltas', ['40 vueltas', '12.56 vueltas', '20 vueltas'],
        'Una vuelta completa son 2π radianes ≈ 6.283 rad. Vueltas = 40 / (2π) = 40 / 6.283 ≈ 6.37 vueltas.',
        'N = 40 / (2*π) ≈ 6.37.', 'basic', 1130
    ))
    q.append(make_mc(
        'La aceleración tangencial at en un movimiento circular variado se relaciona con la aceleración angular α mediante:',
        'at = α · r', ['at = α / r', 'at = α · r²', 'at = ω² · r'],
        'Derivando vt = ω · r respecto al tiempo: dv/dt = (dω/dt) · r ⇒ at = α · r.',
        'at = α * r.', 'basic', 1110
    ))
    q.append(make_mc(
        'La aceleración total resultante a de una partícula en movimiento circular no uniforme se obtiene como:',
        'a = √(ac² + at²)', ['a = ac + at', 'a = ac - at', 'a = ac · at'],
        'Dado que ac es radial y at es tangencial, son perpendiculares entre sí (90°). Su resultante vectorial es la hipotenusa de Pitágoras.',
        'a_total = √(ac² + at²).', 'intermediate', 1190
    ))
    q.append(make_mc(
        'Un carrusel gira con un período de 10 s. ¿Cuál es su velocidad angular?',
        '0.628 rad/s (π/5 rad/s)', ['62.8 rad/s', '0.10 rad/s', '10.0 rad/s'],
        'ω = 2π / T = 2π / 10 = π / 5 ≈ 0.628 rad/s.', 'ω = 2*3.1416 / 10 = 0.628 rad/s.', 'basic', 1100
    ))
    q.append(make_mc(
        'Dos niños están montados en un tiovivo giratorio: uno a 1 m del centro y otro a 3 m del centro. ¿Cuál de ellos tiene mayor velocidad angular ω?',
        'Ambos tienen exactamente la misma velocidad angular ω',
        ['El niño a 3 m tiene el triple de velocidad angular', 'El niño a 1 m tiene mayor velocidad angular', 'Depende de sus masas'],
        'Todos los puntos de un cuerpo rígido en rotación barren el mismo ángulo en el mismo tiempo (mismo ω). El niño más alejado tiene mayor velocidad tangencial (vt = ω·r), pero mismo ω.',
        'ω es idéntico para todo el cuerpo rígido en rotación.', 'intermediate', 1200
    ))
    q.append(make_mc(
        'Un patinador que gira sobre sí mismo cierra los brazos contra su cuerpo y comienza a girar mucho más rápido. Este fenómeno se debe a:',
        'La conservación del momento angular (al reducir su momento de inercia I, la velocidad angular ω debe aumentar)',
        ['Una fuerza centrípeta creada por sus músculos', 'La ganancia de energía cinética de la nada', 'La fuerza de fricción del hielo'],
        'Momento angular L = I · ω = constante. Al encoger los brazos, I disminuye, por lo que ω se incrementa obligatoriamente.',
        'L = I*ω = cte. Menor I ⇒ mayor ω.', 'intermediate', 1230
    ))
    return q
