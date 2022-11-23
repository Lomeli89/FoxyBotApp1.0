
index_list_email = []
index_list_pass = []


listaEmail = []
listaPass = []

temp_line_email = str
temp_line_pass = str

blista_email = str
blista_pass = str

temp_index_email = ""
temp_index_pass = str


##### verificacion de email

problema_email = ""


signos = ['.','_','-']
numeros = ['0','1','2','3','4','5','6','7','8','9']
dominios = ['gmail','hotmail','msn','yahoo','outlook','live','loscabos']
minusculas = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
mayusculas = []
extensiones = ['com','net','com.mx','ea','es','mx','org','gob','tecnm.mx']




################################################
while True:
    print("Menu de sesion")
    print("1. Iniciar sesion")
    print("2. Registrarme")
    print("3. Salir")

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
        temp_line_email = str(input("Email -> "))

        if temp_index_email.find('@'):
            nuevo_email = temp_index_email.split('@')
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
                            blista_email = (temp_line_email in listaEmail)
                            if blista_email == True:
                                print("Usuario ya registrado, intente con uno nuevo")
                            else:
                                temp_line_pass = str(input("contraseña -> "))

                                listaEmail.append(temp_line_email)
                                listaPass.append(temp_line_pass)

                                temp_index_email = listaEmail.index(temp_line_email)
                                temp_line_pass = listaPass.index(temp_line_pass)

                                index_list_email.append(temp_line_email)
                                index_list_pass.append(temp_line_pass)
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
        print("adios")



    else:
        print("opcion no valida. Intente de nuevo")




