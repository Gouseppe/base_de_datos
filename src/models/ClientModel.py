from database.db import get_connection
from .entities.Client import Cliente


class ClientModel():

    @classmethod
    def get_Clientes(self):
        try:
            connection = get_connection()
            Clientes = []

            with connection.cursor() as cursor:
                cursor.execute("SELECT * FROM clientes ORDER BY nombre ASC")
                resultado = cursor.fetchall()

                for row in resultado:
                    ClientAux = Cliente(row[0], row[1], row[2], row[3])
                    Clientes.append(ClientAux.to_JSON())

            connection.close()
            return Clientes
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def get_Cliente(self, id):
        try:
            connection = get_connection()

            with connection.cursor() as cursor:
                cursor.execute("SELECT * FROM clientes WHERE cedula = %s", (id,))
                row = cursor.fetchone()

                cliente = None
                
                if row:
                    cliente = Cliente(row[0], row[1], row[2], row[3])
                    cliente = cliente.to_JSON()

            connection.close()
            return cliente
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def add_Cliente(self, Client):
        try:
            connection = get_connection()

            with connection.cursor() as cursor:
                cursor.execute("""INSERT INTO clientes (cedula, nombre, whatsapp, email) 
                                VALUES (%s, %s, %s, %s)""", (Client.cedula, Client.nombre, Client.whatsapp, Client.email))
                resultado = cursor.rowcount
                connection.commit()

            connection.close()
            return resultado
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def update_Cliente(self, Client):
        try:
            connection = get_connection()

            with connection.cursor() as cursor:
                cursor.execute("""UPDATE clientes SET nombre = %s, whatsapp = %s, email = %s 
                                WHERE cedula = %s""", (Client.nombre, Client.whatsapp, Client.email, Client.cedula))
                resultado = cursor.rowcount
                connection.commit()

            connection.close()
            return resultado
        except Exception as ex:
            raise Exception(ex)
