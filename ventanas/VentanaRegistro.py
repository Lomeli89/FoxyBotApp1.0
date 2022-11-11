from PyQt5 import QtCore, QtWidgets


class Ui_VentanaRegistro(object):
    def setupUi(self, VentanaRegistro: object):

        VentanaRegistro.setObjectName("VentanaRegistro")
        VentanaRegistro.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(VentanaRegistro)
        self.centralwidget.setObjectName("centralwidget")
        self.label_Nombre = QtWidgets.QLabel(self.centralwidget)
        self.label_Nombre.setGeometry(QtCore.QRect(270, 130, 47, 13))
        self.label_Nombre.setObjectName("label_Nombre")
        self.btn_irIniciarSesion = QtWidgets.QPushButton(self.centralwidget)
        self.btn_irIniciarSesion.setGeometry(QtCore.QRect(410, 370, 75, 23))
        self.btn_irIniciarSesion.setObjectName("btn_irIniciarSesion")
        self.input_Email_Reg = QtWidgets.QLineEdit(self.centralwidget)
        self.input_Email_Reg.setGeometry(QtCore.QRect(270, 210, 271, 31))
        self.input_Email_Reg.setStyleSheet("border-color:#808080;")
        self.input_Email_Reg.setObjectName("input_Email_Reg")
        self.btn_Registrarme = QtWidgets.QPushButton(self.centralwidget)
        self.btn_Registrarme.setGeometry(QtCore.QRect(350, 330, 121, 23))
        self.btn_Registrarme.setObjectName("btn_Registrarme")
        self.input_Password_Reg = QtWidgets.QLineEdit(self.centralwidget)
        self.input_Password_Reg.setGeometry(QtCore.QRect(270, 270, 271, 31))
        self.input_Password_Reg.setStyleSheet("border-color:#808080;")
        self.input_Password_Reg.setEchoMode(QtWidgets.QLineEdit.Password)
        self.input_Password_Reg.setObjectName("input_Password_Reg")
        self.label_YaTienesCuenta = QtWidgets.QLabel(self.centralwidget)
        self.label_YaTienesCuenta.setGeometry(QtCore.QRect(300, 370, 91, 16))
        self.label_YaTienesCuenta.setObjectName("label_YaTienesCuenta")
        self.input_Nombre_Reg = QtWidgets.QLineEdit(self.centralwidget)
        self.input_Nombre_Reg.setGeometry(QtCore.QRect(270, 150, 271, 31))
        self.input_Nombre_Reg.setStyleSheet("border-color:#808080;")
        self.input_Nombre_Reg.setObjectName("input_Nombre_Reg")
        self.label_Email_Reg = QtWidgets.QLabel(self.centralwidget)
        self.label_Email_Reg.setGeometry(QtCore.QRect(270, 190, 47, 13))
        self.label_Email_Reg.setObjectName("label_Email_Reg")
        self.label_Password_Reg = QtWidgets.QLabel(self.centralwidget)
        self.label_Password_Reg.setGeometry(QtCore.QRect(270, 250, 71, 16))
        self.label_Password_Reg.setObjectName("label_Password_Reg")
        ############################################################
        ######################################
        self.btn_irIniciarSesion.clicked.connect(VentanaRegistro.close)
        self.btn_irIniciarSesion.clicked.connect(self.abrir_Ingreso)
        #################################################
        self.btn_Registrarme.clicked.connect(VentanaRegistro.close)
        self.btn_Registrarme.clicked.connect(self.abrir_Ingreso)

        VentanaRegistro.setCentralWidget(self.centralwidget)
        self.retranslateUi(VentanaRegistro)
        QtCore.QMetaObject.connectSlotsByName(VentanaRegistro)

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
