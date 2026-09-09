# -*- coding: utf-8 -*-
from app.learning.question_helper import make_mc

def get_circuitos_questions():
    q = []
    q.append(make_mc(
        'Un alambre conductor cilíndrico de longitud L y sección transversal A tiene resistencia R. Si se funde y se estira hasta duplicar su longitud (2L) conservando el volumen, su nueva resistencia es:',
        '4 · R (se cuadruplica)', ['2 · R', 'R / 2', '8 · R'],
        'Si el volumen V = A · L es constante, al duplicar la longitud a 2L la sección se reduce a A/2. Por Ley de Pouillet: R_nueva = ρ (2L) / (A/2) = 4 ρ L / A = 4R.', 'Volumen constante ⇒ L x 2, A / 2 ⇒ R x 4.', 'advanced', 1280
    ))
    q.append(make_mc(
        'Por un resistor de 50 Ω circula una corriente I = 2.0 A durante 10 minutos. ¿Cuánto calor disipa por Efecto Joule?',
        '120000 J (120 kJ)', ['200 J', '1000 J', '1200 J'],
        'P = I² * R = (2.0)² * 50 = 4 * 50 = 200 W. Tiempo t = 10 min * 60 = 600 s. Calor Q = P * t = 200 W * 600 s = 120000 J.', 'Q = I² * R * t = 4 * 50 * 600 = 120 kJ.', 'intermediate', 1210
    ))
    q.append(make_mc(
        'Un calefactor eléctrico de 220 V tiene dos resistencias idénticas de 40 Ω. ¿Cómo deben conectarse para obtener la máxima potencia calórica posible?',
        'En paralelo (producen 2420 W en total)', ['En serie (producen 605 W)', 'Una sola conectada', 'Es indiferente'],
        'P = V² / Req. Para maximizar la potencia se debe minimizar la resistencia equivalente: en paralelo Req = 20 Ω ⇒ P = 220² / 20 = 2420 W. En serie Req = 80 Ω ⇒ P = 605 W.', 'En paralelo Req es mínima ⇒ P es máxima.', 'intermediate', 1220
    ))
    q.append(make_mc(
        'La resistividad eléctrica ρ de los metales conductores como el cobre o el aluminio aumenta con la temperatura debido a:',
        'El aumento de la agitación térmica de los iones de la red cristalina que incrementa la frecuencia de colisiones con los electrones de conducción',
        ['La disminución del número de electrones libres', 'La dilatación del cable únicamente', 'La pérdida de voltaje'],
        'Mayor temperatura genera mayores vibraciones reticulares, aumentando la probabilidad de choques inelásticos de los portadores.', 'Mayor temperatura ⇒ más colisiones ⇒ mayor ρ.', 'intermediate', 1200
    ))
    q.append(make_mc(
        'El fenómeno por el cual ciertos materiales a temperaturas extremadamente bajas (cerca del cero absoluto) pierden completamente toda resistencia eléctrica (R = 0) se denomina:',
        'Superconductividad', ['Semiconducción', 'Piezoelectricidad', 'Ferromagnetismo'],
        'Descubierto por Kamerlingh Onnes en 1911; permite transportar corriente sin ninguna disipación de calor por Joule.', 'Superconductividad (R = 0).', 'basic', 1120
    ))
    q.append(make_mc(
        'Tres resistores iguales de valor R se conectan en paralelo. La resistencia equivalente del conjunto es:',
        'R / 3', ['3 · R', 'R', 'R / 9'],
        '1/Req = 1/R + 1/R + 1/R = 3/R ⇒ Req = R / 3.', 'Req = R / n = R / 3.', 'basic', 1100
    ))
    q.append(make_mc(
        'Un voltímetro real tiene una resistencia interna de 1.0 MΩ (10⁶ Ω). Si se mide una tensión de 10 V, ¿cuánta corriente drena del circuito?',
        '10 μA (1.0 × 10⁻⁵ A)', ['10 mA', '1.0 A', '0.1 A'],
        'I = V / R_int = 10 V / 10⁶ Ω = 10⁻⁵ A = 10 μA (despreciable para no perturbar el circuito).', 'I = 10 / 10⁶ = 10 μA.', 'intermediate', 1190
    ))
    q.append(make_mc(
        'La velocidad de arrastre promedio (drift velocity) de los electrones en un cable de cobre por el que circula 1 A de corriente es aproximadamente del orden de:',
        'Fracciones de milímetro por segundo (≈ 10⁻⁴ m/s)', ['La velocidad de la luz (300000 km/s)', 'La velocidad del sonido (340 m/s)', '100 km/h'],
        'Aunque la señal electromagnética viaja a casi la velocidad de la luz, el desplazamiento físico neto individual de los electrones es muy lento.', 'vd ≈ 0.1 mm/s.', 'intermediate', 1230
    ))
    q.append(make_mc(
        'En un divisor de tensión formado por R1 = 2 kΩ y R2 = 8 kΩ en serie conectado a una fuente V0 = 20 V, ¿cuál es la tensión de salida sobre R2?',
        '16.0 V', ['4.0 V', '10.0 V', '2.0 V'],
        'Fórmula del divisor de tensión: V2 = V0 * [R2 / (R1 + R2)] = 20 V * [8 / (2 + 8)] = 20 * (8/10) = 16.0 V.', 'V2 = 20 * 8 / 10 = 16 V.', 'intermediate', 1210
    ))
    q.append(make_mc(
        'Un cable de extensión de 20 m transporta 10 A. Si la resistencia total del cable es 0.4 Ω, ¿cuál es la caída de tensión en el cable?',
        '4.0 V', ['8.0 V', '2.0 V', '40 V'],
        'V_caída = I * R = 10 A * 0.4 Ω = 4.0 V.', 'V = 10 * 0.4 = 4.0 V.', 'basic', 1110
    ))
    q.append(make_mc(
        'Una fuente de fem E = 12 V tiene una resistencia interna r = 0.5 Ω. Si entrega una corriente de 4.0 A, ¿cuál es la tensión en sus bornes terminales?',
        '10.0 V', ['12.0 V', '14.0 V', '2.0 V'],
        'V_bornes = E - I * r = 12 V - (4.0 A * 0.5 Ω) = 12 - 2.0 = 10.0 V.', 'V = E - I*r = 12 - 2 = 10 V.', 'intermediate', 1220
    ))
    q.append(make_mc(
        'La máxima transferencia de potencia desde una fuente con resistencia interna r hacia una carga exterior R_carga se logra cuando:',
        'R_carga = r (adaptación de impedancias)', ['R_carga = 0 (cortocircuito)', 'R_carga = infinito', 'R_carga = 10 r'],
        'Teorema de máxima transferencia de potencia de Jacobi: dP/dR = 0 ocurre cuando R_carga = r_interna.', 'R_carga = r_interna.', 'advanced', 1280
    ))
    q.append(make_mc(
        'Un fusible de 15 A protege una línea de 220 V. ¿Cuántas bombillas de 100 W en paralelo se pueden encender simultáneamente antes de que se funda?',
        '33 bombillas', ['15 bombillas', '22 bombillas', '45 bombillas'],
        'Potencia máxima admisible: P_máx = V * I_máx = 220 V * 15 A = 3300 W. Número n = 3300 W / 100 W = 33 bombillas.', 'n = 3300 / 100 = 33.', 'intermediate', 1230
    ))
    q.append(make_mc(
        'Un reóstato o potenciómetro es un resistor que permite:',
        'Variar manualmente el valor de su resistencia deslizando un contacto móvil',
        ['Aumentar el voltaje por inducción', 'Almacenar carga electrostática', 'Medir la frecuencia'],
        'Permite ajustar la resistencia y consecuentemente controlar corrientes o niveles de tensión en un circuito.', 'Resistencia variable.', 'basic', 1100
    ))
    q.append(make_mc(
        'Dos lámparas incandescentes de 60 W y 100 W diseñadas para 220 V se conectan accidentalmente en SERIE a 220 V. ¿Cuál brillará con mayor intensidad?',
        'La de 60 W (porque tiene mayor resistencia y al pasar la misma corriente disipa más potencia)',
        ['La de 100 W', 'Ambas brillan igual', 'Ninguna enciende'],
        'R = V²/P ⇒ R60 = 220²/60 ≈ 806 Ω > R100 = 220²/100 = 484 Ω. En serie circula la misma corriente I: P_disipada = I² R. Como R60 > R100, la de 60 W disipa más potencia.', 'Mayor R disipa más en serie (P = I²R).', 'advanced', 1290
    ))
    q.append(make_mc(
        'En un divisor de corriente formado por dos resistencias en paralelo R1 = 10 Ω y R2 = 40 Ω que reciben una corriente total I_total = 5.0 A, ¿cuánta corriente va por R1?',
        '4.0 A', ['1.0 A', '2.5 A', '5.0 A'],
        'Divisor de corriente: I1 = I_tot * [R2 / (R1 + R2)] = 5.0 A * [40 / (10 + 40)] = 5.0 * (40/50) = 4.0 A.', 'I1 = 5 * 40/50 = 4.0 A.', 'intermediate', 1230
    ))
    q.append(make_mc(
        'Un puente de Wheatstone está en equilibrio cuando:',
        'La diferencia de potencial entre sus ramas intermedias es cero (V_galvanómetro = 0 V), cumpliendo R1 · R4 = R2 · R3',
        ['Todas las resistencias son iguales a cero', 'La corriente total es máxima', 'La fuente se desconecta'],
        'Condición de equilibrio de Wheatstone: R1/R2 = R3/R4 ⇒ R1·R4 = R2·R3.', 'Equilibrio de puente: R1 R4 = R2 R3.', 'intermediate', 1240
    ))
    q.append(make_mc(
        'La unidad de conductancia eléctrica en el Sistema Internacional es el Siemens (S), que equivale a:',
        '1 / Ohm (Ω⁻¹)', ['Ohm · metro', 'Voltio / Amperio', 'Joule · segundo'],
        'La conductancia G = 1 / R mide la facilidad con que fluye la corriente: [G] = Ω⁻¹ = Siemens (S).', '1 S = 1 / Ω.', 'basic', 1110
    ))
    q.append(make_mc(
        'Si un cable de cobre de 100 m tiene una sección de 2.5 mm² (2.5 × 10⁻⁶ m²) y ρ_Cu = 1.7 × 10⁻⁸ Ω·m, ¿cuál es su resistencia?',
        '0.68 Ω', ['6.8 Ω', '0.068 Ω', '1.7 Ω'],
        'R = ρ * L / A = 1.7x10⁻⁸ * 100 / (2.5x10⁻⁶) = 1.7x10⁻⁶ / (2.5x10⁻⁶) = 1.7 / 2.5 = 0.68 Ω.', 'R = 170x10⁻⁸ / 2.5x10⁻⁶ = 0.68 Ω.', 'intermediate', 1220
    ))
    q.append(make_mc(
        'El coeficiente térmico de resistencia α para metales puros como el platino o el cobre es típicamente:',
        'Positivo (la resistencia se incrementa al aumentar la temperatura: R(T) = R0(1 + α ΔT))',
        ['Negativo (conduce mejor con calor)', 'Cero', 'Infinito'],
        'En los metales α > 0; en semiconductores y carbón (termistores NTC) α es negativo.', 'α > 0 en metales.', 'intermediate', 1210
    ))
    return q
