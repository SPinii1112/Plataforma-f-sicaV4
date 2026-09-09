# -*- coding: utf-8 -*-
from app.learning.question_helper import make_mc

def get_trabajo_energia_questions():
    q = []
    # 20 preguntas de Trabajo y Energía
    q.append(make_mc(
        'Una fuerza constante F = 50 N tira de un bloque desplazándolo d = 4.0 m en su misma dirección y sentido. ¿Qué trabajo realiza?',
        '200 J', ['12.5 J', '54 J', '0 J'],
        'Trabajo motor W = F * d * cos(0°) = 50 * 4.0 * 1 = 200 J.',
        'W = F * d * cos(0°) = 50 * 4.0 = 200 J.', 'basic', 1100
    ))
    q.append(make_mc(
        'Una persona sostiene en reposo una maleta de 15 kg a 1.0 m del suelo durante 10 minutos. ¿Qué trabajo mecánico realiza la fuerza de sus brazos sobre la maleta?',
        '0 J', ['150 J', '1470 J', '15 J'],
        'Para que exista trabajo mecánico debe haber desplazamiento en la dirección de la fuerza (d = 0 ⇒ W = 0 J).',
        'W = F * d = F * 0 = 0 J.', 'basic', 1110
    ))
    q.append(make_mc(
        'Un bloque de 2.0 kg se mueve a 6.0 m/s sobre una superficie horizontal. ¿Cuál es su energía cinética?',
        '36.0 J', ['12.0 J', '72.0 J', '18.0 J'],
        'Ek = ½ m v² = 0.5 * 2.0 * (6.0)² = 1.0 * 36.0 = 36.0 J.',
        'Ek = 0.5 * 2.0 * 36 = 36.0 J.', 'basic', 1100
    ))
    q.append(make_mc(
        'Si la velocidad de un automóvil se triplica (v_final = 3 · v_inicial), ¿por qué factor se multiplica su energía cinética?',
        'Se multiplica por 9', ['Se multiplica por 3', 'Se multiplica por 6', 'Se mantiene constante'],
        'La energía cinética depende cuadráticamente de la velocidad: Ek ∝ v². Si v se triplica, Ek ∝ (3v)² = 9 v².',
        'Ek_final / Ek_inicial = (3v)² / v² = 9.', 'basic', 1120
    ))
    q.append(make_mc(
        'Un cuerpo de 3.0 kg se suelta desde el reposo a una altura h = 20 m (g = 9.8 m/s²). Despreciando la fricción, ¿cuál es su rapidez al tocar el suelo?',
        '19.8 m/s', ['392.0 m/s', '14.0 m/s', '9.8 m/s'],
        'Conservación de Em: m*g*h = ½ m v² ⇒ v = √(2gh) = √(2 * 9.8 * 20) = √392 ≈ 19.8 m/s.',
        'v = √(2 * 9.8 * 20) = √392 ≈ 19.8 m/s.', 'intermediate', 1180
    ))
    q.append(make_mc(
        'Un resorte con constante elástica k = 500 N/m es comprimido 0.10 m. ¿Cuánta energía potencial elástica almacena?',
        '2.5 J', ['25.0 J', '50.0 J', '5.0 J'],
        'Epe = ½ k x² = 0.5 * 500 * (0.10)² = 250 * 0.01 = 2.5 J.',
        'Epe = 0.5 * 500 * 0.01 = 2.5 J.', 'basic', 1130
    ))
    q.append(make_mc(
        'Una fuerza de fricción constante de 20 N frena un bloque a lo largo de un desplazamiento de 5.0 m. ¿Qué trabajo realiza la fricción?',
        '-100 J', ['+100 J', '0 J', '-4 J'],
        'La fuerza de rozamiento se opone al desplazamiento (θ = 180°): W = 20 * 5 * cos(180°) = -100 J.',
        'W_fr = F_fr * d * cos(180°) = 20 * 5 * (-1) = -100 J.', 'basic', 1120
    ))
    q.append(make_mc(
        'Un motor eleva una carga de 200 kg a una altura de 15 m en 10 s a velocidad constante (g = 9.8 m/s²). ¿Cuál es la potencia desarrollada por el motor?',
        '2940 W', ['2000 W', '300 W', '29400 W'],
        'Trabajo = m*g*h = 200 * 9.8 * 15 = 29400 J. Potencia P = W / t = 29400 J / 10 s = 2940 W.',
        'P = (m * g * h) / t = (200 * 9.8 * 15) / 10 = 2940 W.', 'intermediate', 1210
    ))
    q.append(make_mc(
        '¿Cuál de las siguientes fuerzas es NO conservativa?',
        'La fuerza de rozamiento cinético', ['La fuerza peso', 'La fuerza elástica de un resorte ideal', 'La fuerza electrostática'],
        'El trabajo de las fuerzas de rozamiento depende del camino recorrido y disipa energía en forma de calor.',
        'Fuerzas no conservativas: fricción, resistencia de fluidos, fuerzas musculares.', 'basic', 1110
    ))
    q.append(make_mc(
        'Un bloque de 1.0 kg comprime un resorte de k = 400 N/m una distancia x = 0.2 m y luego se libera. ¿Con qué rapidez sale despedido?',
        '4.0 m/s', ['2.0 m/s', '8.0 m/s', '16.0 m/s'],
        'Toda la Epe se transforma en Ek: ½ k x² = ½ m v² ⇒ v = x * √(k/m) = 0.2 * √(400/1) = 0.2 * 20 = 4.0 m/s.',
        '0.5 * 400 * 0.04 = 0.5 * 1 * v² ⇒ 8 = 0.5 v² ⇒ v² = 16 ⇒ v = 4.0 m/s.', 'intermediate', 1230
    ))
    q.append(make_mc(
        'Un proyectil de 0.02 kg viaja a 300 m/s e impacta en un bloque de madera penetrando 0.15 m hasta detenerse. ¿Cuál fue la fuerza media de resistencia?',
        '6000 N', ['900 N', '1200 N', '3000 N'],
        'Por Teorema del Trabajo y la Energía: W_neto = ΔEk ⇒ - F_media * d = 0 - ½ m v0² ⇒ F_media = (0.5 * 0.02 * 90000) / 0.15 = 900 / 0.15 = 6000 N.',
        'F = (0.5 * m * v²) / d = (0.5 * 0.02 * 90000) / 0.15 = 6000 N.', 'advanced', 1280
    ))
    q.append(make_mc(
        'Un péndulo simple oscila libremente. En los extremos de su trayectoria (amplitud máxima), ¿cómo son su energía cinética y su energía potencial?',
        'Ek = 0 (mínima) y Ep es máxima', ['Ek es máxima y Ep = 0', 'Ambas son iguales a cero', 'Ambas son máximas simultáneamente'],
        'En los puntos de retorno la velocidad instantánea se anula (v = 0 ⇒ Ek = 0) y la altura respecto al punto de equilibrio es máxima.',
        'En los extremos: v = 0 ⇒ Ek = 0; h = h_máx ⇒ Ep = máxima.', 'basic', 1130
    ))
    q.append(make_mc(
        'Un automóvil de 1000 kg acelera de 10 m/s a 20 m/s. ¿Qué trabajo neto realizó el motor sobre él?',
        '150000 J (150 kJ)', ['50000 J', '200000 J', '300000 J'],
        'W_neto = ½ m (vf² - v0²) = 0.5 * 1000 * (400 - 100) = 500 * 300 = 150000 J.',
        'W = 0.5 * 1000 * (20² - 10²) = 500 * 300 = 150 kJ.', 'intermediate', 1200
    ))
    q.append(make_mc(
        'La unidad de potencia Horsepower o Caballo de Fuerza (HP) equivale aproximadamente a:',
        '746 W', ['1000 W', '500 W', '100 W'],
        'Por definición técnica habitual: 1 HP ≈ 745.7 W ≈ 746 Watts.',
        '1 HP = 745.7 W.', 'basic', 1100
    ))
    q.append(make_mc(
        'Un cuerpo de 5 kg desliza por un tobogán desde una altura de 10 m y llega a la base con v = 12 m/s (g = 9.8 m/s²). ¿Cuánta energía mecánica se perdió por rozamiento?',
        '130 J', ['490 J', '360 J', '0 J'],
        'Em_inicial = m*g*h = 5 * 9.8 * 10 = 490 J. Em_final = ½ m v² = 0.5 * 5 * 144 = 360 J. Pérdida = 490 - 360 = 130 J.',
        'W_nc = Em_final - Em_inicial = 360 - 490 = -130 J (se disiparon 130 J en calor).', 'intermediate', 1240
    ))
    q.append(make_mc(
        'Una máquina consume 1000 J de energía eléctrica y produce 800 J de trabajo mecánico útil. ¿Cuál es su rendimiento o eficiencia?',
        '80%', ['20%', '125%', '800%'],
        'Rendimiento η = (Energía útil / Energía total) * 100 = (800 / 1000) * 100 = 80%.',
        'η = 800 / 1000 * 100% = 80%.', 'basic', 1110
    ))
    q.append(make_mc(
        'Si una fuerza F tira de un trineo con un ángulo de 60° respecto a la horizontal, ¿qué fracción de la fuerza realiza trabajo para moverlo hacia adelante?',
        'La mitad de la fuerza (F · cos(60°) = 0.5 F)', ['Toda la fuerza F', '0.866 F', 'Cero'],
        'Solo la componente horizontal paralela al desplazamiento realiza trabajo: Fx = F * cos(60°) = 0.5 F.',
        'Fx = F * cos(60°) = 0.5 F.', 'intermediate', 1190
    ))
    q.append(make_mc(
        'Un saltador de Bungee de 70 kg salta desde un puente. ¿En qué punto de la oscilación su energía cinética es máxima?',
        'En el punto donde la fuerza elástica de la cuerda equilibra exactamente su peso (Fuerza neta = 0)',
        ['En el instante de máxima elongación de la cuerda', 'Justo al saltar del puente', 'A mitad de la longitud natural de la cuerda'],
        'La velocidad es máxima cuando la aceleración se anula (a = 0 ⇒ ΣF = 0), es decir, en la posición de equilibrio dinámico.',
        'a = 0 ⇒ v = v_máx ⇒ Ek = máxima.', 'advanced', 1290
    ))
    q.append(make_mc(
        'Un kilowatt-hora (1 kWh) es una unidad de:',
        'Energía (equivale a 3.6 × 10⁶ Joules)', ['Potencia eléctrica', 'Fuerza eléctrica', 'Tensión'],
        '1 kWh = (1000 W) * (3600 s) = 3.6 × 10⁶ J. Mide energía consumida, no potencia.',
        'Energía = Potencia * Tiempo ⇒ 1000 W * 3600 s = 3.6 MJ.', 'basic', 1120
    ))
    q.append(make_mc(
        'Un patinador desciende por una pista sin rozamiento desde 5.0 m de altura y luego ingresa a una rampa que sube a 3.0 m. ¿Cuál es su rapidez en ese punto más alto de la rampa? (g = 9.8 m/s²).',
        '6.26 m/s', ['9.90 m/s', '7.67 m/s', '4.43 m/s'],
        'Conservación de Em: m*g*h1 = m*g*h2 + ½ m v² ⇒ v = √(2*g*(h1 - h2)) = √(2 * 9.8 * 2.0) = √39.2 ≈ 6.26 m/s.',
        'v = √(2 * 9.8 * 2) = √39.2 ≈ 6.26 m/s.', 'intermediate', 1220
    ))
    return q
