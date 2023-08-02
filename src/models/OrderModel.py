from database.db import get_connection
from .entities.Pedido import Pedido


class OrderModel():

    @classmethod
    def get_Pedidos(self, date, status, cedula,tipo_filtro ):

        
        try:
            connection = get_connection()
            Pedidos = []

            with connection.cursor() as cursor:
                if tipo_filtro == 1:
                    cursor.execute("SELECT * FROM pedidos WHERE date(datatime)=%s and status= %s and cedula=%s", (date,status,cedula))
                elif tipo_filtro == 2:
                    cursor.execute("SELECT * FROM pedidos WHERE date(datatime)=%s and status= %s", (date,status))
                elif tipo_filtro == 3:
                    cursor.execute("SELECT * FROM pedidos WHERE date(datatime)=%s and cedula=%s", (date,cedula))
                elif tipo_filtro == 4:
                    cursor.execute("SELECT * FROM pedidos WHERE status= %s and cedula=%s", (status,cedula))
                elif tipo_filtro == 5:
                    cursor.execute("SELECT * FROM pedidos WHERE date(datatime)=%s", (date,))
                elif tipo_filtro == 6:
                    cursor.execute("SELECT * FROM pedidos WHERE status=%s", (status,))
                elif tipo_filtro == 7:
                    cursor.execute("SELECT * FROM pedidos WHERE cedula=%s", (cedula,))
                else:
                    cursor.execute("SELECT * FROM pedidos")
                
                resultset = cursor.fetchall()
                
                for row in resultset:
                    
                    pedido = Pedido(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10], row[11])
                    Pedidos.append(pedido.to_JSON())

            connection.close()
            return Pedidos
        except Exception as ex:
            raise Exception(ex)
    

    @classmethod
    def get_Pedido(self, id):
        try:
            connection = get_connection()

            with connection.cursor() as cursor:
                cursor.execute("SELECT * FROM pedidos WHERE ID = %s", (id,))
                row = cursor.fetchone()

                Pedido = None
                if row:
                    Pedido = Pedido(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10], row[11])
                    Pedido = Pedido.to_JSON()

            connection.close()
            return Pedido
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def add_Pedido(self, Pedido):
        
        try:
            
            connection = get_connection()
           
            with connection.cursor() as cursor:
                cursor.execute("""INSERT INTO pedidos (quantity, delivery_amount, total, payments_screenshot, status, datatime, city, municipality, payment_method, remarks, Cedula) 
                    VALUES (%s, %s, %s, %s::bytea, %s, localtimestamp(0), %s, %s, %s, %s, %s)""", (Pedido.quantity, Pedido.delivery_amount, Pedido.total, Pedido.payment_screenshot, Pedido.status, Pedido.city, Pedido.municipality, Pedido.payment_method, Pedido.remarks, Pedido.cedula))
                affected_rows = cursor.rowcount
                connection.commit()

            connection.close()
            return affected_rows
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def update_Pedido(self, Pedido):
        try:
            connection = get_connection()

            with connection.cursor() as cursor:
                cursor.execute("""UPDATE pedidos SET cantHamb= %s, montoDelivery= %s, totalPagar= %s, screenshot= %s, status= %s, fechaHoraPedido= %s, ciudad= %s, municipio= %s, metodoPago= %s, observaciones= %s, Cedula = %s 
                    WHERE ID = %s""", (Pedido.quantity, Pedido.delivery_amount, Pedido.total, Pedido.payment_screenshot, Pedido.status, Pedido.datetime, Pedido.city, Pedido.municipality, Pedido.payment_method, Pedido.remarks, Pedido.cedula, Pedido.order_number,))
                affected_rows = cursor.rowcount
                connection.commit()

            connection.close()
            return affected_rows
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def status_Pedido(self, Num_orden, status):
        try:
            connection = get_connection()

            with connection.cursor() as cursor:
                cursor.execute("""UPDATE pedidos SET  status= %s WHERE order_number = %s""", (status, Num_orden))
                affected_rows = cursor.rowcount
                connection.commit()

                
            connection.close()
            return affected_rows
        except Exception as ex:
            raise Exception(ex)
        

    # @classmethod
    # def delete_Pedido(self, Pedido):
    #     try:
    #         connection = get_connection()

    #         with connection.cursor() as cursor:
    #             cursor.execute("DELETE FROM Pedido WHERE id = %s", (Pedido.id,))
    #             affected_rows = cursor.rowcount
    #             connection.commit()

    #         connection.close()
    #         return affected_rows
    #     except Exception as ex:
    #         raise Exception(ex)
