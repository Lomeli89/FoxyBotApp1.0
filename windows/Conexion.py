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
        sql = "SELECT usuarios FROM usuarios WHERE correo_electronico ={}".format(correo_electronico)
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
    def guardarDatos(self):
        cur = self.conexion.cursor()
        sql = 'INSERT * FROM usuarios WHERE  ={}'.format()

#.....................................................Funciones extras

    def gDatos(self,nombre,apellido):
        cur = self.conexion.cursor()
        sql = "INSERT INTO `usuarios` (`nombre`,`apellido`,`correo_electronico`,`id_tipo_usuario`,`estatus`,`fecha_registro`,`password`) VALUES (%s,%s)"
        cur.execute(sql,(format(nombre),format(apellido)))
        self.conexion.commit()
        print(nombre,apellido)

    #def gapellido(self):
    #def gcorreo(self):
    #def gcontra(self):












    def select_info(self, id_usuarios):
        sql = 'SELECT * FROM id_usuarios, nombre, apellido, correo_electronico, id_tipo_usuario, estatus, fecha_registro, password ={}'.format(id_usuarios)

        try:
            cur = self.conexion.cursor()
            cur.execute(sql)
            user = cur.fetchone()

            print("id: ", user[0])
            print("nombre: ", user[1])
            print("apellido: ", user[2])
            print("correo_electronico: ", user[3])
            print("id_tipo_usuario: ", user[4])
            print("estatus: ", user[5])
            print("fecha_registro: ", user[6])
            print("password: ", user[7])

        except Exception as e:
            raise


database = DataBase()