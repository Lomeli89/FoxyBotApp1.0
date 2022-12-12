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
    def buscar_usuarios(self, correo_electronico):
        cur = self.conexion.cursor()
        sql = "SELECT * FROM usuarios WHERE correo_electronico = {}".format(correo_electronico)
        cur.execute(sql)
        busuax = cur.fetchall()
        cur.close()
        return busuax
    def actualizar_usuario(self, id_usuarios, nombre, apellido, correo_electronico, id_tipo_usuario, password, numero_empleado):
        cur = self.conexion.cursor()
        sql = "UPDATE usuarios SET nombre ='{}', apellido ='{}', correo_electronico ='{}', id_tipo_usuario ='{}', password ='{}', numero_empleado = '{}' WHERE id_usuarios ='{}'".format( nombre, apellido, correo_electronico, id_tipo_usuario,password,numero_empleado,id_usuarios)
        cur.execute(sql)
        a = cur.rowcount
        self.conexion.commit()
        cur.close()
        return a
    def gDatos(self, nombre, apellido, correo_electronico, id_tipo_usuario, estatus, password):
        cur = self.conexion.cursor()
        sql = "INSERT INTO `usuarios` (`nombre`,`apellido`,`correo_electronico`,`id_tipo_usuario`,`estatus`,`password`) VALUES (%s,%s,%s,%s,%s,%s)"
        cur.execute(sql, (format(nombre), (apellido), (correo_electronico), (id_tipo_usuario), (estatus), (password)))
        self.conexion.commit()
        print(nombre, apellido, correo_electronico, id_tipo_usuario, estatus, password)
    def bot_responde_pregunta(self, palabra_clave):
        cur = self.conexion.cursor()
        sql = "SELECT * FROM preguntas WHERE palabra_clave = {}".format(palabra_clave)
        cur.execute(sql)
        p1reguntax = cur.fetchall()
        cur.close()
        return p1reguntax
    def mContenido(self):
        cur = self.conexion.cursor()
        sql = "SELECT * FROM Preguntas"
        cur.execute(sql)
        contenidox = cur.fetchall()
        print(contenidox)
        return contenidox
    def mUsuarios(self):
        cur = self.conexion.cursor()
        sql = "SELECT * FROM usuarios"
        cur.execute(sql)
        usuariox = cur.fetchall()
        print(usuariox)
        return usuariox
    def gContenido(self, pregunta, informacion, nombre_servicio,palabra_clave):
        cur = self.conexion.cursor()
        sql = "INSERT INTO `preguntas` (`pregunta`,`informacion`,`nombre_servicio`,`palabra_clave`) VALUES (%s,%s,%s,%s)"
        cur.execute(sql, (format(pregunta),(informacion),(nombre_servicio),(palabra_clave)))
        self.conexion.commit()
        cur.close()
        print("DB: " + pregunta +" "+ informacion +" "+nombre_servicio+" "+palabra_clave)

    def buscar_solucion(self, pregunta):
        cur = self.conexion.cursor()
        sql = "SELECT * FROM preguntas WHERE pregunta ={}".format(pregunta)
        cur.execute(sql)
        preguntax = cur.fetchall()
        cur.close()
        return preguntax
    def eliminar_solucion(self,pregunta):
        cur = self.conexion.cursor()
        sql = "DELETE FROM preguntas WHERE pregunta = {}".format(pregunta)
        cur.execute(sql)
        self.conexion.commit()
        cur.close()
    def actualizar_solucion(self, id_pregunta, pregunta, informacion, nombre_servicio, palabra_clave):
        cur = self.conexion.cursor()
        sql = "UPDATE preguntas SET pregunta ='{}', informacion ='{}', nombre_servicio ='{}', palabra_clave ='{}' WHERE id_pregunta ='{}'".format(pregunta,informacion,nombre_servicio,palabra_clave,id_pregunta)
        cur.execute(sql)
        a = cur.rowcount
        self.conexion.commit()
        cur.close()
        return a
