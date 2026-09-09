# -*- coding: utf-8 -*-
# rewrite_theories_liceo_5to.py
import json

t5 = {}

# 1. Cinemática
t5['5to-cinematica-completa'] = """
<div class='space-y-6 text-slate-700 leading-relaxed'>
    <div class='p-4 bg-physics-50 border-l-4 border-physics-600 rounded-r-xl'>
        <h3 class='text-lg font-black text-physics-900'>¿De qué se trata la Cinemática?</h3>
        <p class='text-sm mt-1'>La cinemática estudia cómo se mueven los objetos (su posición, velocidad y aceleración) a lo largo del tiempo, sin preocuparse todavía por qué fuerzas provocaron ese movimiento.</p>
    </div>

    <div>
        <h4 class='font-bold text-slate-800 text-base mb-2'>Conceptos Básicos: Posición, Desplazamiento y Velocidad</h4>
        <p class='text-sm mb-2'>Una partícula se mueve a lo largo de una recta. No es lo mismo la distancia recorrida (todo lo que caminó) que el <strong>desplazamiento</strong> (la resta directa entre dónde terminó y dónde empezó):</p>
        <div class='formula-card text-center'>
            $$\\Delta x = x_f - x_i \\quad [\\text{metros, m}]$$
        </div>
        <p class='text-sm mt-2'>La <strong>velocidad media</strong> nos dice qué tan rápido cambió de posición en un intervalo de tiempo:</p>
        <div class='formula-card text-center'>
            $$v_m = \\frac{\\Delta x}{\\Delta t} = \\frac{x_f - x_i}{t_f - t_i} \\quad [\\text{m/s}]$$
        </div>
        <p class='text-xs text-slate-500 italic mt-1'>Pique de unidades: Para pasar de km/h a m/s se divide entre 3.6 (ejemplo: $72\\text{ km/h} \\div 3.6 = 20\\text{ m/s}$).</p>
    </div>

    <div>
        <h4 class='font-bold text-slate-800 text-base mb-2'>1. Movimiento Rectilíneo Uniforme (MRU)</h4>
        <p class='text-sm'>Es el movimiento más simple de todos: la velocidad es constante (no cambia de rapidez ni de sentido) y la aceleración es cero ($a = 0$).</p>
        <div class='formula-card text-center'>
            $$x = x_0 + v \\cdot t$$
        </div>
        <p class='text-xs mt-2'><strong>Lectura de gráficos en MRU:</strong></p>
        <ul class='list-disc list-inside text-xs space-y-1 bg-slate-50 p-3 rounded-xl border border-slate-200 mt-1'>
            <li>En el gráfico de posición en función del tiempo ($x$ vs $t$), la gráfica es una recta inclinada. La <strong>pendiente</strong> de esa recta es la velocidad.</li>
            <li>En el gráfico de velocidad en función del tiempo ($v$ vs $t$), la gráfica es una línea horizontal plana. El <strong>área</strong> bajo esa recta representa la distancia recorrida.</li>
        </ul>
    </div>

    <div>
        <h4 class='font-bold text-slate-800 text-base mb-2'>2. Movimiento Rectilíneo Uniformemente Variado (MRUV)</h4>
        <p class='text-sm'>Aquí la velocidad cambia a un ritmo parejo: la <strong>aceleración es constante</strong>.</p>
        <div class='formula-card text-center space-y-2'>
            <div>$$a = \\frac{\\Delta v}{\\Delta t} = \\frac{v_f - v_0}{t} \\quad [\\text{m/s}^2]$$</div>
            <div>$$v_f = v_0 + a \\cdot t$$</div>
            <div>$$\\Delta x = v_0 \\cdot t + \\frac{1}{2} a \\cdot t^2$$</div>
        </div>
        <p class='text-sm mt-3'><strong>La Ecuación de Torricelli (¡salvavidas cuando no tenés el tiempo!):</strong></p>
        <div class='formula-card text-center'>
            $$v_f^2 = v_0^2 + 2 \\cdot a \\cdot \\Delta x$$
        </div>
    </div>

    <div>
        <h4 class='font-bold text-slate-800 text-base mb-2'>Caída Libre y Tiro Vertical</h4>
        <p class='text-sm'>Es un MRUV vertical donde la aceleración siempre es la gravedad ($g \\approx 9.8\\text{ m/s}^2$ o $10\\text{ m/s}^2$ dirigida hacia abajo):</p>
        <ul class='list-disc list-inside text-xs space-y-1 bg-slate-50 p-3 rounded-xl border border-slate-200 mt-1'>
            <li>Si soltás un cuerpo desde el reposo: $v_0 = 0 \\implies h = \\frac{1}{2} g t^2$.</li>
            <li>En el punto más alto de un tiro vertical: la velocidad es $0\\text{ m/s}$ justo antes de empezar a caer.</li>
            <li>El tiempo que tarda en subir es exactamente igual al tiempo que tarda en bajar al mismo nivel.</li>
        </ul>
    </div>

    <div class='p-4 bg-emerald-50 border border-emerald-300 rounded-2xl'>
        <h4 class='font-bold text-emerald-950 text-sm mb-2'>Ejemplo Típico de Escrito Resuelto Paso a Paso</h4>
        <p class='text-xs text-emerald-900 leading-relaxed'>
            <strong>Problema:</strong> Un auto viaja a $20\\text{ m/s}$ por Avenida Italia. Ve un semáforo en rojo y frena con una aceleración constante de $4.0\\text{ m/s}^2$. ¿Qué distancia recorre hasta frenar del todo?<br>
            <strong>Paso 1 (Anotar datos):</strong> $v_0 = 20\\text{ m/s}$, $v_f = 0\\text{ m/s}$ (porque frena), $a = -4.0\\text{ m/s}^2$ (negativa porque frena).<br>
            <strong>Paso 2 (Elegir fórmula):</strong> Como no nos piden ni nos dan el tiempo, usamos Torricelli:<br>
            $$v_f^2 = v_0^2 + 2 \\cdot a \\cdot \\Delta x$$
            <strong>Paso 3 (Despejar y calcular):</strong><br>
            $$0^2 = 20^2 + 2 \\cdot (-4.0) \\cdot \\Delta x \\implies 0 = 400 - 8 \\Delta x$$
            $$8 \\Delta x = 400 \\implies \\Delta x = \\frac{400}{8} = 50\\text{ metros}.$$
            <em>Respuesta:</em> El auto recorre $50\\text{ m}$ hasta detenerse.
        </p>
    </div>

    <div class='formula-card-warning text-xs space-y-1'>
        <span class='font-black text-rose-900 block text-sm'>Piques para no meter la pata en los escritos:</span>
        <p>1. <strong>Los signos en frenado:</strong> Si el auto va hacia adelante ($v > 0$) y frena, la aceleración va hacia atrás ($a < 0$). Si te olvidás del signo menos, la raíz cuadrada te va a dar error o la distancia te va a dar negativa.</p>
        <p>2. <strong>Gráfico v vs t:</strong> El área de un triángulo o rectángulo bajo la gráfica de velocidad siempre es igual a la distancia recorrida.</p>
    </div>
</div>
"""

# 2. Dinámica
t5['5to-leyes-newton-dinamica'] = """
<div class='space-y-6 text-slate-700 leading-relaxed'>
    <div class='p-4 bg-physics-50 border-l-4 border-physics-600 rounded-r-xl'>
        <h3 class='text-lg font-black text-physics-900'>¿De qué se trata la Dinámica?</h3>
        <p class='text-sm mt-1'>Estudia por qué se mueven las cosas. La causa de los cambios en el movimiento son las <strong>fuerzas</strong> (interacciones entre dos cuerpos), explicadas mediante las 3 Leyes de Newton.</p>
    </div>

    <div>
        <h4 class='font-bold text-slate-800 text-base mb-2'>Las 3 Leyes de Newton explicadas fácil</h4>
        <div class='space-y-3 text-sm'>
            <div class='p-3 bg-slate-50 border border-slate-200 rounded-xl'>
                <span class='font-bold text-physics-700 block text-xs uppercase'>1.ª Ley — Principio de Inercia</span>
                <p class='text-xs mt-1'>Si sobre un cuerpo no actúa ninguna fuerza neta (o todas se cancelan), el cuerpo sigue haciendo lo que venía haciendo: si estaba quieto, sigue quieto; si se movía a velocidad constante en línea recta, sigue a velocidad constante.</p>
            </div>

            <div class='p-3 bg-slate-50 border border-slate-200 rounded-xl'>
                <span class='font-bold text-physics-700 block text-xs uppercase'>2.ª Ley — Fuerza, Masa y Aceleración</span>
                <p class='text-xs mt-1'>Si hay una fuerza neta sin compensar, el cuerpo se acelera en la misma dirección de la fuerza. Cuanto más pesado (más masa), más fuerza necesitás para acelerarlo:</p>
                <div class='formula-card text-center my-2'>
                    $$F_{\\text{neta}} = m \\cdot a \\quad [\\text{Newtons, N}]$$
                </div>
                <p class='text-xs text-slate-500'>$1\\text{ Newton} = 1\\text{ kg} \\cdot \\text{m/s}^2$. Si empujás con $10\\text{ N}$ una masa de $2\\text{ kg}$, acelera a $a = \\frac{10}{2} = 5\\text{ m/s}^2$.</p>
            </div>

            <div class='p-3 bg-slate-50 border border-slate-200 rounded-xl'>
                <span class='font-bold text-physics-700 block text-xs uppercase'>3.ª Ley — Acción y Reacción</span>
                <p class='text-xs mt-1'>Las fuerzas siempre vienen de a pares entre dos cuerpos: si vos empujás una pared con $50\\text{ N}$, la pared te empuja a vos con $50\\text{ N}$ en sentido contrario. <em>Ojo: nunca se anulan entre sí porque actúan sobre cuerpos distintos.</em></p>
            </div>
        </div>
    </div>

    <div>
        <h4 class='font-bold text-slate-800 text-base mb-2'>Las Fuerzas Típicas que tenés que dibujar en el DCL</h4>
        <ul class='list-disc list-inside text-xs space-y-2 bg-slate-50 p-3.5 rounded-xl border border-slate-200'>
            <li><strong>Peso ($P$):</strong> Fuerza con la que la Tierra atrae al cuerpo. Siempre apunta vertical hacia abajo:
                $$P = m \\cdot g \\quad (g \\approx 9.8\\text{ o } 10\\text{ m/s}^2)$$
            </li>
            <li><strong>Normal ($N$):</strong> Fuerza de apoyo que hace la superficie. Siempre es perpendicular a la superficie.</li>
            <li><strong>Tensión ($T$):</strong> Fuerza que transmite una cuerda o cable estirado.</li>
            <li><strong>Rozamiento ($f_r$):</strong> Fuerza que se opone a que las superficies deslicen entre sí:
                <br>&bull; <em>Rozamiento cinético (en movimiento):</em> $f_{rc} = \\mu_c \\cdot N$
                <br>&bull; <em>Rozamiento estático máximo (a punto de moverse):</em> $f_{re,\\text{max}} = \\mu_e \\cdot N$
            </li>
        </ul>
    </div>

    <div>
        <h4 class='font-bold text-slate-800 text-base mb-2'>El Plano Inclinado (Clásico de Prueba)</h4>
        <p class='text-sm'>Cuando un bloque está sobre una rampa inclinada un ángulo $\\alpha$, el peso se descompone con trigonometría básica:</p>
        <div class='formula-card text-center space-y-1.5'>
            <div>$$P_x = P \\cdot \\sin\\alpha = m g \\sin\\alpha \\quad (\\text{la componente que lo hace caer rampa abajo})$$</div>
            <div>$$P_y = P \\cdot \\cos\\alpha = m g \\cos\\alpha \\quad (\\text{la componente que lo aprieta contra la rampa}) \\implies N = P_y$$</div>
        </div>
    </div>

    <div class='p-4 bg-emerald-50 border border-emerald-300 rounded-2xl'>
        <h4 class='font-bold text-emerald-950 text-sm mb-2'>Ejemplo Resuelto: Descenso en Rampa</h4>
        <p class='text-xs text-emerald-900 leading-relaxed'>
            <strong>Problema:</strong> Un bloque de $4.0\\text{ kg}$ baja por una rampa inclinada $30^\\circ$ sin rozamiento. ¿Con qué aceleración baja? ($g = 10\\text{ m/s}^2, \\sin 30^\\circ = 0.50$).<br>
            <strong>Paso 1:</strong> La fuerza que empuja rampa abajo es solo $P_x$:<br>
            $$P_x = m \\cdot g \\cdot \\sin 30^\\circ = 4.0 \\cdot 10 \\cdot 0.50 = 20\\text{ N}$$
            <strong>Paso 2:</strong> Aplicamos $F_{\\text{neta}} = m \\cdot a$ en la dirección de la rampa:<br>
            $$20 = 4.0 \\cdot a \\implies a = \\frac{20}{4.0} = 5.0\\text{ m/s}^2.$$
        </p>
    </div>
</div>
"""

# 3. Trabajo y Energía
t5['5to-trabajo-mecanico-energia'] = """
<div class='space-y-6 text-slate-700 leading-relaxed'>
    <div class='p-4 bg-physics-50 border-l-4 border-physics-600 rounded-r-xl'>
        <h3 class='text-lg font-black text-physics-900'>¿De qué se trata el Trabajo y la Energía?</h3>
        <p class='text-sm mt-1'>La energía es la capacidad de generar cambios en el entorno. Cuando aplicás una fuerza a lo largo de una distancia, transferís energía: eso es el <strong>trabajo mecánico ($W$)</strong>.</p>
    </div>

    <div>
        <h4 class='font-bold text-slate-800 text-base mb-2'>Fórmula de Trabajo Mecánico</h4>
        <div class='formula-card text-center'>
            $$W = F \\cdot d \\cdot \\cos\\theta \\quad [\\text{Joules, J}]$$
        </div>
        <ul class='list-disc list-inside text-xs space-y-1 bg-slate-50 p-3 rounded-xl border border-slate-200 mt-2'>
            <li>Si empujás en la misma dirección del movimiento ($\theta = 0^\circ, \cos 0^\circ = 1$): $W = F \\cdot d$ (trabajo positivo o motor).</li>
            <li>Si la fuerza es perpendicular al movimiento ($\theta = 90^\circ, \cos 90^\circ = 0$): $W = 0$. <em>¡La fuerza peso cuando caminás horizontal o la fuerza normal NO hacen trabajo!</em></li>
            <li>Si frena al cuerpo (como el rozamiento, $\theta = 180^\circ, \cos 180^\circ = -1$): el trabajo es negativo (quita energía).</li>
        </ul>
    </div>

    <div>
        <h4 class='font-bold text-slate-800 text-base mb-2'>Las Formas de Energía Mecánica</h4>
        <div class='formula-card text-center space-y-2'>
            <div><strong>Energía Cinética (de movimiento):</strong> $$E_k = \\frac{1}{2} m v^2$$</div>
            <div><strong>Energía Potencial Gravitatoria (por altura):</strong> $$E_{pg} = m \\cdot g \\cdot h$$</div>
            <div><strong>Energía Potencial Elástica (en resortes):</strong> $$E_{pe} = \\frac{1}{2} k x^2$$</div>
            <div><strong>Energía Mecánica Total:</strong> $$E_m = E_k + E_{pg} + E_{pe}$$</div>
        </div>
    </div>

    <div>
        <h4 class='font-bold text-slate-800 text-base mb-2'>Principio de Conservación de la Energía</h4>
        <p class='text-sm'>Si en un problema no hay rozamiento ni pérdidas por calor, la energía mecánica se conserva (la suma inicial es igual a la suma final):</p>
        <div class='formula-card text-center'>
            $$E_{m,\\text{inicial}} = E_{m,\\text{final}}$$
        </div>
        <p class='text-xs mt-1 text-slate-500'>Ejemplo: Si soltás una pelota desde cierta altura, toda la energía potencial se transforma en energía cinética justo al tocar el piso: $m g h = \\frac{1}{2} m v^2 \\implies v = \\sqrt{2 g h}$.</p>
    </div>

    <div>
        <h4 class='font-bold text-slate-800 text-base mb-2'>Potencia Mecánica</h4>
        <p class='text-sm'>Mide qué tan rápido se realiza un trabajo (cuántos Joules por segundo):</p>
        <div class='formula-card text-center'>
            $$P = \\frac{W}{\\Delta t} = F \\cdot v \\quad [\\text{Watts, W}]$$
        </div>
    </div>
</div>
"""

# 4. Cantidad de Movimiento e Impulso
t5['5to-momento-lineal-choques'] = """
<div class='space-y-6 text-slate-700 leading-relaxed'>
    <div class='p-4 bg-physics-50 border-l-4 border-physics-600 rounded-r-xl'>
        <h3 class='text-lg font-black text-physics-900'>Momento Lineal e Impulso en Choques</h3>
        <p class='text-sm mt-1'>Explica qué pasa cuando dos cuerpos chocan (autos, billar, pelotas) o cuando hay retroceso (como al disparar o lanzar algo en patines).</p>
    </div>

    <div>
        <h4 class='font-bold text-slate-800 text-base mb-2'>Fórmulas Principales</h4>
        <div class='formula-card text-center space-y-2'>
            <div><strong>Cantidad de Movimiento (Momento lineal):</strong> $$p = m \\cdot v \\quad [\\text{kg}\\cdot\\text{m/s}]$$</div>
            <div><strong>Impulso de una Fuerza:</strong> $$I = F \\cdot \\Delta t = \\Delta p = m v_f - m v_0 \\quad [\\text{N}\\cdot\\text{s}]$$</div>
        </div>
    </div>

    <div>
        <h4 class='font-bold text-slate-800 text-base mb-2'>Conservación en Choques</h4>
        <p class='text-sm'>En cualquier choque donde no actúen fuerzas externas netas, la suma de los momentos lineales antes del choque es igual a la suma después:</p>
        <div class='formula-card text-center'>
            $$m_1 v_{1i} + m_2 v_{2i} = m_1 v_{1f} + m_2 v_{2f}$$
        </div>
        <ul class='list-disc list-inside text-xs space-y-1 bg-slate-50 p-3 rounded-xl border border-slate-200 mt-2'>
            <li><strong>Choque elástico:</strong> Rebotan sin perder nada de energía cinética.</li>
            <li><strong>Choque plástico (o inelástico):</strong> Chocan y quedan <strong>pegados</strong>, moviéndose juntos a una misma velocidad final $v_f$:
                $$m_1 v_1 + m_2 v_2 = (m_1 + m_2) v_f$$
            </li>
        </ul>
    </div>
</div>
"""

# 5. Movimiento Circular
t5['5to-mcu-fuerza-centripeta'] = """
<div class='space-y-6 text-slate-700 leading-relaxed'>
    <div class='p-4 bg-physics-50 border-l-4 border-physics-600 rounded-r-xl'>
        <h3 class='text-lg font-black text-physics-900'>Movimiento Circular Uniforme (MCU)</h3>
        <p class='text-sm mt-1'>Ocurre cuando un cuerpo gira describiendo una circunferencia a rapidez constante (como las aspas de un molino o una rueda).</p>
    </div>

    <div>
        <h4 class='font-bold text-slate-800 text-base mb-2'>Período, Frecuencia y Velocidad</h4>
        <div class='formula-card text-center space-y-1.5'>
            <div>$$T = \\frac{\\text{tiempo}}{\\text{vueltas}} \\quad [\\text{segundos, s}], \\quad f = \\frac{\\text{vueltas}}{\\text{tiempo}} = \\frac{1}{T} \\quad [\\text{Hertz, Hz}]$$</div>
            <div>$$\\omega = \\frac{2\\pi}{T} = 2\\pi f \\quad [\\text{rad/s}], \\quad v = \\omega \\cdot r \\quad [\\text{m/s}]$$</div>
        </div>
    </div>

    <div>
        <h4 class='font-bold text-slate-800 text-base mb-2'>Aceleración y Fuerza Centrípeta</h4>
        <p class='text-sm'>Como la velocidad cambia constantemente de dirección para doblar, existe una aceleración hacia el centro de la curva:</p>
        <div class='formula-card text-center space-y-1.5'>
            <div>$$a_c = \\frac{v^2}{r} \\quad [\\text{m/s}^2]$$</div>
            <div>$$F_c = m \\cdot a_c = m \\frac{v^2}{r} \\quad [\\text{N}]$$</div>
        </div>
        <p class='text-xs text-slate-500 mt-2'>En una curva de ruta, la fuerza centrípeta que te mantiene en la curva es el <strong>rozamiento</strong> de las ruedas con el asfalto. Si hay hielo o vas muy rápido, no alcanza y el auto derrapa hacia afuera.</p>
    </div>
</div>
"""

# 6. Gravitacion
t5['5to-gravitacion-kepler'] = """
<div class='space-y-6 text-slate-700 leading-relaxed'>
    <div class='p-4 bg-physics-50 border-l-4 border-physics-600 rounded-r-xl'>
        <h3 class='text-lg font-black text-physics-900'>Gravitación Universal y Leyes de Kepler</h3>
        <p class='text-sm mt-1'>Explica la atracción entre planetas, satélites y la razón por la que las cosas caen hacia el centro de la Tierra.</p>
    </div>

    <div>
        <h4 class='font-bold text-slate-800 text-base mb-2'>Ley de Newton de Gravitación</h4>
        <div class='formula-card text-center'>
            $$F = G \\frac{m_1 \\cdot m_2}{r^2} \\quad (G = 6.67 \\times 10^{-11} \\text{ N}\\cdot\\text{m}^2/\\text{kg}^2)$$
        </div>
        <p class='text-sm mt-2'>Si te alejás al doble de distancia ($2r$), la fuerza gravitatoria se divide entre 4 ($2^2$).</p>
    </div>

    <div>
        <h4 class='font-bold text-slate-800 text-base mb-2'>Leyes de Kepler (Muy tomadas en teórico)</h4>
        <ul class='list-disc list-inside text-xs space-y-1.5 bg-slate-50 p-3 rounded-xl border border-slate-200'>
            <li><strong>1.ª Ley:</strong> Los planetas giran en elipses, con el Sol en uno de sus focos.</li>
            <li><strong>2.ª Ley:</strong> El planeta viaja más rápido cuando está cerca del Sol (perihelio) y más lento cuando está lejos (afelio).</li>
            <li><strong>3.ª Ley:</strong> Cuanto más lejos orbita un planeta, más tarda en dar la vuelta: $\\frac{T^2}{r^3} = \\text{constante}$.</li>
        </ul>
    </div>
</div>
"""

# 7. Estática
t5['5to-estatica-torque'] = """
<div class='space-y-6 text-slate-700 leading-relaxed'>
    <div class='p-4 bg-physics-50 border-l-4 border-physics-600 rounded-r-xl'>
        <h3 class='text-lg font-black text-physics-900'>Estática y Equilibrio (Torque)</h3>
        <p class='text-sm mt-1'>Estudia cuándo un cuerpo no se mueve ni se pone a girar (como una balanza, una viga, un subibaja o una puerta).</p>
    </div>

    <div>
        <h4 class='font-bold text-slate-800 text-base mb-2'>Torque o Momento de una Fuerza (Giro)</h4>
        <p class='text-sm'>El torque mide la capacidad de una fuerza de hacer girar un objeto respecto a un punto de apoyo:</p>
        <div class='formula-card text-center'>
            $$\\tau = F \\cdot d \\cdot \\sin\\theta \\quad [\\text{N}\\cdot\\text{m}]$$
        </div>
        <p class='text-xs mt-1 text-slate-500'>Donde $d$ es el brazo de palanca (la distancia desde el eje de giro a donde aplicás la fuerza). Si empujás la puerta cerca de la bisagra cuesta un montón; si empujás en el picaporte (lejos de la bisagra), abrís fácil porque aumentás el brazo $d$.</p>
    </div>

    <div>
        <h4 class='font-bold text-slate-800 text-base mb-2'>Las 2 Condiciones de Equilibrio</h4>
        <ul class='list-disc list-inside text-xs space-y-1 bg-slate-50 p-3 rounded-xl border border-slate-200'>
            <li><strong>No se traslada:</strong> La suma de todas las fuerzas debe dar cero: $\\sum F_x = 0$ y $\\sum F_y = 0$.</li>
            <li><strong>No gira:</strong> La suma de todos los torques debe dar cero: $\\sum \\tau = 0$ (los giros hacia un lado equilibran a los del otro).</li>
        </ul>
    </div>
</div>
"""

# 8. Fluidos
t5['5to-fluidos-presion-empuje'] = """
<div class='space-y-6 text-slate-700 leading-relaxed'>
    <div class='p-4 bg-physics-50 border-l-4 border-physics-600 rounded-r-xl'>
        <h3 class='text-lg font-black text-physics-900'>Fluidos: Presión y Empuje de Arquímedes</h3>
        <p class='text-sm mt-1'>Estudia los líquidos y gases en reposo, prensas hidráulicas y por qué flotan los barcos.</p>
    </div>

    <div>
        <h4 class='font-bold text-slate-800 text-base mb-2'>Presión y Principio Fundamental</h4>
        <div class='formula-card text-center space-y-1.5'>
            <div>$$P = \\frac{F}{A} \\quad [\\text{Pascales, Pa} = \\text{N/m}^2]$$</div>
            <div>$$P = \\rho \\cdot g \\cdot h \\quad (\\text{Presión bajo una columna de líquido de profundidad } h)$$</div>
        </div>
        <p class='text-xs text-slate-500'>A mayor profundidad, mayor presión soportás (más peso de agua arriba).</p>
    </div>

    <div>
        <h4 class='font-bold text-slate-800 text-base mb-2'>Principio de Pascal (Prensa Hidráulica)</h4>
        <p class='text-sm'>La presión aplicada en un punto de un líquido cerrado se transmite idéntica a todos los puntos:</p>
        <div class='formula-card text-center'>
            $$\\frac{F_1}{A_1} = \\frac{F_2}{A_2} \\implies F_2 = F_1 \\cdot \\frac{A_2}{A_1}$$
        </div>
        <p class='text-xs text-slate-500'>Si el émbolo de salida es 20 veces más grande en área, levantás 20 veces más peso con poca fuerza.</p>
    </div>

    <div>
        <h4 class='font-bold text-slate-800 text-base mb-2'>Principio de Arquímedes (Flotación)</h4>
        <p class='text-sm'>Todo cuerpo sumergido recibe una fuerza hacia arriba llamada <strong>Empuje ($E$)</strong> igual al peso del líquido que desalojó:</p>
        <div class='formula-card text-center'>
            $$E = \\rho_{\\text{líquido}} \\cdot V_{\\text{sumergido}} \\cdot g$$
        </div>
        <p class='text-xs mt-1'>Si el Empuje iguala al Peso ($E = P$), el objeto flota en equilibrio.</p>
    </div>
</div>
"""

# 9. Ondas
t5['5to-ondas-sonido-fenomenos'] = """
<div class='space-y-6 text-slate-700 leading-relaxed'>
    <div class='p-4 bg-physics-50 border-l-4 border-physics-600 rounded-r-xl'>
        <h3 class='text-lg font-black text-physics-900'>Ondas y Sonido</h3>
        <p class='text-sm mt-1'>Una onda es una perturbación que viaja transportando <strong>energía sin transportar materia</strong>.</p>
    </div>

    <div>
        <h4 class='font-bold text-slate-800 text-base mb-2'>La Ecuación Fundamental de las Ondas</h4>
        <div class='formula-card text-center'>
            $$v = \\lambda \\cdot f \\quad [\\text{m/s}]$$
        </div>
        <ul class='list-disc list-inside text-xs space-y-1 bg-slate-50 p-3 rounded-xl border border-slate-200 mt-2'>
            <li>$v$: velocidad de propagación (en el aire el sonido viaja a unos $340\\text{ m/s}$).</li>
            <li>$\\lambda$ (lambda): longitud de onda (distancia entre cresta y cresta, en metros).</li>
            <li>$f$: frecuencia (cuántas ondas pasan por segundo, en Hertz $\\text{Hz}$).</li>
        </ul>
    </div>

    <div>
        <h4 class='font-bold text-slate-800 text-base mb-2'>Fenómenos Ondulatorios</h4>
        <ul class='list-disc list-inside text-xs space-y-1.5 bg-slate-50 p-3.5 rounded-xl border border-slate-200'>
            <li><strong>Reflexión:</strong> Rebote de la onda al chocar contra un obstáculo (ejemplo: el eco).</li>
            <li><strong>Refracción (Ley de Snell):</strong> Cambio de dirección y velocidad al pasar de un medio a otro (del aire al agua): $n_1 \\sin\\theta_1 = n_2 \\sin\\theta_2$. La frecuencia <em>nunca cambia</em> al refractarse.</li>
            <li><strong>Difracción:</strong> La capacidad de las ondas de doblar esquinas o pasar por rendijas estrechas.</li>
            <li><strong>Efecto Doppler:</strong> Cuando una ambulancia se acerca la sirena se escucha más aguda (mayor frecuencia), y cuando se aleja se escucha más grave.</li>
        </ul>
    </div>
</div>
"""

# 10. Electricidad 5to
t5['5to-electricidad-circuitos-basicos'] = """
<div class='space-y-6 text-slate-700 leading-relaxed'>
    <div class='p-4 bg-physics-50 border-l-4 border-physics-600 rounded-r-xl'>
        <h3 class='text-lg font-black text-physics-900'>Electricidad Básica y Circuitos</h3>
        <p class='text-sm mt-1'>Comportamiento de cargas eléctricas, Ley de Ohm y circuitos simples en serie y paralelo.</p>
    </div>

    <div>
        <h4 class='font-bold text-slate-800 text-base mb-2'>Ley de Coulomb y Campo Eléctrico</h4>
        <div class='formula-card text-center space-y-1.5'>
            <div>$$F = k \\frac{|q_1 \\cdot q_2|}{r^2} \\quad (k = 9 \\times 10^9 \\text{ N}\\cdot\\text{m}^2/\\text{C}^2)$$</div>
            <div>$$E = \\frac{F}{q} = k \\frac{Q}{r^2} \\quad [\\text{N/C o V/m}]$$</div>
        </div>
        <p class='text-xs text-slate-500 mt-1'>Cargas de igual signo se repelen; cargas de signo contrario se atraen.</p>
    </div>

    <div>
        <h4 class='font-bold text-slate-800 text-base mb-2'>Ley de Ohm y Circuitos</h4>
        <div class='formula-card text-center space-y-2'>
            <div>$$V = I \\cdot R \\quad (V \\text{ en Volts, } I \\text{ en Amperes, } R \\text{ en Ohms } \\Omega)$$</div>
            <div>$$P = V \\cdot I = I^2 \\cdot R \\quad [\\text{Watts, W}]$$</div>
        </div>
        <p class='text-xs mt-2'><strong>Asociación de Resistencias:</strong></p>
        <ul class='list-disc list-inside text-xs space-y-1 bg-slate-50 p-3 rounded-xl border border-slate-200 mt-1'>
            <li><strong>En serie:</strong> Misma corriente pasa por todas. Se suman directo: $R_t = R_1 + R_2 + R_3$.</li>
            <li><strong>En paralelo:</strong> Mismo voltaje en todas. Se calcula: $\\frac{1}{R_t} = \\frac{1}{R_1} + \\frac{1}{R_2}$.</li>
        </ul>
    </div>
</div>
"""

with open("app/learning/theory_5to.json", "w", encoding="utf-8") as f:
    json.dump(t5, f, ensure_ascii=False, indent=2)

print("theory_5to.json reescrito en nivel liceal real sin derivadas ni integrales.")
