

from PyQt5 import QtCore, QtGui, QtWidgets
from ventanas.vrfCorreoPass import verificadorCorreo
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


def validador_pass(self, passw):
    if 8 < len(passw) < 32:
        if any([c.isdigit() for c in passw]):
            if any([c.islower() for c in passw]):
                if any([c.isupper() for c in passw]):
                    if any([True if c in punctuation else False for c in passw]):
                        listaEmail.append(temp_line_email)
                        listaPass.append(temp_line_pass)
                        print("Agregados con exito")
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

class Ui_VentanaRegistro(object):
    def setupUi(self, VentanaRegistro):
        VentanaRegistro.setObjectName("VentanaRegistro")
        VentanaRegistro.resize(800, 600)
        VentanaRegistro.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.centralwidget = QtWidgets.QWidget(VentanaRegistro)
        self.centralwidget.setObjectName("centralwidget")
        self.label_Nombre = QtWidgets.QLabel(self.centralwidget)
        self.label_Nombre.setGeometry(QtCore.QRect(290, 250, 47, 13))
        self.label_Nombre.setObjectName("label_Nombre")
        self.btn_irIniciarSesion = QtWidgets.QPushButton(self.centralwidget)
        self.btn_irIniciarSesion.setGeometry(QtCore.QRect(420, 490, 75, 23))
        self.btn_irIniciarSesion.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_irIniciarSesion.setStyleSheet("background-color: transparent;\n"
"font: 75 11pt \"Calibri\";")
        self.btn_irIniciarSesion.setObjectName("btn_irIniciarSesion")
        self.input_Email_Reg = QtWidgets.QLineEdit(self.centralwidget)
        self.input_Email_Reg.setGeometry(QtCore.QRect(290, 330, 271, 31))
        self.input_Email_Reg.setStyleSheet("QLineEdit{\n"
"    \n"
"    \n"
"    \n"
"    \n"
"    background-color: rgb(217, 217, 217);\n"
"    padding-top:1px;\n"
"    border-radius:15px;\n"
"    \n"
"    border-color: rgb(0, 46, 109);\n"
"}")
        self.input_Email_Reg.setObjectName("input_Email_Reg")
        self.btn_Registrarme = QtWidgets.QPushButton(self.centralwidget)
        self.btn_Registrarme.setGeometry(QtCore.QRect(370, 450, 121, 23))
        self.btn_Registrarme.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_Registrarme.setStyleSheet("border-radius:10px;\n"
"font: 10pt \"Nirmala UI\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(1, 45, 108);")
        self.btn_Registrarme.setObjectName("btn_Registrarme")
        self.input_Password_Reg = QtWidgets.QLineEdit(self.centralwidget)
        self.input_Password_Reg.setGeometry(QtCore.QRect(290, 390, 271, 31))
        self.input_Password_Reg.setStyleSheet("QLineEdit{\n"
"    \n"
"    \n"
"    \n"
"    \n"
"    background-color: rgb(217, 217, 217);\n"
"    padding-top:1px;\n"
"    border-radius:15px;\n"
"    \n"
"    border-color: rgb(0, 46, 109);\n"
"}")
        self.input_Password_Reg.setEchoMode(QtWidgets.QLineEdit.Password)
        self.input_Password_Reg.setObjectName("input_Password_Reg")
        self.label_YaTienesCuenta = QtWidgets.QLabel(self.centralwidget)
        self.label_YaTienesCuenta.setGeometry(QtCore.QRect(320, 490, 91, 16))
        self.label_YaTienesCuenta.setObjectName("label_YaTienesCuenta")
        self.input_Nombre_Reg = QtWidgets.QLineEdit(self.centralwidget)
        self.input_Nombre_Reg.setGeometry(QtCore.QRect(290, 270, 271, 31))
        self.input_Nombre_Reg.setStyleSheet("QLineEdit{\n"
"    \n"
"    \n"
"    \n"
"    \n"
"    background-color: rgb(217, 217, 217);\n"
"    padding-top:1px;\n"
"    border-radius:15px;\n"
"    \n"
"    border-color: rgb(0, 46, 109);\n"
"}")
        self.input_Nombre_Reg.setObjectName("input_Nombre_Reg")
        self.label_Email_Reg = QtWidgets.QLabel(self.centralwidget)
        self.label_Email_Reg.setGeometry(QtCore.QRect(290, 310, 47, 13))
        self.label_Email_Reg.setObjectName("label_Email_Reg")
        self.label_Password_Reg = QtWidgets.QLabel(self.centralwidget)
        self.label_Password_Reg.setGeometry(QtCore.QRect(290, 370, 71, 16))
        self.label_Password_Reg.setObjectName("label_Password_Reg")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(200, 0, 451, 251))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("../../../Downloads/title.jpg"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.label.raise_()
        self.label_Nombre.raise_()
        self.btn_irIniciarSesion.raise_()
        self.input_Email_Reg.raise_()
        self.btn_Registrarme.raise_()
        self.input_Password_Reg.raise_()
        self.label_YaTienesCuenta.raise_()
        self.input_Nombre_Reg.raise_()
        self.label_Email_Reg.raise_()
        self.label_Password_Reg.raise_()
        VentanaRegistro.setCentralWidget(self.centralwidget)

        self.retranslateUi(VentanaRegistro)
        QtCore.QMetaObject.connectSlotsByName(VentanaRegistro)

        self.btn_irIniciarSesion.clicked.connect(VentanaRegistro.close)
        self.btn_irIniciarSesion.clicked.connect(self.abrir_Ingreso)
        #################################################
        #self.btn_Registrarme.clicked.connect(VentanaRegistro.close)
        #self.btn_Registrarme.clicked.connect(self.abrir_Ingreso)
        self.btn_Registrarme.clicked.connect(self.registrarCorreo)



    def registrarCorreo(self):
        email = str(self.input_Email_Reg.text())
        global problema_email
        for x in mayusculas:
            mayusculas.append(x.upper())
        print("Registro correo")
        temp_line_email = email

        if temp_line_email.find('@'):
            print("aqui llego")
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
                                print("correo ya registrado, intente con uno nuevo")


                            else:
                                print("correo registrado")
                                passw = str(self.input_Password_Reg.text())
                                validador_pass(passw)
                                break
                        else:
                            problema_email += "La terminación no es común pero puede ser valido \n"


                    else:
                        problema_email += "El dominio  no es reconocido pero puede ser privado \n"

                else:
                    problema_email += "El valor " + x + " no es valido para un correo \n"

        else:
            problema_email += "El correo no tiene un @ \n"



    def abrir_Ingreso(self):
        self.ventana = QtWidgets.QMainWindow()
        from ventanas import VentanaIngreso
        self.ui = VentanaIngreso.Ui_VentanaIngreso()
        self.ui.setupUi(self.ventana)
        self.ventana.show()
    def retranslateUi(self, VentanaRegistro):
        _translate = QtCore.QCoreApplication.translate
        VentanaRegistro.setWindowTitle(_translate("VentanaRegistro", "MainWindow"))
        self.label_Nombre.setText(_translate("VentanaRegistro", "Nombre"))
        self.btn_irIniciarSesion.setText(_translate("VentanaRegistro", "!Inicia sesión¡"))
        self.btn_Registrarme.setText(_translate("VentanaRegistro", "Registrarme"))
        self.label_YaTienesCuenta.setText(_translate("VentanaRegistro", "¿Ya tienes cuenta?"))
        self.label_Email_Reg.setText(_translate("VentanaRegistro", "E-mail"))
        self.label_Password_Reg.setText(_translate("VentanaRegistro", "Contraseña"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    VentanaRegistro = QtWidgets.QMainWindow()
    ui = Ui_VentanaRegistro()
    ui.setupUi(VentanaRegistro)
    VentanaRegistro.show()
    sys.exit(app.exec_())
