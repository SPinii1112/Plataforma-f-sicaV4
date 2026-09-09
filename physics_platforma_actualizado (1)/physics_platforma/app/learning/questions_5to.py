# Generador de 20 preguntas por tema para 5.º año
from app.learning.question_helper import make_mc

def get_cinematica_questions():
    q = []
    # 1 a 5: MRU y conversiones
    q.append(make_mc(
        'Un ciclista se desplaza en línea recta a rapidez constante de 18 km/h durante 20 minutos. ¿Qué distancia recorre en metros?',
        '6000 m',
        ['360 m', '3600 m', '1800 m'],
        'Convertir km/h a m/s dividiendo entre 3.6 (18/3.6 = 5.0 m/s) y los 20 min a segundos (20*60 = 1200 s). Distancia = 5.0 * 1200 = 6000 m.',
        '1. v = 18 km/h / 3.6 = 5.0 m/s.\n2. t = 20 min * 60 s/min = 1200 s.\n3. d = v * t = 5.0 m/s * 1200 s = 6000 m.',
        'basic', 1100
    ))
    q.append(make_mc(
        '¿Cuál es la diferencia fundamental entre el vector desplazamiento y la distancia recorrida?',
        'El desplazamiento es un vector que une la posición inicial con la final independientemente de la trayectoria; la distancia es un escalar que mide la longitud del camino.',
        ['El desplazamiento siempre es mayor que la distancia recorrida.', 'Ambas son magnitudes vectoriales con la misma unidad.', 'La distancia tiene dirección y sentido, mientras que el desplazamiento es escalar.'],
        'El desplazamiento Δr depende únicamente de los puntos inicial y final. La distancia d es la longitud acumulada a lo largo de la trayectoria real.',
        'Definición de cinemática vectorial: Δr = r_f - r_0 (vector). Distancia = longitud de arco recorrida (escalar no negativo).',
        'basic', 1120
    ))
    q.append(make_mc(
        'Dos móviles parten uno hacia el otro desde dos puntos distantes 600 m a 20 m/s y 10 m/s en MRU. ¿En qué instante se cruzan?',
        't = 20 s',
        ['t = 30 s', 't = 15 s', 't = 60 s'],
        'En encuentro en sentido contrario, las rapideces se suman: v_relativa = 20 + 10 = 30 m/s. Tiempo de encuentro = 600 m / 30 m/s = 20 s.',
        'x1 = 20*t; x2 = 600 - 10*t. Igualando: 20*t = 600 - 10*t => 30*t = 600 => t = 20 s.',
        'intermediate', 1180
    ))
    q.append(make_mc(
        'Un automóvil que parte del reposo acelera uniformemente a 3.0 m/s² durante 6.0 s. ¿Qué rapidez adquiere al cabo de ese tiempo?',
        '18.0 m/s',
        ['9.0 m/s', '36.0 m/s', '12.0 m/s'],
        'En el MRUV con v0 = 0: v(t) = a * t = 3.0 m/s² * 6.0 s = 18.0 m/s.',
        'v = v0 + a*t = 0 + 3.0 * 6.0 = 18.0 m/s.',
        'basic', 1110
    ))
    q.append(make_mc(
        'Un tren circula a 108 km/h y frena uniformemente con a = -2.5 m/s² hasta detenerse. ¿Qué distancia necesita para frenar?',
        '180 m',
        ['216 m', '108 m', '90 m'],
        '108 km/h / 3.6 = 30 m/s. Por Torricelli: vf² = v0² + 2*a*d => 0 = 30² + 2*(-2.5)*d => 5*d = 900 => d = 180 m.',
        'v0 = 30 m/s, vf = 0, a = -2.5 m/s². d = (vf² - v0²) / (2*a) = (0 - 900) / (-5) = 180 m.',
        'intermediate', 1210
    ))
    # 6 a 10: Torricelli y gráficos
    q.append(make_mc(
        'En un gráfico de velocidad en función del tiempo (v vs. t), ¿qué magnitud física representa el área bajo la curva?',
        'El desplazamiento neto (Δx)',
        ['La aceleración instantánea', 'La velocidad media', 'La fuerza resultante'],
        'El área bajo la curva v vs t es la integral definida ∫ v dt, que representa exactamente el desplazamiento neto con su signo.',
        'Área = ∫ v(t) dt = Δx. Las áreas sobre el eje t representan avance positivo y bajo el eje retroceso.',
        'basic', 1130
    ))
    q.append(make_mc(
        'En un gráfico posición-tiempo (x vs. t), si la curva es una parábola cóncava hacia abajo (∩), ¿qué signo tiene la aceleración?',
        'Aceleración negativa (a < 0)',
        ['Aceleración positiva (a > 0)', 'Aceleración nula (a = 0)', 'Velocidad constante'],
        'La concavidad de x(t) está dada por la segunda derivada d²x/dt² = a. Si es cóncava hacia abajo, la aceleración es negativa.',
        'Segunda derivada: d²x/dt² = a. Curvatura hacia abajo (∩) indica que la velocidad va disminuyendo en el tiempo (a < 0).',
        'intermediate', 1200
    ))
    q.append(make_mc(
        'Un móvil recorre los primeros 100 m a 10 m/s y los siguientes 100 m a 20 m/s. ¿Cuál es su velocidad media en todo el trayecto?',
        '13.3 m/s',
        ['15.0 m/s', '12.5 m/s', '16.7 m/s'],
        '¡Error común: no es el promedio aritmético! Tiempo 1 = 100/10 = 10 s; Tiempo 2 = 100/20 = 5 s. vm = d_total / t_total = 200 m / 15 s = 13.33 m/s.',
        '1. t1 = 100/10 = 10 s.\n2. t2 = 100/20 = 5 s.\n3. vm = (100+100)/(10+5) = 200/15 ≈ 13.3 m/s.',
        'intermediate', 1250
    ))
    q.append(make_mc(
        'Un cuerpo es lanzado verticalmente hacia arriba con v0 = 29.4 m/s. ¿Cuánto tiempo tarda en alcanzar su altura máxima? (g = 9.8 m/s²).',
        '3.0 s',
        ['1.5 s', '6.0 s', '4.5 s'],
        'En el punto más alto vf = 0: t = v0 / g = 29.4 / 9.8 = 3.0 s.',
        'vf = v0 - g*t => 0 = 29.4 - 9.8*t => t = 29.4 / 9.8 = 3.0 s.',
        'basic', 1140
    ))
    q.append(make_mc(
        'En el punto más alto del tiro vertical, ¿cuáles son los valores de la velocidad y de la aceleración?',
        'v = 0 m/s y a = 9.8 m/s² hacia abajo',
        ['v = 0 m/s y a = 0 m/s²', 'v = 9.8 m/s y a = 0 m/s²', 'v = 0 m/s y a = 9.8 m/s² hacia arriba'],
        'En el vértice la velocidad se anula instantáneamente, pero la aceleración gravitatoria NO se anula: sigue valiendo g hacia abajo.',
        'La gravedad nunca cesa de actuar sobre el cuerpo en caída libre, por lo que a = -g en todo instante del vuelo.',
        'intermediate', 1210
    ))
    # 11 a 20: MRUV avanzado, vectores y gráficas
    q.append(make_mc(
        'Si un vector A tiene componentes Ax = 6.0 m y Ay = 8.0 m, ¿cuál es su módulo y su versor unitario?',
        '||A|| = 10.0 m, u = 0.6 i + 0.8 j',
        ['||A|| = 14.0 m, u = 0.6 i + 0.8 j', '||A|| = 10.0 m, u = 6.0 i + 8.0 j', '||A|| = 7.0 m, u = 0.5 i + 0.5 j'],
        'Módulo = √(6² + 8²) = √(36+64) = 10 m. Versor = A / ||A|| = (6/10) i + (8/10) j = 0.6 i + 0.8 j.',
        '||A|| = √(6² + 8²) = 10 m. u_A = (6/10)i + (8/10)j = 0.6i + 0.8j.',
        'basic', 1150
    ))
    q.append(make_mc(
        'Dos vectores A y B son perpendiculares si y solo si su producto escalar cumple:',
        'A · B = 0',
        ['A × B = 0', '||A|| = ||B||', 'A · B = 1'],
        'El producto escalar es ||A|| ||B|| cos(θ). Si θ = 90°, cos(90°) = 0, por lo que el producto punto es nulo.',
        'Condición analítica de ortogonalidad: A · B = Ax*Bx + Ay*By = 0.',
        'basic', 1120
    ))
    q.append(make_mc(
        'Un proyectil se deja caer desde una torre de altura h = 44.1 m. ¿Cuánto tiempo tarda en impactar el suelo? (g = 9.8 m/s²).',
        '3.0 s',
        ['4.5 s', '2.0 s', '9.0 s'],
        'h = ½ g t² => t = √(2h / g) = √(2 * 44.1 / 9.8) = √9 = 3.0 s.',
        '44.1 = 0.5 * 9.8 * t² => 44.1 = 4.9 * t² => t² = 9 => t = 3.0 s.',
        'basic', 1160
    ))
    q.append(make_mc(
        '¿Cuál es la rapidez de impacto con el suelo del proyectil que cae desde 44.1 m? (g = 9.8 m/s²).',
        '29.4 m/s',
        ['14.7 m/s', '44.1 m/s', '9.8 m/s'],
        'vf = g * t = 9.8 * 3.0 = 29.4 m/s (o por Torricelli: vf = √(2gh) = √(2*9.8*44.1) = 29.4 m/s).',
        'vf = √(2 * 9.8 * 44.1) = 29.4 m/s.',
        'intermediate', 1190
    ))
    q.append(make_mc(
        'En un gráfico v vs. t lineal, una recta horizontal a valor v = 15 m/s representa:',
        'Un MRU a 15 m/s con aceleración nula',
        ['Un MRUV con aceleración constante de 15 m/s²', 'Un cuerpo en reposo a 15 m de distancia', 'Un movimiento acelerado'],
        'Si la velocidad no cambia en el tiempo (pendiente cero), la aceleración es nula y el movimiento es rectilíneo uniforme.',
        'Pendiente dv/dt = a = 0. Recta horizontal en v(t) = MRU.',
        'basic', 1100
    ))
    q.append(make_mc(
        'Un móvil pasa por x = 10 m a t = 0 s con v = 4 m/s y acelera a 2 m/s². ¿Cuál es su posición a los t = 5 s?',
        '55 m',
        ['35 m', '50 m', '65 m'],
        'x(t) = x0 + v0*t + 0.5*a*t² = 10 + 4*5 + 0.5*2*(25) = 10 + 20 + 25 = 55 m.',
        'x(5) = 10 + 4(5) + 0.5(2)(5²) = 10 + 20 + 25 = 55 m.',
        'intermediate', 1200
    ))
    q.append(make_mc(
        'Si un auto frena de 20 m/s a 10 m/s en 50 m, ¿cuál es su aceleración?',
        '-3.0 m/s²',
        ['-1.5 m/s²', '-6.0 m/s²', '-2.0 m/s²'],
        'Torricelli: vf² = v0² + 2*a*d => 10² = 20² + 2*a*50 => 100 = 400 + 100*a => 100*a = -300 => a = -3.0 m/s².',
        'a = (vf² - v0²) / (2*d) = (100 - 400) / (100) = -300 / 100 = -3.0 m/s².',
        'advanced', 1280
    ))
    q.append(make_mc(
        'Un móvil parte del reposo y en el primer segundo recorre 2.0 m. ¿Qué distancia recorrerá en los primeros 3 segundos?',
        '18.0 m',
        ['6.0 m', '12.0 m', '9.0 m'],
        'En t=1 s: d1 = 0.5*a*(1)² = 2 m => a = 4 m/s². En t=3 s: d3 = 0.5*4*(3)² = 2 * 9 = 18 m.',
        'd(3) = 0.5 * 4.0 * 9 = 18.0 m. La distancia crece con el cuadrado del tiempo (3² = 9 veces más que en el 1er segundo: 9 * 2 = 18 m).',
        'advanced', 1290
    ))
    q.append(make_mc(
        'La pendiente de la recta secante entre dos puntos de una gráfica x vs. t representa:',
        'La velocidad media en ese intervalo',
        ['La velocidad instantánea', 'La aceleración media', 'El desplazamiento'],
        'La secante conecta (t1, x1) y (t2, x2): pendiente = (x2 - x1)/(t2 - t1) = Δx / Δt = velocidad media.',
        'Pendiente secante = Δx/Δt = vm. Pendiente tangente = dx/dt = v instantánea.',
        'intermediate', 1190
    ))
    q.append(make_mc(
        'Si un vehículo que va a 90 km/h debe detenerse ante un obstáculo y el tiempo de reacción del conductor es 0.8 s, ¿qué distancia recorre antes de apretar los frenos?',
        '20.0 m',
        ['72.0 m', '15.0 m', '25.0 m'],
        'Durante el tiempo de reacción el auto mantiene velocidad constante: v = 90 / 3.6 = 25 m/s. Distancia = 25 m/s * 0.8 s = 20.0 m.',
        'd_reacción = v * t_reacción = 25.0 m/s * 0.8 s = 20.0 m.',
        'intermediate', 1220
    ))
    return q

print('get_cinematica_questions definida')

def get_dinamica_questions():
    q = []
    # 20 preguntas de Dinamica
    q.append(make_mc(
        'Un cuerpo de 5.0 kg sobre un plano horizontal liso recibe una fuerza neta constante de 15 N. ¿Cuál es su aceleración?',
        '3.0 m/s²', ['75.0 m/s²', '0.33 m/s²', '10.0 m/s²'],
        'Segunda Ley de Newton: a = F_neta / m = 15 N / 5.0 kg = 3.0 m/s².',
        'a = F / m = 15 / 5 = 3.0 m/s².', 'basic', 1100
    ))
    q.append(make_mc(
        'Si la fuerza neta externa sobre un cuerpo es nula (ΣF = 0), podemos asegurar con certeza que:',
        'El cuerpo se encuentra en reposo o con movimiento rectilíneo uniforme (velocidad constante)',
        ['El cuerpo está obligatoriamente en reposo absoluto', 'El cuerpo está frenando', 'No actúa ninguna fuerza sobre él'],
        'La Primera Ley de Newton afirma que aceleración nula implica velocidad constante, lo que incluye v = 0 (reposo) o v = cte (MRU).',
        'ΣF = 0 ⇔ a = 0 ⇔ v = constante.', 'basic', 1110
    ))
    q.append(make_mc(
        '¿Por qué las fuerzas de acción y reacción nunca pueden anularse entre sí?',
        'Porque actúan siempre sobre dos cuerpos físicos distintos',
        ['Porque tienen sentidos contrarios', 'Porque sus módulos son diferentes', 'Porque no actúan al mismo tiempo'],
        'La Tercera Ley establece que F_AB actúa sobre B y F_BA actúa sobre A. Para anularse deberían actuar sobre el mismo cuerpo.',
        'Actúan en cuerpos diferentes; la resultante sobre cada cuerpo individual se calcula por separado.', 'intermediate', 1180
    ))
    q.append(make_mc(
        'Un bloque de 8.0 kg reposa sobre una mesa horizontal (g = 9.8 m/s²). ¿Cuánto vale la fuerza normal que la mesa ejerce sobre él?',
        '78.4 N hacia arriba', ['8.0 N hacia abajo', '9.8 N hacia arriba', '0 N'],
        'En equilibrio vertical: N - P = 0 ⇒ N = P = m*g = 8.0 * 9.8 = 78.4 N.',
        'N = m*g = 8.0 * 9.8 = 78.4 N.', 'basic', 1110
    ))
    q.append(make_mc(
        'Un cuerpo de masa m = 10 kg se encuentra sobre un plano con μ_e = 0.50 y μ_c = 0.35 (g = 9.8 m/s²). ¿Cuál es la fuerza horizontal mínima para iniciar el movimiento?',
        '49.0 N', ['34.3 N', '98.0 N', '5.0 N'],
        'Para vencer el reposo se debe superar la fuerza de rozamiento estático máxima: f_re_max = μ_e * N = 0.50 * (10 * 9.8) = 49.0 N.',
        'f_re,máx = μ_e * N = 0.50 * 98 = 49.0 N.', 'intermediate', 1210
    ))
    q.append(make_mc(
        'Una vez iniciado el movimiento del bloque anterior con F = 49.0 N constante, ¿cuál será su aceleración durante el deslizamiento?',
        '1.47 m/s²', ['4.90 m/s²', '0 m/s²', '3.43 m/s²'],
        'En movimiento actúa fricción cinética: f_rc = μ_c * N = 0.35 * 98 = 34.3 N. Fuerza neta: F - f_rc = 49.0 - 34.3 = 14.7 N. Aceleración: a = 14.7 / 10 = 1.47 m/s².',
        'a = (F - f_rc) / m = (49.0 - 34.3) / 10 = 1.47 m/s².', 'intermediate', 1240
    ))
    q.append(make_mc(
        'Un cuerpo desciende por un plano inclinado de ángulo α sin rozamiento. ¿Cuál es su aceleración a lo largo del plano?',
        'a = g · sen(α)', ['a = g · cos(α)', 'a = g · tan(α)', 'a = g'],
        'La componente del peso paralela al plano es P_x = m*g*sen(α). Por 2.ª Ley: m*g*sen(α) = m*a ⇒ a = g*sen(α).',
        'ΣFx = m*a ⇒ m*g*sen(α) = m*a ⇒ a = g*sen(α).', 'basic', 1150
    ))
    q.append(make_mc(
        'En un plano inclinado con rozamiento, la condición de deslizamiento inminente por el propio peso del bloque ocurre en el ángulo crítico α_c donde:',
        'tan(α_c) = μ_e', ['sen(α_c) = μ_e', 'cos(α_c) = μ_e', 'α_c = 45° siempre'],
        'm*g*sen(α_c) = f_re_max = μ_e * m*g*cos(α_c) ⇒ sen(α_c)/cos(α_c) = μ_e ⇒ tan(α_c) = μ_e.',
        'Deducción: Px = f_re,máx ⇒ m*g*sen(α_c) = μ_e * m*g*cos(α_c) ⇒ tan(α_c) = μ_e.', 'intermediate', 1230
    ))
    q.append(make_mc(
        'Un ascensor de 500 kg desciende frenando con una aceleración hacia arriba de 2.0 m/s². ¿Cuál es la tensión en el cable? (g = 9.8 m/s²).',
        '5900 N', ['3900 N', '4900 N', '1000 N'],
        'Si frena al bajar, la aceleración neta es hacia arriba: T - P = m*a ⇒ T = m*(g + a) = 500 * (9.8 + 2.0) = 500 * 11.8 = 5900 N.',
        'T = m*(g + a) = 500 * 11.8 = 5900 N.', 'advanced', 1270
    ))
    q.append(make_mc(
        'Un resorte ideal de k = 200 N/m se estira 0.05 m desde su posición de equilibrio. ¿Qué fuerza elástica ejerce?',
        '10.0 N', ['4000 N', '4.0 N', '20.0 N'],
        'Ley de Hooke: Fe = k * x = 200 N/m * 0.05 m = 10.0 N.',
        'Fe = 200 * 0.05 = 10.0 N.', 'basic', 1110
    ))
    q.append(make_mc(
        'Dos bloques de masas m1 = 2 kg y m2 = 3 kg están en contacto sobre una superficie horizontal lisa. Se empuja m1 con F = 10 N. ¿Cuál es la fuerza de contacto entre los dos bloques?',
        '6.0 N', ['10.0 N', '4.0 N', '5.0 N'],
        'Aceleración total: a = 10 / (2+3) = 2.0 m/s². La fuerza de contacto es la única fuerza horizontal que empuja a m2: F_contacto = m2 * a = 3 kg * 2.0 m/s² = 6.0 N.',
        '1. a = F / (m1+m2) = 10/5 = 2 m/s².\n2. F_12 = m2 * a = 3 * 2 = 6.0 N.', 'intermediate', 1250
    ))
    q.append(make_mc(
        'Si un astronauta tiene una masa de 70 kg en la Tierra, ¿cuál será su masa en la Luna donde la gravedad es un sexto?',
        '70 kg', ['11.7 kg', '420 kg', '0 kg'],
        'La masa es una propiedad intrínseca e inercial de la materia y no cambia con el campo gravitatorio. Su peso sí disminuye a la sexta parte.',
        'Masa = 70 kg constante en cualquier lugar del universo. Peso = m * g_luna ≈ 114 N.', 'basic', 1100
    ))
    q.append(make_mc(
        'Un bloque se lanza hacia arriba por un plano inclinado de 30° con fricción μ_c = 0.20. Durante el ascenso, ¿cómo actúa la fuerza de rozamiento?',
        'Hacia abajo del plano, sumándose a la componente del peso para frenar el bloque',
        ['Hacia arriba del plano, impulsándolo', 'Perpendicular al plano', 'Nula porque el cuerpo asciende'],
        'El rozamiento cinético se opone siempre al sentido del deslizamiento relativo; si el bloque sube, el rozamiento apunta hacia abajo.',
        'Sentido de f_rc opuesto a v: al subir, tanto Px como f_rc apuntan plano abajo frenando el cuerpo.', 'intermediate', 1220
    ))
    q.append(make_mc(
        'Un bloque de 4.0 kg cuelga del techo mediante una cuerda ligera. ¿Cuál es el valor de la tensión en la cuerda? (g = 9.8 m/s²).',
        '39.2 N', ['4.0 N', '19.6 N', '0 N'],
        'En reposo estático: T - P = 0 ⇒ T = m*g = 4.0 * 9.8 = 39.2 N.',
        'T = m*g = 39.2 N.', 'basic', 1110
    ))
    q.append(make_mc(
        'La unidad de medida de la fuerza en el Sistema Internacional, el Newton, equivale en magnitudes fundamentales a:',
        'kg · m / s²', ['kg · m² / s²', 'kg / s²', 'N · m / s'],
        'Por la 2.ª Ley F = m*a: [m] = kg, [a] = m/s², por lo que [F] = kg · m/s².',
        '1 N = 1 kg * 1 m/s².', 'basic', 1100
    ))
    q.append(make_mc(
        'Un bloque desliza sobre un plano horizontal rugoso con desaceleración constante a = 1.96 m/s² debido únicamente a la fricción. ¿Cuánto vale μ_c? (g = 9.8 m/s²).',
        '0.20', ['0.10', '0.40', '0.05'],
        'f_rc = m*a ⇒ μ_c * m*g = m*a ⇒ μ_c = a / g = 1.96 / 9.8 = 0.20.',
        'μ_c = a / g = 1.96 / 9.8 = 0.20.', 'intermediate', 1230
    ))
    q.append(make_mc(
        'Un cuerpo de 12 kg cuelga de dos cuerdas simétricas que forman un ángulo de 60° entre sí. ¿Qué tensión soporta cada cuerda? (g = 9.8 m/s²).',
        '67.9 N', ['117.6 N', '58.8 N', '33.9 N'],
        'Peso P = 12 * 9.8 = 117.6 N. Cada cuerda forma 30° con la vertical: 2 * T * cos(30°) = P ⇒ T = 117.6 / (2 * cos(30°)) = 117.6 / 1.732 ≈ 67.9 N.',
        '2*T*cos(30°) = 117.6 ⇒ T = 117.6 / (2*0.866) ≈ 67.9 N.', 'advanced', 1290
    ))
    q.append(make_mc(
        'Si sobre un cuerpo de 2 kg actúa una fuerza hacia la derecha de 20 N y una fuerza hacia la izquierda de 8 N, ¿cuál es su aceleración?',
        '6.0 m/s² hacia la derecha', ['14.0 m/s² hacia la derecha', '10.0 m/s²', '4.0 m/s²'],
        'Fuerza neta = 20 - 8 = 12 N hacia la derecha. Aceleración = 12 N / 2 kg = 6.0 m/s².',
        'a = F_neta / m = 12 / 2 = 6.0 m/s².', 'basic', 1120
    ))
    q.append(make_mc(
        'Al frenar bruscamente un autobús, los pasajeros son lanzados hacia adelante debido a:',
        'La inercia de sus propios cuerpos que tienden a conservar la velocidad que llevaban',
        ['Una fuerza misteriosa hacia adelante que surge de la nada', 'La fuerza de reacción del freno', 'La gravedad'],
        'Por la 1.ª Ley de Newton (inercia), todo cuerpo tiende a mantener su velocidad previa en ausencia de fuerzas netas que actúen sobre él.',
        'Principio de Inercia: los pasajeros continúan con el movimiento rectilíneo uniforme que tenían antes de que el bus frenara.', 'basic', 1110
    ))
    q.append(make_mc(
        'Un plano inclinado tiene un ángulo de 30°. Si g = 9.8 m/s² y se desprecia el rozamiento, ¿cuánto tarda un cuerpo en recorrer 4.9 m partiendo del reposo?',
        '1.41 s (√2 s)', ['1.0 s', '2.0 s', '0.5 s'],
        'a = g * sen(30°) = 9.8 * 0.5 = 4.9 m/s². d = 0.5*a*t² ⇒ 4.9 = 0.5*4.9*t² ⇒ t² = 2 ⇒ t = √2 ≈ 1.41 s.',
        'd = 0.5 * a * t² ⇒ 4.9 = 0.5 * 4.9 * t² ⇒ t² = 2 ⇒ t = 1.41 s.', 'advanced', 1260
    ))
    return q

print('get_dinamica_questions definida')
