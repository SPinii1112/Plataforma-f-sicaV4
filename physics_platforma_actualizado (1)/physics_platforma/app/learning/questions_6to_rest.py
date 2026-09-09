# -*- coding: utf-8 -*-
from app.learning.question_helper import make_mc

def get_potencial_questions():
    q = []
    q.append(make_mc(
        'El potencial eléctrico V a una distancia r = 0.50 m de una carga puntual Q = +10 nC en el vacío es:',
        '180 V', ['360 V', '90 V', '1800 V'],
        'V = ke * Q / r = 9.0x10⁹ * 10x10⁻⁹ / 0.50 = 90 / 0.50 = 180 V.', 'V = 90 / 0.5 = 180 V.', 'basic', 1120
    ))
    q.append(make_mc(
        '¿Cuánto trabajo realiza el campo electrostático al mover una carga q = +2.0 μC entre dos puntos con diferencia de potencial VA - VB = 50 V?',
        '1.0 × 10⁻⁴ J (0.10 mJ)', ['2.5 × 10⁻⁵ J', '100 J', '0 J'],
        'W = q * (VA - VB) = 2.0x10⁻⁶ C * 50 V = 1.0x10⁻⁴ J.', 'W = q * ΔV = 2x10⁻⁶ * 50 = 10⁻⁴ J.', 'intermediate', 1190
    ))
    q.append(make_mc(
        'El trabajo necesario para trasladar una carga q a lo largo de una superficie equipotencial es:',
        'Estrictamente 0 J', ['q · V', 'Infinito', 'Depende de la distancia recorrida'],
        'En una superficie equipotencial VA = VB, por lo que ΔV = 0 y W = -q ΔV = 0 J.', 'ΔV = 0 ⇒ W = 0 J.', 'basic', 1100
    ))
    q.append(make_mc(
        'Las superficies equipotenciales creadas por una carga puntual aislada en el espacio son:',
        'Esferas concéntricas centradas en la carga', ['Planos paralelos', 'Cilindros coaxiales', 'Líneas rectas'],
        'Como V = ke Q / r, todos los puntos con el mismo potencial están a idéntico radio r (esferas concéntricas).', 'Esferas concéntricas.', 'basic', 1110
    ))
    q.append(make_mc(
        'En un campo eléctrico uniforme de magnitud E = 400 V/m, dos superficies equipotenciales difieren en ΔV = 20 V. ¿Cuál es la distancia d entre ellas?',
        '0.05 m (5.0 cm)', ['0.20 m', '20.0 m', '0.005 m'],
        '|ΔV| = E * d ⇒ d = |ΔV| / E = 20 V / 400 V/m = 0.05 m = 5 cm.', 'd = 20 / 400 = 0.05 m.', 'intermediate', 1180
    ))
    q.append(make_mc(
        'La energía potencial electrostática U de dos cargas q1 = +4 μC y q2 = -3 μC separadas r = 0.20 m en el vacío es:',
        '-0.54 J (sistema ligado estable)', ['+0.54 J', '-5.4 J', '-0.027 J'],
        'U = ke * (q1 * q2) / r = 9.0x10⁹ * (4x10⁻⁶ * -3x10⁻⁶) / 0.20 = -0.108 / 0.20 = -0.54 J.', 'U = -0.108 / 0.20 = -0.54 J.', 'intermediate', 1210
    ))
    q.append(make_mc(
        'La relación diferencial general entre el campo eléctrico y el potencial escalar en una dimensión es:',
        'E = - dV / dx (el campo apunta hacia donde el potencial decrece más rápido)',
        ['E = dV / dx', 'E = ∫ V dx', 'E = V / x²'],
        'El campo eléctrico es el gradiente negativo del potencial electrostático: E = - ∇V.', 'E = - dV/dx.', 'intermediate', 1220
    ))
    q.append(make_mc(
        'Si el potencial eléctrico es constante en toda una región del espacio (V(x,y,z) = 100 V = cte), ¿cuál es el campo eléctrico en esa región?',
        'E = 0 N/C', ['100 N/C', '10 N/C', 'Infinito'],
        'Como E = - dV/dx y la derivada de una constante es cero, el campo eléctrico es estrictamente nulo.', 'dV/dx = 0 ⇒ E = 0.', 'basic', 1130
    ))
    q.append(make_mc(
        'Una partícula alfa (q = +2e = 3.2 × 10⁻¹⁹ C) parte del reposo y se acelera a través de una diferencia de potencial de 5000 V. ¿Cuál es su energía cinética final?',
        '10 keV (equivale a 1.6 × 10⁻¹⁵ J)', ['5 keV', '2.5 keV', '20 keV'],
        'Ek = q * ΔV = (2 e) * (5000 V) = 10000 eV = 10 keV = 1.6 × 10⁻¹⁵ J.', 'Ek = 2 * 5000 eV = 10 keV.', 'intermediate', 1230
    ))
    q.append(make_mc(
        'En un conductor en equilibrio electrostático cargado, el potencial eléctrico en cualquier punto de su volumen interior es:',
        'Constante e idéntico al potencial de su superficie exterior', ['Cero en el centro y máximo afuera', 'Mayor en el centro', 'Infinito'],
        'Como E = 0 en el interior y E = -dV/dr, entonces dV/dr = 0, lo que significa que V es constante en todo el conductor.', 'V = constante en todo el conductor.', 'intermediate', 1200
    ))
    q.append(make_mc(
        'El electrón-voltio (eV) es una unidad de:',
        'Energía (equivale a 1.602 × 10⁻¹⁹ Joules)', ['Tensión o potencial', 'Potencia', 'Carga eléctrica'],
        '1 eV es la energía cinética que gana un electrón al ser acelerado por una diferencia de potencial de 1 Voltio.', '1 eV = 1.6x10⁻¹⁹ J.', 'basic', 1110
    ))
    q.append(make_mc(
        'Una carga positiva libre colocada en un campo eléctrico tiende a moverse espontáneamente hacia zonas de:',
        'Menor potencial eléctrico (disminuyendo su energía potencial U)', ['Mayor potencial eléctrico', 'Igual potencial', 'Potencial infinito'],
        'La fuerza F = q E empuja las cargas positivas en la dirección de E, que es hacia donde V decrece.', 'De mayor V a menor V.', 'basic', 1120
    ))
    q.append(make_mc(
        'Una carga negativa libre (como un electrón) colocada en un campo eléctrico tiende a moverse espontáneamente hacia zonas de:',
        'Mayor potencial eléctrico (disminuyendo su energía potencial U)', ['Menor potencial eléctrico', 'Hacia donde E es mayor', 'Hacia el infinito'],
        'F = -e E empuja en sentido contrario a E, es decir, subiendo el potencial eléctrico hacia zonas de mayor V.', 'De menor V a mayor V.', 'basic', 1130
    ))
    q.append(make_mc(
        'Dos cargas puntuales +q y -q separadas por distancia d están en el eje X simétricas respecto al origen. ¿Cuánto vale el potencial eléctrico en el punto medio (x = 0)?',
        'V = 0 Voltios', ['V = 2 ke q / (d/2)', 'V = ke q / d', 'V = -2 ke q / d'],
        'El potencial es un escalar aditivo puro: V_total = V1 + V2 = ke q / (d/2) + ke (-q) / (d/2) = 0 V.', 'V = V(+) + V(-) = 0 V.', 'basic', 1140
    ))
    q.append(make_mc(
        'El trabajo para traer una tercera carga q3 = +1 μC desde el infinito hasta el centro del dipolo anterior donde V = 0 es:',
        'W_externo = 0 J', ['1.0 J', '9.0 × 10⁹ J', 'Infinito'],
        'W_ext = q3 * (V_final - V_inicial) = q3 * (0 - 0) = 0 J.', 'W = q * ΔV = 0 J.', 'intermediate', 1210
    ))
    q.append(make_mc(
        'El gradiente de potencial eléctrico ||∇V|| indica:',
        'La dirección y sentido de máxima tasa de variación espacial del potencial, siendo su opuesto el campo eléctrico E',
        ['La energía total del circuito', 'La fuerza de Coulomb neta', 'La densidad de carga'],
        'E = - grad(V). El gradiente apunta hacia donde el potencial crece más rápido.', 'E = - grad(V).', 'advanced', 1280
    ))
    q.append(make_mc(
        'Una esfera metálica de radio R = 0.10 m tiene una carga superficial Q = +2.0 μC. ¿Cuál es el potencial eléctrico en su centro?',
        '1.8 × 10⁵ V (180 kV)', ['0 V', '3.6 × 10⁵ V', 'Infinito'],
        'En equilibrio todo el conductor es equipotencial: V_interior = V_superficie = ke Q / R = 9x10⁹ * 2x10⁻⁶ / 0.10 = 180000 V.', 'V = ke Q / R = 180 kV.', 'advanced', 1270
    ))
    q.append(make_mc(
        '¿Cuál es el valor del campo eléctrico en el centro de la esfera conductora del ejercicio anterior?',
        'E = 0 N/C', ['1.8 × 10⁶ N/C', '180 V/m', '9.0 × 10⁹ N/C'],
        'Aunque el potencial V = 180 kV es alto, como es uniforme en todo el interior, su derivada espacial dV/dr es nula y E = 0.', 'E_interior = 0 N/C.', 'intermediate', 1220
    ))
    q.append(make_mc(
        'Dos puntos A y B están sobre una misma línea de campo eléctrico uniforme de 500 N/C separados por 0.10 m. Si A está más cerca de la placa positiva que B, ¿cuánto vale VA - VB?',
        '+50 V', ['-50 V', '5000 V', '0 V'],
        'En el sentido de las líneas de campo el potencial disminuye: VA > VB ⇒ VA - VB = E * d = 500 * 0.10 = +50 V.', 'ΔV = 500 * 0.10 = 50 V.', 'intermediate', 1200
    ))
    q.append(make_mc(
        'La rigidez dieléctrica del aire seco (campo máximo antes de que salte una chispa o arco eléctrico) es aproximadamente:',
        '3.0 × 10⁶ V/m (3000 V por milímetro)', ['100 V/m', '1000 V/m', '10⁹ V/m'],
        'A partir de 3 MV/m el aire se ioniza y conduce bruscamente, provocando chispas o rayos.', 'E_máx ≈ 3 MV/m.', 'basic', 1140
    ))
    return q
