# -*- coding: utf-8 -*-
from app.learning.question_helper import make_mc

def get_campo_lineas_questions():
    q = []
    q.append(make_mc(
        'El vector campo eléctrico E en cualquier punto de una línea de fuerza es:',
        'Estrictamente tangente a la línea de fuerza en dicho punto', ['Perpendicular a la línea', 'Opuesto a la línea', 'Secante'],
        'Por definición de línea de campo o de fuerza, el vector E(r) es tangente en cada coordenada espacial.', 'Tangente a la línea.', 'basic', 1100
    ))
    q.append(make_mc(
        'Las líneas de campo electrostático se originan en:',
        'Las cargas positivas (fuentes) o el infinito y terminan en las negativas (sumideros) o el infinito',
        ['Las cargas negativas y terminan en las positivas', 'Lazos cerrados continuos', 'El polo norte magnético'],
        'Las cargas positivas actúan como fuentes divergentes y las negativas como sumideros convergentes.', 'De (+) a (-).', 'basic', 1100
    ))
    q.append(make_mc(
        '¿Por qué dos líneas de campo electrostático jamás pueden cruzarse en el espacio?',
        'Porque en el punto de cruce el campo tendría dos direcciones simultáneas, violando la unicidad del vector E',
        ['Porque las cargas tienen igual signo', 'Porque las líneas son siempre paralelas', 'Porque la fuerza es cero'],
        'En cada punto del espacio existe un único vector campo neto E = Σ E_i. Dos líneas cruzadas exigirían dos tangentes simultáneas.', 'Unicidad del campo vectorial.', 'intermediate', 1180
    ))
    q.append(make_mc(
        'En una región del espacio donde las líneas de campo están muy juntas y densas, podemos inferir que:',
        'La intensidad del campo eléctrico ||E|| es grande (campo intenso)', ['El campo es débil', 'El potencial es cero', 'No hay cargas cerca'],
        'La densidad espacial de líneas de campo por unidad de área transversal es directamente proporcional a la magnitud ||E||.', 'Mayor densidad ⇒ mayor ||E||.', 'basic', 1120
    ))
    q.append(make_mc(
        '¿Cuál es el campo eléctrico en el interior de un conductor metálico en equilibrio electrostático?',
        'E = 0 N/C en todo el volumen interior', ['E es máximo en el centro', 'E depende del potencial exterior', 'E = infinito'],
        'Si existiera campo interior, los electrones libres experimentarían fuerza y se moverían, contradiciendo el equilibrio estático.', 'E_interior = 0.', 'basic', 1120
    ))
    q.append(make_mc(
        'Una carga puntual Q = -8.0 nC crea a 0.20 m de distancia un campo eléctrico de magnitud:',
        '1800 N/C apuntando hacia la carga (convergente)', ['1800 N/C saliendo de la carga', '360 N/C', '90 N/C'],
        'E = ke * |Q| / r² = 9.0x10⁹ * 8.0x10⁻⁹ / (0.20)² = 72 / 0.04 = 1800 N/C. Al ser negativa, apunta hacia ella.', 'E = 72 / 0.04 = 1800 N/C convergente.', 'intermediate', 1200
    ))
    q.append(make_mc(
        'Un electrón (qe = -1.6 × 10⁻¹⁹ C, me = 9.11 × 10⁻³¹ kg) se suelta en un campo eléctrico uniforme E = 1000 N/C hacia la derecha. Su aceleración es:',
        '1.76 × 10¹⁴ m/s² hacia la izquierda', ['1.76 × 10¹⁴ m/s² hacia la derecha', '1.6 × 10⁻¹⁶ m/s²', '9.8 m/s²'],
        'F = q*E = 1.6x10⁻¹⁹ * 1000 = 1.6x10⁻¹⁶ N. Al ser negativo, F va hacia la izquierda. a = F / me = 1.6x10⁻¹⁶ / 9.11x10⁻³¹ ≈ 1.76 × 10¹⁴ m/s².', 'a = qE/m hacia la izquierda.', 'advanced', 1270
    ))
    q.append(make_mc(
        'El flujo eléctrico Φ_E a través de cualquier superficie cerrada que encierra una carga neta Q_encerrada viene dado por la Ley de Gauss:',
        'Φ_E = ∮ E · dA = Q_encerrada / ε0', ['Φ_E = Q_encerrada · ε0', 'Φ_E = ke · Q_encerrada', 'Φ_E = 0 siempre'],
        'La Ley de Gauss vincula el flujo neto saliente con la carga interior total dividida por la permitividad del vacío ε0.', 'Φ = Q_enc / ε0.', 'intermediate', 1230
    ))
    q.append(make_mc(
        'Si una superficie esférica cerrada gaussiana no encierra ninguna carga eléctrica neta en su interior (Q_int = 0), el flujo total a través de ella es:',
        '0 (todo lo que entra por un lado sale por el otro)', ['Infinito', 'Positivo si hay cargas afuera', 'Negativo'],
        'Por la Ley de Gauss: Φ = Q_enc / ε0 = 0 / ε0 = 0.', 'Φ_neto = 0.', 'basic', 1130
    ))
    q.append(make_mc(
        'El campo eléctrico producido por una placa plana infinita no conductora con densidad superficial de carga σ uniforme es:',
        'E = σ / (2 ε0) (independiente de la distancia a la placa)', ['E = σ / ε0', 'E = σ · r / (2 ε0)', 'E ∝ 1/r²'],
        'Aplicando Gauss con un cilindro simétrico que atraviesa la placa: E = σ / (2ε0) constante en todo el semi-espacio.', 'E = σ / (2 ε0).', 'advanced', 1280
    ))
    q.append(make_mc(
        'Justo en la superficie exterior de un conductor cargado en equilibrio electrostático, el campo eléctrico es:',
        'E = σ / ε0 perpendicular a la superficie', ['E = 0', 'E = σ / (2 ε0)', 'E tangente a la superficie'],
        'El campo es ortogonal a la superficie equipotencial del conductor y su magnitud es σ / ε0.', 'E = σ / ε0 perpendicular.', 'intermediate', 1240
    ))
    q.append(make_mc(
        'El efecto punta (concentración de campo eléctrico en los vértices y zonas de menor radio de curvatura de un conductor) explica el funcionamiento de:',
        'Los pararrayos (ionización y descarga corona de aire)', ['Los transformadores', 'Las baterías químicas', 'Los fusibles térmicos'],
        'La densidad de carga superficial σ crece inversamente con el radio de curvatura (σ ∝ 1/r), generando campos locales intensísimos que ionizan el aire.', 'Pararrayos por efecto punta.', 'intermediate', 1210
    ))
    q.append(make_mc(
        'Una jaula de Faraday protege su interior de campos electrostáticos externos gracias a:',
        'La redistribución de cargas libres en el metal que crea un campo inducido opuesto que anula exactamente el campo externo en el interior',
        ['La absorción de la energía por calor', 'La masa del metal que bloquea los protones', 'El magnetismo del material'],
        'En equilibrio electrostático el campo dentro de una cavidad cerrada de un conductor es estrictamente nulo.', 'Blindaje electrostático.', 'basic', 1140
    ))
    q.append(make_mc(
        'El campo eléctrico en el punto medio exacto entre dos cargas idénticas +q separadas por distancia d es:',
        '0 N/C', ['2 ke q / (d/2)²', 'ke q / d²', '4 ke q / d²'],
        'Ambas cargas positivas generan en el centro vectores campo de igual módulo pero sentidos opuestos que se cancelan vectorialmente.', 'E_neto = E1 - E2 = 0.', 'basic', 1120
    ))
    q.append(make_mc(
        'El campo eléctrico en el punto medio entre dos cargas de igual magnitud pero signos opuestos (+q y -q) separadas por distancia d es:',
        '8 ke q / d² apuntando hacia la carga negativa', ['0 N/C', '4 ke q / d²', '2 ke q / d² hacia la positiva'],
        'Ambos vectores apuntan hacia la carga negativa en el mismo sentido: E = ke q / (d/2)² + ke q / (d/2)² = 2 * (4 ke q / d²) = 8 ke q / d².', 'E = 8 ke q / d² hacia (-).', 'intermediate', 1240
    ))
    q.append(make_mc(
        '¿Cuál es la unidad del flujo eléctrico en el Sistema Internacional?',
        'N · m² / C (equivalente a V · m)', ['Tesla · m²', 'Joule / C', 'Weber'],
        'Φ_E = E · A ⇒ [Φ_E] = (N/C) * m² = N·m²/C = (V/m) * m² = V · m.', 'N·m²/C o V·m.', 'basic', 1130
    ))
    q.append(make_mc(
        'Un campo eléctrico uniforme E = 2000 N/C atraviesa perpendicularmente una superficie cuadrada de lado L = 0.20 m. ¿Cuál es el flujo eléctrico?',
        '80 N · m² / C', ['400 N · m² / C', '20 N · m² / C', '40 N · m² / C'],
        'Área A = (0.20)² = 0.04 m². Flujo Φ = E * A * cos(0°) = 2000 * 0.04 * 1 = 80 N·m²/C.', 'Φ = 2000 * 0.04 = 80 N·m²/C.', 'basic', 1140
    ))
    q.append(make_mc(
        'A grandes distancias (r >> d), el campo eléctrico creado por un dipolo eléctrico disminuye con la distancia según:',
        '1 / r³ (decae más rápido que el de una carga puntual)', ['1 / r²', '1 / r', 'e^(-r)'],
        'Por superposición de cargas cercanas de signos opuestos que casi se cancelan: E_dipolo ∝ p / r³.', 'E_dipolo ∝ 1/r³.', 'advanced', 1280
    ))
    q.append(make_mc(
        'Si un dipolo eléctrico p se coloca en un campo eléctrico uniforme E, la fuerza neta sobre el dipolo y el torque que experimenta son:',
        'Fuerza neta = 0, pero experimenta un torque τ = p × E que tiende a alinearlo con el campo',
        ['Fuerza neta grande y torque cero', 'Fuerza neta y torque nulos', 'Fuerza paralela al campo'],
        'F_neta = +qE - qE = 0. El par de fuerzas crea un torque restaurador τ = p * E * sen(θ).', 'F_neta = 0; τ = p x E.', 'intermediate', 1230
    ))
    q.append(make_mc(
        'El concepto de líneas de campo eléctrico fue introducido originalmente en la física por:',
        'Michael Faraday (como "líneas de fuerza")', ['James Clerk Maxwell', 'Isaac Newton', 'Charles Coulomb'],
        'Faraday concibió visual e intuitivamente las líneas de tensión física en el espacio, formalizadas luego por Maxwell.', 'Michael Faraday.', 'basic', 1100
    ))
    return q
