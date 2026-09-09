# -*- coding: utf-8 -*-
from app.learning.question_helper import make_mc

def get_ondas_questions():
    q = []
    q.append(make_mc(
        'Una emisora de radio emite a una frecuencia f = 100 MHz (100 × 10⁶ Hz). Si las ondas viajan a la velocidad de la luz (c = 3.0 × 10⁸ m/s), ¿cuál es su longitud de onda λ?',
        '3.0 m', ['30.0 m', '0.30 m', '300.0 m'],
        'c = λ * f ⇒ λ = c / f = (3.0 × 10⁸ m/s) / (100 × 10⁶ Hz) = 3.0 m.', 'λ = 3.0x10⁸ / 10⁸ = 3.0 m.', 'basic', 1100
    ))
    q.append(make_mc(
        'El oído humano promedio percibe frecuencias sonoras en el rango de:',
        '20 Hz a 20000 Hz (20 kHz)', ['1 Hz a 100 Hz', '20 kHz a 200 kHz', '0 Hz a 5000 Hz'],
        'Rango audible estándar: por debajo de 20 Hz es infrasonido, por encima de 20 kHz es ultrasonido.', '20 Hz a 20 kHz.', 'basic', 1100
    ))
    q.append(make_mc(
        'Cuando una onda pasa de un medio a otro y se refracta, la magnitud que permanece estrictamente constante e invariable es:',
        'La frecuencia (f)', ['La longitud de onda (λ)', 'La velocidad de propagación (v)', 'La dirección'],
        'La frecuencia está fijada por la fuente emisora original y no depende de las propiedades elásticas del medio que atraviesa.', 'f = constante en refracción.', 'intermediate', 1190
    ))
    q.append(make_mc(
        'Una cuerda de guitarra vibra en su modo fundamental con dos nodos en los extremos y un antinodo en el centro. Si la cuerda mide L = 0.65 m, ¿cuánto vale la longitud de onda λ?',
        '1.30 m', ['0.65 m', '0.325 m', '2.60 m'],
        'En el modo fundamental: L = λ / 2 ⇒ λ = 2 * L = 2 * 0.65 m = 1.30 m.', 'λ = 2 * L = 1.30 m.', 'intermediate', 1210
    ))
    q.append(make_mc(
        'El tono o altura de una nota musical (aguda vs. grave) está determinado físicamente por:',
        'La frecuencia de la onda sonora', ['La amplitud de la onda', 'La velocidad del sonido en el aire', 'La duración'],
        'Mayor frecuencia produce sonidos más agudos; menor frecuencia produce sonidos más graves.', 'Tono ∝ frecuencia.', 'basic', 1110
    ))
    q.append(make_mc(
        'El timbre de un instrumento musical nos permite distinguir un violín de un piano tocando la misma nota con igual volumen gracias a:',
        'La cantidad y proporción de armónicos superiores que componen la forma de la onda sonora compleja',
        ['La diferente velocidad del sonido de cada instrumento', 'La frecuencia fundamental distinta', 'La longitud de la onda fundamental'],
        'El timbre depende del espectro armónico característico de cada caja de resonancia.', 'Timbre = composición de armónicos.', 'intermediate', 1180
    ))
    q.append(make_mc(
        'Una ambulancia con sirena de f0 = 700 Hz se acerca a un peatón en reposo a 34 m/s (v_sonido = 340 m/s). ¿Qué frecuencia percibe el peatón?',
        '777.8 Hz (tono más agudo)', ['630.0 Hz', '700.0 Hz', '840.0 Hz'],
        'Efecto Doppler con fuente acercándose: f = f0 * [v / (v - vf)] = 700 * [340 / (340 - 34)] = 700 * (340 / 306) ≈ 777.8 Hz.', 'f = 700 * (340 / 306) ≈ 777.8 Hz.', 'intermediate', 1240
    ))
    q.append(make_mc(
        'Si la ambulancia anterior ahora se aleja del peatón a 34 m/s, ¿qué frecuencia percibe el peatón?',
        '636.4 Hz (tono más grave)', ['777.8 Hz', '700.0 Hz', '595.0 Hz'],
        'Efecto Doppler con fuente alejándose: f = f0 * [v / (v + vf)] = 700 * [340 / (340 + 34)] = 700 * (340 / 374) ≈ 636.4 Hz.', 'f = 700 * (340 / 374) ≈ 636.4 Hz.', 'intermediate', 1240
    ))
    q.append(make_mc(
        'La propiedad de una onda de bordear la esquina de un edificio o propagarse a través de una rendija pequeña se denomina:',
        'Difracción', ['Reflexión', 'Refracción', 'Dispersión'],
        'La difracción es el fenómeno ondulatorio por el cual una onda rodea obstáculos de dimensiones comparables a λ.', 'Difracción.', 'basic', 1120
    ))
    q.append(make_mc(
        'El fenómeno de pulsaciones o batidos acústicos se produce cuando:',
        'Se superponen dos ondas sonoras de frecuencias muy cercanas pero ligeramente distintas (f1 ≈ f2)',
        ['Dos sonidos tienen intensidades opuestas', 'El sonido rebota en una cueva', 'La fuente se mueve a la velocidad del sonido'],
        'La interferencia constructiva y destructiva periódica produce una fluctuación de volumen con frecuencia de batido: f_bat = |f1 - f2|.', 'f_batido = |f1 - f2|.', 'intermediate', 1220
    ))
    q.append(make_mc(
        'La velocidad del sonido en el aire a temperatura ambiente (20 °C) es aproximadamente:',
        '343 m/s', ['3.0 × 10⁸ m/s', '1500 m/s', '100 m/s'],
        'v ≈ 331.4 + 0.6 · T(°C) ⇒ a 20 °C es ≈ 343.4 m/s.', 'v ≈ 343 m/s.', 'basic', 1100
    ))
    q.append(make_mc(
        'El sonido NO puede propagarse a través de:',
        'El vacío del espacio exterior', ['El agua líquida', 'El acero sólido', 'El aire caliente'],
        'El sonido es una onda mecánica longitudinal y requiere obligatoriamente un medio material elástico para transmitir sus oscilaciones de presión.', 'Requiere medio material ⇒ no viaja en el vacío.', 'basic', 1100
    ))
    q.append(make_mc(
        'En las ondas transversales, las partículas del medio oscilan:',
        'Perpendicularmente a la dirección de propagación de la onda', ['En la misma dirección de propagación', 'En círculos cerrados únicamente', 'En reposo'],
        'Onda transversal: oscilación ⊥ propagación (ej. cuerda, luz). Onda longitudinal: oscilación colineal a la propagación (ej. sonido).', 'Oscilación ⊥ propagación.', 'basic', 1110
    ))
    q.append(make_mc(
        'Un eco se percibe claramente como un sonido separado del original si la superficie reflectora está a una distancia mínima de aproximadamente:',
        '17 metros', ['1 metro', '100 metros', '340 metros'],
        'El oído humano distingue dos sonidos separados si llegan con un retardo mínimo de 0.1 s. Distancia ida y vuelta = v * t = 340 * 0.1 = 34 m ⇒ distancia al obstáculo d = 17 m.', 'd = (340 * 0.1) / 2 = 17 m.', 'intermediate', 1210
    ))
    q.append(make_mc(
        'La intensidad sonora se mide comúnmente en una escala logarítmica de decibelios (dB). Un incremento de 20 dB en el nivel sonoro corresponde a:',
        'Multiplicar la intensidad física de la onda (W/m²) por 100', ['Multiplicar la intensidad por 20', 'Duplicar la intensidad', 'Multiplicar la intensidad por 10'],
        'Nivel β = 10 * log10(I / I0). Si Δβ = 20 dB ⇒ 2 = log10(I / I0) ⇒ I = 10² * I0 = 100 I0.', '20 dB = factor 10² = 100.', 'intermediate', 1250
    ))
    q.append(make_mc(
        'Una onda en el agua tiene λ = 0.50 m y se propaga a v = 2.0 m/s. ¿Cuál es su período T?',
        '0.25 s', ['1.0 s', '4.0 s', '0.50 s'],
        'v = λ / T ⇒ T = λ / v = 0.50 m / 2.0 m/s = 0.25 s.', 'T = 0.5 / 2 = 0.25 s.', 'basic', 1120
    ))
    q.append(make_mc(
        'Dos ondas idénticas con igual amplitud A interfieren en un punto exactamente en contrafase (desfasadas 180° o π rad). La amplitud resultante es:',
        '0 (interferencia destructiva total)', ['2A', 'A', 'A/2'],
        'Al encontrarse una cresta con un valle idéntico, las elongaciones instantáneas se cancelan punto a punto.', 'A_neta = A - A = 0.', 'basic', 1130
    ))
    q.append(make_mc(
        'En un tubo sonoro cerrado por un extremo de longitud L, solo pueden formarse ondas estacionarias con armónicos:',
        'Impares (1.º, 3.º, 5.º...) con λ_n = 4L / n (n = 1, 3, 5...)', ['Pares únicamente', 'Todos los números naturales', 'Ninguno'],
        'El extremo cerrado exige un nodo de desplazamiento y el abierto un antinodo, forzando longitudes de onda de cuartos impares: L = n λ / 4.', 'Armónicos impares: n = 1, 3, 5...', 'advanced', 1280
    ))
    q.append(make_mc(
        'El ultrasonido utilizado en ecografías médicas emplea ondas sonoras con frecuencias:',
        'Superiores a 20000 Hz (típicamente entre 2 MHz y 15 MHz)', ['Inferiores a 20 Hz', 'Entre 500 Hz y 2000 Hz', 'Ondas electromagnéticas de radio'],
        'Las altísimas frecuencias brindan longitudes de onda milimétricas ideales para resolución anatómica sin radiación ionizante.', 'f > 20 kHz (MHz).', 'basic', 1120
    ))
    q.append(make_mc(
        'La refracción de las ondas sonoras en la atmósfera entre capas de aire frío y caliente explica por qué:',
        'El sonido se escucha con mayor claridad y alcance a larga distancia durante las noches despejadas',
        ['El sonido no viaja de noche', 'El eco solo ocurre de día', 'El sonido cambia de frecuencia'],
        'La temperatura altera la velocidad del sonido en el aire, curvando los frentes de onda hacia la superficie terrestre por refracción térmica.', 'Curvatura por refracción térmica.', 'intermediate', 1230
    ))
    return q

def get_electricidad_5to_questions():
    q = []
    q.append(make_mc(
        'Dos cargas puntuales q1 = +2.0 μC y q2 = +3.0 μC están separadas d = 0.20 m en el vacío (ke = 9.0 × 10⁹ N·m²/C²). ¿Cuál es la fuerza entre ellas?',
        '1.35 N de repulsión', ['1.35 N de atracción', '13.5 N de repulsión', '0.27 N'],
        'F = 9.0x10⁹ * (2.0x10⁻⁶ * 3.0x10⁻⁶) / (0.20)² = 54x10⁻³ / 0.04 = 1.35 N. Al ser ambas positivas se repelen.', 'F = 9x10⁹ * 6x10⁻¹² / 0.04 = 1.35 N.', 'basic', 1120
    ))
    q.append(make_mc(
        'Un circuito tiene una batería de 12 V conectada a una resistencia de 24 Ω. ¿Qué corriente circula?',
        '0.50 A', ['2.0 A', '288 A', '12 A'],
        'Ley de Ohm: I = V / R = 12 V / 24 Ω = 0.50 A.', 'I = 12 / 24 = 0.5 A.', 'basic', 1100
    ))
    q.append(make_mc(
        '¿Cuánta energía consume una lámpara de 60 W encendida durante 2 horas?',
        '432000 J (120 Wh = 0.12 kWh)', ['120 J', '7200 J', '60 J'],
        't = 2 h * 3600 s/h = 7200 s. E = P * t = 60 W * 7200 s = 432000 J.', 'E = 60 * 7200 = 432 kJ.', 'basic', 1120
    ))
    q.append(make_mc(
        'Tres resistores de 10 Ω, 20 Ω y 30 Ω se conectan en serie. ¿Cuál es la resistencia equivalente?',
        '60 Ω', ['5.45 Ω', '30 Ω', '15 Ω'],
        'En serie las resistencias se suman directamente: Req = 10 + 20 + 30 = 60 Ω.', 'Req = 10 + 20 + 30 = 60 Ω.', 'basic', 1100
    ))
    q.append(make_mc(
        'Dos resistores de 20 Ω y 20 Ω se conectan en paralelo. ¿Cuál es la resistencia equivalente?',
        '10 Ω', ['40 Ω', '20 Ω', '5 Ω'],
        'En paralelo: Req = (R1 * R2) / (R1 + R2) = (20 * 20) / (20 + 20) = 400 / 40 = 10 Ω.', 'Req = 20 / 2 = 10 Ω.', 'basic', 1110
    ))
    q.append(make_mc(
        'Si por un cable conductor pasa una carga neta de 120 C durante 1 minuto, ¿cuál es la intensidad de corriente?',
        '2.0 A', ['120 A', '0.5 A', '60 A'],
        't = 60 s. I = q / t = 120 C / 60 s = 2.0 A.', 'I = 120 / 60 = 2.0 A.', 'basic', 1110
    ))
    q.append(make_mc(
        'El campo eléctrico creado por una carga puntual Q = +5.0 nC a una distancia r = 0.30 m en el vacío es:',
        '500 N/C radialmente hacia afuera', ['500 N/C hacia la carga', '150 N/C', '1500 N/C'],
        'E = ke * Q / r² = 9.0x10⁹ * 5.0x10⁻⁹ / (0.30)² = 45 / 0.09 = 500 N/C. Al ser positiva, es divergente hacia afuera.', 'E = 45 / 0.09 = 500 N/C.', 'intermediate', 1190
    ))
    q.append(make_mc(
        'La diferencia de potencial eléctrico entre dos puntos A y B mide:',
        'El trabajo que realiza el campo por unidad de carga positiva al trasladarla de A hacia B',
        ['La fuerza total del circuito', 'La corriente máxima que puede circular', 'La potencia de la batería'],
        'ΔV = W / q0 [Voltio = Joule / Coulomb].', 'V = W / q.', 'basic', 1120
    ))
    q.append(make_mc(
        'Una estufa eléctrica de 220 V disipa una potencia de 1100 W. ¿Cuál es su resistencia interna y qué corriente absorbe?',
        'R = 44 Ω, I = 5.0 A', ['R = 22 Ω, I = 10.0 A', 'R = 5 Ω, I = 44 A', 'R = 100 Ω, I = 2.2 A'],
        'I = P / V = 1100 / 220 = 5.0 A. R = V / I = 220 / 5.0 = 44 Ω.', 'I = 1100 / 220 = 5 A; R = 220 / 5 = 44 Ω.', 'intermediate', 1210
    ))
    q.append(make_mc(
        'Si se conecta un voltímetro ideal a un circuito, este debe colocarse en:',
        'Paralelo con el componente cuya tensión se desea medir (tiene resistencia interna infinita)',
        ['Serie abriendo la rama', 'En serie con la batería únicamente', 'En cualquier parte indistintamente'],
        'El voltímetro mide diferencia de potencial entre dos nodos y requiere muy alta resistencia para no desviar corriente.', 'Voltímetro en paralelo.', 'basic', 1110
    ))
    q.append(make_mc(
        'Si se conecta por error un amperímetro en paralelo con una fuente de 12 V:',
        'Se produce un cortocircuito que quema el fusible del instrumento debido a su resistencia casi nula',
        ['El instrumento mide 12 V normalmente', 'No pasa nada', 'El circuito funciona al doble de potencia'],
        'El amperímetro tiene resistencia interna prácticamente cero; en paralelo cortocircuita la fuente.', 'Cortocircuito.', 'intermediate', 1180
    ))
    q.append(make_mc(
        'Un alambre de cobre de resistividad ρ, longitud L y sección A tiene resistencia R. Si se duplica su longitud (2L) y se reduce su sección a la mitad (A/2), su nueva resistencia será:',
        '4 · R (se cuadruplica)', ['2 · R', 'R / 2', 'Permanecerá igual'],
        'Ley de Pouillet: R = ρ · L / A. R_nuevo = ρ · (2L) / (A/2) = 4 · (ρ · L / A) = 4R.', 'R_nuevo = 2 / 0.5 * R = 4R.', 'intermediate', 1220
    ))
    q.append(make_mc(
        'En una casa, todos los electrodomésticos y tomacorrientes están conectados entre sí en:',
        'Paralelo (para que todos reciban la misma tensión de 220 V independientemente de cuáles estén encendidos)',
        ['Serie', 'Mixto aleatorio', 'En bucle cerrado'],
        'En paralelo, cada aparato opera con la misma tensión nominal y si uno se apaga o desconecta, los demás siguen funcionando.', 'Instalación domiciliaria en paralelo.', 'basic', 1100
    ))
    q.append(make_mc(
        'Un protón (qp = +1.6 × 10⁻¹⁹ C) es acelerado por una diferencia de potencial de 1000 V. ¿Cuánta energía cinética gana?',
        '1000 eV (equivale a 1.6 × 10⁻¹⁶ J)', ['1.6 × 10⁻¹⁹ J', '1000 J', '1.6 J'],
        'ΔEk = q * ΔV = 1.6x10⁻¹⁹ C * 1000 V = 1.6x10⁻¹⁶ J = 1000 eV (electronvoltios).', 'Ek = q * V = 1.6x10⁻¹⁶ J = 1 keV.', 'intermediate', 1220
    ))
    q.append(make_mc(
        '¿Cuál es el valor de la carga neta de un cuerpo neutro al que se le extraen 5.0 × 10¹² electrones?',
        '+ 8.0 × 10⁻⁷ C (+ 0.80 μC)', ['- 8.0 × 10⁻⁷ C', '+ 5.0 × 10¹² C', '+ 1.6 × 10⁻¹⁹ C'],
        'Al perder electrones (negativos), el cuerpo queda con déficit y carga positiva: q = + n * e = 5.0x10¹² * 1.6x10⁻¹⁹ = + 8.0x10⁻⁷ C.', 'q = + 5x10¹² * 1.6x10⁻¹⁹ = +0.80 μC.', 'intermediate', 1210
    ))
    q.append(make_mc(
        'Si la distancia entre dos cargas puntuales se reduce a la mitad (d/2), la fuerza de Coulomb:',
        'Se cuadruplica (4 · F)', ['Se duplica', 'Se reduce a la mitad', 'Se reduce a la cuarta parte'],
        'F ∝ 1/d². Al reducir a d/2: F_nueva = 1 / (1/2)² = 4 F.', 'F ∝ 1 / (0.5)² = 4.', 'basic', 1120
    ))
    q.append(make_mc(
        'Un fusible eléctrico es un dispositivo de seguridad calibrado que protege la instalación mediante:',
        'La fusión de su filamento por Efecto Joule al superar la corriente límite prescrita, abriendo el circuito',
        ['La reducción del voltaje a la mitad', 'El desvío de la corriente a tierra', 'La disipación magnética'],
        'Al sobrepasar la corriente segura, I²R calienta el filamento calibrado hasta fundirlo e interrumpir la corriente.', 'Fusión por sobrecorriente Joule.', 'basic', 1110
    ))
    q.append(make_mc(
        'Entre dos placas paralelas separadas 0.02 m hay un campo eléctrico uniforme E = 5000 V/m. ¿Cuál es la diferencia de potencial entre ellas?',
        '100 V', ['250000 V', '250 V', '50 V'],
        'ΔV = E * d = 5000 V/m * 0.02 m = 100 V.', 'V = 5000 * 0.02 = 100 V.', 'basic', 1130
    ))
    q.append(make_mc(
        'Dos resistencias de 6 Ω y 12 Ω se conectan en paralelo a una fuente de 24 V. ¿Qué corriente circula por la resistencia de 6 Ω?',
        '4.0 A', ['2.0 A', '6.0 A', '0.5 A'],
        'En paralelo, la rama recibe los 24 V íntegros: I_6 = V / R = 24 V / 6 Ω = 4.0 A.', 'I = 24 / 6 = 4.0 A.', 'intermediate', 1200
    ))
    q.append(make_mc(
        'La unidad de carga eléctrica en el Sistema Internacional, el Coulomb, equivale a:',
        'Amperio · segundo (1 C = 1 A · s)', ['Amperio / segundo', 'Voltio · Amperio', 'Joule / segundo'],
        'Como I = dq/dt ⇒ q = I * t ⇒ 1 Coulomb = 1 Amperio * 1 segundo.', '1 C = 1 A * s.', 'basic', 1100
    ))
    return q
