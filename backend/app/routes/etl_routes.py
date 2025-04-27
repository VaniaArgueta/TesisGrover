from flask import Blueprint, jsonify
from app.services.etl_service import ejecutar_proceso_etl

etl_bp = Blueprint('etl', __name__)

@etl_bp.route('/ejecutar', methods=['POST'])
def ejecutar_etl():
    mensaje = ejecutar_proceso_etl()
    return jsonify({"mensaje": mensaje})