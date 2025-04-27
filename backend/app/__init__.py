from flask import Flask

def create_app():
    app = Flask(__name__)

    from app.routes.etl_routes import etl_bp
    from app.routes.busqueda_simulacion import busqueda_simulacion_bp
    from app.routes.busqueda_hardware_ibm import busqueda_hardware_ibm_bp

    app.register_blueprint(etl_bp, url_prefix='/etl')
    app.register_blueprint(busqueda_simulacion_bp, url_prefix='/busqueda')
    app.register_blueprint(busqueda_hardware_ibm_bp, url_prefix='/busqueda')

    return app