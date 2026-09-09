# -*- coding: utf-8 -*-
from app.learning.question_helper import make_mc

def get_gravitacion_questions():
    q = []
    q.append(make_mc(
        'Si la distancia entre dos planetas se triplica (r_nuevo = 3 · r_antiguo), ¿cómo varía la fuerza gravitatoria entre ellos?',
        'Se reduce a la novena parte (F / 9)', ['Se reduce a la tercera parte (F / 3)', 'Se triplica', 'Permanece igual'],
        'F ∝ 1/r². Al triplicar r: F_nuevo = G m1 m2 / (3r)² = (G m1 m2 / r²) / 9 = F / 9.', 'F ∝ 1/r² ⇒ 1/3² = 1/9.', 'basic', 1100
    ))
    q.append(make_mc(
        'Si la masa de la Tierra se duplicara manteniendo constante su radio, la aceleración de la gravedad g en la superficie:',
        'Se duplicaría (pasaría a ser ≈ 19.6 m/s²)', ['Se reduciría a la mitad', 'Se cuadruplicaría', 'No cambiaría'],
        'g = G · M / R². Como M está linealmente en el numerador, al duplicar M, g se duplica.', 'g = G*(2M)/R² = 2*g.', 'basic', 1110
    ))
    q.append(make_mc(
        'Si el radio de la Tierra se duplicara manteniendo constante su masa, la gravedad en la superficie:',
        'Se reduciría a la cuarta parte (g / 4 ≈ 2.45 m/s²)', ['Se reduciría a la mitad', 'Se duplicaría', 'Permanecería en 9.8 m/s²'],
        'g = G · M / R². Como R está elevado al cuadrado en el denominador, al duplicar R: g_nuevo = g / 2² = g / 4.', 'g ∝ 1/R² ⇒ 1/2² = 1/4.', 'basic', 1120
    ))
    q.append(make_mc(
        'La Tercera Ley de Kepler establece que para todos los planetas del Sistema Solar:',
        'T² / a³ = constante (el cuadrado del período orbital es proporcional al cubo del semieje mayor)',
        ['T / a = constante', 'T³ / a² = constante', 'T² · a³ = constante'],
        'La Tercera Ley (armónica) de Kepler vincula los períodos con las distancias medias: T² ∝ a³.', 'T² / a³ = 4π² / (G M_Sol).', 'basic', 1130
    ))
    q.append(make_mc(
        'Un satélite geoestacionario permanece fijo sobre el mismo punto del ecuador terrestre. ¿Cuál es su período orbital?',
        '24 horas (1 día sideral)', ['12 horas', '90 minutos', '365 días'],
        'Para acompañar la rotación sincrónica de la Tierra, su período orbital debe ser idéntico al período de rotación terrestre (24 h).', 'T = 24 h.', 'basic', 1100
    ))
    q.append(make_mc(
        'La constante de gravitación universal G tiene un valor numérico aproximado de:',
        '6.674 × 10⁻¹¹ N · m² / kg²', ['9.8 m/s²', '3.0 × 10⁸ m/s', '8.99 × 10⁹ N · m² / C²'],
        'Medida experimentalmente por Henry Cavendish con la balanza de torsión: G ≈ 6.674 × 10⁻¹¹ N·m²/kg².', 'G = 6.674x10⁻¹¹ N·m²/kg².', 'basic', 1100
    ))
    q.append(make_mc(
        'La velocidad de escape de un planeta de masa M y radio R representa:',
        'La rapidez mínima necesaria para escapar de la atracción gravitatoria del planeta hacia el infinito sin impulso adicional',
        ['La velocidad para orbitar a baja altura', 'La velocidad del sonido en su atmósfera', 'La velocidad de la luz'],
        'Se calcula igualando la energía mecánica inicial a cero: ½ m v_esc² - G M m / R = 0 ⇒ v_esc = √(2 G M / R).', 'v_esc = √(2 G M / R).', 'intermediate', 1190
    ))
    q.append(make_mc(
        '¿A qué altura sobre la superficie terrestre la aceleración de gravedad se reduce a g/4? (R = radio terrestre ≈ 6370 km).',
        'A una altura h = R (a 6370 km sobre la superficie)', ['A una altura h = 2R', 'A una altura h = R/2', 'A una altura h = 4R'],
        'g(r) = G*M / r². Para que sea g/4, la distancia desde el centro debe ser r = 2R. Como r = R + h, entonces h = R.', 'r = 2R ⇒ h = r - R = R.', 'intermediate', 1230
    ))
    q.append(make_mc(
        'Según la Segunda Ley de Kepler (Ley de las Áreas), cuando un planeta en órbita elíptica pasa por su perihelio (punto más cercano al Sol):',
        'Su velocidad orbital es máxima', ['Su velocidad orbital es mínima', 'Su aceleración es nula', 'La fuerza gravitatoria es mínima'],
        'Al barrer áreas iguales en tiempos iguales, al estar más cerca del Sol el radio vector es menor, requiriendo mayor velocidad lineal.', 'Perihelio: r mínimo ⇒ v máxima. Afelio: r máximo ⇒ v mínima.', 'intermediate', 1210
    ))
    q.append(make_mc(
        'Dos masas puntuales de 100 kg cada una están separadas 1.0 m. ¿Cuál es la fuerza de atracción gravitatoria mutua?',
        '6.67 × 10⁻⁷ N', ['6.67 × 10⁻¹¹ N', '100 N', '980 N'],
        'F = G * m1 * m2 / r² = 6.674x10⁻¹¹ * 100 * 100 / (1.0)² = 6.674x10⁻⁷ N.', 'F = 6.674x10⁻¹¹ * 10000 = 6.67x10⁻⁷ N.', 'basic', 1140
    ))
    q.append(make_mc(
        'Los astronautas en la Estación Espacial Internacional flotan ingrávidos debido a que:',
        'Están en constante estado de caída libre orbital alrededor de la Tierra junto con la nave',
        ['En el espacio no existe gravedad terrestre', 'La atmósfera los sostiene', 'La fuerza centrífuga anula mágicamente la masa'],
        'A 400 km de altura la gravedad terrestre es aún el 90% de la superficie; la sensación de ingravidez se debe a la caída libre orbital perpetua.', 'Caída libre orbital continua.', 'intermediate', 1200
    ))
    q.append(make_mc(
        'La velocidad orbital circular de un satélite cerca de la superficie de un planeta depende de:',
        'La masa del planeta y el radio de la órbita, siendo totalmente independiente de la masa del satélite',
        ['La masa del satélite únicamente', 'El combustible que lleve a bordo', 'La forma aerodinámica del satélite'],
        'G M m / r² = m v² / r ⇒ v = √(G M / r). La masa m del satélite se simplifica.', 'v = √(G M / r).', 'intermediate', 1190
    ))
    q.append(make_mc(
        'Si un planeta hipotético tiene el doble de radio que la Tierra (Rp = 2 Rt) y cuatro veces su masa (Mp = 4 Mt), ¿cuánto vale la gravedad en su superficie?',
        '9.8 m/s² (igual que en la Tierra)', ['19.6 m/s²', '4.9 m/s²', '39.2 m/s²'],
        'gp = G * (4 Mt) / (2 Rt)² = G * 4 Mt / (4 Rt²) = G Mt / Rt² = gt = 9.8 m/s².', 'gp = 4 / 2² * gt = 4/4 * gt = gt.', 'intermediate', 1220
    ))
    q.append(make_mc(
        'El semieje mayor de la órbita de un asteroide es a = 4 UA (Unidades Astronómicas). ¿Cuál es su período orbital en años terrestres?',
        '8 años', ['16 años', '64 años', '2 años'],
        'T² = a³ (en años y UA) ⇒ T² = 4³ = 64 ⇒ T = √64 = 8 años terrestres.', 'T = √(4³) = √64 = 8 años.', 'intermediate', 1210
    ))
    q.append(make_mc(
        '¿Cuál es la trayectoria de un cuerpo que es lanzado desde la superficie de la Tierra con una velocidad exactamente igual a la velocidad de escape?',
        'Parabólica (energía mecánica total Em = 0)', ['Elíptica cerrada', 'Circular', 'Hiperbólica abierta (Em > 0)'],
        'Em < 0: órbita elíptica o circular; Em = 0: trayectoria parabólica de escape límite; Em > 0: trayectoria hiperbólica.', 'Em = 0 ⇒ parábola.', 'advanced', 1270
    ))
    q.append(make_mc(
        'La Primera Ley de Kepler demuestra que el Sol no está en el centro de la órbita, sino en:',
        'Uno de los dos focos de la elipse', ['El vértice menor', 'El centro geométrico', 'El infinito'],
        'Las órbitas planetarias son elipses y el cuerpo central masivo ocupa uno de los focos.', 'Foco elíptico.', 'basic', 1110
    ))
    q.append(make_mc(
        'La velocidad de escape de la superficie de la Tierra es aproximadamente:',
        '11.2 km/s', ['7.9 km/s', '30 km/s', '3.0 × 10⁵ km/s'],
        'v_esc = √(2 * 6.67x10⁻¹¹ * 5.97x10²⁴ / 6.37x10⁶) ≈ 11200 m/s = 11.2 km/s.', 'v_esc ≈ 11.2 km/s.', 'basic', 1140
    ))
    q.append(make_mc(
        'El punto de mayor acercamiento de la Luna a la Tierra en su órbita elíptica se denomina:',
        'Perigeo (en el Sol es Perihelio)', ['Apogeo', 'Afelio', 'Cenit'],
        'Perigeo = punto más cercano a la Tierra; Apogeo = punto más lejano. Perihelio / Afelio son respecto al Sol.', 'Perigeo.', 'basic', 1120
    ))
    q.append(make_mc(
        '¿Por qué las mareas oceánicas en la Tierra son producidas principalmente por la Luna y no por el Sol, a pesar de que el Sol es muchísimo más masivo?',
        'Porque la fuerza de marea depende del gradiente (1/r³) y la Luna está muchísimo más cerca de la Tierra que el Sol',
        ['Porque la Luna tiene mayor fuerza gravitatoria neta que el Sol', 'Porque el Sol solo atrae a la tierra sólida', 'Por el viento solar'],
        'El efecto diferencial de marea decae con el cubo de la distancia (dF/dr ∝ M/r³), haciendo que la proximidad lunar predomine.', 'Efecto de marea ∝ M/r³.', 'advanced', 1290
    ))
    q.append(make_mc(
        'La energía potencial gravitatoria canónica entre dos masas m1 y m2 a distancia r con referencia cero en el infinito es:',
        'U(r) = - G · (m1 · m2) / r', ['U(r) = + G · (m1 · m2) / r', 'U(r) = - G · (m1 · m2) / r²', 'U(r) = m · g · r'],
        'Es negativa porque la gravedad es puramente atractiva y se requiere trabajo positivo para separar las masas hasta el infinito.', 'U = - G m1 m2 / r.', 'intermediate', 1230
    ))
    return q

def get_estatica_questions():
    q = []
    q.append(make_mc(
        'Para que un cuerpo rígido esté en equilibrio estático completo se requiere:',
        'Que la fuerza neta sea cero (ΣF = 0) Y el torque neto sea cero (Στ = 0)',
        ['Solo que la fuerza neta sea cero (ΣF = 0)', 'Solo que el torque neto sea cero (Στ = 0)', 'Que su velocidad sea máxima'],
        'La 1.ª condición garantiza equilibrio traslacional y la 2.ª condición garantiza equilibrio rotacional.', 'ΣF = 0 y Στ = 0.', 'basic', 1100
    ))
    q.append(make_mc(
        'Una fuerza F = 40 N se aplica perpendicularmente al extremo de una barra de 0.50 m articulada en el otro extremo. ¿Cuál es el torque?',
        '20.0 N · m', ['80.0 N · m', '40.0 N · m', '10.0 N · m'],
        'τ = F * d * sen(90°) = 40 N * 0.50 m * 1 = 20.0 N·m.', 'τ = 40 * 0.5 = 20 N·m.', 'basic', 1110
    ))
    q.append(make_mc(
        'Si una fuerza pasa exactamente por el punto de rotación (centro de giro O), ¿cuánto vale su torque respecto a ese punto?',
        '0 N · m', ['F · r', 'Infinito', 'Depende del ángulo'],
        'La distancia perpendicular d_brazo desde el eje de giro a la línea de acción es cero, por lo que τ = F * 0 = 0.', 'Brazo d = 0 ⇒ τ = 0.', 'basic', 1100
    ))
    q.append(make_mc(
        'En un balancín horizontal en equilibrio de 4.0 m de largo con fulcro en el centro, un niño de 30 kg se sienta en un extremo (a 2.0 m). ¿Dónde debe sentarse un niño de 40 kg?',
        'A 1.5 m del fulcro del lado opuesto', ['A 2.0 m del fulcro', 'A 1.0 m del fulcro', 'A 1.33 m del fulcro'],
        'Equilibrio de torques: τ1 = τ2 ⇒ m1 * g * d1 = m2 * g * d2 ⇒ 30 * 2.0 = 40 * d2 ⇒ 60 = 40 * d2 ⇒ d2 = 1.5 m.', 'd2 = 60 / 40 = 1.5 m.', 'intermediate', 1190
    ))
    q.append(make_mc(
        'Una palanca de segundo género (como una carretilla) se caracteriza por tener:',
        'La resistencia ubicada entre el punto de apoyo y la potencia (fulcro en un extremo)',
        ['El punto de apoyo en el medio entre potencia y resistencia', 'La potencia en el medio', 'Ningún punto de apoyo'],
        'En 2.º género la resistencia está en el centro, lo que garantiza siempre una ventaja mecánica mayor que 1 (VM > 1).', '2.º género: R en el medio.', 'basic', 1120
    ))
    q.append(make_mc(
        'Una palanca de tercer género (como una pinza o el antebrazo humano) tiene ventaja mecánica:',
        'Siempre menor que 1 (VM < 1, gana velocidad y rango de movimiento)', ['Siempre mayor que 1', 'Exactamente igual a 1', 'Infinito'],
        'Como la potencia está más cerca del fulcro que la resistencia, se requiere mayor fuerza pero se gana desplazamiento.', 'VM < 1.', 'intermediate', 1180
    ))
    q.append(make_mc(
        'Una barra homogénea de 10 kg y 2.0 m reposa horizontalmente sobre dos apoyos en sus extremos A y B. ¿Qué fuerza ejerce cada apoyo? (g = 9.8 m/s²).',
        '49.0 N cada uno', ['98.0 N cada uno', '24.5 N cada uno', '10.0 N cada uno'],
        'Peso P = 10 * 9.8 = 98 N actuando en el centro de gravedad (a 1.0 m). Por simetría simétrica: Ra = Rb = P / 2 = 49.0 N.', 'Ra = Rb = 98 / 2 = 49 N.', 'basic', 1130
    ))
    q.append(make_mc(
        'Si una fuerza F = 60 N forma un ángulo de 30° con una llave de 0.40 m, ¿cuál es el torque respecto a la tuerca?',
        '12.0 N · m', ['24.0 N · m', '20.78 N · m', '6.0 N · m'],
        'τ = F * r * sen(θ) = 60 * 0.40 * sen(30°) = 24.0 * 0.5 = 12.0 N·m.', 'τ = 60 * 0.4 * 0.5 = 12 N·m.', 'intermediate', 1200
    ))
    q.append(make_mc(
        'El centro de gravedad de un cuerpo homogéneo simétrico coincide con:',
        'Su centro geométrico (centroide)', ['Su punto más bajo', 'Cualquier extremo', 'Un punto fuera del cuerpo siempre'],
        'En cuerpos de densidad uniforme y simetría geométrica, el baricentro coincide con el centro geométrico.', 'Centroide geométrico.', 'basic', 1110
    ))
    q.append(make_mc(
        'Dos fuerzas paralelas de igual magnitud F pero sentidos opuestos separadas por una distancia d constituyen:',
        'Un par de fuerzas o cupla (produce rotación pura con fuerza neta nula)',
        ['Un equilibrio estático completo', 'Una fuerza neta 2F', 'Un movimiento rectilíneo acelerado'],
        'F_neta = F - F = 0 (no hay traslación), pero el torque neto es τ = F · d en cualquier punto del plano.', 'Cupla o par de fuerzas: τ = F*d.', 'intermediate', 1210
    ))
    q.append(make_mc(
        'Una escalera uniforme de peso P reposa apoyada en una pared vertical lisa (sin fricción) y en un suelo horizontal rugoso. La fuerza ejercida por la pared sobre la escalera es:',
        'Estrictamente perpendicular a la pared (horizontal)', ['Paralela a la pared hacia arriba', 'En la dirección de la escalera', 'Cero'],
        'Al ser la pared perfectamente lisa, no puede ejercer fuerza tangencial de rozamiento, solo fuerza normal perpendicular.', 'Normal a la pared lisa.', 'intermediate', 1220
    ))
    q.append(make_mc(
        'La unidad de medida del torque en el Sistema Internacional es:',
        'N · m (Newton metro)', ['Joule (J)', 'Watt (W)', 'N / m'],
        'Aunque dimensionalmente es fuerza por distancia, el torque no es energía y se expresa formalmente como N·m, nunca en Joules.', 'N·m.', 'basic', 1100
    ))
    q.append(make_mc(
        'Un cartel de 20 kg cuelga del extremo de una barra horizontal de 2.0 m sostenida por un cable diagonal a 45°. ¿Cuál es la tensión en el cable? (g = 9.8 m/s²). Despreciar masa de la barra.',
        '277.2 N', ['196.0 N', '138.6 N', '392.0 N'],
        'Torque respecto al pivote de la pared: T * sen(45°) * L - P * L = 0 ⇒ T * sen(45°) = P = 20 * 9.8 = 196 N ⇒ T = 196 / 0.7071 ≈ 277.2 N.', 'T = 196 / sen(45°) ≈ 277.2 N.', 'advanced', 1280
    ))
    q.append(make_mc(
        'En un sistema de polea simple fija, la ventaja mecánica teórica es:',
        'VM = 1 (no reduce la fuerza requerida, solo cambia la dirección de aplicación)',
        ['VM = 2', 'VM = 4', 'VM = 0.5'],
        'Una polea fija solo redirige la fuerza para mayor comodidad ergonómica: F = P.', 'VM = 1.', 'basic', 1120
    ))
    q.append(make_mc(
        'En un polipasto o aparejo factorial con 4 poleas (2 fijas y 2 móviles), la fuerza F para elevar un peso P = 800 N es:',
        '200 N', ['400 N', '800 N', '100 N'],
        'Con 2 poleas móviles que sostienen 4 tramos de cuerda: F = P / 4 = 800 / 4 = 200 N.', 'F = P / 2n = 800 / 4 = 200 N.', 'intermediate', 1210
    ))
    q.append(make_mc(
        'Un cuerpo suspendido se encuentra en equilibrio estable cuando:',
        'Al apartarlo ligeramente de su posición de equilibrio, surge un torque restaurador que lo devuelve a su posición original',
        ['Al apartarlo, se aleja indefinidamente', 'Permanece en cualquier nueva posición', 'Su centro de gravedad está en el punto más alto'],
        'Equilibrio estable: el centro de gravedad asciende al perturbarlo, creando un par restaurador.', 'Equilibrio estable.', 'intermediate', 1190
    ))
    q.append(make_mc(
        'Para abrir una puerta con la menor fuerza posible, ¿dónde conviene empujar?',
        'En el borde más alejado de las bisagras, aplicando la fuerza perpendicularmente',
        ['Cerca de las bisagras', 'A 45° en el centro', 'En las mismas bisagras'],
        'Para maximizar el torque con la menor fuerza se debe maximizar el brazo de palanca r y el ángulo sen(90°) = 1.', 'τ = r*F ⇒ mayor r exige menor F.', 'basic', 1100
    ))
    q.append(make_mc(
        'Si sobre una rueda actúan dos fuerzas de 10 N y 15 N en sentidos de giro opuestos a radios r1 = 0.3 m y r2 = 0.2 m, ¿cuál es el torque neto?',
        '0 N · m (la rueda está en equilibrio rotacional)', ['3.0 N · m', '6.0 N · m', '0.5 N · m'],
        'τ1 = 10 * 0.3 = 3.0 N·m (antihorario +). τ2 = 15 * 0.2 = 3.0 N·m (horario -). Torque neto = +3.0 - 3.0 = 0 N·m.', 'τ_neto = 3.0 - 3.0 = 0.', 'intermediate', 1200
    ))
    q.append(make_mc(
        'Un bloque de 50 kg se encuentra apoyado sobre una base de 0.2 m de ancho. Si su centro de gravedad está a 0.8 m de altura, el bloque volcará cuando se incline un ángulo tal que:',
        'La vertical que pasa por su centro de gravedad caiga fuera de la base de sustentación',
        ['La fuerza normal sea mayor que el peso', 'El rozamiento sea cero', 'El ángulo sea exactamente 45°'],
        'Condición geométrica de estabilidad de vuelco: la línea de acción del peso debe intersectar la base de apoyo.', 'Línea del peso fuera de la base.', 'intermediate', 1230
    ))
    q.append(make_mc(
        'Un tablón de 6 m de largo y 30 kg tiene su centro de gravedad en el centro (a 3 m). Se apoya a 2 m de un extremo. ¿Qué masa colocada en ese extremo equilibra el tablón?',
        '15 kg', ['30 kg', '10 kg', '7.5 kg'],
        'El peso del tablón (30 kg) actúa a 1 m del apoyo (a 3m del extremo - 2m = 1m). Torque del tablón = 30 * 1 = 30 kg·m. El contrapeso está a 2 m: m * 2 = 30 ⇒ m = 15 kg.', 'm * 2 = 30 * 1 ⇒ m = 15 kg.', 'advanced', 1270
    ))
    return q

def get_fluidos_questions():
    q = []
    q.append(make_mc(
        '¿Cuál es la presión hidrostática a 10 m de profundidad en agua dulce? (ρ = 1000 kg/m³, g = 9.8 m/s²).',
        '98000 Pa (0.98 bar ≈ 1 atm)', ['980 Pa', '9800 Pa', '1000000 Pa'],
        'P = ρ * g * h = 1000 * 9.8 * 10 = 98000 Pa.', 'P = 1000 * 9.8 * 10 = 98000 Pa.', 'basic', 1110
    ))
    q.append(make_mc(
        'La presión atmosférica normal a nivel del mar equivale aproximadamente a:',
        '101325 Pa (1 atm = 760 mmHg)', ['1000 Pa', '9.8 Pa', '1000000 Pa'],
        'Valor estándar: 1 atm = 101325 Pa ≈ 1.013 bar = 760 Torr o mmHg.', '1 atm = 101325 Pa.', 'basic', 1100
    ))
    q.append(make_mc(
        'En una prensa hidráulica, los émbolos tienen radios r1 = 2.0 cm y r2 = 20.0 cm. Si se aplica F1 = 50 N, ¿cuál es la fuerza F2 generada?',
        '5000 N', ['500 N', '100 N', '50000 N'],
        'Las áreas crecen con el cuadrado del radio: A2 / A1 = (r2/r1)² = (20/2)² = 10² = 100. F2 = F1 * (A2/A1) = 50 N * 100 = 5000 N.', 'F2 = 50 * (20/2)² = 50 * 100 = 5000 N.', 'intermediate', 1210
    ))
    q.append(make_mc(
        'El principio de Arquímedes afirma que el empuje hidrostático sobre un cuerpo sumergido es igual a:',
        'El peso del volumen de fluido desalojado por el cuerpo',
        ['El peso total del cuerpo', 'La densidad del cuerpo multiplicada por el volumen', 'La presión atmosférica'],
        'E = m_fluido_desalojado * g = ρ_fluido * V_sumergido * g.', 'Empuje = Peso del fluido desalojado.', 'basic', 1100
    ))
    q.append(make_mc(
        'Un bloque de hielo de densidad ρ = 920 kg/m³ flota en agua dulce (ρ = 1000 kg/m³). ¿Qué porcentaje de su volumen queda sumergido?',
        '92%', ['8%', '50%', '100%'],
        'En flotación E = P ⇒ ρ_agua * V_sum * g = ρ_hielo * V_tot * g ⇒ V_sum / V_tot = 920 / 1000 = 0.92 = 92%.', 'Fracción sumergida = ρ_cuerpo / ρ_fluido = 920/1000 = 92%.', 'intermediate', 1200
    ))
    q.append(make_mc(
        'Si un objeto pesa 50 N en el aire y al sumergirlo en agua pesa 35 N en el dinamómetro, ¿cuál es el empuje que recibe?',
        '15 N', ['85 N', '50 N', '35 N'],
        'Peso aparente = Peso real - Empuje ⇒ Empuje = Peso real - Peso aparente = 50 - 35 = 15 N.', 'E = 50 - 35 = 15 N.', 'basic', 1120
    ))
    q.append(make_mc(
        'En vasos comunicantes con un mismo líquido en reposo, las alturas de líquido en cada columna:',
        'Son exactamente iguales independientemente de la forma y ancho de los tubos',
        ['Son mayores en los tubos más anchos', 'Son mayores en los tubos inclinados', 'Son inversas al radio'],
        'La presión en el fondo solo depende de la profundidad vertical h: P = ρgh. Por ello las superficies libres quedan al mismo nivel.', 'Mismo nivel h.', 'basic', 1110
    ))
    q.append(make_mc(
        'Un tubo en U contiene agua (1000 kg/m³) y aceite inmiscible. Si la columna de aceite mide 10.0 cm y equilibra una columna de agua de 8.0 cm, ¿cuál es la densidad del aceite?',
        '800 kg/m³', ['1250 kg/m³', '900 kg/m³', '80 kg/m³'],
        'P_aceite = P_agua ⇒ ρ_aceite * g * h_aceite = ρ_agua * g * h_agua ⇒ ρ_aceite = 1000 * (8.0 / 10.0) = 800 kg/m³.', 'ρ = 1000 * 8 / 10 = 800 kg/m³.', 'intermediate', 1220
    ))
    q.append(make_mc(
        'La paradoja hidrostática de Stevin demuestra que la fuerza ejercida por un líquido sobre el fondo plano de un recipiente:',
        'Depende únicamente del área de la base y de la altura de la columna de líquido, no del peso total de líquido contenido',
        ['Es siempre igual al peso total del líquido', 'Depende de la inclinación de las paredes', 'Es nula'],
        'F = P * A = (ρ * g * h) * A, independientemente de si el recipiente se ensancha o angosta arriba.', 'F = ρ*g*h*A.', 'intermediate', 1230
    ))
    q.append(make_mc(
        'Un submarino desciende en agua de mar (ρ = 1030 kg/m³) a 100 m de profundidad. ¿Cuál es la presión manométrica (hidrostática)? (g = 9.8 m/s²).',
        '1.01 × 10⁶ Pa (≈ 10 atm)', ['1.03 × 10⁵ Pa', '1.01 × 10⁷ Pa', '9.8 × 10⁴ Pa'],
        'P = ρ * g * h = 1030 * 9.8 * 100 = 1009400 Pa ≈ 1.01 × 10⁶ Pa.', 'P = 1030 * 9.8 * 100 ≈ 1.01 MPa.', 'intermediate', 1190
    ))
    q.append(make_mc(
        'Un cuerpo de masa 0.5 kg y volumen 0.0004 m³ se sumerge en agua (ρ = 1000 kg/m³). ¿Flota o se hunde?',
        'Se hunde (densidad del cuerpo = 1250 kg/m³ > 1000 kg/m³)', ['Flota con la mitad sumergida', 'Flota neutro', 'Asciende con aceleración'],
        'ρ_cuerpo = m / V = 0.5 kg / 0.0004 m³ = 1250 kg/m³. Como supera a la del agua, su peso supera al empuje máximo y se hunde.', 'ρ = 0.5 / 0.0004 = 1250 kg/m³ > 1000 ⇒ se hunde.', 'basic', 1140
    ))
    q.append(make_mc(
        'La ecuación de continuidad para un fluido incompresible en régimen estacionario establece que:',
        'El caudal volumétrico Q = A · v es constante a lo largo de la tubería',
        ['La presión se mantiene constante', 'La velocidad es igual en tubos anchos y estrechos', 'La viscosidad es infinita'],
        'Conservación de masa: A1 · v1 = A2 · v2 = constante. En secciones estrechas el fluido aumenta su velocidad.', 'A1 v1 = A2 v2 = Q.', 'intermediate', 1210
    ))
    q.append(make_mc(
        'Por una manguera de sección A = 4 cm² fluye agua a 2.0 m/s. Al colocar el dedo reduciendo la salida a 1 cm², ¿cuál es la rapidez de salida?',
        '8.0 m/s', ['4.0 m/s', '0.5 m/s', '16.0 m/s'],
        'A1 * v1 = A2 * v2 ⇒ 4 cm² * 2.0 m/s = 1 cm² * v2 ⇒ v2 = 8.0 m/s.', 'v2 = (4 * 2) / 1 = 8.0 m/s.', 'intermediate', 1200
    ))
    q.append(make_mc(
        'El efecto Venturi derivado del Teorema de Bernoulli establece que cuando un fluido aumenta su velocidad al pasar por un estrechamiento:',
        'Su presión estática disminuye', ['Su presión aumenta', 'Su temperatura se eleva al doble', 'Su densidad se duplica'],
        'Por conservación de energía (Bernoulli): P + ½ ρ v² = cte. Al aumentar v, la presión P debe reducirse obligatoriamente.', 'Mayor v ⇒ menor P.', 'intermediate', 1220
    ))
    q.append(make_mc(
        'El instrumento utilizado para medir la presión atmosférica se denomina:',
        'Barómetro (inventado por Torricelli)', ['Manómetro', 'Termómetro', 'Densímetro'],
        'El barómetro mide la presión del aire ambiente (columna de mercurio de Torricelli). El manómetro mide presión relativa en recintos cerrados.', 'Barómetro.', 'basic', 1100
    ))
    q.append(make_mc(
        '¿Por qué una aguja de acero (ρ = 7800 kg/m³) puede flotar horizontalmente sobre la superficie del agua si se coloca con cuidado?',
        'Por la tensión superficial del agua que actúa como una membrana elástica',
        ['Por el empuje de Arquímedes', 'Porque el acero flota naturalmente', 'Por la presión atmosférica'],
        'Las fuerzas intermoleculares de cohesión en la superficie libre generan tensión superficial capaz de sostener pequeños objetos densos.', 'Tensión superficial.', 'intermediate', 1190
    ))
    q.append(make_mc(
        'Un neumático marca 30 psi en el manómetro. Si la presión atmosférica es 14.7 psi, ¿cuál es la presión absoluta dentro del neumático?',
        '44.7 psi', ['30.0 psi', '15.3 psi', '60.0 psi'],
        'P_absoluta = P_manométrica + P_atmosférica = 30 + 14.7 = 44.7 psi.', 'P_abs = 30 + 14.7 = 44.7 psi.', 'basic', 1130
    ))
    q.append(make_mc(
        'Un globo aerostático de volumen V = 500 m³ se llena con helio (ρ = 0.18 kg/m³) en aire (ρ_aire = 1.20 kg/m³). ¿Cuál es la fuerza de empuje que recibe? (g = 9.8 m/s²).',
        '5880 N', ['882 N', '5000 N', '4900 N'],
        'E = ρ_aire * V * g = 1.20 kg/m³ * 500 m³ * 9.8 m/s² = 5880 N.', 'E = 1.20 * 500 * 9.8 = 5880 N.', 'intermediate', 1230
    ))
    q.append(make_mc(
        'El principio de Arquímedes NO se cumple en:',
        'Un entorno con gravedad cero (en caída libre o ingravidez pura)',
        ['En el fondo del mar', 'En líquidos viscosos', 'En el mercurio'],
        'El empuje requiere peso del fluido desplazado (E = ρ V g). Si g = 0, el empuje se anula por completo.', 'g = 0 ⇒ Empuje = 0.', 'advanced', 1280
    ))
    q.append(make_mc(
        'Un densímetro flota en un líquido A sumergiéndose más que en un líquido B. ¿Qué podemos concluir de las densidades?',
        'El líquido B es más denso que el líquido A (ρB > ρA)', ['El líquido A es más denso', 'Tienen igual densidad', 'El densímetro pesa más en B'],
        'V_sum = m_aparato / ρ_líquido. A mayor densidad del líquido, menor volumen sumergido se requiere para flotar.', 'Mayor inmersión ⇒ menor densidad del fluido.', 'intermediate', 1210
    ))
    return q
