from flask import Flask
from flasgger import Swagger

def create_app():
    app = Flask(__name__)

    #Configuração do Swagger
    app.config['SWAGGER'] = {
        'title': 'LDW Merge Skills',
        'universion': 3,
        'spec_route': '/apidocs/'
    }

    Swagger(app)

    #Espaço reservado para registrar Blueprints depois
    from routes.health import health_bp
    from routes.courses import courses_bp

    app.register_blueprint(health_bp, url_prefix='/api')
    app.register_blueprint(courses_bp, url_prefix='/api/courses')

    return app
if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)