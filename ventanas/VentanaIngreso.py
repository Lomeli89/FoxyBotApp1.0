from PyQt5 import QtCore, QtWidgets
from VentanaRegistro import *
from VentanaVisitante import *
from VentanaEstudiante import *
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
        self.input_Email.setStyleSheet("border-color:#808080;")
        self.input_Email.setObjectName("input_Email")
        self.input_Password = QtWidgets.QLineEdit(self.centralwidget)
        self.input_Password.setGeometry(QtCore.QRect(270, 290, 271, 31))
        self.input_Password.setStyleSheet("border-color:#808080;")
        self.input_Password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.input_Password.setObjectName("input_Password")
        self.btn_iniciarSesion = QtWidgets.QPushButton(self.centralwidget)
        self.btn_iniciarSesion.setGeometry(QtCore.QRect(350, 350, 121, 23))
        self.btn_iniciarSesion.setObjectName("btn_iniciarSesion")
        self.btn_irRegistrate = QtWidgets.QPushButton(self.centralwidget)
        self.btn_irRegistrate.setGeometry(QtCore.QRect(410, 390, 75, 23))
        self.btn_irRegistrate.setObjectName("btn_irRegistrate")
        self.label_eresNuevo = QtWidgets.QLabel(self.centralwidget)
        self.label_eresNuevo.setGeometry(QtCore.QRect(340, 390, 71, 16))
        self.label_eresNuevo.setObjectName("label_eresNuevo")
        self.btn_PruebaFoxyBot = QtWidgets.QPushButton(self.centralwidget)
        self.btn_PruebaFoxyBot.setGeometry(QtCore.QRect(340, 450, 121, 31))
        self.btn_PruebaFoxyBot.setObjectName("btn_PruebaFoxyBot")

        '''Eventos registro ir'''

        self.btn_irRegistrate.clicked.connect(self.abrir)
        self.btn_irRegistrate.clicked.connect(VentanaIngreso.close)
        '''Evento probar foxybot como visitante'''
        self.btn_PruebaFoxyBot.clicked.connect(self.abrir_Visitante)
        self.btn_PruebaFoxyBot.clicked.connect(VentanaIngreso.close)
        '''Evento probar foxybot como estudiante'''
        self.btn_iniciarSesion.clicked.connect(self.abrir_Estudiante)
        self.btn_iniciarSesion.clicked.connect(VentanaIngreso.close)

        VentanaIngreso.setCentralWidget(self.centralwidget)

        self.retranslateUi(VentanaIngreso)
        QtCore.QMetaObject.connectSlotsByName(VentanaIngreso)

    '''Eventos registro ir'''
    def abrir(self):
        self.ventana = QtWidgets.QMainWindow()
        self.ui = Ui_VentanaRegistro()
        self.ui.setupUi(self.ventana)
        self.ventana.show()

    '''Evento probar foxybot como visitante'''
    def abrir_Visitante(self):
        self.ventana = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.ventana)
        self.ventana.show()
        ####################################
    def abrir_Estudiante(self):
        self.ventana = QtWidgets.QMainWindow()
        self.ui = Ui_VentanaEstudiante()
        self.ui.setupUi(self.ventana)
        self.ventana.show()

    def retranslateUi(self, VentanaIngreso):
        _translate = QtCore.QCoreApplication.translate
        VentanaIngreso.setWindowTitle(_translate("VentanaIngreso", "MainWindow"))
        self.btn_iniciarSesion.setText(_translate("VentanaIngreso", "Iniciar sesión"))
        self.btn_irRegistrate.setText(_translate("VentanaIngreso", "Registrate"))
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
