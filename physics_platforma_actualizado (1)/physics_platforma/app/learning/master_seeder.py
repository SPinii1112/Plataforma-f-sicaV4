# -*- coding: utf-8 -*-
import json
import os
import random
from pathlib import Path
from sqlalchemy.orm import Session
from app.database.engine import SessionLocal, Base, engine
from app.database.models import Module, Topic, Concept, Exercise, ExerciseConcept, Attempt, TopicProgress, ConceptMastery

# 1. Cargar teorias
with open('app/learning/theory_5to.json', 'r', encoding='utf-8') as f:
    theory_5to = json.load(f)

with open('app/learning/theory_6to.json', 'r', encoding='utf-8') as f:
    theory_6to = json.load(f)

# 2. Importar generadores de preguntas
from app.learning.questions_5to import get_cinematica_questions, get_dinamica_questions
from app.learning.questions_5to_part2 import get_trabajo_energia_questions
from app.learning.questions_5to_part3 import get_momento_lineal_questions
from app.learning.questions_5to_circular import generate_circular_questions
from app.learning.questions_5to_grav_stat_fluids import get_gravitacion_questions, get_estatica_questions, get_fluidos_questions
from app.learning.questions_5to_waves_elec import get_ondas_questions, get_electricidad_5to_questions

from app.learning.questions_6to_part1 import get_coulomb_questions
from app.learning.questions_6to_part2 import get_campo_lineas_questions
from app.learning.questions_6to_rest import get_potencial_questions
from app.learning.questions_6to_final import get_circuitos_questions
from app.learning.questions_6to_rest2 import get_kirchhoff_questions
from app.learning.questions_6to_mag_ind import get_magnetismo_questions, get_induccion_questions
from app.learning.questions_6to_practico import get_tester_questions, get_capacitores_questions, get_resistencias_questions


# 2b. Importar generadores de preguntas adicionales (20 por tema con hints y balance)
from app.learning.questions_5to_ext import (
    get_questions_cinematica_extra,
    get_questions_dinamica_extra,
    get_questions_trabajo_energia_extra,
    get_questions_cantidad_movimiento_extra,
    get_questions_mov_circular_extra,
    get_questions_gravitacion_extra,
    get_questions_estatica_extra,
    get_questions_fluidos_extra,
    get_questions_ondas_extra,
    get_questions_electricidad_5to_extra,
)
from app.learning.questions_6to_ext import (
    get_questions_coulomb_extra,
    get_questions_campo_electrico_extra,
    get_questions_potencial_electrico_extra,
    get_questions_circuitos_corriente_extra,
    get_questions_kirchhoff_extra,
    get_questions_campo_magnetico_extra,
    get_questions_fuerza_magnetica_extra,
    get_questions_induccion_extra,
    get_questions_capacitores_rc_extra,
    get_questions_practico_tester_extra,
)

print('Modulos de preguntas importados exitosamente.')

def seed_database():
    db: Session = SessionLocal()
    try:
        # Limpiar unicamente tablas de contenido educativo, PRESERVANDO a todos los usuarios
        db.query(ExerciseConcept).delete()
        db.query(Attempt).delete()
        db.query(Exercise).delete()
        db.query(ConceptMastery).delete()
        db.query(Concept).delete()
        db.query(TopicProgress).delete()
        db.query(Topic).delete()
        db.query(Module).delete()
        db.commit()
        print('Tablas de contenido educativo limpiadas (Usuarios preservados intactos).')

        # ========================================================
        # DEFINICION DE MODULOS Y TEMAS DE 5.º ANO
        # ========================================================
        modules_5to = [
            {
                'title': 'Cinemática',
                'slug': '5to-cinematica',
                'order': 1,
                'topics': [{
                    'title': 'Cinemática: MRU, MRUV, Vectores y Gráficos',
                    'slug': '5to-cinematica-completa',
                    'summary': 'Estudio integral del movimiento rectilíneo, vectores, ecuaciones horarias y análisis gráfico x-t, v-t, a-t.',
                    'theory_content': theory_5to['5to-cinematica-completa'],
                    'questions': get_cinematica_questions() + get_questions_cinematica_extra(),
                    'concepts': ['MRU', 'MRUV', 'Vectores', 'Gráficos x-t v-t']
                }]
            },
            {
                'title': 'Dinámica',
                'slug': '5to-dinamica',
                'order': 2,
                'topics': [{
                    'title': 'Dinámica: Leyes de Newton y Rozamiento',
                    'slug': '5to-leyes-newton-dinamica',
                    'summary': 'Las Tres Leyes de Newton, diagramas de cuerpo libre, plano inclinado y fricción estática y cinética.',
                    'theory_content': theory_5to['5to-leyes-newton-dinamica'],
                    'questions': get_dinamica_questions() + get_questions_dinamica_extra(),
                    'concepts': ['Leyes de Newton', 'Fricción', 'Plano Inclinado']
                }]
            },
            {
                'title': 'Trabajo y Energía',
                'slug': '5to-trabajo-energia',
                'order': 3,
                'topics': [{
                    'title': 'Trabajo Mecánico, Energía y Potencia',
                    'slug': '5to-trabajo-mecanico-energia',
                    'summary': 'Trabajo de fuerzas constantes, energía cinética y potencial, teorema de las fuerzas vivas y conservación.',
                    'theory_content': theory_5to['5to-trabajo-mecanico-energia'],
                    'questions': get_trabajo_energia_questions() + get_questions_trabajo_energia_extra(),
                    'concepts': ['Trabajo Mecánico', 'Energía Cinética', 'Conservación de Energía']
                }]
            },
            {
                'title': 'Cantidad de Movimiento e Impulso',
                'slug': '5to-momento-impulso',
                'order': 4,
                'topics': [{
                    'title': 'Momento Lineal, Impulso y Choques',
                    'slug': '5to-momento-lineal-choques',
                    'summary': 'Teorema del impulso, conservación del momento lineal, choques elásticos y plásticos.',
                    'theory_content': theory_5to['5to-momento-lineal-choques'],
                    'questions': get_momento_lineal_questions() + get_questions_cantidad_movimiento_extra(),
                    'concepts': ['Momento Lineal', 'Impulso', 'Colisiones']
                }]
            },
            {
                'title': 'Movimiento Circular',
                'slug': '5to-movimiento-circular',
                'order': 5,
                'topics': [{
                    'title': 'Movimiento Circular: MCU, MCUV y Fuerza Centrípeta',
                    'slug': '5to-mcu-fuerza-centripeta',
                    'summary': 'Cinemática y dinámica rotacional, aceleración centrípeta y curvas con peralte.',
                    'theory_content': theory_5to['5to-mcu-fuerza-centripeta'],
                    'questions': generate_circular_questions() + get_questions_mov_circular_extra(),
                    'concepts': ['MCU', 'Aceleración Centrípeta', 'Fuerza Centrípeta']
                }]
            },
            {
                'title': 'Gravitación',
                'slug': '5to-gravitacion',
                'order': 6,
                'topics': [{
                    'title': 'Gravitación Universal y Leyes de Kepler',
                    'slug': '5to-gravitacion-kepler',
                    'summary': 'Ley de atracción universal de Newton, aceleración gravitatoria y leyes del movimiento planetario.',
                    'theory_content': theory_5to['5to-gravitacion-kepler'],
                    'questions': get_gravitacion_questions() + get_questions_gravitacion_extra(),
                    'concepts': ['Gravitación Universal', 'Leyes de Kepler', 'Velocidad Orbital']
                }]
            },
            {
                'title': 'Estática / Equilibrio',
                'slug': '5to-estatica-equilibrio',
                'order': 7,
                'topics': [{
                    'title': 'Estática: Condiciones de Equilibrio y Torque',
                    'slug': '5to-estatica-torque',
                    'summary': 'Primera y segunda condición de equilibrio mecánico, momento de una fuerza y máquinas simples.',
                    'theory_content': theory_5to['5to-estatica-torque'],
                    'questions': get_estatica_questions() + get_questions_estatica_extra(),
                    'concepts': ['Torque', 'Condiciones de Equilibrio', 'Palancas']
                }]
            },
            {
                'title': 'Fluidos',
                'slug': '5to-fluidos',
                'order': 8,
                'topics': [{
                    'title': 'Fluidos: Presión, Pascal y Principio de Arquímedes',
                    'slug': '5to-fluidos-presion-empuje',
                    'summary': 'Hidrostática, principio fundamental, prensa hidráulica y flotabilidad de cuerpos.',
                    'theory_content': theory_5to['5to-fluidos-presion-empuje'],
                    'questions': get_fluidos_questions() + get_questions_fluidos_extra(),
                    'concepts': ['Presión Hidrostática', 'Principio de Pascal', 'Principio de Arquímedes']
                }]
            },
            {
                'title': 'Ondas',
                'slug': '5to-ondas',
                'order': 9,
                'topics': [{
                    'title': 'Ondas, Acústica y Fenómenos Ondulatorios',
                    'slug': '5to-ondas-sonido-fenomenos',
                    'summary': 'Propagación de ondas, ecuación fundamental v=λf, sonido, Doppler, reflexión y refracción.',
                    'theory_content': theory_5to['5to-ondas-sonido-fenomenos'],
                    'questions': get_ondas_questions() + get_questions_ondas_extra(),
                    'concepts': ['Ecuación de Onda', 'Acústica', 'Efecto Doppler']
                }]
            },
            {
                'title': 'Electricidad',
                'slug': '5to-electricidad',
                'order': 10,
                'topics': [{
                    'title': 'Electricidad: Carga, Campo, Potencial y Circuitos Básicos',
                    'slug': '5to-electricidad-circuitos-basicos',
                    'summary': 'Fundamentos electrostáticos, corriente continua, ley de Ohm y asociaciones serie/paralelo.',
                    'theory_content': theory_5to['5to-electricidad-circuitos-basicos'],
                    'questions': get_electricidad_5to_questions() + get_questions_electricidad_5to_extra(),
                    'concepts': ['Ley de Coulomb', 'Ley de Ohm', 'Asociación Serie Paralelo']
                }]
            }
        ]

        # ========================================================
        # DEFINICION DE MODULOS Y TEMAS DE 6.º ANO
        # ========================================================
        modules_6to = [
            {
                'title': 'Electrostática',
                'slug': '6to-electrostatica',
                'order': 1,
                'topics': [
                    {
                        'title': 'Ley de Coulomb y Carga Eléctrica',
                        'slug': '6to-ley-de-coulomb',
                        'summary': 'Cuantización y conservación de la carga, ley de Coulomb vectorial y principio de superposición.',
                        'theory_content': theory_6to['6to-ley-de-coulomb'],
                        'questions': get_coulomb_questions() + get_questions_coulomb_extra(),
                        'concepts': ['Ley de Coulomb Vectorial', 'Cuantización de Carga', 'Superposición Electrostática']
                    },
                    {
                        'title': 'Campo Eléctrico y Líneas de Campo',
                        'slug': '6to-campo-lineas',
                        'summary': 'Definición operacional del campo E, propiedades rigurosas de líneas de fuerza y ley de Gauss.',
                        'theory_content': theory_6to['6to-campo-lineas'],
                        'questions': get_campo_lineas_questions() + get_questions_campo_electrico_extra(),
                        'concepts': ['Campo Eléctrico', 'Líneas de Campo', 'Ley de Gauss']
                    },
                    {
                        'title': 'Potencial Eléctrico y Energía Potencial Electrostática',
                        'slug': '6to-potencial-energia-electrica',
                        'summary': 'Energía potencial en campos conservativos, potencial escalar V, superficies equipotenciales y relación E = -dV/dx.',
                        'theory_content': theory_6to['6to-potencial-energia-electrica'],
                        'questions': get_potencial_questions() + get_questions_potencial_electrico_extra(),
                        'concepts': ['Potencial Eléctrico', 'Energía Potencial', 'Equipotenciales']
                    }
                ]
            },
            {
                'title': 'Circuitos Eléctricos',
                'slug': '6to-circuitos-electricos',
                'order': 2,
                'topics': [
                    {
                        'title': 'Corriente, Tensión, Resistencia y Ley de Ohm',
                        'slug': '6to-corriente-tension-ohm',
                        'summary': 'Dinámica de electrones de conducción, Ley de Pouillet, efecto Joule y potencia disipada.',
                        'theory_content': theory_6to['6to-corriente-tension-ohm'],
                        'questions': get_circuitos_questions() + get_questions_circuitos_corriente_extra(),
                        'concepts': ['Ley de Pouillet', 'Ley de Ohm', 'Efecto Joule']
                    },
                    {
                        'title': 'Leyes de Kirchhoff (Nodos y Mallas)',
                        'slug': '6to-leyes-kirchhoff',
                        'summary': 'Conservación de carga en nodos (LCK) y de energía en mallas cerradas (LTK) con convención de signos.',
                        'theory_content': theory_6to['6to-leyes-kirchhoff'],
                        'questions': get_kirchhoff_questions() + get_questions_kirchhoff_extra(),
                        'concepts': ['Kirchhoff Nodos', 'Kirchhoff Mallas', 'Redes Eléctricas']
                    }
                ]
            },
            {
                'title': 'Magnetismo',
                'slug': '6to-magnetismo',
                'order': 3,
                'topics': [
                    {
                        'title': 'Campo Magnético y Fuerza de Lorentz',
                        'slug': '6to-campo-fuerza-magnetica',
                        'summary': 'Vector inducción magnética B, fuerza sobre cargas en movimiento (F ⊥ v, trabajo W=0) y regla de la mano derecha.',
                        'theory_content': theory_6to['6to-campo-fuerza-magnetica'],
                        'questions': get_magnetismo_questions() + get_questions_campo_magnetico_extra() + get_questions_fuerza_magnetica_extra(),
                        'concepts': ['Fuerza de Lorentz', 'Regla Mano Derecha', 'Fuerza Magnética']
                    },
                    {
                        'title': 'Inducción Electromagnética (Faraday y Lenz)',
                        'slug': '6to-induccion-faraday-lenz',
                        'summary': 'Flujo magnético, ley de Faraday, principio de oposición de Lenz y corrientes parásitas.',
                        'theory_content': theory_6to['6to-induccion-faraday-lenz'],
                        'questions': get_induccion_questions() + get_questions_induccion_extra(),
                        'concepts': ['Flujo Magnético', 'Ley de Faraday', 'Ley de Lenz']
                    }
                ]
            },
            {
                'title': 'Práctico e Instrumental',
                'slug': '6to-practico-instrumental',
                'order': 4,
                'topics': [
                    {
                        'title': 'El Tester / Multímetro: Funcionamiento, Partes y Medición Segura',
                        'slug': '6to-tester-multimetro',
                        'summary': 'Partes del multímetro, funciones (voltímetro, amperímetro, óhmetro), conexión correcta y prevención de cortocircuitos.',
                        'theory_content': theory_6to['6to-tester-multimetro'],
                        'questions': get_tester_questions() + get_questions_practico_tester_extra(),
                        'concepts': ['Multímetro Digital', 'Conexión Segura', 'Prevención de Cortocircuitos']
                    },
                    {
                        'title': 'Capacitores: Carga, Descarga RC y Mantenimiento de Carga',
                        'slug': '6to-capacitores-rc',
                        'summary': 'Capacitancia C=Q/V, constante de tiempo τ=RC, transitorios de carga/descarga y protocolos de descarga segura.',
                        'theory_content': theory_6to['6to-capacitores-rc'],
                        'questions': get_capacitores_questions() + get_questions_capacitores_rc_extra(),
                        'concepts': ['Capacitancia', 'Constante Tau RC', 'Transitorios de Carga']
                    },
                    {
                        'title': 'Resistencias: Código de Colores, Disipación y Pruebas de Estrés',
                        'slug': '6to-resistencias-colores-estres',
                        'summary': 'Código de 4 y 5 bandas, tolerancias, potencias normalizadas, derating y comportamiento ante sobrecarga térmica.',
                        'theory_content': theory_6to['6to-resistencias-colores-estres'],
                        'questions': get_resistencias_questions() + get_questions_practico_tester_extra(),
                        'concepts': ['Código de Colores', 'Potencia Nominal', 'Estrés Térmico']
                    }
                ]
            }
        ]

        total_topics = 0
        total_exercises = 0
        answer_distribution = {'A': 0, 'B': 0, 'C': 0, 'D': 0}

        def process_year(year_num, modules_list):
            nonlocal total_topics, total_exercises
            for m_idx, m_data in enumerate(modules_list, 1):
                mod = Module(
                    year_level=year_num,
                    name=m_data['title'],
                    slug=m_data['slug'],
                    description=f'Módulo oficial de física para {year_num}.º año de educación media en Uruguay.',
                    order_index=m_idx
                )
                db.add(mod)
                db.flush()

                for t_idx, t_data in enumerate(m_data['topics'], 1):
                    total_topics += 1
                    topic = Topic(
                        module_id=mod.id,
                        name=t_data['title'],
                        slug=t_data['slug'],
                        summary=t_data['summary'],
                        theory_content=t_data['theory_content'],
                        estimated_minutes=35,
                        order_index=t_idx
                    )
                    db.add(topic)
                    db.flush()

                    # Conceptos del tema
                    concept_objs = []
                    for c_name in t_data['concepts']:
                        concept = Concept(
                            topic_id=topic.id,
                            name=c_name,
                            description=f'Concepto fundamental: {c_name}'
                        )
                        db.add(concept)
                        db.flush()
                        concept_objs.append(concept)

                    # Preguntas del tema (mínimo 20)
                    questions = t_data['questions']
                    for q in questions:
                        total_exercises += 1
                        correct_opt = q['correct']
                        answer_distribution[correct_opt] += 1

                        ex = Exercise(
                            topic_id=topic.id,
                            exercise_type='multiple_choice',
                            difficulty=q['difficulty'],
                            statement=q['statement'],
                            options=q['options'],
                            correct_answer=correct_opt,
                            solution_steps=q['solution'],
                            explanation=q['explanation'],
                            elo_rating=float(q['elo']),
                            is_active=True,
                            common_errors={"hint": q.get('hint', '¿Revisaste qué fórmula o principio físico aplica?')}
                        )
                        db.add(ex)
                        db.flush()

                        # Vincular con el primer concepto representativo
                        if concept_objs:
                            assoc = ExerciseConcept(exercise_id=ex.id, concept_id=concept_objs[0].id)
                            db.add(assoc)

        process_year(5, modules_5to)
        process_year(6, modules_6to)

        db.commit()
        print('========================================================')
        print(f'SEEMBRADO MAESTRO COMPLETADO:')
        print(f'Total de Temas: {total_topics} (10 de 5to + 10 de 6to)')
        print(f'Total de Ejercicios: {total_exercises}')
        print(f'Distribución de Opciones Correctas: {answer_distribution}')
        print('========================================================')

    finally:
        db.close()

if __name__ == '__main__':
    seed_database()
