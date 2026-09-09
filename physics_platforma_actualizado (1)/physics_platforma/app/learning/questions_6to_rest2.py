# -*- coding: utf-8 -*-
from app.learning.question_helper import make_mc

def get_kirchhoff_questions():
    q = []
    q.append(make_mc(
        'La Primera Ley de Kirchhoff (Ley de Corrientes o Regla de Nodos) se deduce físicamente de:',
        'El Principio de Conservación de la Carga Eléctrica', ['La conservación de la energía', 'La ley de inercia', 'El efecto Joule'],
        'En un nodo sin acumulación neta de carga, la suma de corrientes entrantes es idéntica a la suma de salientes.', 'Conservación de carga.', 'basic', 1100
    ))
    q.append(make_mc(
        'La Segunda Ley de Kirchhoff (Ley de Tensiones o Regla de Mallas) se deduce físicamente de:',
        'El Principio de Conservación de la Energía en un campo electrostático conservativo',
        ['La conservación de la carga', 'La Tercera Ley de Newton', 'El principio de Pascal'],
        'Al recorrer un lazo cerrado y volver al punto de partida, el cambio neto de energía por unidad de carga es nulo (∮ E · dl = 0).', 'Conservación de energía.', 'basic', 1100
    ))
    q.append(make_mc(
        'En un nodo entran las corrientes I1 = 2.5 A e I2 = 3.5 A, y salen I3 = 1.0 A e I4. ¿Cuánto vale I4?',
        '5.0 A (saliendo del nodo)', ['7.0 A', '1.0 A', '6.0 A'],
        'Σ I_entran = Σ I_salen ⇒ 2.5 + 3.5 = 1.0 + I4 ⇒ 6.0 = 1.0 + I4 ⇒ I4 = 5.0 A.', 'I4 = 6.0 - 1.0 = 5.0 A.', 'basic', 1110
    ))
    q.append(make_mc(
        'Al recorrer una malla de Kirchhoff en un sentido elegido, al atravesar una fuente de fem E del polo negativo al positivo (- → +):',
        'Se asigna un valor positivo (+E) porque representa una ganancia de potencial eléctrico',
        ['Se asigna un valor negativo (-E)', 'Se multiplica por la resistencia', 'Se ignora'],
        'Ir de menor a mayor potencial (- a +) es una subida o ganancia de potencial (+E).', '- a + ⇒ +E.', 'basic', 1120
    ))
    q.append(make_mc(
        'Al recorrer una malla en el mismo sentido que la corriente asignada I a través de una resistencia R:',
        'Se asigna un signo negativo (- I · R) porque representa una caída de potencial por disipación óhmica',
        ['Se asigna un signo positivo (+ I · R)', 'Se suma la fem', 'Se anula'],
        'La corriente fluye naturalmente de mayor a menor potencial; recorrerla en su sentido es una caída (- I · R).', 'Mismo sentido ⇒ - I*R.', 'basic', 1120
    ))
    q.append(make_mc(
        'Si al resolver un sistema de ecuaciones de Kirchhoff el valor numérico de una corriente da negativo (ej. I = -2.0 A):',
        'Significa que su magnitud es 2.0 A pero su sentido físico real de circulación es exactamente opuesto al que se supuso arbitrariamente',
        ['El circuito explotará', 'Hubo un error aritmético obligatorio', 'El voltaje es negativo'],
        'El signo negativo en el resultado solo indica que la flecha supuesta en el diagrama era contraria al flujo real.', 'Sentido opuesto al supuesto.', 'intermediate', 1190
    ))
    q.append(make_mc(
        'En un circuito de una sola malla con una batería E1 = 18 V, una batería en oposición E2 = 6 V y dos resistencias R1 = 3 Ω y R2 = 3 Ω, ¿cuál es la corriente?',
        '2.0 A en el sentido de E1', ['4.0 A', '1.0 A', '3.0 A'],
        'Σ E = 18 - 6 = 12 V. R_total = 3 + 3 = 6 Ω. I = 12 V / 6 Ω = 2.0 A.', 'I = (18 - 6) / (3 + 3) = 12 / 6 = 2.0 A.', 'intermediate', 1210
    ))
    q.append(make_mc(
        '¿Cuántas ecuaciones de nodo independientes se pueden formular en una red eléctrica que posee N nodos?',
        'N - 1 ecuaciones independientes', ['N ecuaciones', 'N + 1 ecuaciones', 'N / 2 ecuaciones'],
        'La ecuación del último nodo N es una combinación lineal redundante de las anteriores por conservación global.', 'Ecuaciones de nodo = N - 1.', 'intermediate', 1230
    ))
    q.append(make_mc(
        '¿Cuántas ecuaciones de malla independientes existen en un circuito planar con B ramas y N nodos?',
        'M = B - N + 1', ['M = B - N', 'M = B + N', 'M = 2B - N'],
        'Fórmula topológica de redes eléctricas (relacionada con la característica de Euler): Mallas = Ramas - Nodos + 1.', 'M = B - N + 1.', 'advanced', 1280
    ))
    q.append(make_mc(
        'En una rama con una batería E = 10 V y una resistencia R = 5 Ω, los extremos A y B tienen potenciales VA = 25 V y VB = 10 V (recorrido A → B). Si la corriente va de A a B con I = 1 A y la batería tiene el polo positivo hacia B:',
        'La ecuación de rama cumple: VA + E - I·R = VB', ['VA - E + I·R = VB', 'VA = VB', 'E = I·R'],
        'Partiendo de A: VA + E (si va de - a +) - I·R = VB.', 'VA + E - I·R = VB.', 'intermediate', 1240
    ))
    q.append(make_mc(
        'En un nodo convergen 5 ramas. Si entran 2 A, 4 A y 1 A, y por una cuarta rama salen 5 A, ¿qué ocurre en la quinta rama?',
        'Salen 2.0 A', ['Entran 2.0 A', 'Salen 7.0 A', 'No circula corriente'],
        'Entran = 2 + 4 + 1 = 7 A. Salen = 5 A. Para equilibrar deben salir 7 - 5 = 2 A.', '7 A entran = 5 A salen + I5 ⇒ I5 = 2 A saliendo.', 'basic', 1130
    ))
    q.append(make_mc(
        'Si una malla contiene dos resistencias de 4 Ω y 6 Ω en serie con una fuente de 30 V, ¿cuál es la caida de tensión en la resistencia de 6 Ω?',
        '18.0 V', ['12.0 V', '30.0 V', '6.0 V'],
        'Req = 4 + 6 = 10 Ω. I = 30 / 10 = 3.0 A. V6 = I * R = 3.0 A * 6 Ω = 18.0 V.', 'V = 3 * 6 = 18 V.', 'basic', 1120
    ))
    q.append(make_mc(
        'La Ley de Mallas de Kirchhoff NO es aplicable directamente si:',
        'Existe un flujo magnético variable en el tiempo que atraviesa el plano de la malla (Ley de Faraday: ∮ E·dl = -dΦB/dt ≠ 0)',
        ['Hay resistencias en paralelo', 'Hay fuentes de corriente continua', 'Las resistencias son de carbón'],
        'En régimen con inducción electromagnética el campo eléctrico no es conservativo y la suma de voltajes en un lazo cerrado no es cero.', 'Campos magnéticos variables violan LTK clásica.', 'advanced', 1290
    ))
    q.append(make_mc(
        'En un circuito de dos mallas con una rama central común que lleva corriente I3 = I1 + I2 a través de una resistencia R_c, el término de acoplamiento en la malla 1 es:',
        '- (I1 + I2) · R_c', ['- I1 · R_c únicamente', '+ I2 · R_c', '0'],
        'La caída de tensión en la resistencia compartida se debe a la superposición aditiva de ambas corrientes de rama.', 'Caída en rama común: -(I1+I2)Rc.', 'intermediate', 1230
    ))
    q.append(make_mc(
        'Al aplicar la ley de mallas a un lazo superconductor (R = 0 en toda la malla) que no encierra fuentes ni fem:',
        'La suma de caídas es idénticamente 0 = 0 (tensión cero en todo el lazo)', ['La corriente es nula obligatoriamente', 'El voltaje es infinito', 'El circuito se quema'],
        'En un anillo superconductor cerrado V = 0 en cualquier trayectoria cerrada.', 'ΣΔV = 0.', 'intermediate', 1210
    ))
    q.append(make_mc(
        'Un circuito multirrama se puede resolver analíticamente mediante:',
        'Un sistema de ecuaciones lineales simultáneas igual al número de corrientes de rama desconocidas',
        ['Una sola ecuación simple', 'Fórmulas de MRUV', 'La constante de Planck'],
        'Se combinan (N-1) ecuaciones de nodo y (B-N+1) ecuaciones de malla formando una matriz resoluble por Cramer o Gauss-Jordan.', 'Sistema lineal NxN.', 'basic', 1140
    ))
    q.append(make_mc(
        'En un circuito puente con ramas simétricas R y fuente V, si se conecta un voltímetro entre los dos nodos centrales:',
        'Indica exactamente 0.0 V (puente balanceado)', ['Indica V', 'Indica V/2', 'Indica infinito'],
        'Por simetría los potenciales en ambos nodos centrales son idénticos a V/2, resultando en diferencia de potencial nula.', 'Puente balanceado ⇒ ΔV = 0.', 'basic', 1130
    ))
    q.append(make_mc(
        'Si una rama contiene una fuente de corriente ideal de 3 A, la corriente que circula por esa rama:',
        'Es exactamente 3 A independientemente de los voltajes y resistencias del resto del circuito',
        ['Depende de la ley de Ohm local', 'Es cero', 'Varía con el tiempo'],
        'Una fuente de corriente ideal impone fijamente la corriente en su rama sin importar la tensión en sus terminales.', 'I_rama fija por la fuente.', 'intermediate', 1220
    ))
    q.append(make_mc(
        'Gustav Kirchhoff formuló estas dos leyes fundamentales en el año:',
        '1845 (mientras era estudiante universitario)', ['1945', '1700', '1687'],
        'Kirchhoff enunció sus leyes en 1845 como generalización de la ley de Ohm para circuitos complejos.', '1845.', 'basic', 1100
    ))
    q.append(make_mc(
        'En una red con 3 mallas independientes y 2 nodos, el número de ecuaciones linealmente independientes necesarias y suficientes para hallar las corrientes es:',
        '4 ecuaciones (1 de nodo y 3 de malla)', ['5 ecuaciones', '2 ecuaciones', '6 ecuaciones'],
        'Nodos: N - 1 = 2 - 1 = 1 ecuación. Mallas: 3 ecuaciones. Total = 1 + 3 = 4 ecuaciones.', '1 nodo + 3 mallas = 4.', 'advanced', 1270
    ))
    return q
