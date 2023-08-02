from flask import Blueprint, jsonify, request
import datetime

# Entities
from models.entities.Pedido import Pedido

# Models
from models.OrderModel import OrderModel
from models.ClientModel import ClientModel

main = Blueprint('Pedido_blueprint', __name__)


@main.route('')
def get_Pedidos():
    
    
    # if(request.args.keys)
    date = request.args.get('date')
    status = request.args.get('status')
    cedula = request.args.get('cedula')
    
    try:
        if(date and status and cedula):
            print('todo')
            Pedidos = OrderModel.get_Pedidos(date, status, cedula, 1)
        elif(date and status and not cedula):
            print('date y status')
            Pedidos = OrderModel.get_Pedidos(date, status, cedula, 2)
        elif(date and not status and cedula):
            print('date y cedula')
            Pedidos = OrderModel.get_Pedidos(date, status, cedula, 3)
        elif(not date and status and cedula):
            print('status y cedula')
            Pedidos = OrderModel.get_Pedidos(date, status, cedula, 4)
        elif(date and not status and not cedula):
            print('solo date')
            Pedidos = OrderModel.get_Pedidos(date, status, cedula, 5)
        elif(status and not date and not cedula):
            print('solo status')
            Pedidos = OrderModel.get_Pedidos(date, status, cedula, 6)
        elif(cedula and not date and not status):
            print('solo cedula')
            Pedidos = OrderModel.get_Pedidos(date, status, cedula, 7)
        else:
            print('todo')
            Pedidos = OrderModel.get_Pedidos(date, status, cedula, 8)
        
        return jsonify(Pedidos)
    except Exception as ex:
        return jsonify({'message': str(ex)}), 500


@main.route('/<order_number>')
def get_Pedido(order_number):
    try:
        order = OrderModel.get_Pedido(order_number)
        if order:
            return jsonify(order)
        else:
            return jsonify({}), 404
    except Exception as ex:
        return jsonify({'message': str(ex)}), 500


@main.route('', methods=['POST'])
def add_Pedido():
    try:
        
        cedula = int(request.json['cedula'])
        buscar = ClientModel.get_Cliente(cedula)
        
        result = 0
        if buscar:
            
            quantity = int(request.json['quantity'])
            
            payment_method = request.json['payment_method']
            remarks = request.json['remarks']
            
            city = request.json['city']
            municipality = request.json['municipality']
            payment_screenshot = None
            status = 'Pendiente'
            
            if city and municipality:
                delivery_amount = 2
                if municipality == 'Maneiro':
                    delivery_amount = 0
            total = quantity * 5 + delivery_amount

            # order = Pedido(payment_method, cedula, total, status, delivery_amount, remarks, city, municipality, payment_screenshot, quantity)
            order = Pedido(payment_method=payment_method,quantity=quantity,remarks=remarks,city=city,municipality=municipality,cedula=cedula,payment_screenshot=payment_screenshot, status=status, delivery_amount=delivery_amount,total=total)
            
            
            result = OrderModel.add_Pedido(order)

        if result == 1:
            return "fino"
        else:
            return jsonify({'message': "Error on insert"}), 500

    except Exception as ex:
        return jsonify({'message': str(ex)}), 500

@main.route('/<order_number>/status', methods=['PATCH'])
def status_Pedido(order_number):
    try:
        status = request.json['status']
        order = Pedido(order_number,  status) 
        result = OrderModel.status_Pedido(order_number, status)

        
        if result == 1:
            return jsonify(order.order_number)
        else:
            return jsonify({'message': "No status updated"}), 404
    except Exception as ex:
       return jsonify({'message': str(ex)}), 500


# @main.route('/<order_number>', methods=['PUT'])
# def update_Pedido(order_number):
#     try:
#         cedula = int(request.json['cedula'])
#         quantity = int(request.json['quantity'])
#         payment_method = request.json['payment_method']
#         remarks = request.json['remarks']
#         city = request.json['city']
#         municipality = request.json['municipality']
#         payment_screenshot = None
#         status = 'Pendiente'
#         Datetime = datetime.datetime.now()
#         if city and municipality:
#             delivery_amount = 2
#             if municipality == 'Maneiro':
#                 delivery_amount = 0
#         total = quantity * 5 + delivery_amount

#         order = Pedido(order_number, payment_method, quantity, remarks, city, municipality, cedula, payment_screenshot, status, delivery_amount, Datetime, total)

#         result = OrderModel.update_Pedido(order)

#         if result == 1:
#             return jsonify(order.order_number)
#         else:
#             return jsonify({'message': "No Pedido updated"}), 404

#     except Exception as ex:
#         return jsonify({'message': str(ex)}), 500