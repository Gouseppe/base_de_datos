from utils.DateFormat import DateFormat

    
class Pedido():
    def __init__(self, order_number = None, payment_method=None, quantity=None, remarks=None, city=None, municipality=None, cedula=None, payment_screenshot=None, status='Pendiente', delivery_amount=None,datatime = None, total=None) -> None:
        self.order_number = order_number
        self.quantity = quantity
        self.payment_method = payment_method
        self.remarks = remarks
        self.city = city
        self.municipality = municipality
        self.cedula = cedula
        self.payment_screenshot = payment_screenshot
        self.status = status
        self.delivery_amount = delivery_amount
        self.total = total
        self.datatime = datatime

    def to_JSON(self):
        return {
            'order_number' : self.order_number,
            'quantity': self.quantity,
            'payment_method': self.payment_method,
            'remarks': self.remarks,
            'city': self.city,
            'municipality': self.municipality,
            'cedula': self.cedula,
            'payment_screenshot': self.payment_screenshot,
            'status': self.status,
            'delivery_amount': self.delivery_amount,
            'datatime' : self.datatime,
            'total': self.total
        }
