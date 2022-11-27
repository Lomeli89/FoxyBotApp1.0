#import curses.ascii
from string import punctuation
index_list_email = []
index_list_pass = []


listaEmail = []
listaPass = []

temp_line_email = ""
temp_line_pass = ""

blista_email = ""
blista_pass = ""

temp_index_email = ""
temp_index_pass = ""


problema_email = ""


signos = ['.','_','-']
numeros = ['0','1','2','3','4','5','6','7','8','9']
dominios = ['loscabos']
minusculas = ['a','b','anc','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
mayusculas = []
extensiones = ['mx','tecnm.mx','tecnm']

def validador_pass(passw):
    if 8 < len(passw) < 32:
        if any([c.isdigit() for c in passw]):
            if any([c.islower() for c in passw]):
                if any([c.isupper() for c in passw]):
                    if any([True if c in punctuation else False for c in passw]):
                        listaEmail.append(temp_line_email)
                        listaPass.append(temp_line_pass)
                        return True


                    else:
                        print("la contraseña debe tener algun character especial")
                else:
                    print("la contraseña debe tener alguna mayuscula")
            else:
                print("la contraseña debe tener alguna minuscula")
        else:
            print("la contraseña debe tener algun numero")
    else:
        print("la contraseña debe tener entre 8 y 32 characteres")

    return False
################################################
while True:
    print("Menu de sesion")
    print("1. Iniciar sesion")
    print("2. Registrarme")
    print("3. Lista de registros")
    print("4. Salir")

    menu = int(input("-> "))
    if menu == 1:
        print("Inicio de sesion")

        temp_line_email = str(input("Email -> "))
        temp_line_pass = str(input("contraseña -> "))

        blista_email = (temp_line_email in listaEmail)
        blista_pass = (temp_line_pass in listaPass)




        if blista_email == True and blista_pass == True:
            temp_index_email = listaEmail.index(temp_line_email)
            temp_index_pass = listaPass.index(temp_line_pass)
            if temp_index_email == temp_index_pass:
                print("Iniciado con exito")
            else:
                print("error: Datos no coinciden")
        else:
            print("error: intente de nuevo")

    elif menu == 2:
        for x in mayusculas:
            mayusculas.append(x.upper())
        print("Registro")
        temp_line_email = input(str("Email -> "))

        if temp_line_email.find('@'):
            nuevo_email = temp_line_email.split('@')
            usuario = nuevo_email[0]
            resto = nuevo_email[1]
            continuacion = resto.split('.')
            dominio = continuacion[0]
            terminacion = continuacion[1]
            for x in usuario:
                if x in signos or x in numeros or x in minusculas or x in mayusculas:
                    if dominio in dominios:
                        if terminacion in extensiones:
                            problema_email = "El email es correcto"
                            if blista_email == True:
                                print("Usuario ya registrado, intente con uno nuevo")
                            else:
                                temp_line_pass = str(input("contraseña -> "))
                                validador_pass(temp_line_pass)
                                break
                        else:
                            problema_email += "La terminación no es común pero puede ser valido \n"
                    else:
                        problema_email += "El dominio  no es reconocido pero puede ser privado \n"
                else:
                    problema_email += "El valor " + x + " no es valido para un correo \n"
        else:
            problema_email +="El correo no tiene un @ \n"
        print(problema_email)




    elif menu == 3:
        print("Sesiones")
        print(listaEmail)
        print(listaPass)

    elif menu == 4:
        print("adios")
        break


    else:
        print("opcion no valida. Intente de nuevo")




