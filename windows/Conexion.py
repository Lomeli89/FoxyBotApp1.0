import pymysql
import re



class DataBase:
    def __init__(self):
        self.conexion = pymysql.connect(
            host='localhost',
            user='root',
            password='angelus',
            db='foxybotdb')

        self.cursor = self.conexion.cursor()
        print("conexion establecida")

    def busca_user(self, correo_electronico):
        cur = self.conexion.cursor()
        sql = "SELECT correo_electronico FROM usuarios WHERE correo_electronico ={}".format(correo_electronico)
        cur.execute(sql)
        correox = cur.fetchall()
        cur.close()

        return correox

    def busca_contra(self, password):
        cur = self.conexion.cursor()
        sql = "SELECT password FROM usuarios WHERE password ={}".format(password)
        cur.execute(sql)
        passwordx = cur.fetchall()
        cur.close()
        return passwordx

    def gDatos(self, nombre, apellido, correo_electronico, id_tipo_usuario, estatus, password):
        cur = self.conexion.cursor()
        sql = "INSERT INTO `usuarios` (`nombre`,`apellido`,`correo_electronico`,`id_tipo_usuario`,`estatus`,`password`) VALUES (%s,%s,%s,%s,%s,%s)"
        cur.execute(sql, (format(nombre), (apellido), (correo_electronico), (id_tipo_usuario), (estatus), (password)))
        self.conexion.commit()
        print(nombre, apellido, correo_electronico, id_tipo_usuario, estatus, password)

    def mContenido(self):
        cur = self.conexion.cursor()
        sql = "SELECT * FROM Preguntas"
        cur.execute(sql)
        contenidox = cur.fetchall()
        return contenidox

    def gServicios(self, nombre_servicio):
        cur = self.conexion.cursor()
        sql = "INSERT INTO `servicio` (`nombre_servicio`) VALUES (%s)"
        cur.execute(sql, (format(nombre_servicio)))
        self.conexion.commit()
        print("DB: " + nombre_servicio)
    def gContenido(self, pregunta, informacion, nombre_servicio,palabra_clave):
        cur = self.conexion.cursor()
        sql = "INSERT INTO `preguntas` (`pregunta`,`informacion`,`nombre_servicio`,`palabra_clave`) VALUES (%s,%s,%s,%s)"
        cur.execute(sql, (format(pregunta),(informacion),(nombre_servicio),(palabra_clave)))
        self.conexion.commit()
        cur.close()
        print("DB: " + pregunta +" "+ informacion +" "+nombre_servicio+" "+palabra_clave)

    '''def buscar_usuario_y_contrasena(self, correo_electronico, password):
        cur = self.conexion.cursor()
        # Crea una consulta SQL para buscar un usuario con el email y contraseña especificados.
        sql = "SELECT * FROM usuarios WHERE correo_electronico = ? AND password = ?"

        # Agrega un mensaje de depuración para mostrar los parámetros pasados a la función.
        print("Buscando usuario con correo electrónico: {} y contraseña: {}".format(correo_electronico, password))

        # Ejecuta la consulta y retorna los resultados.
        try:
            # Ejecuta la consulta y retorna los resultados.
            cur.execute(sql, (correo_electronico, password))
            cuentax = cur.fetchall()
            cur.close()

            # Agrega un mensaje de depuración para mostrar el resultado de la consulta SQL.
            print("Resultado de la consulta SQL: {}".format(cuentax))

            return cuentax
        except Exception as e:
            print("error")
    # En caso de error, imprime un mensaje con información so

'''


