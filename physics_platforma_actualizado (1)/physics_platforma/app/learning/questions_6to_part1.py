# -*- coding: utf-8 -*-
from app.learning.question_helper import make_mc

def get_coulomb_questions():
    q = []
    q.append(make_mc(
        'Dos cargas puntuales de +1.0 C cada una están separadas 1.0 km en el vacío. ¿Cuál es el orden de magnitud de la fuerza de repulsión? (ke ≈ 9.0 × 10⁹ N·m²/C²).',
        '9000 N (≈ 9.0 × 10³ N)', ['9.0 × 10⁹ N', '9.0 × 10⁶ N', '9.0 N'],
        'F = ke * q1 * q2 / r² = 9.0x10⁹ * (1 * 1) / (1000)² = 9.0x10⁹ / 10⁶ = 9000 N.', 'F = 9x10⁹ / 10⁶ = 9000 N.', 'basic', 1130
    ))
    q.append(make_mc(
        'La permitividad dieléctrica del vacío ε0 tiene un valor de aproximadamente:',
        '8.854 × 10⁻¹² C² / (N · m²)', ['8.99 × 10⁹ N · m² / C²', '1.60 × 10⁻¹⁹ C', '6.67 × 10⁻¹¹ N · m² / kg²'],
        'Constante universal: ε0 ≈ 8.854 × 10⁻¹² F/m = C²/(N·m²). Se vincula con ke mediante ke = 1 / (4πε0).', 'ε0 ≈ 8.85x10⁻¹² C²/(N·m²).', 'basic', 1110
    ))
    q.append(make_mc(
        'Si dos cargas puntuales sumergidas en agua destilada (constante dieléctrica relativa κ = 80) mantienen su separación, la fuerza electrostática entre ellas:',
        'Se reduce 80 veces respecto al vacío (F_agua = F_vacío / 80)', ['Se multiplica por 80', 'Permanece idéntica', 'Se hace nula'],
        'En un medio material dieléctrico la permitividad efectiva es ε = κ · ε0, por lo que F = F0 / κ.', 'F_medio = F_vacío / κ = F / 80.', 'intermediate', 1210
    ))
    q.append(make_mc(
        'Tres cargas puntuales q1 = +2 μC, q2 = -4 μC y q3 = +1 μC forman un sistema aislado. Tras interactuar y tocarse, ¿cuál es la carga neta total final?',
        '-1.0 μC', ['+7.0 μC', '+3.0 μC', '0 μC'],
        'Por el Principio de Conservación de la Carga: q_total = q1 + q2 + q3 = +2 - 4 + 1 = -1.0 μC.', 'Σq = 2 - 4 + 1 = -1 μC.', 'basic', 1100
    ))
    q.append(make_mc(
        '¿Puede un cuerpo macroscópico poseer una carga neta de 2.5 × 10⁻¹⁹ C en reposo?',
        'No, porque toda carga real debe ser un múltiplo entero estricto de la carga elemental e = 1.6 × 10⁻¹⁹ C',
        ['Sí, cualquier valor continuo es válido', 'Solo si es positivo', 'Solo a temperaturas bajo cero'],
        'Cuantización: q = n · e. 2.5x10⁻¹⁹ / 1.6x10⁻¹⁹ = 1.5625 (no es un entero n). Es físicamente imposible.', 'No es múltiplo entero de e.', 'intermediate', 1200
    ))
    q.append(make_mc(
        'Dos cargas puntuales q y 4q están separadas una distancia L. ¿En qué punto sobre la línea que las une se debe colocar una tercera carga Q para que quede en equilibrio?',
        'A una distancia L/3 de la carga q (entre ambas cargas)', ['En el punto medio L/2', 'A L/4 de la carga q', 'Fuera de la recta'],
        'F1 = F2 ⇒ ke * q * Q / x² = ke * (4q) * Q / (L - x)² ⇒ 1/x² = 4/(L - x)² ⇒ 1/x = 2/(L - x) ⇒ L - x = 2x ⇒ 3x = L ⇒ x = L/3.', 'x = L / (1 + √4) = L / 3.', 'advanced', 1280
    ))
    q.append(make_mc(
        'Si la distancia entre dos cargas se reduce a la tercera parte (r / 3), la fuerza de repulsión mutua:',
        'Se multiplica por 9 (9 · F)', ['Se multiplica por 3', 'Se reduce a un tercio', 'Se multiplica por 6'],
        'F ∝ 1/r². Al dividir la distancia entre 3: F_nueva = F / (1/3)² = 9 F.', 'F ∝ 1/(1/3)² = 9.', 'basic', 1110
    ))
    q.append(make_mc(
        'La fuerza de Coulomb entre un electrón y un protón en el átomo de hidrógeno supera a la fuerza gravitatoria entre ellos en un factor aproximado de:',
        '10³⁹ veces a favor de la fuerza electrostática', ['10² veces', 'Son exactamente iguales', '10⁻¹¹ veces'],
        'La fuerza eléctrica es inmensamente más potente que la gravedad a escala atómica: Fe / Fg ≈ 2.3 × 10³⁹.', 'Fe / Fg ≈ 10³⁹.', 'intermediate', 1190
    ))
    q.append(make_mc(
        'Una carga puntual q = -3.0 μC experimenta una fuerza electrostática de 0.60 N hacia el este. ¿Cuál es el vector campo eléctrico en esa posición?',
        '2.0 × 10⁵ N/C hacia el oeste', ['2.0 × 10⁵ N/C hacia el este', '1.8 × 10⁶ N/C', '0.2 N/C'],
        'E = F / q. Como q es negativa, el vector campo E apunta en sentido rigurosamente opuesto al vector fuerza: E = 0.60 / 3.0x10⁻⁶ = 2.0x10⁵ N/C hacia el oeste.', 'q < 0 ⇒ E tiene sentido opuesto a F.', 'intermediate', 1230
    ))
    q.append(make_mc(
        'Dos esferas metálicas idénticas con cargas +6 μC y -2 μC se ponen en contacto y luego se separan. ¿Qué carga adquiere cada una?',
        '+2.0 μC cada una', ['+4.0 μC cada una', '-2.0 μC cada una', '0 μC'],
        'Carga neta = +6 + (-2) = +4 μC. Al ser esferas idénticas, se reparten la carga por simetría geométrica en partes iguales: q_final = +4 / 2 = +2.0 μC.', 'q = (+6 - 2)/2 = +2 μC.', 'basic', 1140
    ))
    q.append(make_mc(
        'En un triángulo equilátero de lado L se colocan tres cargas positivas idénticas +q en los vértices. La fuerza electrostática neta en el baricentro del triángulo es:',
        '0 N (nula por simetría vectorial)', ['3 ke q² / L²', 'ke q² / L²', '√3 ke q² / L²'],
        'Los tres vectores fuerza tienen idéntico módulo y están desfasados 120° entre sí en el plano. Su resultante vectorial es exactamente cero.', 'ΣF = 0 por simetría 120°.', 'intermediate', 1220
    ))
    q.append(make_mc(
        'La Ley de Coulomb es válida rigurosamente cuando:',
        'Las cargas están en reposo electrostático relativo y sus dimensiones espaciales son despreciables frente a la distancia de separación (cargas puntuales)',
        ['Las cargas se mueven a velocidades cercanas a la de la luz', 'En cualquier conductor sin importar la forma', 'Solo para electrones libres'],
        'Para cargas en movimiento actúan fuerzas magnéticas de Lorentz y campos retardados (ecuaciones de Maxwell).', 'Cargas puntuales en reposo.', 'basic', 1130
    ))
    q.append(make_mc(
        'Si se duplica el valor de ambas cargas (q1 y q2) y se duplica también la distancia r entre ellas, la fuerza electrostática:',
        'Permanece inalterada (igual a F)', ['Se duplica', 'Se cuadruplica', 'Se reduce a la mitad'],
        'F_nueva = ke * (2 q1 * 2 q2) / (2 r)² = ke * 4(q1 q2) / (4 r²) = ke * q1 q2 / r² = F.', '4 / 4 = 1 ⇒ F constante.', 'intermediate', 1180
    ))
    q.append(make_mc(
        'Dos cargas q1 = +8 μC y q2 = -8 μC separadas 0.1 m constituyen:',
        'Un dipolo eléctrico de momento p = q · d = 8.0 × 10⁻⁷ C · m', ['Un monopolo magnético', 'Una carga neta de 16 μC', 'Un condensador plano'],
        'Un par de cargas de igual magnitud y signo opuesto separadas por distancia d forma un dipolo eléctrico p = q · d.', 'Dipolo eléctrico.', 'basic', 1130
    ))
    q.append(make_mc(
        'Al frotar una varilla de vidrio con seda, el vidrio adquiere carga positiva debido a que:',
        'Transfiere electrones hacia la seda', ['Absorbe protones de la seda', 'Crea cargas positivas de la nada', 'Pierde neutrones'],
        'Los únicos portadores móviles transferibles en sólidos son los electrones periféricos. Perder electrones deja exceso de protones (+).', 'Pérdida de electrones.', 'basic', 1100
    ))
    q.append(make_mc(
        'La fuerza electrostática es una fuerza de acción a distancia que cumple la Tercera Ley de Newton en la forma:',
        'F_12 = - F_21 (misma magnitud, colineales y sentidos opuestos)', ['F_12 = F_21 en el mismo sentido', 'F_12 > F_21 si q1 > q2', 'F_12 no depende de q2'],
        'La fuerza que ejerce q1 sobre q2 es siempre igual en módulo y opuesta a la que q2 ejerce sobre q1, sin importar cuál carga sea mayor.', 'Tercera Ley: F12 = - F21.', 'basic', 1110
    ))
    q.append(make_mc(
        'En el sistema CGS electromagnético histórico, la unidad de carga electrostática (StatCoulomb o Fr) se definía de modo que la constante ke fuera igual a:',
        '1 (adimensional pura)', ['9 × 10⁹', '4π', '10⁻⁷'],
        'En el sistema cegesimal Gaussiano la ley de Coulomb se escribía simplemente F = q1 q2 / r² con ke = 1.', 'ke = 1 en CGS.', 'advanced', 1280
    ))
    q.append(make_mc(
        'Una carga puntual q = 10 μC en el vacío dista r = 0.05 m de otra idéntica. ¿Cuál es la fuerza?',
        '360 N', ['36 N', '180 N', '720 N'],
        'F = 9.0x10⁹ * (10x10⁻⁶)² / (0.05)² = 9.0x10⁹ * 10⁻¹⁰ / 0.0025 = 0.9 / 0.0025 = 360 N.', 'F = 0.9 / 0.0025 = 360 N.', 'intermediate', 1210
    ))
    q.append(make_mc(
        'La fuerza de Coulomb es una fuerza central porque:',
        'Su línea de acción pasa siempre por la recta que une los centros de ambas cargas puntuales',
        ['Actúa en el centro del átomo', 'Depende de la masa de las cargas', 'Tiene simetría cilíndrica'],
        'Fuerza central: F(r) = f(r) · r̂, dirigida hacia o desde el centro del origen de coordenadas.', 'Fuerza colineal central.', 'intermediate', 1190
    ))
    q.append(make_mc(
        'Si un conductor esférico cargado se encuentra en equilibrio electrostático, la carga neta reside:',
        'Exclusivamente en su superficie exterior', ['En el centro geométrico', 'Uniformemente en todo el volumen interior', 'En el aire cercano'],
        'Por repulsión de Coulomb mutua, las cargas libres se alejan lo máximo posible ubicándose en la superficie externa (campo interior E = 0).', 'Superficie exterior.', 'basic', 1140
    ))
    return q
