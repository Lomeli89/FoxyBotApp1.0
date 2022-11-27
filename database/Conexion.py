import mysql.connector
import pymysql

class DataBase:
    def __init__(self):
        self.conexion = pymysql.connect(
            host='localhost',
            user = 'root',
            password = 'angelus',
            db = 'appdatabase',)

        self.cursor = self.conexion.cursor()
        print("conexion establecida")

    def select_user(self, id):
        sql = 'SELECT id, correo_db, nombre_db FROM usuarios_database WHERE id = {}'.format(id)

        try:
            self.cursor.execute(sql)
            user = self.cursor.fetchone()

            print("Id:", user[0])
            print("Nombre_db:", user[1])
            print("Correo_db:", user[2])

        except Exception as e:
            raise
database = DataBase()