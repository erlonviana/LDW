from flask import Blueprint, jsonify

health_bp = Blueprint('health', __name__)

# healthcheck é rota para verificar a saúde da api
@health_bp.route('/health', methods=['GET']) 
def health_check():
    """
    Health check Endpoint
    ---
    tags:
        - Health
    responses:
        200: 
            description: API está rodando
            schema:
                type: object
                properties:
                    status:
                        type: string
                        example: ok
                    message:
                        type: string
                        example: MergeSkills API OK
    """
    return jsonify({
        "status": "ok",
        "message": "MergeSkills API OK"
    })