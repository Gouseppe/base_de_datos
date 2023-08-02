class Cliente():

    def __init__(self, cedula, nombre=None, whatsapp=None, email=None) -> None:
        self.cedula = cedula
        self.nombre = nombre
        self.whatsapp = whatsapp
        self.email = email

    def to_JSON(self):
        return {
            'cedula': self.cedula,
            'nombre': self.nombre,
            'whatsapp': self.whatsapp,
            'email': self.email
        }
