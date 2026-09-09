# -*- coding: utf-8 -*-
from app.learning.question_helper import make_mc

def get_magnetismo_questions():
    q = []
    q.append(make_mc(
        'Una carga puntual q = +2.0 μC entra a una región con campo magnético uniforme B = 0.50 T con velocidad v = 4.0 × 10⁵ m/s perpendicular a las líneas de campo. ¿Cuál es la fuerza magnética de Lorentz?',
        '0.40 N', ['4.0 N', '0.04 N', '0 N'],
        'F = q * v * B * sen(90°) = 2.0x10⁻⁶ C * 4.0x10⁵ m/s * 0.50 T * 1 = 0.40 N.', 'F = 2x10⁻⁶ * 4x10⁵ * 0.5 = 0.40 N.', 'basic', 1120
    ))
    q.append(make_mc(
        '¿Por qué la fuerza magnética ejercida sobre una carga libre en movimiento NUNCA realiza trabajo mecánico (W = 0)?',
        'Porque el vector fuerza magnética es en todo instante estrictamente perpendicular al vector velocidad (F ⊥ v)',
        ['Porque el campo magnético no tiene energía', 'Porque los campos se anulan', 'Porque la carga es puntual'],
        'Como F_mag = q (v × B), por propiedades del producto vectorial F ⊥ v. La potencia instantánea P = F · v = 0, luego W = 0 J.', 'F ⊥ v ⇒ P = F·v = 0 ⇒ W = 0 J.', 'intermediate', 1210
    ))
    q.append(make_mc(
        '¿Qué consecuencia física directa tiene el hecho de que la fuerza magnética no realice trabajo sobre una partícula cargada libre?',
        'Su energía cinética y su rapidez escalar permanecen rigurosamente constantes (solo se desvía su trayectoria)',
        ['La partícula se detiene inmediatamente', 'Su velocidad se duplica', 'Pierde su carga'],
        'Como W = ΔEk = 0, la rapidez ||v|| no cambia; la fuerza magnética actúa únicamente como aceleración centrípeta desviadora.', 'Rapidez y Ek constantes.', 'intermediate', 1220
    ))
    q.append(make_mc(
        'Si una partícula cargada entra a un campo magnético uniforme con velocidad estrictamente paralela a las líneas de campo (θ = 0°):',
        'La fuerza magnética es exactamente 0 N y continúa en MRU sin desviarse',
        ['Experimenta la fuerza máxima', 'Frena bruscamente', 'Comienza a girar en círculos'],
        'F = q * v * B * sen(0°). Como sen(0°) = 0, la fuerza magnética es nula.', 'sen(0°) = 0 ⇒ F = 0.', 'basic', 1110
    ))
    q.append(make_mc(
        'Una partícula cargada que penetra perpendicularmente a un campo magnético uniforme describe una trayectoria:',
        'Circular uniforme con radio r = (m · v) / (|q| · B)', ['Parabólica abierta', 'Rectilínea acelerada', 'Hiperbólica'],
        'La fuerza de Lorentz actúa como fuerza centrípeta: |q| v B = m v² / r ⇒ r = (m v) / (|q| B).', 'r = mv / (qB).', 'intermediate', 1220
    ))
    q.append(make_mc(
        'El período de ciclotrón T (tiempo que demora la partícula en dar una vuelta completa en el campo magnético):',
        'Es independiente de la velocidad y del radio de la órbita: T = 2π m / (|q| B)',
        ['Es proporcional a la velocidad v', 'Aumenta con el cuadrado del radio', 'Disminuye con la masa'],
        'T = 2π r / v = 2π (mv/qB) / v = 2π m / (|q| B), propiedad clave de los aceleradores de partículas de ciclotrón.', 'T = 2πm / (qB).', 'advanced', 1280
    ))
    q.append(make_mc(
        'La regla de la mano derecha para la fuerza magnética sobre una carga POSITIVA establece que:',
        'El pulgar apunta en la velocidad v, los dedos extendidos en el campo B, y la fuerza sale de la palma',
        ['El pulgar apunta en el campo magnético', 'Se usa la mano izquierda siempre', 'La fuerza apunta en la velocidad'],
        'Convenio vectorial: v × B apunta saliendo de la palma con mano derecha para carga positiva (si q < 0, se invierte 180°).', 'Regla de la mano derecha.', 'basic', 1120
    ))
    q.append(make_mc(
        'La unidad de inducción magnética en el Sistema Internacional, el Tesla (T), equivale a:',
        '1 N / (A · m)', ['1 N / (C · s)', '1 Joule / Tesla', '1 Weber / segundo'],
        'De F = I * L * B ⇒ B = F / (I * L) ⇒ 1 Tesla = 1 Newton / (Amperio * metro).', '1 T = 1 N / (A · m).', 'basic', 1110
    ))
    q.append(make_mc(
        'Un conductor rectilíneo de longitud L = 0.40 m transporta una corriente I = 5.0 A perpendicular a un campo B = 0.20 T. ¿Cuál es la fuerza sobre el cable?',
        '0.40 N', ['4.0 N', '0.04 N', '1.0 N'],
        'F = I * L * B * sen(90°) = 5.0 A * 0.40 m * 0.20 T * 1 = 0.40 N.', 'F = 5 * 0.4 * 0.2 = 0.40 N.', 'basic', 1130
    ))
    q.append(make_mc(
        'Dos conductores rectilíneos paralelos muy largos por los que circulan corrientes en el MISMO sentido:',
        'Se atraen mutuamente con una fuerza proporcional al producto de sus corrientes',
        ['Se repelen mutuamente', 'No ejercen ninguna fuerza', 'Giran 90°'],
        'Experimento de Ampère: corrientes paralelas y del mismo sentido se atraen; en sentidos opuestos se repelen.', 'Mismo sentido ⇒ atracción.', 'basic', 1140
    ))
    q.append(make_mc(
        'La inexistencia de monopolos magnéticos aislados en la naturaleza se expresa formalmente en las ecuaciones de Maxwell por:',
        '∮ B · dA = 0 (Ley de Gauss para el magnetismo)', ['∮ E · dA = Q/ε0', '∮ B · dl = μ0 I', 'dΦB/dt = 0'],
        'Las líneas de campo magnético son lazos cerrados continuos; no existen cargas magnéticas puntuales aisladas (fuentes o sumideros puros).', 'Div B = 0 ⇒ No hay monopolos.', 'intermediate', 1240
    ))
    q.append(make_mc(
        'Si un protón y un electrón entran con la misma velocidad perpendicular a un campo magnético uniforme, ¿cuál describirá una circunferencia de mayor radio?',
        'El protón (su masa es ≈ 1836 veces mayor que la del electrón)',
        ['El electrón', 'Describen el mismo radio porque tienen igual carga en valor absoluto', 'Ninguno gira'],
        'r = (m · v) / (|q| · B). Con igual v, q y B, el radio es directamente proporcional a la masa inercial m.', 'r ∝ m ⇒ r_protón >> r_electrón.', 'intermediate', 1230
    ))
    q.append(make_mc(
        'El campo magnético B en el centro de una espira circular de radio R por la que circula corriente I en el vacío es:',
        'B = (μ0 · I) / (2 · R)', ['B = μ0 · I / (2π · R)', 'B = μ0 · I · R', 'B = 0'],
        'Por Ley de Biot-Savart integrada en la espira: B = μ0 I / (2R). (μ0 = 4π × 10⁻⁷ T·m/A).', 'B_espira = μ0 I / (2R).', 'intermediate', 1220
    ))
    q.append(make_mc(
        'El campo magnético en el interior de un solenoide ideal largo y compacto con n vueltas por unidad de longitud es:',
        'B = μ0 · n · I uniforme y paralelo al eje del solenoide', ['B = 0', 'B ∝ 1/r²', 'B radial'],
        'Por la Ley de Ampère: B = μ0 · (N/L) · I = μ0 · n · I.', 'B_solenoide = μ0 n I.', 'intermediate', 1210
    ))
    q.append(make_mc(
        'La fuerza magnética total de Lorentz sobre una partícula en presencia de campos E y B simultáneos es:',
        'F = q · (E + v × B)', ['F = q · E - q · (v × B)', 'F = q · v · B', 'F = m · a · B'],
        'Ecuación de Lorentz completa que unifica las fuerzas eléctrica y magnética sobre una carga.', 'F = q (E + v x B).', 'basic', 1120
    ))
    q.append(make_mc(
        'Un selector de velocidades utiliza campos E y B perpendiculares entre sí y a la velocidad de las partículas. Solo pasan sin desviarse las partículas con rapidez:',
        'v = E / B', ['v = B / E', 'v = E · B', 'v = √(E/B)'],
        'Para que no se desvíe: F_eléctrica = F_magnética ⇒ q E = q v B ⇒ v = E / B.', 'qE = qvB ⇒ v = E / B.', 'intermediate', 1220
    ))
    q.append(make_mc(
        'El campo magnético terrestre (geomagnético) tiene un orden de magnitud en la superficie de aproximadamente:',
        '0.5 Gauss (≈ 5 × 10⁻⁵ Tesla)', ['100 Tesla', '1 Tesla', '10⁻¹² Tesla'],
        'El campo de la Tierra es débil (≈ 30 a 60 μT), pero suficiente para orientar brújulas y desviar el viento solar.', 'B_tierra ≈ 0.5 G = 50 μT.', 'basic', 1130
    ))
    q.append(make_mc(
        'Los materiales ferromagnéticos como el hierro, níquel y cobalto se caracterizan por:',
        'Poseer dominios magnéticos que pueden alinearse fuertemente con un campo externo multiplicando B por miles de veces',
        ['Repeler violentamente los campos magnéticos', 'Tener permeabilidad magnética nula', 'Ser superconductores a temperatura ambiente'],
        'Estructura de dominios de Weiss con fuerte acoplamiento cuántico de espín.', 'Dominios ferromagnéticos.', 'basic', 1140
    ))
    q.append(make_mc(
        'Una partícula neutra (como un neutrón, q = 0) entra a un campo magnético intenso a gran velocidad. ¿Qué fuerza experimenta?',
        '0 N (no experimenta ninguna fuerza magnética)', ['Fuerza máxima', 'Fuerza gravitatoria magnética', 'Se desvía a la derecha'],
        'F = q (v × B). Si q = 0, F = 0 siempre.', 'q = 0 ⇒ F = 0.', 'basic', 1100
    ))
    q.append(make_mc(
        'El efecto Hall consiste en la aparición de una diferencia de potencial transversal en un conductor con corriente sumergido en un campo magnético, y permite determinar:',
        'El signo de los portadores de carga reales y su densidad volumétrica n',
        ['La masa del conductor', 'El calor disipado', 'La frecuencia de la luz'],
        'Descubierto por Edwin Hall en 1879; demostró experimentalmente que en los metales los portadores móviles son negativos (electrones).', 'Signo y densidad de portadores.', 'advanced', 1290
    ))
    return q

def get_induccion_questions():
    q = []
    q.append(make_mc(
        'El flujo magnético Φ_B a través de una espira plana de área A = 0.05 m² colocada perpendicular a un campo B = 0.40 T es:',
        '0.020 Wb (Weber)', ['8.0 Wb', '0.20 Wb', '0 Wb'],
        'Φ_B = B * A * cos(0°) = 0.40 T * 0.05 m² * 1 = 0.020 Wb.', 'Φ = 0.4 * 0.05 = 0.020 Wb.', 'basic', 1110
    ))
    q.append(make_mc(
        'La Ley de Inducción de Faraday establece que la fuerza electromotriz inducida E en un circuito es proporcional a:',
        'La rapidez temporal con la que varía el flujo magnético que atraviesa el circuito (E = - dΦB / dt)',
        ['El valor instantáneo del campo magnético B', 'La resistencia del cable', 'La masa del imán'],
        'No importa cuán grande sea el campo; lo que induce voltaje es su tasa de variación en el tiempo.', 'E = - dΦB/dt.', 'basic', 1100
    ))
    q.append(make_mc(
        'El signo negativo (-) en la Ley de Faraday-Lenz (E = - dΦB/dt) representa la Ley de Lenz, cuyo significado físico fundamental es:',
        'Que la corriente inducida siempre genera un campo magnético que se OPONE a la variación de flujo que la originó (conservación de la energía)',
        ['Que el voltaje es siempre negativo', 'Que se pierde energía en el proceso', 'Que el campo apunta hacia el sur'],
        'La oposición de Lenz garantiza que no se genere energía gratis violando el 1.er principio de la termodinámica.', 'Oposición a la variación de flujo.', 'basic', 1120
    ))
    q.append(make_mc(
        'Al acercar el polo norte de un imán hacia una espira metálica, la cara de la espira enfrentada al imán genera:',
        'Un polo norte inducido (corriente antihoraria) para repeler el acercamiento del imán',
        ['Un polo sur inducido para atraerlo', 'Ninguna corriente porque no hay pilas', 'Carga estática'],
        'Por Ley de Lenz, para oponerse al aumento de flujo entrante la espira crea un campo en sentido contrario (polo norte frente a norte).', 'Polo norte para repeler el avance.', 'intermediate', 1210
    ))
    q.append(make_mc(
        'Una bobina de N = 200 espiras experimenta una variación de flujo de 0.05 Wb a 0.01 Wb en un tiempo de 0.02 s. ¿Cuál es la fem media inducida?',
        '400 V', ['200 V', '80 V', '40 V'],
        'E = - N * (ΔΦ / Δt) = - 200 * (0.01 - 0.05) / 0.02 = - 200 * (-0.04) / 0.02 = 200 * 2 = 400 V.', 'E = 200 * 0.04 / 0.02 = 400 V.', 'intermediate', 1230
    ))
    q.append(make_mc(
        'Una barra conductora de longitud L = 0.50 m se mueve a rapidez constante v = 4.0 m/s perpendicularmente a un campo B = 0.30 T sobre rieles lisos. ¿Cuál es la fem motriz inducida?',
        '0.60 V', ['6.0 V', '0.06 V', '1.20 V'],
        'Fem de movimiento: E = B * L * v = 0.30 T * 0.50 m * 4.0 m/s = 0.60 V.', 'E = 0.3 * 0.5 * 4 = 0.60 V.', 'basic', 1130
    ))
    q.append(make_mc(
        'Las corrientes de Foucault (eddy currents) son corrientes parásitas inducidas en masas sólidas conductoras que se aprovechan en:',
        'Los frenos electromagnéticos de trenes de alta velocidad y cocinas de inducción',
        ['Las baterías de litio', 'Los fusibles de vidrio', 'Los condensadores cerámicos'],
        'La disipación Joule y el frenado magnético por Lenz de las corrientes parásitas se usan para frenado suave y cocción eficiente.', 'Frenos y cocinas de inducción.', 'intermediate', 1200
    ))
    q.append(make_mc(
        'Un transformador eléctrico ideal tiene N1 = 1000 espiras en el primario y N2 = 100 espiras en el secundario. Si se alimenta con 220 V de corriente alterna, la tensión de salida es:',
        '22.0 V (transformador reductor)', ['2200 V', '110 V', '44 V'],
        'Relación de transformación: V2 / V1 = N2 / N1 ⇒ V2 = 220 V * (100 / 1000) = 220 * 0.1 = 22.0 V.', 'V2 = 220 * 100/1000 = 22 V.', 'basic', 1130
    ))
    q.append(make_mc(
        '¿Por qué un transformador eléctrico NO funciona con corriente continua pura (DC)?',
        'Porque con corriente continua el campo magnético es constante en el tiempo y el flujo no varía (dΦB/dt = 0 ⇒ fem = 0)',
        ['Porque la corriente continua quema el cobre', 'Porque la continua no tiene electrones', 'Porque los cables son gruesos'],
        'La inducción exige tasa de cambio de flujo temporal (dΦ/dt ≠ 0), lo que requiere corriente alternada periódicamente.', 'dΦ/dt = 0 con DC ⇒ E = 0.', 'basic', 1110
    ))
    q.append(make_mc(
        'La autoinductancia L de una bobina se mide en el Sistema Internacional en:',
        'Henrios [1 H = 1 V · s / A = 1 Wb / A]', ['Faradios', 'Ohmios', 'Teslas'],
        'E_auto = - L (dI/dt) ⇒ [L] = V / (A/s) = V · s / A = Henrio (H).', 'Henrio (H).', 'basic', 1100
    ))
    q.append(make_mc(
        'La energía magnética almacenada en el campo magnético de un inductor de inductancia L por el que circula una corriente I es:',
        'U_B = ½ L · I²', ['U_B = L · I', 'U_B = ½ L · I', 'U_B = L · I²'],
        'Análogo magnético de la energía potencial del resorte (½ k x²) y del capacitor (½ C V²): U = ½ L I².', 'U = ½ L I².', 'intermediate', 1210
    ))
    q.append(make_mc(
        'Un alternador o generador eléctrico básico transforma:',
        'Energía mecánica de rotación en energía eléctrica mediante la rotación de una espira en un campo magnético',
        ['Energía química en energía magnética', 'Calor en trabajo estático', 'Energía solar en nuclear'],
        'Al rotar con velocidad angular ω, el flujo varía senoidalmente: Φ(t) = B A cos(ωt) ⇒ E(t) = B A ω sen(ωt) (fem alterna).', 'Generador: mecánica a eléctrica.', 'basic', 1120
    ))
    q.append(make_mc(
        'Si el área de una espira se reduce a la mitad en un campo magnético constante uniforme en un tiempo Δt:',
        'Se induce una corriente eléctrica durante ese intervalo de contracción de área',
        ['No se induce nada porque B es constante', 'El campo B se anula', 'Se quema la espira'],
        'Como Φ = B · A, variar el área geométrica A cambia el flujo (dΦ/dt = B dA/dt ≠ 0) induciendo voltaje.', 'Variar área induce fem.', 'intermediate', 1220
    ))
    q.append(make_mc(
        'Para reducir las pérdidas de potencia por corrientes parásitas de Foucault en el núcleo de un transformador, se suele:',
        'Construir el núcleo con láminas delgadas de acero al silicio aisladas entre sí por un barniz dieléctrico',
        ['Hacer el núcleo hueco de aire', 'Usar cables de cobre desnudos', 'Enfriar con hielo seco'],
        'El laminado corta físicamente las trayectorias de las corrientes de Foucault, reduciendo las pérdidas Joule drásticamente.', 'Núcleo laminado.', 'intermediate', 1240
    ))
    q.append(make_mc(
        'Si un imán cae verticalmente a través de un tubo de cobre largo hueco no magnético:',
        'Cae notablemente más lento que en el aire debido a una fuerza de frenado magnético ascendente producida por las corrientes inducidas de Lenz',
        ['Cae más rápido acelerado por el metal', 'Se detiene en la boca del tubo', 'Cae a velocidad normal'],
        'Las corrientes parásitas inducidas en las paredes del cobre crean campos que se oponen a la caída del imán (frenado por Lenz).', 'Frenado magnético por Lenz.', 'intermediate', 1200
    ))
    q.append(make_mc(
        'Una espira circular rota a frecuencia constante en un campo B uniforme. Si se triplica la velocidad angular de rotación (3ω), la fem máxima generada:',
        'Se triplica (E_máx = 3 · E_anterior)', ['Se multiplica por 9', 'Se reduce a la tercera parte', 'No varía'],
        'E(t) = N B A ω sen(ωt). El valor pico de la fem es directamente proporcional a la frecuencia angular ω.', 'E_máx ∝ ω.', 'intermediate', 1230
    ))
    q.append(make_mc(
        'La unidad del flujo magnético en el Sistema Internacional, el Weber (Wb), equivale a:',
        'Tesla · metro cuadrado (1 Wb = 1 T · m²)', ['Tesla / metro cuadrado', 'Newton · Amperio', 'Voltio / segundo'],
        'Φ = B * A ⇒ 1 Weber = 1 T * 1 m² = 1 Voltio * segundo.', '1 Wb = 1 T·m² = 1 V·s.', 'basic', 1100
    ))
    q.append(make_mc(
        'En un transformador ideal sin pérdidas que reduce el voltaje a la mitad (V2 = V1 / 2), la corriente secundaria I2:',
        'Se duplica (I2 = 2 · I1) para conservar la potencia eléctrica total (P1 = P2)',
        ['Se reduce a la mitad', 'Se cuadruplica', 'Permanece constante'],
        'Por conservación de la energía P1 = P2 ⇒ V1 · I1 = V2 · I2 ⇒ I2 = I1 * (V1 / V2) = 2 I1.', 'Menor voltaje implica mayor corriente.', 'intermediate', 1220
    ))
    q.append(make_mc(
        'Si un circuito de autoinductancia L = 0.2 H transporta una corriente que varía a razón de dI/dt = 50 A/s, ¿cuál es la fem autoinducida?',
        '10.0 V en sentido opuesto a la variación de corriente', ['250 V', '2.5 V', '0.004 V'],
        '|E| = L * (dI/dt) = 0.2 H * 50 A/s = 10.0 V.', 'E = 0.2 * 50 = 10.0 V.', 'intermediate', 1220
    ))
    q.append(make_mc(
        'La formulación final de la teoría electromagnética clásica unificada que incluye la corriente de desplazamiento de Maxwell fue publicada en:',
        '1865 (Las Ecuaciones de Maxwell)', ['1785', '1905', '1687'],
        'James Clerk Maxwell presentó en 1865 su teoría dinámica unificada de campos eléctricos y magnéticos prediciendo las ondas electromagnéticas.', '1865.', 'basic', 1110
    ))
    return q
