import pymysql

class DataBase:
    def __init__(self):
        self.conexion = pymysql.connect(
            host='localhost',
            user = 'root',
            password = 'angelus',
            db = 'foxybotdb')

        self.cursor = self.conexion.cursor()
        print("conexion establecida")
    def busca_user(self, correo_electronico):
        cur = self.conexion.cursor()
        sql = "SELECT correo_electronico FROM usuarios WHERE correo_electronico = {}".format(correo_electronico)
        cur.execute(sql)
        correox = cur.fetchall()
        cur.close()
        return correox
    def busca_contra(self, password):
        cur = self.conexion.cursor()
        sql = "SELECT password FROM usuarios WHERE password = {}".format(password)
        cur.execute(sql)
        passwordx = cur.fetchall()
        cur.close()
        return passwordx
    def guardar_correo(self):
        cur = self.conexion.cursor()

        sql = "INSERT INTO usuarios (nombre, apellido, correo_electronico, id_tipo_usuario, estatus, fecha_registro, password) VALUES (%s,%s,%s,%i,%i%,%s,%s)"
        val = (nombre, apellido, correo_electronico, id_tipo_usuario, estatus, fecha_registro, password);

        cur.execute(sql, val)

        DataBase.commit()