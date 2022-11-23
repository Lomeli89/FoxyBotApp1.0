
index_list_email = []
index_list_pass = []


listaEmail = []
listaPass = []

temp_line_email = str
temp_line_pass = str

blista_email = str
blista_pass = str

temp_index_email = str
temp_index_pass = str


while True:
    print("Menu de sesion")
    print("1. Iniciar sesion")
    print("2. Registrarme")

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
        print("Registro")
        temp_line_email = str(input("Email -> "))
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
        print("opcion no valida. Intente de nuevo")




