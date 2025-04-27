from flask import Blueprint, request, jsonify
from app.services.busqueda_simulacion_service import ejecutar_busqueda_simulacion

busqueda_simulacion_bp = Blueprint('busqueda_simulacion', __name__)

@busqueda_simulacion_bp.route('/simulacion', methods=['POST'])
def buscar_con_simulacion():
    filtros = request.get_json()
    resultado = ejecutar_busqueda_simulacion(filtros)
    return jsonify({"mensaje": "Búsqueda simulada OK", "resultado": resultado})