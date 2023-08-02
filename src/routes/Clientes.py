from flask import Blueprint, jsonify, request
# Entities
from models.entities.Client import Cliente
# Models
from models.ClientModel import ClientModel

main = Blueprint('Client_blueprint', __name__)

@main.route('')#Metodo GET
def get_Clientes():
    try:
        Clientes = ClientModel.get_Clientes()
        return jsonify(Clientes)
    except Exception as ex:
        return jsonify({'message': str(ex)}), 500


@main.route('', methods=['POST'])
def add_Cliente():
    try:
        nombre = request.json['nombre']
        whatsapp = request.json['whatsapp']
        email = request.json['email']
        cedula = int(request.json['cedula'])
        client = Cliente(cedula, nombre, whatsapp, email)

        affected_rows = ClientModel.add_Cliente(client)

        if affected_rows == 1:
            return jsonify(client.cedula)
        else:
            return jsonify({'message': "Error al insertar un cliente"}), 500

    except Exception as ex:
        return jsonify({'message': str(ex)}), 500


@main.route('/<cedula>', methods=['PUT'])
def update_Cliente(cedula):
    try:
        
        nombre = request.json['nombre']
        whatsapp = request.json['whatsapp']
        email = request.json['email']
        
        client = Cliente(cedula, nombre, whatsapp, email)

        affected_rows = ClientModel.update_Cliente(client)
        
        if affected_rows == 1:
            return jsonify(client.cedula)
        else:
            return jsonify({'message': "No se pudo editara un cliente"}), 404

    except Exception as ex:
        return jsonify({'message': str(ex)}), 500
