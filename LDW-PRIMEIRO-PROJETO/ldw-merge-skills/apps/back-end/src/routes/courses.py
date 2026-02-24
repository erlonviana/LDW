from typing import List, Dict, Any
from flask import Blueprint, jsonify

courses_bp = Blueprint('courses', __name__)

# Dados Mockados (simulando banco de dados)
COURSES_DB: List[Dict[str, Any]] = [
    {
        "id": 1,
        "title": "Python Fundamentos",
        "description": "Aprenda o básico de Python",
        "total_lessons": 4,
        "active": True
    },
    {
        "id": 2,
        "title": "Flask API Masterclass",
        "description": "Crie APIs profissionais",
        "total_lessons": 10,
        "active": True
    }
]

@courses_bp.route('/', methods=['GET'])
def get_courses():
    """
    Lista todos os cursos disponíveis
    ---
    tags:
      - cursos
    responses:
      200:
        description: Lista de cursos
        schema:
          type: array
          items:
            type: object
            properties:
              id:
                type: integer
              title:
                type: string
              description:
                type: string
              total_lessons:
                type: integer
              active:
                type: boolean
    """
    return jsonify(COURSES_DB)

@courses_bp.route('/<int:course_id>', methods=['GET'])
def get_course_by_id(course_id) :
    course = next()
    