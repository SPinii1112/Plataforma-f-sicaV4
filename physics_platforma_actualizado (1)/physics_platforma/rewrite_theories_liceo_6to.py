# -*- coding: utf-8 -*-
# rewrite_theories_liceo_6to.py
import json

t6 = {}

# 1. Coulomb
t6['6to-ley-de-coulomb'] = """
<div class='space-y-6 text-slate-700 leading-relaxed'>
    <div class='p-4 bg-physics-50 border-l-4 border-physics-600 rounded-r-xl'>
        <h3 class='text-lg font-black text-physics-900'>Ley de Coulomb y Carga Eléctrica</h3>
        <p class='text-sm mt-1'>Estudia la fuerza de atracción o repulsión entre cargas eléctricas en reposo. En el liceo uruguayo se trabaja con cargas puntuales en el vacío o aire.</p>
    </div>

    <div>
        <h4 class='font-bold text-slate-800 text-base mb-2'>Propiedades de la Carga Eléctrica</h4>
        <ul class='list-disc list-inside text-xs space-y-1 bg-slate-50 p-3 rounded-xl border border-slate-200 mb-3'>
            <li><strong>Conservación:</strong> La carga total de un sistema aislado nunca se destruye ni se crea, solo se traslada (los electrones pasan de un cuerpo a otro).</li>
            <li><strong>Cuantización:</strong> Toda carga es múltiplo entero de la carga del electrón ($e = 1.6 \\times 10^{-19}\\text{ C}$): $q = n \\cdot e$.</li>
            <li>Cargas de igual signo se repelen ($+ +$ o $- -$); cargas de distinto signo se atraen ($+ -$).</li>
        </ul>

        <h4 class='font-bold text-slate-800 text-base mb-2'>Fórmula de la Ley de Coulomb</h4>
        <div class='formula-card text-center space-y-1.5'>
            <div>$$F = k \\frac{|q_1 \\cdot q_2|}{r^2} \\quad [\\text{Newtons, N}]$$</div>
            <div>$$k = 9.0 \\times 10^9 \\text{ N}\\cdot\\text{m}^2/\\text{C}^2 \\quad (\\text{constante electrostática en el vacío})$$</div>
        </div>
        <p class='text-xs text-slate-500 mt-2'>Si la distancia entre las cargas se reduce a la mitad ($r/2$), la fuerza se cuadruplica ($4F$).</p>
    </div>

    <div class='p-4 bg-emerald-50 border border-emerald-300 rounded-2xl'>
        <h4 class='font-bold text-emerald-950 text-sm mb-2'>Ejemplo Típico Resuelto</h4>
        <p class='text-xs text-emerald-900 leading-relaxed'>
            Dos cargas de $3.0\\mu\\text{C}$ ($3.0 \\times 10^{-6}\\text{ C}$) y $-4.0\\mu\\text{C}$ están separadas por $0.20\\text{ m}$. ¿Qué fuerza experimentan?<br>
            $$F = 9 \\times 10^9 \\cdot \\frac{3 \\times 10^{-6} \\cdot 4 \\times 10^{-6}}{0.20^2} = 9 \\times 10^9 \\cdot \\frac{12 \\times 10^{-12}}{0.04} = \\frac{0.108}{0.04} = 2.7\\text{ N}$$
            Como tienen signos contrarios, la fuerza es de <strong>atracción</strong> con un módulo de $2.7\\text{ N}$.
        </p>
    </div>
</div>
"""

# 2. Campo Eléctrico
t6['6to-campo-lineas'] = """
<div class='space-y-6 text-slate-700 leading-relaxed'>
    <div class='p-4 bg-physics-50 border-l-4 border-physics-600 rounded-r-xl'>
        <h3 class='text-lg font-black text-physics-900'>Campo Eléctrico y Líneas de Campo</h3>
        <p class='text-sm mt-1'>Toda carga eléctrica altera el espacio a su alrededor creando un <strong>campo eléctrico ($\vec{E}$)</strong>. Cualquier otra carga que entre en esa región sentirá una fuerza.</p>
    </div>

    <div>
        <h4 class='font-bold text-slate-800 text-base mb-2'>Fórmulas Principales</h4>
        <div class='formula-card text-center space-y-2'>
            <div><strong>Definición general:</strong> $$E = \\frac{F}{q} \\quad [\\text{N/C o V/m}]$$</div>
            <div><strong>Campo creado por una carga puntual $Q$:</strong> $$E = k \\frac{|Q|}{r^2}$$</div>
            <div><strong>Campo uniforme entre dos placas paralelas separadas una distancia $d$:</strong> $$E = \\frac{V}{d}$$</div>
        </div>
    </div>

    <div>
        <h4 class='font-bold text-slate-800 text-base mb-2'>Líneas de Campo (Propiedades que se preguntan en escritos)</h4>
        <ul class='list-disc list-inside text-xs space-y-1.5 bg-slate-50 p-3.5 rounded-xl border border-slate-200'>
            <li>Salen de las cargas positivas ($+$) y entran a las cargas negativas ($-$).</li>
            <li><strong>Nunca se cruzan:</strong> En cada punto del espacio el vector campo tiene una sola dirección.</li>
            <li>Donde las líneas están más juntas y apretadas, el campo es más intenso.</li>
            <li>En el interior de un conductor metálico en equilibrio, el campo es siempre <strong>cero</strong> ($E = 0$).</li>
        </ul>
    </div>
</div>
"""

# 3. Potencial Eléctrico
t6['6to-potencial-energia-electrica'] = """
<div class='space-y-6 text-slate-700 leading-relaxed'>
    <div class='p-4 bg-physics-50 border-l-4 border-physics-600 rounded-r-xl'>
        <h3 class='text-lg font-black text-physics-900'>Potencial Eléctrico y Voltaje</h3>
        <p class='text-sm mt-1'>El potencial eléctrico ($V$) mide la energía eléctrica que tendría cada Coulomb de carga colocado en un punto del espacio.</p>
    </div>

    <div>
        <h4 class='font-bold text-slate-800 text-base mb-2'>Fórmulas Básicas de Potencial</h4>
        <div class='formula-card text-center space-y-2'>
            <div>$$V = k \\frac{Q}{r} \\quad [\\text{Volts, V} = \\text{J/C}]$$</div>
            <div>$$W = q \\cdot \\Delta V = q \\cdot (V_A - V_B) \\quad [\\text{Joules, J}]$$</div>
        </div>
        <p class='text-xs text-slate-500 mt-2'>A diferencia del campo (que es vector con flecha), el potencial es un <strong>escalar</strong> (un número que puede ser positivo o negativo, según el signo de la carga).</p>
    </div>

    <div>
        <h4 class='font-bold text-slate-800 text-base mb-2'>Superficies Equipotenciales</h4>
        <p class='text-sm'>Son planos o esferas donde todos los puntos tienen exactamente el mismo voltaje ($V = \\text{cte}$).</p>
        <ul class='list-disc list-inside text-xs space-y-1 bg-slate-50 p-3 rounded-xl border border-slate-200 mt-1'>
            <li>Mover una carga sobre una superficie equipotencial no cuesta ningún trabajo ($W = 0$).</li>
            <li>Las líneas de campo eléctrico siempre cortan a las superficies equipotenciales a $90^\\circ$ (perpendiculares).</li>
        </ul>
    </div>
</div>
"""

# 4. Corriente y Ley de Ohm
t6['6to-corriente-tension-ohm'] = """
<div class='space-y-6 text-slate-700 leading-relaxed'>
    <div class='p-4 bg-physics-50 border-l-4 border-physics-600 rounded-r-xl'>
        <h3 class='text-lg font-black text-physics-900'>Corriente, Resistencia y Ley de Ohm</h3>
        <p class='text-sm mt-1'>El flujo ordenado de electrones por un cable conductor y las leyes que determinan su intensidad y calentamiento.</p>
    </div>

    <div>
        <h4 class='font-bold text-slate-800 text-base mb-2'>Fórmulas Clave</h4>
        <div class='formula-card text-center space-y-2'>
            <div><strong>Intensidad de Corriente:</strong> $$I = \\frac{q}{t} \\quad [\\text{Amperes, A} = \\text{C/s}]$$</div>
            <div><strong>Ley de Pouillet (Resistencia de un cable):</strong> $$R = \\rho \\frac{L}{A} \\quad [\\text{Ohms, } \\Omega]$$</div>
            <div><strong>Ley de Ohm:</strong> $$V = I \\cdot R$$</div>
            <div><strong>Potencia y Efecto Joule (Calor disipado):</strong> $$P = V \\cdot I = I^2 \\cdot R = \\frac{V^2}{R} \\quad [\\text{Watts, W}]$$</div>
        </div>
        <p class='text-xs text-slate-500 mt-2'>En la Ley de Pouillet: si el cable es más largo ($L$) tiene más resistencia; si es más grueso (mayor sección $A$), tiene menos resistencia.</p>
    </div>
</div>
"""

# 5. Kirchhoff
t6['6to-leyes-kirchhoff'] = """
<div class='space-y-6 text-slate-700 leading-relaxed'>
    <div class='p-4 bg-physics-50 border-l-4 border-physics-600 rounded-r-xl'>
        <h3 class='text-lg font-black text-physics-900'>Leyes de Kirchhoff para Circuitos</h3>
        <p class='text-sm mt-1'>El método estándar para resolver circuitos con varias mallas y ramas en paralelo sin marearse.</p>
    </div>

    <div>
        <h4 class='font-bold text-slate-800 text-base mb-2'>Las 2 Reglas de Oro</h4>
        <div class='space-y-3 text-sm'>
            <div class='p-3 bg-slate-50 border border-slate-200 rounded-xl'>
                <span class='font-bold text-physics-700 block text-xs uppercase'>1.ª Ley — Ley de Nodos (Corrientes)</span>
                <p class='text-xs mt-1'>En cualquier empalme o bifurcación (nodo), toda la corriente que entra tiene que salir:
                    $$\\sum I_{\\text{entran}} = \\sum I_{\\text{salen}}$$
                </p>
            </div>

            <div class='p-3 bg-slate-50 border border-slate-200 rounded-xl'>
                <span class='font-bold text-physics-700 block text-xs uppercase'>2.ª Ley — Ley de Mallas (Voltajes)</span>
                <p class='text-xs mt-1'>Al recorrer un lazo cerrado completo (malla) y volver al mismo punto, la suma de las subidas de voltaje en pilas menos las caídas en resistencias da cero:
                    $$\\sum V_{\\text{pilas}} - \\sum (I \\cdot R) = 0$$
                </p>
            </div>
        </div>
    </div>
</div>
"""

# 6. Campo y Fuerza Magnética
t6['6to-campo-fuerza-magnetica'] = """
<div class='space-y-6 text-slate-700 leading-relaxed'>
    <div class='p-4 bg-physics-50 border-l-4 border-physics-600 rounded-r-xl'>
        <h3 class='text-lg font-black text-physics-900'>Campo Magnético y Fuerza de Lorentz</h3>
        <p class='text-sm mt-1'>Los imanes y las corrientes eléctricas crean un campo magnético ($\vec{B}$, medido en Teslas). Este campo desvía cargas en movimiento y hace funcionar los motores eléctricos.</p>
    </div>

    <div>
        <h4 class='font-bold text-slate-800 text-base mb-2'>Fórmulas del Tema</h4>
        <div class='formula-card text-center space-y-2'>
            <div><strong>Fuerza sobre una carga móvil:</strong> $$F = |q| \\cdot v \\cdot B \\cdot \\sin\\theta \\quad [\\text{N}]$$</div>
            <div><strong>Fuerza sobre un cable con corriente:</strong> $$F = I \\cdot L \\cdot B \\cdot \\sin\\theta \\quad [\\text{N}]$$</div>
            <div><strong>Campo alrededor de un cable recto:</strong> $$B = \\frac{\\mu_0 \\cdot I}{2\\pi \\cdot r} \\quad (\\mu_0 = 4\\pi \\times 10^{-7} \\text{ T}\\cdot\\text{m/A})$$</div>
        </div>
        <p class='text-xs text-slate-500 mt-2'>Si la carga viaja paralela al campo ($\theta = 0^\circ$), la fuerza es cero. La fuerza magnética es máxima cuando entra a $90^\circ$.</p>
    </div>

    <div>
        <h4 class='font-bold text-slate-800 text-base mb-2'>Regla de la Mano Derecha (Fácil)</h4>
        <p class='text-sm'>Poné la mano derecha abierta: el pulgar apunta hacia la velocidad ($v$ o corriente $I$), los otros cuatro dedos apuntan hacia el campo magnético ($B$), y la <strong>palma</strong> empuja en el sentido de la fuerza ($F$) para cargas positivas.</p>
    </div>
</div>
"""

# 7. Inducción
t6['6to-induccion-faraday-lenz'] = """
<div class='space-y-6 text-slate-700 leading-relaxed'>
    <div class='p-4 bg-physics-50 border-l-4 border-physics-600 rounded-r-xl'>
        <h3 class='text-lg font-black text-physics-900'>Inducción Electromagnética (Faraday y Lenz)</h3>
        <p class='text-sm mt-1'>Explica cómo generar electricidad a partir del movimiento de imanes (generadores de UTE en Salto Grande y transformadores domiciliarios).</p>
    </div>

    <div>
        <h4 class='font-bold text-slate-800 text-base mb-2'>Flujo Magnético y Ley de Faraday</h4>
        <div class='formula-card text-center space-y-2'>
            <div><strong>Flujo Magnético (cuántas líneas atraviesan un área):</strong> $$\\Phi = B \\cdot A \\cdot \\cos\\theta \\quad [\\text{Webers, Wb}]$$</div>
            <div><strong>Voltaje Inducido (Ley de Faraday):</strong> $$\\mathcal{E} = N \\frac{\\Delta \\Phi}{\\Delta t} \\quad [\\text{Volts, V}]$$</div>
            <div><strong>Varilla conductora que se mueve en un campo:</strong> $$\\mathcal{E} = B \\cdot L \\cdot v$$</div>
        </div>
    </div>

    <div>
        <h4 class='font-bold text-slate-800 text-base mb-2'>Ley de Lenz</h4>
        <p class='text-sm'>La corriente inducida siempre circula en un sentido tal que su propio campo magnético <strong>se opone</strong> al cambio que la provocó (es una consecuencia directa de la conservación de la energía).</p>
    </div>

    <div>
        <h4 class='font-bold text-slate-800 text-base mb-2'>Transformadores</h4>
        <div class='formula-card text-center'>
            $$\\frac{V_s}{V_p} = \\frac{N_s}{N_p} \\implies V_s = V_p \\cdot \\frac{N_s}{N_p}$$
        </div>
        <p class='text-xs text-slate-500'>Permite elevar o bajar el voltaje alterno según la cantidad de vueltas de alambre en el primario y secundario.</p>
    </div>
</div>
"""

# 8. Tester
t6['6to-tester-multimetro'] = """
<div class='space-y-6 text-slate-700 leading-relaxed'>
    <div class='p-4 bg-physics-50 border-l-4 border-physics-600 rounded-r-xl'>
        <h3 class='text-lg font-black text-physics-900'>El Multímetro / Tester en el Práctico</h3>
        <p class='text-sm mt-1'>Guía rápida de uso seguro en el laboratorio de física para medir sin quemar el aparato ni hacer saltar las térmicas.</p>
    </div>

    <div>
        <h4 class='font-bold text-slate-800 text-base mb-2'>Las 3 Reglas Sagradas de Conexión</h4>
        <ul class='list-disc list-inside text-xs space-y-2 bg-slate-50 p-3.5 rounded-xl border border-slate-200'>
            <li><strong>Para medir Voltaje (Voltímetro):</strong> Se conecta <strong>en paralelo</strong> (apoyando las puntas roja y negra a los lados del componente). Tiene resistencia interna casi infinita.</li>
            <li><strong>Para medir Corriente (Amperímetro):</strong> Se conecta <strong>en serie</strong> (hay que abrir el cable o desconectar una patita y poner el tester en el medio para que la corriente lo atraviese). <em>Peligro: conectar el amperímetro en paralelo hace cortocircuito y quema el fusible.</em></li>
            <li><strong>Para medir Resistencia (Óhmetro):</strong> El circuito debe estar <strong>completamente apagado y desenchufado</strong>. Si hay corriente externa, la medición da error o se quema el instrumento.</li>
        </ul>
    </div>
</div>
"""

# 9. Capacitores RC
t6['6to-capacitores-rc'] = """
<div class='space-y-6 text-slate-700 leading-relaxed'>
    <div class='p-4 bg-physics-50 border-l-4 border-physics-600 rounded-r-xl'>
        <h3 class='text-lg font-black text-physics-900'>Capacitores y Circuitos RC</h3>
        <p class='text-sm mt-1'>Un capacitor almacena carga y energía eléctrica en dos placas metálicas separadas por un aislante (dieléctrico).</p>
    </div>

    <div>
        <h4 class='font-bold text-slate-800 text-base mb-2'>Fórmulas Básicas</h4>
        <div class='formula-card text-center space-y-2'>
            <div>$$C = \\frac{Q}{V} \\quad [\\text{Faradios, F o } \\mu\\text{F}], \\quad E = \\frac{1}{2} C V^2 \\quad [\\text{Joules, J}]$$</div>
            <div><strong>Constante de tiempo de carga/descarga:</strong> $$\\tau = R \\cdot C \\quad [\\text{segundos, s}]$$</div>
        </div>
        <p class='text-xs text-slate-500 mt-2'>En un tiempo $t = 1\\tau$, el capacitor se carga al $63.2\\%$. Se considera prácticamente lleno a los $5\\tau$ ($99.3\\%$).</p>
    </div>
</div>
"""

# 10. Resistencias y Código de Colores
t6['6to-resistencias-colores-estres'] = """
<div class='space-y-6 text-slate-700 leading-relaxed'>
    <div class='p-4 bg-physics-50 border-l-4 border-physics-600 rounded-r-xl'>
        <h3 class='text-lg font-black text-physics-900'>Resistencias y Código de Colores</h3>
        <p class='text-sm mt-1'>Cómo leer las bandas de colores de las resistencias en el laboratorio y calcular su disipación máxima.</p>
    </div>

    <div>
        <h4 class='font-bold text-slate-800 text-base mb-2'>Lectura de las 4 Bandas</h4>
        <ul class='list-disc list-inside text-xs space-y-1 bg-slate-50 p-3 rounded-xl border border-slate-200'>
            <li><strong>Banda 1:</strong> Primer dígito (ejemplo: Marrón = 1, Rojo = 2, Amarillo = 4).</li>
            <li><strong>Banda 2:</strong> Segundo dígito (ejemplo: Negro = 0, Violeta = 7).</li>
            <li><strong>Banda 3:</strong> Multiplicador de ceros (ejemplo: Rojo = $\\times 100$, Naranja = $\\times 1000$).</li>
            <li><strong>Banda 4:</strong> Tolerancia (Dorado = $\\pm 5\\%$, Plateado = $\\pm 10\\%$).</li>
        </ul>
        <p class='text-xs mt-2 text-slate-500'>Ejemplo: <strong>Marrón-Negro-Rojo-Dorado</strong> = $1$ - $0$ - $\\times 100$ = $1000\\;\\Omega = 1.0\\text{ k}\\Omega$ con $\\pm 5\\%$ de tolerancia.</p>
    </div>

    <div>
        <h4 class='font-bold text-slate-800 text-base mb-2'>Límite de Potencia</h4>
        <p class='text-sm'>Toda resistencia tiene una potencia máxima antes de quemarse (típicamente $1/4\\text{ W} = 0.25\\text{ W}$):</p>
        <div class='formula-card text-center'>
            $$V_{\\text{max}} = \\sqrt{P_{\\text{max}} \\cdot R}$$
        </div>
    </div>
</div>
"""

with open("app/learning/theory_6to.json", "w", encoding="utf-8") as f:
    json.dump(t6, f, ensure_ascii=False, indent=2)

print("theory_6to.json reescrito en nivel liceal real sin derivadas, integrales ni Gauss.")
