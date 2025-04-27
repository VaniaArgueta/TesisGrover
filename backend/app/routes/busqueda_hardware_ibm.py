from flask import Blueprint, request, jsonify
from app.services.busqueda_hardware_ibm_service import ejecutar_busqueda_hardware_ibm

busqueda_hardware_ibm_bp = Blueprint('busqueda_hardware_ibm', __name__)

@busqueda_hardware_ibm_bp.route('/hardware-ibm', methods=['POST'])
def buscar_con_hardware_ibm():
    filtros = request.get_json()
    resultado = ejecutar_busqueda_hardware_ibm(filtros)
    return jsonify({"mensaje": "Búsqueda en hardware IBM OK.", "resultado": resultado})