import datetime
import Conexion


print("registro datos en mysql")

#     id_usuario generado automatico ,   guardar nombre, apellido, correo, tipo de usuario, estatus ,fecha de registro, contraseña
temp_nombre = ""
temp_apellido = ""
temp_correo = ""
temp_tipo_usuario = 1
estatus = 0
temp_fecha_registro = datetime.now()

# entradas

temp_nombre = input('nombre ->')
temp_apellido = input('apellido ->')
temp_correo = input('correo ->')


# conexión
datos = Conexion.DataBase()
#asignación de tipo de formato

##### datos a guardar conectados a mysql


