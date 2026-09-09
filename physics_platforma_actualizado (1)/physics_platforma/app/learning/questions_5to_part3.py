# -*- coding: utf-8 -*-
from app.learning.question_helper import make_mc

def get_momento_lineal_questions():
    q = []
    q.append(make_mc(
        'Un camión de 4000 kg se mueve a 15 m/s. ¿Cuál es la magnitud de su cantidad de movimiento?',
        '60000 kg · m/s', ['266.7 kg · m/s', '450000 kg · m/s', '30000 kg · m/s'],
        'p = m * v = 4000 kg * 15 m/s = 60000 kg·m/s.', 'p = 4000 * 15 = 60000 kg·m/s.', 'basic', 1100
    ))
    q.append(make_mc(
        'Una pelota de tenis de 0.06 kg llega a 30 m/s y es golpeada por la raqueta saliendo en sentido opuesto a 40 m/s. ¿Cuál es la magnitud del impulso recibido?',
        '4.2 N · s', ['0.6 N · s', '2.4 N · s', '1.8 N · s'],
        'Considerando signos: v0 = +30 m/s, vf = -40 m/s. Δp = m * (vf - v0) = 0.06 * (-40 - 30) = 0.06 * (-70) = -4.2 N·s. Módulo = 4.2 N·s.',
        'I = |m * (vf - v0)| = 0.06 * |-40 - 30| = 4.2 N·s.', 'intermediate', 1220
    ))
    q.append(make_mc(
        'Si el impacto de la pelota anterior con la raqueta duró 0.007 s, ¿cuál fue la fuerza media ejercida por la raqueta?',
        '600 N', ['420 N', '120 N', '300 N'],
        'F_media = I / Δt = 4.2 N·s / 0.007 s = 600 N.', 'F = 4.2 / 0.007 = 600 N.', 'intermediate', 1230
    ))
    q.append(make_mc(
        'En cualquier choque aislado (ΣF_ext = 0), la magnitud que se conserva SIEMPRE independientemente de si es elástico o inelástico es:',
        'La cantidad de movimiento lineal total', ['La energía cinética total', 'La velocidad de cada cuerpo', 'La temperatura'],
        'La cantidad de movimiento total se conserva en todo choque aislado por la 3.ª Ley de Newton. La energía cinética solo se conserva si es elástico.',
        'Conservación de p es universal para sistemas aislados; conservación de Ek solo en colisiones puramente elásticas.', 'basic', 1120
    ))
    q.append(make_mc(
        'En un choque perfectamente plástico (totalmente inelástico), los dos cuerpos tras colisionar:',
        'Quedan unidos y continúan moviéndose con la misma velocidad común', ['Rebotan con la misma rapidez que traían', 'Se detienen por completo siempre', 'Salen despedidos a 90°'],
        'Por definición de choque plástico (e = 0), los cuerpos coalescen en una sola masa combinada.',
        'e = 0 ⇒ vf1 = vf2 = vf_común.', 'basic', 1110
    ))
    q.append(make_mc(
        'Un patinador de 60 kg en reposo lanza una pelota de 2.0 kg a 15 m/s hacia adelante. ¿Con qué rapidez retrocede el patinador?',
        '0.50 m/s', ['15.0 m/s', '30.0 m/s', '1.0 m/s'],
        'P_inicial = 0. P_final = m_pat * v_pat + m_pel * v_pel = 0 ⇒ 60 * v_pat + 2.0 * 15 = 0 ⇒ v_pat = -30 / 60 = -0.50 m/s.',
        '0 = 60 * v + 30 ⇒ v = -0.5 m/s (retroceso).', 'intermediate', 1210
    ))
    q.append(make_mc(
        'Un cuerpo de 3 kg a 4 m/s choca elásticamente de frente contra otro de 3 kg idéntico en reposo. ¿Cuáles son las velocidades tras el choque?',
        'El primero se detiene (v1f = 0) y el segundo sale a 4 m/s (v2f = 4 m/s)', ['Ambos se mueven a 2 m/s juntos', 'Ambos rebotan a 2 m/s en sentidos opuestos', 'El primero rebota a 4 m/s'],
        'En choques elásticos frontales entre masas idénticas, los cuerpos intercambian completamente sus velocidades.',
        'm1 = m2 en choque elástico 1D: v1f = v2i = 0; v2f = v1i = 4 m/s.', 'intermediate', 1230
    ))
    q.append(make_mc(
        'Dos carritos m1 = 1 kg y m2 = 2 kg chocan plásticamente de frente a 6 m/s y 3 m/s en sentidos opuestos. ¿Cuál es su velocidad final?',
        '0 m/s (se detienen por completo)', ['1.0 m/s hacia la derecha', '3.0 m/s', '4.5 m/s'],
        'p_inicial = m1*v1 + m2*v2 = 1*(+6) + 2*(-3) = 6 - 6 = 0. Como p_inicial = 0, tras el choque plástico el conjunto queda en reposo.',
        'p_tot = 1(6) - 2(3) = 0 ⇒ (1+2)*vf = 0 ⇒ vf = 0 m/s.', 'advanced', 1260
    ))
    q.append(make_mc(
        'El principio de propulsión a chorro de los cohetes espaciales en el vacío se fundamenta en:',
        'La conservación de la cantidad de movimiento (expulsión de gases a alta velocidad hacia atrás)', ['El empuje del aire contra el cohete', 'La gravedad cero', 'La energía solar'],
        'Al expulsar masa de gases hacia atrás a altísima velocidad, el cohete recibe un impulso hacia adelante igual y opuesto en el vacío.',
        'dp_cohete/dt = - dp_gases/dt (Tercera Ley y conservación del momento lineal).', 'basic', 1130
    ))
    q.append(make_mc(
        '¿Cuál es la unidad del impulso en el Sistema Internacional?',
        'N · s (equivalente a kg · m / s)', ['N / s', 'J · s', 'kg · m² / s'],
        'Impulso = Fuerza * Tiempo ⇒ [I] = N · s = (kg·m/s²) * s = kg · m/s.', '1 N·s = 1 kg·m/s.', 'basic', 1100
    ))
    q.append(make_mc(
        'Un proyectil de 10 g viaja a 400 m/s. ¿Qué impulso se necesita para frenarlo por completo?',
        '4.0 N · s', ['4000 N · s', '40 N · s', '0.04 N · s'],
        'm = 0.01 kg, v = 400 m/s. I = Δp = m * (0 - 400) = - 4.0 N·s. Módulo = 4.0 N·s.',
        'I = 0.01 kg * 400 m/s = 4.0 N·s.', 'basic', 1120
    ))
    q.append(make_mc(
        'En un gráfico de Fuerza versus tiempo (F vs. t), ¿qué magnitud representa el área bajo la curva?',
        'El impulso total de la fuerza', ['El trabajo mecánico', 'La aceleración media', 'La potencia'],
        'Por definición matemática: I = ∫ F(t) dt = Área bajo la curva F vs t.', 'Área = ∫ F dt = Impulso.', 'basic', 1130
    ))
    q.append(make_mc(
        'Un airbag reduce las lesiones en un choque automovilístico principalmente porque:',
        'Aumenta el tiempo del impacto (Δt), reduciendo notablemente la fuerza media recibida para un mismo cambio de momento Δp',
        ['Reduce el cambio de cantidad de movimiento del pasajero', 'Elimina la inercia del cuerpo', 'Aumenta la energía cinética'],
        'Como I = Δp = F_media * Δt, al aumentar el tiempo de desaceleración Δt la fuerza media de impacto disminuye drásticamente.',
        'Δp constante: mayor Δt implica menor F_media.', 'intermediate', 1190
    ))
    q.append(make_mc(
        'Un bloque de 4 kg se mueve a 2 m/s. Si se le aplica una fuerza neta de 8 N durante 3 s en su misma dirección, ¿cuál es su velocidad final?',
        '8.0 m/s', ['6.0 m/s', '10.0 m/s', '4.0 m/s'],
        'Impulso = F * Δt = 8 * 3 = 24 N·s. Δp = m * (vf - v0) ⇒ 24 = 4 * (vf - 2) ⇒ 6 = vf - 2 ⇒ vf = 8.0 m/s.',
        'vf = v0 + (F*t)/m = 2 + (8*3)/4 = 2 + 6 = 8.0 m/s.', 'intermediate', 1210
    ))
    q.append(make_mc(
        'Una bola de billar blanca choca elásticamente a 5 m/s contra otra idéntica en reposo de forma oblicua. Si la blanca se desvía a 30° con v1 = 4.33 m/s, ¿qué ángulo forman las direcciones de salida de ambas bolas?',
        '90°', ['60°', '45°', '180°'],
        'En colisiones elásticas bidimensionales entre masas idénticas donde una está en reposo, el ángulo entre las direcciones finales es siempre 90°.',
        'Propiedad geométrica del choque elástico m1 = m2: v1f · v2f = 0 ⇒ ángulo = 90°.', 'advanced', 1290
    ))
    q.append(make_mc(
        'Un cuerpo de 5 kg se desplaza a 10 m/s hacia el norte. ¿Cuál es su cantidad de movimiento?',
        '50 kg · m/s hacia el norte', ['50 J hacia el norte', '250 kg · m/s', '2 kg · m/s hacia el norte'],
        'p = m * v = 5 * 10 = 50 kg·m/s con la misma dirección y sentido que el vector velocidad.', 'p = 50 kg·m/s norte.', 'basic', 1100
    ))
    q.append(make_mc(
        'El coeficiente de restitución e entre dos esferas que chocan se define como:',
        'El cociente entre la rapidez relativa de alejamiento y la de acercamiento: e = |v2f - v1f| / |v1i - v2i|',
        ['El cociente de las energías cinéticas', 'La masa mayor sobre la menor', 'El tiempo de contacto'],
        'e = (v2f - v1f) / (v1i - v2i). Para choques elásticos e = 1, para plásticos e = 0.', 'intermediate', 1210
    ))
    q.append(make_mc(
        'Un cazador de 80 kg dispara una bala de 0.04 kg a 600 m/s. ¿Cuál es la velocidad de retroceso del cazador si está sobre hielo sin fricción?',
        '0.30 m/s', ['3.0 m/s', '0.03 m/s', '24.0 m/s'],
        '0 = 80 * v_cazador + 0.04 * 600 ⇒ 80 * v = -24 ⇒ v = -0.30 m/s.', 'v = (0.04 * 600) / 80 = 0.30 m/s.', 'intermediate', 1220
    ))
    q.append(make_mc(
        'Dos objetos de masas m y 2m tienen la misma energía cinética. ¿Cuál tiene mayor cantidad de movimiento?',
        'El objeto de masa 2m', ['El objeto de masa m', 'Tienen la misma cantidad de movimiento', 'Falta conocer las velocidades'],
        'Relación p y Ek: Ek = p² / (2m) ⇒ p = √(2 m Ek). A igual Ek, el de mayor masa tiene mayor cantidad de movimiento.',
        'p = √(2*m*Ek). Mayor m ⇒ mayor p.', 'advanced', 1270
    ))
    q.append(make_mc(
        'Un pez de 4 kg nada a 2 m/s y se traga a un pez pequeño de 1 kg en reposo. ¿A qué velocidad sigue nadando el pez grande tras la comida?',
        '1.6 m/s', ['1.0 m/s', '2.0 m/s', '0.5 m/s'],
        'Choque plástico: 4 * 2 + 1 * 0 = (4 + 1) * vf ⇒ 8 = 5 * vf ⇒ vf = 1.6 m/s.', 'vf = 8 / 5 = 1.6 m/s.', 'intermediate', 1200
    ))
    return q
