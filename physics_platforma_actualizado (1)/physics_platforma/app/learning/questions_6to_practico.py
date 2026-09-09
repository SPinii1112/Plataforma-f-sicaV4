# -*- coding: utf-8 -*-
from app.learning.question_helper import make_mc

def get_tester_questions():
    q = []
    q.append(make_mc(
        'Al medir la tensión continua (V DC) en los bornes de una batería de 9 V con un multímetro digital, ¿cómo deben colocarse las puntas de prueba?',
        'En PARALELO con la batería (punta roja en borne V/Ω y punta negra en borne COM)',
        ['En SERIE abriendo el circuito', 'Punta roja en borne 10A y negra en COM en serie', 'Ambas puntas en el borne positivo'],
        'El voltímetro tiene altísima impedancia de entrada (> 10 MΩ) y se conecta siempre en paralelo con el componente a contrastar.', 'Voltímetro en paralelo.', 'basic', 1100
    ))
    q.append(make_mc(
        '¿Cuál es la consecuencia directa de conectar accidentalmente las puntas del tester en PARALELO con una batería teniendo la clavija roja en el borne de corriente de 10A?',
        'Se produce un CORTOCIRCUITO severo porque el amperímetro tiene resistencia interna prácticamente nula (< 0.05 Ω), pudiendo fundir fusibles o provocar chispas',
        ['El tester mide el voltaje normalmente', 'No ocurre nada', 'Se mide la resistencia de la batería'],
        'El amperímetro está diseñado para conectarse en serie abriendo el circuito. En paralelo actúa como un cable directo cortocircuitando la fuente.', 'Cortocircuito severo.', 'basic', 1110
    ))
    q.append(make_mc(
        'Al medir la resistencia de un resistor individual con el óhmetro del multímetro:',
        'El circuito o componente debe estar TOTALMENTE DESENERGIZADO (apagado sin tensión externa)',
        ['El circuito debe estar conectado a 220 V', 'Se debe aplicar corriente máxima', 'La batería debe estar encendida'],
        'El óhmetro inyecta una corriente de prueba generada por su propia pila interna. Si hay tensión externa se falsea la medición y se daña el instrumento.', 'Medir resistencia sin tensión.', 'basic', 1100
    ))
    q.append(make_mc(
        'Si en la pantalla LCD del multímetro en escala de resistencia o tensión aparece el símbolo "OL" o "1 .", esto significa:',
        'Over Load (Sobrecarga / Fuera de rango): el valor medido supera la escala seleccionada o el circuito está abierto (resistencia infinita)',
        ['Batería baja', 'Cortocircuito total (cero Ohmios)', 'Error de software del microprocesador', 'Corriente alterna detectada'],
        'OL indica que la magnitud excede el fondo de escala del conversor analógico-digital.', 'OL = Over Load (fuera de escala).', 'basic', 1120
    ))
    q.append(make_mc(
        'Para medir la corriente eléctrica que circula por una lámpara con el multímetro en función amperímetro, es OBLIGATORIO:',
        'Abrir el circuito físico e intercalar el tester en SERIE para que toda la corriente fluya a través de él',
        ['Conectar las puntas en paralelo con la bombilla', 'Poner una punta en la pared y otra en la mesa', 'Medir sin tocar los cables'],
        'Para medir el flujo de portadores, el instrumento debe formar parte de la trayectoria de corriente en serie.', 'Amperímetro en serie.', 'basic', 1110
    ))
    q.append(make_mc(
        'El borne marcado como "COM" en un multímetro corresponde a:',
        'El terminal Común o referencia de masa (negativo), donde se conecta siempre la punta de prueba NEGRA',
        ['La entrada de corriente de 10 Amperios', 'La conexión de alta tensión', 'La salida de audio'],
        'COM = Common. Es el punto de referencia común de masa para todas las mediciones.', 'COM = Común (punta negra).', 'basic', 1100
    ))
    q.append(make_mc(
        '¿Por qué el voltímetro de un multímetro digital moderno tiene una resistencia interna extremadamente elevada (típicamente > 10 MΩ)?',
        'Para minimizar el "efecto de carga", asegurando que drene una corriente despreciable y no altere las tensiones originales del circuito',
        ['Para evitar que el usuario reciba choques eléctricos', 'Para aumentar la velocidad de lectura', 'Para medir temperaturas'],
        'Un voltímetro ideal debe tener resistencia infinita para no perturbar el circuito que mide.', 'Alta impedancia evita perturbaciones.', 'intermediate', 1210
    ))
    q.append(make_mc(
        'La función de prueba de diodos del multímetro inyecta una pequeña corriente continua constante y muestra en el display:',
        'La caída de tensión directa en polarización directa en milivoltios (≈ 0.6 V - 0.7 V para silicio; ≈ 0.2 V - 0.3 V para germanio)',
        ['La resistencia de aislamiento', 'La capacidad en picofaradios', 'La temperatura de la juntura'],
        'Indica el umbral de conducción de la juntura p-n polarizada en directa.', 'Caída directa Vf del diodo.', 'intermediate', 1230
    ))
    q.append(make_mc(
        'La función de zumbador o comprobador acústico de continuidad emite un pitido audible cuando:',
        'La resistencia entre ambas puntas de prueba es muy baja (típicamente inferior a 30 Ω - 50 Ω), indicando camino cerrado continuo',
        ['El circuito tiene más de 1000 Ω', 'Se detectan ondas de radio', 'El cable está cortado'],
        'Permite comprobar cableados, pistas de circuito impreso y contactos cerrados de forma rápida sin mirar la pantalla.', 'Continuidad: R < 50 Ω emite sonido.', 'basic', 1120
    ))
    q.append(make_mc(
        'Si se desea medir una tensión desconocida con un multímetro analógico o de rango manual, la regla de seguridad estándar indica que se debe:',
        'Comenzar siempre seleccionando la escala de voltaje MÁS ALTA posible y luego descender progresivamente hasta optimizar la resolución',
        ['Empezar por la escala de menor voltaje (milivoltios)', 'Elegir la escala del medio al azar', 'Poner la escala en amperios'],
        'Empezar por la escala más alta previene sobretensiones que puedan dañar el galvanómetro o circuito de entrada.', 'Comenzar por la escala más alta.', 'basic', 1130
    ))
    q.append(make_mc(
        'Un multímetro "True RMS" (Valor Eficaz Verdadero) es necesario cuando se miden tensiones o corrientes alternas que:',
        'Tienen formas de onda no sinusoidales puras (como ondas cuadradas, triangulares o con armónicos de distorsión)',
        ['Son de corriente continua', 'Tienen frecuencias menores a 1 Hz', 'Son de más de 1000 Amperios'],
        'Los testers básicos calculan el promedio rectificado asumiendo senos puros y cometen errores graves (> 40%) con ondas distorsionadas.', 'True RMS mide cualquier forma de onda periódica.', 'intermediate', 1240
    ))
    q.append(make_mc(
        'El fusible interno que protege el borne "mA / μA" de un tester típico suele tener una capacidad de corte de:',
        '200 mA a 500 mA (0.5 A) de acción rápida', ['10 A', '100 A', '50 A'],
        'El borne de corrientes bajas tiene un fusible cerámico rápido de 200 a 500 mA para proteger el shunt delicado.', 'Fusible rápido 200-500 mA.', 'basic', 1140
    ))
    q.append(make_mc(
        'Al medir el voltaje de un tomacorriente hogareño de 220 V de corriente alterna, el selector del tester debe situarse en:',
        'V~ (ACV - Tensión Alterna) en escala superior a 220 V (ej. 600 V o 750 V)',
        ['V= (DCV - Continua) en 20 V', 'A~ (Amperios alternos)', 'Ω (Ohmios)'],
        'El tomacorriente domiciliario es tensión alterna y requiere modo ACV con rango mayor al valor pico (> 311 V).', 'ACV > 220 V.', 'basic', 1100
    ))
    q.append(make_mc(
        'Si se mide el voltaje de una pila de 1.5 V invirtiendo las puntas (punta roja en el negativo y negra en el positivo), el display digital mostrará:',
        '-1.5 V (el valor correcto con signo negativo)', ['0 V', 'OL', 'El tester se rompe'],
        'Los multímetros digitales modernos tienen convertidores bipolares y detectan automáticamente la polaridad mostrando el signo "-".', 'Display muestra -1.5 V.', 'basic', 1110
    ))
    q.append(make_mc(
        'La categoría de seguridad de un tester (ej. CAT III 600 V, CAT IV 1000 V) especifica:',
        'Su capacidad para resistir transitorios de sobretensión e impulsos de picos de energía destructivos sin generar arcos eléctricos peligrosos para el operador',
        ['La precisión del display', 'El tamaño de la batería interna', 'El peso del instrumento'],
        'Norma IEC 61010 sobre seguridad eléctrica en instalaciones industriales y de distribución.', 'Categoría CAT contra picos transitorios.', 'intermediate', 1220
    ))
    q.append(make_mc(
        'Al comprobar un condensador electrolítico con la función de óhmetro analógico, la aguja debe:',
        'Deflactar rápidamente hacia baja resistencia (carga inicial) y luego retornar lentamente hacia resistencia muy alta (aislamiento del dieléctrico)',
        ['Quedarse fija en cero', 'No moverse nunca', 'Vibrar continuamente'],
        'El flujo transitorio de corriente de carga de la pila interna produce una deflexión temporal característica.', 'Deflexión y retorno por carga.', 'intermediate', 1230
    ))
    q.append(make_mc(
        'Un multímetro con resolución de "3 ½ dígitos" puede mostrar un valor numérico máximo en su pantalla de:',
        '1999 (el medio dígito es un "1" inicial o apagado)', ['9999', '3500', '999'],
        'Convenio industrial: el dígito "½" solo puede valer 0 ó 1, permitiendo cuentas de -1999 a +1999.', '3 ½ dígitos = hasta 1999 cuentas.', 'intermediate', 1250
    ))
    q.append(make_mc(
        'Si un amperímetro ideal tiene resistencia interna cero (R_int = 0), un voltímetro ideal debe tener resistencia interna:',
        'Infinita (R_int = ∞)', ['Cero', '100 Ω', '1 Ω'],
        'R_int = ∞ asegura que el voltímetro no robe corriente a la rama en paralelo.', 'R_voltímetro ideal = ∞.', 'basic', 1100
    ))
    q.append(make_mc(
        'Antes de guardar un multímetro digital que no se utilizará durante varios meses, la mejor práctica de mantenimiento es:',
        'Apagar el selector rotativo en OFF y retirar la batería interna de 9 V para prevenir derrames de electrolito corrosivo',
        ['Dejarlo en modo de resistencia máxima', 'Dejar las puntas cortocircuitadas', 'Guardarlo en el congelador'],
        'Las pilas sulfatadas por degradación química destruyen irreversiblemente las pistas del circuito impreso.', 'Apagar y retirar pila.', 'basic', 1100
    ))
    q.append(make_mc(
        'La pinza amperimétrica es una variante de multímetro que permite medir corrientes alternas intensas:',
        'Abrazando un solo conductor sin necesidad de cortar ni abrir físicamente el circuito (por inducción magnética del núcleo toroidal)',
        ['Abrazando el cable de fase y neutro juntos al mismo tiempo', 'Midiendo la tensión del aire', 'Conectándose en paralelo'],
        'Detecta el campo magnético alterno generado por la corriente del cable central sin interrupción física.', 'Pinza amperimétrica por inducción.', 'intermediate', 1200
    ))
    return q

def get_capacitores_questions():
    q = []
    q.append(make_mc(
        'Un capacitor de C = 100 μF se conecta en serie con una resistencia R = 10 kΩ (10000 Ω) a una fuente continua V0 = 12 V. ¿Cuánto vale la constante de tiempo τ del circuito RC?',
        '1.0 segundo', ['10.0 segundos', '0.10 segundos', '100 segundos'],
        'τ = R * C = 10000 Ω * (100 × 10⁻⁶ F) = 1.0 s.', 'τ = 10000 * 10⁻⁴ = 1.0 s.', 'basic', 1100
    ))
    q.append(make_mc(
        'En el circuito RC anterior, al cabo de un tiempo transcurrido exactamente igual a una constante de tiempo (t = 1 τ = 1.0 s desde el inicio de la carga), ¿qué porcentaje de la tensión final V0 ha alcanzado el capacitor?',
        '63.2% de V0 (aproximadamente 7.58 V)', ['50.0%', '86.5%', '99.3%'],
        'VC(t) = V0 · (1 - e^(-t/τ)). Para t = τ: VC(τ) = V0 · (1 - e⁻¹) = V0 · (1 - 0.3679) = 0.6321 · V0 = 63.2%.', '1 - e⁻¹ ≈ 0.632 = 63.2%.', 'basic', 1120
    ))
    q.append(make_mc(
        'Durante el proceso de DESCARGA de un capacitor a través de una resistencia R desde una tensión inicial V0, al transcurrir t = 1 τ la tensión remanente es:',
        '36.8% de V0 (e⁻¹ · V0)', ['50.0%', '63.2%', '0%'],
        'VC_descarga(t) = V0 · e^(-t/τ). Para t = τ: VC(τ) = V0 · e⁻¹ ≈ 0.3679 · V0 = 36.8%.', 'e⁻¹ ≈ 0.368 = 36.8%.', 'basic', 1130
    ))
    q.append(make_mc(
        'Se considera que un capacitor alcanza su estado estacionario de CARGA COMPLETA (prácticamente el 99.3% de su tensión final) tras un tiempo de:',
        '5 τ (cinco constantes de tiempo)', ['1 τ', '2 τ', '10 τ'],
        '1 - e⁻⁵ = 1 - 0.0067 = 0.9933 = 99.3%. En ingeniería se asume régimen permanente a partir de 5τ.', 'Régimen estacionario en t ≥ 5τ.', 'basic', 1110
    ))
    q.append(make_mc(
        'En el instante inicial t = 0 s de la conexión de un circuito RC desenergizado frente a una fuente de tensión continua V0, el capacitor se comporta físicamente como:',
        'Un cortocircuito (resistencia nula aparente, tensión VC = 0 y corriente inicial máxima I_máx = V0 / R)',
        ['Un circuito abierto (corriente cero)', 'Una resistencia de 1 MΩ', 'Una fuente de fem'],
        'Como VC(0) = 0, toda la tensión de la fuente cae inicialmente en la resistencia R, produciendo la corriente de pico máxima I0 = V0 / R.', 'En t=0, capacitor descargado = cortocircuito.', 'intermediate', 1210
    ))
    q.append(make_mc(
        'Una vez que el capacitor se carga por completo (t ≥ 5τ) en un circuito de corriente continua (DC), su comportamiento en el circuito equivale a:',
        'Un circuito abierto (bloquea totalmente la corriente continua, I = 0 A)',
        ['Un cortocircuito', 'Un resistor de valor R', 'Un fusible fundido'],
        'Al alcanzar VC = V0, el potencial del capacitor equilibra al de la fuente; la diferencia de potencial sobre R se anula y la corriente cesa.', 'En régimen DC estacionario, capacitor cargado = circuito abierto.', 'basic', 1120
    ))
    q.append(make_mc(
        '¿Cuánta energía electrostática almacena un capacitor de C = 470 μF cargado a una tensión V = 20 V?',
        '0.094 J (94 mJ)', ['9.4 J', '0.188 J', '0.0047 J'],
        'U = ½ C V² = 0.5 * (470 × 10⁻⁶ F) * (20 V)² = 0.5 * 470x10⁻⁶ * 400 = 200 * 470x10⁻⁶ = 0.094 J.', 'U = 0.5 * 470x10⁻⁶ * 400 = 0.094 J.', 'basic', 1130
    ))
    q.append(make_mc(
        'Dos capacitores de 20 μF y 20 μF se conectan en PARALELO. La capacidad equivalente del conjunto es:',
        '40 μF (en paralelo las capacidades se suman)', ['10 μF', '20 μF', '5 μF'],
        'En paralelo las placas aumentan el área efectiva total: C_eq = C1 + C2 = 20 + 20 = 40 μF.', 'C_paralelo = C1 + C2 = 40 μF.', 'basic', 1100
    ))
    q.append(make_mc(
        'Dos capacitores de 20 μF y 20 μF se conectan en SERIE. La capacidad equivalente del conjunto es:',
        '10 μF', ['40 μF', '20 μF', '5 μF'],
        'En serie: 1/C_eq = 1/C1 + 1/C2 ⇒ C_eq = (20 * 20) / (20 + 20) = 400 / 40 = 10 μF.', 'C_serie = (C1*C2)/(C1+C2) = 10 μF.', 'basic', 1110
    ))
    q.append(make_mc(
        'Si un capacitor cargado a 300 V se desconecta de la fuente y se mantiene aislado en un estante de laboratorio, ¿por qué representa un riesgo severo de descarga eléctrica incluso días después?',
        'Porque el dieléctrico posee una resistencia de fuga muy elevada y mantiene la carga electrostática acumulada durante mucho tiempo si no se drena externamente',
        ['Porque absorbe energía del aire ambiente', 'Porque genera radiación nuclear', 'Porque la gravedad lo carga'],
        'Los capacitores electrolíticos de alta tensión retienen voltajes letales por semanas; deben descargarse con una resistencia de seguridad antes de manipularlos.', 'Mantenimiento de carga por alta resistencia de aislamiento.', 'intermediate', 1200
    ))
    q.append(make_mc(
        'El método seguro de laboratorio para descargar un capacitor de alta tensión consiste en:',
        'Conectar entre sus bornes una resistencia de potencia (bleeder resistor) de valor adecuado (ej. 1 kΩ a 10 kΩ de varios Watts) y verificar con el voltímetro que V < 1 V',
        ['Hacer un puente directo con un destornillador metálico produciendo chispas', 'Tocar ambos terminales con las manos desnudas', 'Sumergirlo en agua'],
        'Cortocircuitar directamente daña las placas internas por corriente destructiva y puede proyectar esquirlas de metal.', 'Descarga controlada con resistencia de drenaje.', 'intermediate', 1190
    ))
    q.append(make_mc(
        'Si se inserta una lámina de material dieléctrico (constante κ = 4) llenando todo el espacio entre las placas de un capacitor aislado con carga Q fija:',
        'La capacidad se multiplica por 4 (4C) y la diferencia de potencial se reduce a la cuarta parte (V / 4)',
        ['La capacidad disminuye a C/4', 'La tensión se cuadruplica', 'La carga se multiplica por 4'],
        'C_nueva = κ · C0 = 4C. Como Q es fija: V = Q / C_nueva = Q / (4C) = V0 / 4.', 'C aumenta x κ; V decae / κ.', 'intermediate', 1230
    ))
    q.append(make_mc(
        'La capacidad de un condensador de placas plano-paralelas de área A y separación d con vacío entre ellas es:',
        'C = ε0 · (A / d)', ['C = ε0 · (d / A)', 'C = ε0 · A · d', 'C = A / (ε0 d)'],
        'Fórmula geométrica fundamental: la capacitancia crece con el área A y decae con la distancia d entre placas.', 'C = ε0 A / d.', 'basic', 1110
    ))
    q.append(make_mc(
        'Un capacitor electrolítico se diferencia de uno cerámico principalmente porque:',
        'Posee polaridad obligatoria (borne positivo y negativo marcados) y ofrece altísima capacidad en volumen reducido',
        ['No puede cargarse con corriente continua', 'Tiene capacidad fija de 1 pF', 'Es superconductor'],
        'Los electrolíticos usan una delgadísima capa de óxido de aluminio como dieléctrico polarizado; conectarlos al revés provoca sobrecalentamiento y explosión.', 'Capacitor electrolítico polarizado.', 'basic', 1120
    ))
    q.append(make_mc(
        'En un circuito de temporización RC se necesita un retardo de τ = 5.0 segundos. Si se utiliza un capacitor C = 50 μF, ¿qué valor de resistencia R se debe emplear?',
        '100 kΩ (100000 Ω)', ['10 kΩ', '250 kΩ', '500 kΩ'],
        'R = τ / C = 5.0 s / (50 × 10⁻⁶ F) = 5.0 / (5x10⁻⁵) = 100000 Ω = 100 kΩ.', 'R = 5 / 50x10⁻⁶ = 100 kΩ.', 'intermediate', 1220
    ))
    q.append(make_mc(
        'El fenómeno de "absorción dieléctrica" (o efecto de memoria) en capacitores de gran tamaño hace que:',
        'Tras descargarlos brevemente a cero y dejarlos en circuito abierto, recuperen espontáneamente una fracción de su tensión original por relajación de dipolos en el dieléctrico',
        ['La capacidad aumente cada día', 'Se descarguen más rápido', 'Cambien de color'],
        'Por seguridad en laboratorios de alta potencia se colocan puentes cortocircuitadores permanentes durante el almacenamiento.', 'Absorción dieléctrica recupera voltaje residual.', 'advanced', 1290
    ))
    q.append(make_mc(
        'La corriente que atraviesa un capacitor ideal en cualquier instante viene dada por la relación diferencial:',
        'i(t) = C · (dv / dt)', ['i(t) = v(t) / C', 'i(t) = C · ∫ v dt', 'i(t) = C · v(t)'],
        'Como q(t) = C · v(t), derivando respecto al tiempo: i(t) = dq/dt = C · (dv/dt).', 'i = C (dv/dt).', 'intermediate', 1230
    ))
    q.append(make_mc(
        'La máxima tensión de trabajo especificada en el cuerpo de un capacitor (ej. "470 μF / 25 V") indica:',
        'La tensión continua máxima de seguridad que el dieléctrico soporta de forma continua sin sufrir perforación por ruptura dieléctrica',
        ['La tensión a la que siempre debe funcionar obligatoriamente', 'El voltaje de la batería', 'La tolerancia'],
        'Superar la tensión nominal perfora el dieléctrico destruyendo el componente en cortocircuito irreversible.', 'Voltaje máximo antes de perforación.', 'basic', 1130
    ))
    q.append(make_mc(
        'Al transcurrir t = 2 τ en el proceso de carga de un circuito RC, la tensión en el capacitor alcanza aproximadamente:',
        '86.5% de V0', ['63.2%', '95.0%', '75.0%'],
        'VC(2τ) = V0 · (1 - e⁻²) = V0 · (1 - 0.1353) = 0.8647 · V0 ≈ 86.5%.', '1 - e⁻² ≈ 0.865 = 86.5%.', 'intermediate', 1210
    ))
    q.append(make_mc(
        'Un capacitor de 1 Faradio es una unidad gigantesca que a 10 V de tensión almacena una carga electrostática de:',
        '10 Coulombs (equivalente a 6.24 × 10¹⁹ electrones)', ['1 Coulomb', '100 Coulombs', '0.1 Coulomb'],
        'Q = C * V = 1 F * 10 V = 10 C.', 'Q = 1 * 10 = 10 C.', 'basic', 1110
    ))
    return q

def get_resistencias_questions():
    q = []
    q.append(make_mc(
        'Una resistencia de 4 bandas tiene los siguientes colores: Marrón, Negro, Rojo y Dorado. ¿Cuál es su valor nominal y tolerancia?',
        '1000 Ω (1 kΩ) ± 5%', ['100 Ω ± 10%', '10 kΩ ± 5%', '120 Ω ± 5%'],
        'Banda 1 (Marrón = 1), Banda 2 (Negro = 0) ⇒ Cifra = 10. Banda 3 (Rojo = multiplicador 10² = 100). Valor = 10 * 100 = 1000 Ω = 1 kΩ. Banda 4 (Dorado = tolerancia ± 5%).', '1-0-x100 ± 5% = 1 kΩ ± 5%.', 'basic', 1100
    ))
    q.append(make_mc(
        '¿Cuál es el rango de valores válidos en Ohmios para la resistencia anterior de 1 kΩ ± 5% al contrastarla con un óhmetro?',
        'De 950 Ω a 1050 Ω', ['De 900 Ω a 1100 Ω', 'De 995 Ω a 1005 Ω', 'Exactamente 1000 Ω sin variación'],
        'El 5% de 1000 Ω es 50 Ω. Rango admisible = 1000 ± 50 Ω = [950 Ω, 1050 Ω].', '1000 ± 50 = [950, 1050] Ω.', 'basic', 1110
    ))
    q.append(make_mc(
        'Una resistencia tiene bandas: Amarillo, Violeta, Naranja y Dorado. ¿Cuál es su valor?',
        '47 kΩ (47000 Ω) ± 5%', ['4.7 kΩ ± 5%', '470 Ω ± 5%', '37 kΩ ± 10%'],
        'Amarillo = 4, Violeta = 7 ⇒ Cifra 47. Naranja = multiplicador 10³ (x 1000). Valor = 47 * 1000 = 47000 Ω = 47 kΩ ± 5%.', '4-7-x1000 = 47 kΩ.', 'basic', 1110
    ))
    q.append(make_mc(
        'Una resistencia de precisión de 5 bandas tiene los colores: Rojo, Rojo, Negro, Negro y Marrón. ¿Cuál es su valor?',
        '220 Ω ± 1%', ['22 Ω ± 1%', '2.2 kΩ ± 2%', '2200 Ω ± 5%'],
        'En 5 bandas hay 3 cifras significativas: Rojo (2), Rojo (2), Negro (0) ⇒ 220. Cuarta banda multiplicador Negro (x 10⁰ = 1) ⇒ 220 * 1 = 220 Ω. Quinta banda tolerancia Marrón = ± 1%.', '2-2-0 x 1 ± 1% = 220 Ω ± 1%.', 'intermediate', 1210
    ))
    q.append(make_mc(
        'Una resistencia estándar de carbón de 100 Ω tiene una potencia nominal de 1/4 W (0.25 W). ¿Cuál es la corriente continua máxima segura que puede atravesarla sin sobrecalentarse?',
        '50 mA (0.050 A)', ['2.5 A', '100 mA', '25 mA'],
        'P = I² * R ⇒ I_máx = √(P / R) = √(0.25 W / 100 Ω) = √0.0025 = 0.050 A = 50 mA.', 'I = √(0.25/100) = 0.05 A = 50 mA.', 'intermediate', 1220
    ))
    q.append(make_mc(
        '¿Cuál es la tensión máxima continua admisible sobre la resistencia de 100 Ω y 0.25 W del ejercicio anterior?',
        '5.0 V', ['25.0 V', '10.0 V', '2.5 V'],
        'P = V² / R ⇒ V_máx = √(P * R) = √(0.25 W * 100 Ω) = √25 = 5.0 V (o V = I*R = 0.05A * 100Ω = 5V).', 'V = √(0.25 * 100) = 5.0 V.', 'intermediate', 1210
    ))
    q.append(make_mc(
        'En una prueba de estrés térmico de laboratorio, se somete un resistor de carbón a una potencia 5 veces superior a su valor nominal (P_aplicada ≥ 5 · P_nominal). ¿Cuál es el modo de fallo típico característico?',
        'El recubrimiento cerámico se quema, emite humo y olor a resina carbonizada y la película resistiva se funde, fallando de forma irreversible en CIRCUITO ABIERTO (R → ∞ Ω)',
        ['La resistencia se convierte en un cortocircuito perfecto (0 Ω)', 'El valor de resistencia se reduce a la mitad permanentemente', 'La resistencia no sufre ningún cambio'],
        'La sobrecarga extrema destruye la continuidad de la película resistiva por sublimación térmica, abriendo el circuito.', 'Falla irreversible en circuito abierto (R → ∞).', 'intermediate', 1200
    ))
    q.append(make_mc(
        'Al aplicar una sobrecarga moderada (ej. 2 × P_nominal) a una resistencia sin destruirla, su valor óhmico medido en caliente experimenta una variación transitoria debida a:',
        'El Coeficiente Térmico de Resistencia (TCR), que altera reversiblemente la resistencia mientras el componente está a alta temperatura',
        ['La evaporación de los electrones', 'La pérdida de masa de la cerámica', 'El magnetismo parásito'],
        'Al enfriarse vuelve a su valor nominal original; es una deriva térmica normal cuantificada por el TCR en ppm/°C.', 'Deriva térmica por TCR.', 'intermediate', 1220
    ))
    q.append(make_mc(
        'El color de la banda multiplicadora para multiplicar por 0.1 (10⁻¹) en resistencias de bajo valor (ej. 2.2 Ω) es:',
        'Dorado', ['Plateado', 'Negro', 'Marrón'],
        'Dorado en la 3.ª banda multiplica por 0.1 (Rojo-Rojo-Dorado = 2-2-x0.1 = 2.2 Ω). Plateado multiplica por 0.01.', 'Dorado = x 0.1.', 'basic', 1130
    ))
    q.append(make_mc(
        'El color de la banda multiplicadora para multiplicar por 0.01 (10⁻²) es:',
        'Plateado', ['Dorado', 'Negro', 'Gris'],
        'Plateado como multiplicador equivale a 10⁻² (ej. Verde-Azul-Plateado = 5-6-x0.01 = 0.56 Ω).', 'Plateado = x 0.01.', 'basic', 1130
    ))
    q.append(make_mc(
        '¿Cuáles son los colores correspondientes a una resistencia de 330 Ω con 5% de tolerancia en 4 bandas?',
        'Naranja, Naranja, Marrón, Dorado', ['Naranja, Naranja, Rojo, Dorado', 'Rojo, Rojo, Marrón, Plateado', 'Marrón, Negro, Naranja, Dorado'],
        'Naranja (3), Naranja (3) ⇒ 33. Marrón (x 10¹ = 10) ⇒ 33 * 10 = 330 Ω. Dorado (± 5%).', '3-3-x10 ±5% = Naranja-Naranja-Marrón-Dorado.', 'basic', 1120
    ))
    q.append(make_mc(
        '¿Cuáles son los colores para una resistencia de 10 kΩ (10000 Ω) con 5% de tolerancia?',
        'Marrón, Negro, Naranja, Dorado', ['Marrón, Negro, Rojo, Dorado', 'Marrón, Negro, Amarillo, Dorado', 'Rojo, Negro, Naranja, Plateado'],
        'Marrón (1), Negro (0) ⇒ 10. Naranja (x 10³ = 1000) ⇒ 10 * 1000 = 10000 Ω = 10 kΩ. Dorado (± 5%).', '1-0-x1000 = Marrón-Negro-Naranja-Dorado.', 'basic', 1120
    ))
    q.append(make_mc(
        '¿Cuáles son los colores para una resistencia de 470 kΩ (470000 Ω) con 5% de tolerancia?',
        'Amarillo, Violeta, Amarillo, Dorado', ['Amarillo, Violeta, Naranja, Dorado', 'Verde, Azul, Amarillo, Dorado', 'Amarillo, Violeta, Verde, Plateado'],
        'Amarillo (4), Violeta (7) ⇒ 47. Amarillo (x 10⁴ = 10000) ⇒ 47 * 10000 = 470000 Ω = 470 kΩ.', '4-7-x10000 = Amarillo-Violeta-Amarillo-Dorado.', 'basic', 1130
    ))
    q.append(make_mc(
        'Las resistencias cerámicas cementadas de gran tamaño (resistencias de alambre bobinado) se utilizan en circuitos cuando:',
        'Se requiere disipar potencias elevadas (5 W, 10 W, 25 W o más) con excelente resistencia a altas temperaturas',
        ['Se necesitan valores de más de 100 Megaohmios', 'Para circuitos integrados de teléfonos móviles', 'Solo para alta frecuencia'],
        'El encapsulado cerámico ignífugo disipa eficientemente grandes cantidades de calor por convección y radiación.', 'Alta disipación de potencia (5W - 25W).', 'basic', 1120
    ))
    q.append(make_mc(
        'Una resistencia SMD (montaje superficial) lleva impreso el código numérico "103". ¿Cuál es su valor óhmico?',
        '10 kΩ (10000 Ω)', ['103 Ω', '1.03 kΩ', '100 kΩ'],
        'Código EIA de 3 dígitos: dos primeras cifras (10) y la tercera es el número de ceros (3 ceros) ⇒ 10000 Ω = 10 kΩ.', '10 + 3 ceros = 10000 Ω = 10 kΩ.', 'intermediate', 1210
    ))
    q.append(make_mc(
        'Una resistencia SMD con código "472" tiene un valor de:',
        '4.7 kΩ (4700 Ω)', ['472 Ω', '47 kΩ', '47.2 Ω'],
        '47 seguido de 2 ceros = 4700 Ω = 4.7 kΩ.', '47 + 2 ceros = 4.7 kΩ.', 'intermediate', 1210
    ))
    q.append(make_mc(
        'Una resistencia SMD con código "R22" o "0R22" indica un valor de:',
        '0.22 Ω (la letra "R" actúa como coma decimal)', ['22 Ω', '220 Ω', '2.2 Ω'],
        'La letra R reemplaza el punto decimal: R22 = 0.22 Ω; 4R7 = 4.7 Ω.', 'R = punto decimal ⇒ R22 = 0.22 Ω.', 'intermediate', 1220
    ))
    q.append(make_mc(
        'La serie normalizada E12 de resistencias estándar al 10% incluye 12 valores base por década: 10, 12, 15, 18, 22, 27, 33, 39, 47, 56, 68 y 82. Esta distribución geométrica asegura que:',
        'Los intervalos de tolerancia de valores consecutivos se solapen ligeramente sin dejar huecos de cobertura de valores comerciales',
        ['Todas las resistencias cuesten lo mismo', 'Sean divisibles entre 2', 'Tengan igual potencia'],
        'Distribución logarítmica de la norma internacional IEC 60063.', 'Cobertura continua de tolerancias.', 'intermediate', 1240
    ))
    q.append(make_mc(
        'La "curva de derating" de potencia de una resistencia especifica cómo:',
        'Se debe reducir la potencia máxima admisible de trabajo a medida que la temperatura ambiente de operación supera los 70 °C para evitar averías',
        ['Aumenta la resistencia con la humedad', 'Varía el voltaje con el tiempo', 'Se enfría el componente'],
        'A mayor temperatura ambiente, el componente tiene menor margen de disipación antes de alcanzar su temperatura máxima interna de unión (155 °C).', 'Derating térmico de potencia.', 'advanced', 1280
    ))
    q.append(make_mc(
        '¿Cuál es el valor y tolerancia de una resistencia con bandas: Gris, Rojo, Negro y Plateado?',
        '82 Ω ± 10%', ['820 Ω ± 5%', '8.2 Ω ± 10%', '82 Ω ± 5%'],
        'Gris = 8, Rojo = 2 ⇒ Cifra 82. Negro = multiplicador 10⁰ (x 1) ⇒ 82 * 1 = 82 Ω. Plateado = tolerancia ± 10%.', '8-2-x1 ± 10% = 82 Ω ± 10%.', 'basic', 1130
    ))
    return q
