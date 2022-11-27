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

def verificadorCorreo(temp_line_email):
    global problema_email
    for x in mayusculas:
        mayusculas.append(x.upper())
    print("Registro correo")

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
                        import tkinter
                        from tkinter import messagebox
                        error = tkinter.messagebox.showerror("Error Correo", "La terminación no es común pero puede ser valido \n")
                else:
                    problema_email += "El dominio  no es reconocido pero puede ser privado \n"
                    import tkinter
                    from tkinter import messagebox
                    error = tkinter.messagebox.showerror("Error Correo", "El dominio  no es reconocido pero puede ser privado")
            else:
                problema_email += "El valor " + x + " no es valido para un correo \n"
                import tkinter
                from tkinter import messagebox
                error = tkinter.messagebox.showerror("Error Correo", "El valor " + x + " no es valido para un correo")
    else:
        problema_email += "El correo no tiene un @ \n"
        import tkinter
        from tkinter import messagebox
        error = tkinter.messagebox.showerror("Error Correo", "El correo no tiene un @")
    print(problema_email)

