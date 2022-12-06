import datetime
import Conexion


print("registro datos en mysql")

#     id_usuario generado automatico ,   guardar nombre, apellido, correo, tipo de usuario, estatus ,fecha de registro, contraseña
temp_nombre = ""
temp_apellido = ""
temp_correo = ""
temp_tipo_usuario = 1
estatus = 0
temp_fecha_registro = "datetime.now()"

# entradas



datos = Conexion.DataBase()

temp_nombre = input('Nombre ->')

temp_nombre_1 = str("'"+ temp_nombre + "'")
print(temp_nombre_1)
dato1 = datos.gnombre(temp_nombre)
##### datos a guardar

