# ⚛️ PhysicsLab — Plataforma Adaptativa de Aprendizaje de Física
### *Bachillerato / Educación Media de Uruguay (5.º y 6.º Año)*

PhysicsLab es una plataforma web educativa diseñada para el aprendizaje adaptativo y personalizado de la Física, alineada rigurosamente con los programas educativos oficiales de **5.º y 6.º año de educación media en Uruguay**.

A diferencia de una simple página con teoría y ejercicios, PhysicsLab integra un **sistema de aprendizaje adaptativo determinista local** (basado en *Bayesian Knowledge Tracing* y calibración *Elo*), sin requerir Inteligencia Artificial externa ni APIs de pago, garantizando máxima velocidad, privacidad y persistencia total del progreso académico.

---

## 🚀 Características Principales

* 🔒 **Seguridad y Ciberseguridad Robusta**:
  - Hashing de contraseñas con el algoritmo internacional de máxima seguridad **Argon2id** (64 MB de memoria RAM, 3 iteraciones de tiempo y 4 hilos en paralelo).
  - Autenticación mediante tokens **JWT** en cookies seguras HttpOnly y SameSite=Lax, blindadas contra ataques XSS y CSRF.
  - Aislamiento estricto de roles (student, 	eacher, dmin) y cuentas de usuario.
* 🎯 **Motor Adaptativo Local (Cero IA / Cero APIs externas)**:
  - **Bayesian Knowledge Tracing (BKT)**: Modela el estado latente de maestría conceptual (L_t)$ del alumno tras cada respuesta correcta o incorrecta.
  - **Calibración Elo**: Calibra la destreza del estudiante y la dificultad intrínseca de los ejercicios tras cada intento.
  - Recomendaciones pedagógicas dinámicas y adaptadas al progreso real.
* 📚 **Contenido Curricular Oficial y Riguroso**:
  - **20 temas oficiales en total** (10 de 5.º de Liceo y 10 de 6.º de Liceo).
  - **Banco de 400 ejercicios de física** (mínimo 20 ejercicios por tema), divididos en dificultades Básica, Intermedia y Avanzada.
  - **Respuestas Aleatorizadas**: Opciones barajadas con distribución equilibrada e impredecible entre A, B, C y D sin patrones fijos.
  - Procedimientos de resolución paso a paso y explicaciones pedagógicas formativas.
* 🧮 **Renderizado Matemático Elegante con KaTeX ($\\LaTeX$)**:
  - Fórmulas matemáticas presentadas con tipografía científica auténtica (fracciones verdaderas, vectores $\\vec{F} = m\\vec{a}$, integrales, raíces y matrices).
  - Tarjetas visuales de fórmulas destacadas (ormula-card) y advertencias de seguridad en laboratorio.
  - Soporte dinámico para recargas parciales con **HTMX** sin refrescar la página.
* 📈 **Historial Académico y Promoción de Año**:
  - Aislamiento por período escolar (AcademicPeriod).
  - Al ser promovido de 5.º a 6.º año, el registro histórico del año cursado se archiva cerrado e inalterable, y el nuevo año comienza limpio.

---

## 📋 Temario Oficial Incluido

### 📘 5.º Año — Física (10 Módulos)
1. **Cinemática**: Vectores en el plano cartesiano, Movimiento Rectilíneo Uniforme (MRU), Movimiento Rectilíneo Uniformemente Variado (MRUV), Ecuación de Torricelli y análisis gráfico exhaustivo (-t$, -t$, -t$).
2. **Dinámica**: Las Tres Leyes de Newton, Diagramas de Cuerpo Libre (DCL), descomposición en plano inclinado y modelo de fricción de Amontons-Coulomb (estático y cinético).
3. **Trabajo y Energía**: Trabajo mecánico, Teorema de las Fuerzas Vivas, energía potencial gravitatoria y elástica, conservación de la energía mecánica y potencia.
4. **Cantidad de Movimiento e Impulso**: Teorema del impulso, conservación del momento lineal y colisiones elásticas, inelásticas y plásticas.
5. **Movimiento Circular**: Cinemática angular, relación lineal-angular, aceleración centrípeta, dinámica de curvas y peralte.
6. **Gravitación**: Ley de Gravitación Universal de Newton, campo gravitatorio terrestre, velocidades orbital y de escape, y las Tres Leyes de Kepler.
7. **Estática / Equilibrio**: Primera y segunda condición de equilibrio, momento de una fuerza (torque), brazo de palanca y máquinas simples (palancas).
8. **Fluidos**: Presión hidrostática, principio fundamental de la estática de fluidos, Principio de Pascal (prensa hidráulica) y Principio de Arquímedes (empuje y flotación).
9. **Ondas**: Propagación de ondas ( = \\lambda f$), reflexión, refracción (Ley de Snell), difracción, interferencia, acústica musical y Efecto Doppler.
10. **Electricidad**: Carga eléctrica, Ley de Coulomb, campo eléctrico, potencial eléctrico, Ley de Ohm y circuitos resistivos en serie y paralelo.

### 📕 6.º Año — Física (4 Módulos Especializados)
1. **Electrostática**:
   - Ley de Coulomb vectorial, conservación y cuantización de la carga.
   - Campo eléctrico $\\vec{E}$, propiedades rigurosas de las líneas de fuerza y Ley de Gauss.
   - Potencial escalar $, superficies equipotenciales y energía electrostática.
2. **Circuitos Eléctricos**:
   - Densidad de corriente, Ley de Pouillet ( = \\rho L/A$) y velocidad de arrastre.
   - Ley de Ohm, Efecto Joule y disipación de potencia ( = I^2 R$).
   - Leyes de Kirchhoff: conservación de carga en nodos (LCK) y de energía en mallas cerradas (LTK).
3. **Magnetismo**:
   - Vector campo magnético $\\vec{B}$, inexistencia de monopolos magnéticos.
   - Fuerza magnética de Lorentz sobre cargas libres ($\\vec{F} = q(\\vec{v} \\times \\vec{B})$), regla de la mano derecha y demostración de trabajo nulo (=0$).
   - Fuerza sobre conductores y principio de inducción electromagnética de Faraday-Lenz.
4. **Práctico e Instrumental de Laboratorio**:
   - **El Multímetro / Tester**: Bornes (COM, V/$\\Omega$, mA, 10A), impedancias de entrada, medición segura y prevención crítica de cortocircuitos.
   - **Capacitores y Circuito RC**: Capacidad  = Q/V$, constante de tiempo $\\tau = R \\cdot C$, transitorios de carga y descarga, evolución temporal (\\tau$ al .2\\%$, \\tau$ al .3\\%$) y protocolos de descarga segura.
   - **Resistencias**: Código de colores de 4 y 5 bandas, cálculo de tolerancias, potencia nominal de catálogo, curva de *derating* térmico y prueba de sobrecarga destructiva hacia circuito abierto ( \\to \\infty$).

---

## 🛠️ Stack Tecnológico

| Componente | Tecnología | Propósito |
|---|---|---|
| **Backend** | Python 3.10+ / **FastAPI** | API REST rápida, asíncrona y modular |
| **Base de Datos** | **SQLAlchemy 2.0** + SQLite / PostgreSQL | Abstracción relacional ORM completa |
| **Frontend** | **Jinja2** + **HTMX** + **Tailwind CSS** | Renderizado del servidor moderno, reactivo y sin recargas |
| **Tipografía Matemática** | **KaTeX** | Renderizado instantáneo de fórmulas en $\\LaTeX$ |
| **Seguridad** | **Argon2id** (rgon2-cffi) + **PyJWT** | Cifrado militar de claves y sesiones seguras en cookies |
| **Testing** | **pytest** | Suite de pruebas unitarias y de integración automatizadas |

---

## ⚡ Instalación y Puesta en Marcha

### Requisitos Previos
- Python 3.10 o superior instalado en el sistema.
- Navegador web moderno (Chrome, Firefox, Edge, etc.).

### 1. Clonar o acceder a la carpeta del proyecto
`ash
cd physics_platform
`

### 2. Instalar dependencias
`ash
pip install -r requirements.txt
`

### 3. Ejecución Rápida
Puedes iniciar la plataforma de dos formas:

* **En Windows (Recomendado):**  
  Haz doble clic en el archivo jecutar_plataforma.bat.  
  *Inicia el servidor local y abre automáticamente tu navegador predeterminado.*

* **Vía Consola de Comandos:**
  `ash
  python run.py
  `

El servidor estará disponible en:  
👉 **http://localhost:8000**

---

## 🧪 Ejecución de Pruebas Automatizadas

El proyecto incluye 11 tests automatizados que validan la seguridad criptográfica, el motor BKT/Elo, el flujo web y el banco de preguntas:

`ash
python -m pytest tests/ -v
`

---

## 📁 Estructura del Proyecto

`	ext
physics_platform/
├── app/
│   ├── adaptive/              # Motor adaptativo determinista local (BKT y Elo)
│   │   ├── bkt.py             # Algoritmo Bayesian Knowledge Tracing
│   │   ├── elo.py             # Sistema de calibración de dificultad Elo
│   │   └── engine.py          # Orquestador adaptativo de maestría
│   ├── auth/                  # Autenticación, JWT y control de acceso
│   ├── core/                  # Configuraciones y seguridad (Argon2id)
│   ├── database/              # Modelos ORM (SQLAlchemy 2.0) y motor SQLite
│   ├── exercises/             # Lógica de evaluación y retroalimentación
│   ├── learning/              # Currículo oficial, banco de 400 ejercicios y seeders
│   ├── progress/              # Servicios de progreso, historial y promoción de año
│   └── templates/             # Vistas Jinja2 con HTMX, Tailwind CSS y KaTeX
├── data/                      # Base de datos local SQLite (physics.db)
├── tests/                     # Suite de pruebas automatizadas (11 tests)
├── ejecutar_plataforma.bat    # Lanzador directo de un solo clic para Windows
├── requirements.txt           # Dependencias del proyecto
├── run.py                     # Script de inicio con auto-apertura del navegador
└── README.md                  # Documentación oficial del proyecto
`

---

## 📜 Licencia y Proyección
Diseñado con arquitectura modular apta para adopción institucional en liceos de educación secundaria de Uruguay (CES / ANEP), servidores locales de centros educativos y futura escalabilidad hacia esquemas de licencias multi-institucionales.
