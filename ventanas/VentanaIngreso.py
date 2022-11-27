

from typing import Tuple
from PyQt5 import QtCore, QtGui, QtWidgets





class Ui_VentanaIngreso(object):
    def setupUi(self, VentanaIngreso):
        VentanaIngreso.setObjectName("VentanaIngreso")
        VentanaIngreso.resize(800, 600)
        VentanaIngreso.setAutoFillBackground(False)
        VentanaIngreso.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.centralwidget = QtWidgets.QWidget(VentanaIngreso)
        self.centralwidget.setObjectName("centralwidget")
        self.input_Email = QtWidgets.QLineEdit(self.centralwidget)
        self.input_Email.setGeometry(QtCore.QRect(270, 230, 271, 31))
        self.input_Email.setStyleSheet("QLineEdit{\n"
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
        self.input_Email.setMaxLength(70)
        self.input_Email.setObjectName("input_Email")
        self.input_Password = QtWidgets.QLineEdit(self.centralwidget)
        self.input_Password.setGeometry(QtCore.QRect(270, 290, 271, 31))
        self.input_Password.setStyleSheet("QLineEdit{\n"
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
        self.input_Password.setMaxLength(60)
        self.input_Password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.input_Password.setObjectName("input_Password")
        self.btn_iniciarSesion = QtWidgets.QPushButton(self.centralwidget)
        self.btn_iniciarSesion.setGeometry(QtCore.QRect(350, 350, 121, 23))
        self.btn_iniciarSesion.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_iniciarSesion.setStyleSheet("\n"
"border-radius:10px;\n"
"font: 10pt \"Nirmala UI\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(1, 45, 108);")
        self.btn_iniciarSesion.setObjectName("btn_iniciarSesion")
        self.btn_irRegistrate = QtWidgets.QPushButton(self.centralwidget)
        self.btn_irRegistrate.setGeometry(QtCore.QRect(410, 390, 75, 31))
        self.btn_irRegistrate.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_irRegistrate.setStyleSheet("background-color: transparent;\n"
"font: 75 11pt \"Calibri\";")
        self.btn_irRegistrate.setObjectName("btn_irRegistrate")
        self.label_eresNuevo = QtWidgets.QLabel(self.centralwidget)
        self.label_eresNuevo.setGeometry(QtCore.QRect(340, 390, 71, 31))
        self.label_eresNuevo.setObjectName("label_eresNuevo")
        self.btn_PruebaFoxyBot = QtWidgets.QPushButton(self.centralwidget)
        self.btn_PruebaFoxyBot.setGeometry(QtCore.QRect(340, 450, 121, 31))
        self.btn_PruebaFoxyBot.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_PruebaFoxyBot.setStyleSheet("\n"
"border-radius:10px;\n"
"font: 10pt \"Nirmala UI\";\n"
"color: rgb(1, 45, 108);\n"
"background-color: rgb(217, 217, 217);")
        self.btn_PruebaFoxyBot.setObjectName("btn_PruebaFoxyBot")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(180, 40, 451, 251))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("../../../Downloads/title.jpg"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.label.raise_()
        self.input_Email.raise_()
        self.input_Password.raise_()
        self.btn_iniciarSesion.raise_()
        self.btn_irRegistrate.raise_()
        self.label_eresNuevo.raise_()
        self.btn_PruebaFoxyBot.raise_()
        VentanaIngreso.setCentralWidget(self.centralwidget)

        self.retranslateUi(VentanaIngreso)
        QtCore.QMetaObject.connectSlotsByName(VentanaIngreso)

        self.btn_irRegistrate.clicked.connect(self.abrir_Registro)
        self.btn_irRegistrate.clicked.connect(VentanaIngreso.close)
        '''Evento probar foxybot como visitante'''
        self.btn_PruebaFoxyBot.clicked.connect(self.abrir_Visitante)
        self.btn_PruebaFoxyBot.clicked.connect(VentanaIngreso.close)
        '''Evento probar foxybot como estudiante'''
        self.btn_iniciarSesion.clicked.connect(self.vfnIngreso)
        #self.btn_iniciarSesion.clicked.connect(VentanaIngreso.close)


        #size grid


    def senDatos(self):
        print("datos")

    def vfnIngreso(self):
        varEmail = str
        varPass = str
        varEmail(str(self.input_Email.text()))
        varPass(str(self.input_Password.text()))
        if str(self.input_Email.text()) == "19380605@loscabos.tecnm.mx" and str(self.input_Password.text()) == "1234":
            print("Ingresado exitosamente")
            self.input_Email.setText("")
            VentanaIngreso.close()
            self.abrir_Estudiante()
        elif str(self.input_Email.text()) == "admin" and str(self.input_Password.text()) == "1234":
            self.input_Email.setText("")
            VentanaIngreso.close()
            self.abrir_Admin()
        else:
            import tkinter
            from tkinter import messagebox
            error = tkinter.messagebox.showerror("Error", "datos incorrectos")


    def abrir_Registro(self):
        self.ventana = QtWidgets.QMainWindow()
        from ventanas.VentanaRegistro import Ui_VentanaRegistro
        self.ui = Ui_VentanaRegistro()
        self.ui.setupUi(self.ventana)
        self.ventana.show()
    def abrir_Admin(self):
        self.ventana = QtWidgets.QMainWindow()
        from ventanas.VentanaAdmin import Ui_VentanaAdmin
        self.ui = Ui_VentanaAdmin()
        self.ui.setupUi(self.ventana)
        self.ventana.show()

    '''Evento probar foxybot como visitante'''

    def abrir_Visitante(self):
        self.ventana = QtWidgets.QMainWindow()
        from ventanas.VentanaVisitante import Ui_MainWindow
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.ventana)
        self.ventana.show()
        ####################################

    def abrir_Estudiante(self):
        self.ventana = QtWidgets.QMainWindow()
        from VentanaEstudiante import Ui_VentanaEstudiante
        self.ui = Ui_VentanaEstudiante()
        self.ui.setupUi(self.ventana)
        self.ventana.show()


    def retranslateUi(self, VentanaIngreso):
        _translate = QtCore.QCoreApplication.translate
        VentanaIngreso.setWindowTitle(_translate("VentanaIngreso", "MainWindow"))
        self.input_Email.setPlaceholderText(_translate("VentanaIngreso", "Email"))
        self.input_Password.setPlaceholderText(_translate("VentanaIngreso", "Contraseña"))
        self.btn_iniciarSesion.setText(_translate("VentanaIngreso", "Iniciar sesión"))
        self.btn_irRegistrate.setText(_translate("VentanaIngreso", "¡Registrate!"))
        self.label_eresNuevo.setText(_translate("VentanaIngreso", "¿Eres nuevo?"))
        self.btn_PruebaFoxyBot.setText(_translate("VentanaIngreso", "¡PRUEBA A FOXY BOT!"))



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    VentanaIngreso = QtWidgets.QMainWindow()
    ui = Ui_VentanaIngreso()
    ui.setupUi(VentanaIngreso)
    VentanaIngreso.show()
    sys.exit(app.exec_())
