
from PyQt5 import QtCore, QtGui, QtWidgets
import Conexion
import datetime

class Ui_MainWindowRegistro(object):
    def setupUi(self, MainWindowRegistro):
        MainWindowRegistro.setObjectName("MainWindowRegistro")
        MainWindowRegistro.resize(879, 646)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../img/298809902_539628011298194_5839572564237821349_n.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindowRegistro.setWindowIcon(icon)
        MainWindowRegistro.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.centralwidget = QtWidgets.QWidget(MainWindowRegistro)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setStyleSheet("background-color: rgb(255, 0, 0);\n"
"background-color: rgb(255, 255, 255);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.frame_4 = QtWidgets.QFrame(self.frame)
        self.frame_4.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame_4)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.frame_4)
        self.label.setMaximumSize(QtCore.QSize(100, 45))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("../img/LOGO_TECNM_AZUL-1024x437.png"))
        self.label.setScaledContents(True)
        self.label.setWordWrap(False)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.label_2 = QtWidgets.QLabel(self.frame_4)
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.horizontalLayout_2.addWidget(self.frame_4)
        self.frame_3 = QtWidgets.QFrame(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_3.sizePolicy().hasHeightForWidth())
        self.frame_3.setSizePolicy(sizePolicy)
        self.frame_3.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame_3)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_3 = QtWidgets.QLabel(self.frame_3)
        self.label_3.setMaximumSize(QtCore.QSize(400, 260))
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap("../img/title.jpg"))
        self.label_3.setScaledContents(True)
        self.label_3.setWordWrap(False)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_2.addWidget(self.label_3)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.input_Nombre_Reg = QtWidgets.QLineEdit(self.frame_3)
        self.input_Nombre_Reg.setEnabled(True)
        self.input_Nombre_Reg.setMaximumSize(QtCore.QSize(271, 31))
        self.input_Nombre_Reg.setStyleSheet("QLineEdit{\n"
"    \n"
"    font: 9pt \"MS Sans Serif\";\n"
"    border: 2px solid rgb(158, 158, 158);\n"
"    border-radius: 15px;\n"
"    \n"
"}")
        self.input_Nombre_Reg.setMaxLength(90)
        self.input_Nombre_Reg.setObjectName("input_Nombre_Reg")
        self.horizontalLayout.addWidget(self.input_Nombre_Reg)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.input_apellido_Reg = QtWidgets.QLineEdit(self.frame_3)
        self.input_apellido_Reg.setEnabled(True)
        self.input_apellido_Reg.setMaximumSize(QtCore.QSize(271, 31))
        self.input_apellido_Reg.setStyleSheet("QLineEdit{\n"
"    \n"
"    font: 9pt \"MS Sans Serif\";\n"
"    border: 2px solid rgb(158, 158, 158);\n"
"    border-radius: 15px;\n"
"    \n"
"}")
        self.input_apellido_Reg.setText("")
        self.input_apellido_Reg.setMaxLength(90)
        self.input_apellido_Reg.setObjectName("input_apellido_Reg")
        self.horizontalLayout_9.addWidget(self.input_apellido_Reg)
        self.verticalLayout_2.addLayout(self.horizontalLayout_9)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.input_Email_Reg = QtWidgets.QLineEdit(self.frame_3)
        self.input_Email_Reg.setEnabled(True)
        self.input_Email_Reg.setMaximumSize(QtCore.QSize(271, 31))
        self.input_Email_Reg.setStyleSheet("QLineEdit{\n"
"    \n"
"    font: 9pt \"MS Sans Serif\";\n"
"    border: 2px solid rgb(158, 158, 158);\n"
"    border-radius: 15px;\n"
"    \n"
"}")
        self.input_Email_Reg.setObjectName("input_Email_Reg")
        self.horizontalLayout_4.addWidget(self.input_Email_Reg)
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.input_Password_Reg = QtWidgets.QLineEdit(self.frame_3)
        self.input_Password_Reg.setEnabled(True)
        self.input_Password_Reg.setMaximumSize(QtCore.QSize(271, 31))
        self.input_Password_Reg.setStyleSheet("QLineEdit{\n"
"    \n"
"    font: 9pt \"MS Sans Serif\";\n"
"    border: 2px solid rgb(158, 158, 158);\n"
"    border-radius: 15px;\n"
"    \n"
"}")
        self.input_Password_Reg.setEchoMode(QtWidgets.QLineEdit.Password)
        self.input_Password_Reg.setObjectName("input_Password_Reg")
        self.horizontalLayout_5.addWidget(self.input_Password_Reg)
        self.verticalLayout_2.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.btn_Registrarme = QtWidgets.QPushButton(self.frame_3)
        self.btn_Registrarme.setMaximumSize(QtCore.QSize(161, 31))
        self.btn_Registrarme.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_Registrarme.setStyleSheet("border-radius:15px;\n"
"font: 12pt \"MS Sans Serif\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(1, 45, 108);")
        self.btn_Registrarme.setObjectName("btn_Registrarme")
        self.horizontalLayout_7.addWidget(self.btn_Registrarme)
        self.verticalLayout_2.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_6 = QtWidgets.QLabel(self.frame_3)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_3.addWidget(self.label_6)
        self.label_5 = QtWidgets.QLabel(self.frame_3)
        self.label_5.setMaximumSize(QtCore.QSize(20, 16))
        self.label_5.setStyleSheet("font: 75 8pt \"MS Sans Serif\";")
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_3.addWidget(self.label_5)
        self.label_7 = QtWidgets.QLabel(self.frame_3)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_3.addWidget(self.label_7)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.btn_irIniciarSesion = QtWidgets.QPushButton(self.frame_3)
        self.btn_irIniciarSesion.setMaximumSize(QtCore.QSize(200, 16777215))
        self.btn_irIniciarSesion.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_irIniciarSesion.setStyleSheet("background-color: transparent;\n"
"font: 75 11pt \"Calibri\";")
        self.btn_irIniciarSesion.setObjectName("btn_irIniciarSesion")
        self.horizontalLayout_8.addWidget(self.btn_irIniciarSesion)
        self.verticalLayout_2.addLayout(self.horizontalLayout_8)
        self.label_4 = QtWidgets.QLabel(self.frame_3)
        self.label_4.setMaximumSize(QtCore.QSize(16777215, 200))
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")
        self.verticalLayout_2.addWidget(self.label_4)
        self.horizontalLayout_2.addWidget(self.frame_3)
        self.frame_2 = QtWidgets.QFrame(self.frame)
        self.frame_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.horizontalLayout_2.addWidget(self.frame_2)
        self.gridLayout.addWidget(self.frame, 0, 1, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)
        MainWindowRegistro.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindowRegistro)
        QtCore.QMetaObject.connectSlotsByName(MainWindowRegistro)

        self.btn_Registrarme.clicked.connect(self.registro)

    def registro(self):

        self.datos = Conexion.DataBase()

        temp_nombre = self.input_Nombre_Reg.text()
        temp_apellido = self.input_Nombre_Reg.text()
        temp_correo_electronico = self.input_Email_Reg.text()
        temp_password = self.input_Password_Reg.text()



        print(temp_nombre+" "+temp_apellido+" "+temp_correo_electronico+" "+temp_password)

        self.datos.gDatos(temp_nombre, temp_apellido, temp_correo_electronico, temp_password)




    def info_campos_texto(self):
        import tkinter
        from tkinter import messagebox
        informacion = tkinter.messagebox.showinfo("Sin datos", "No hay datos en los campos de texto")


    def retranslateUi(self, MainWindowRegistro):
        _translate = QtCore.QCoreApplication.translate
        MainWindowRegistro.setWindowTitle(_translate("MainWindowRegistro", "Registro"))
        self.input_Nombre_Reg.setPlaceholderText(_translate("MainWindowRegistro", "Nombre"))
        self.input_apellido_Reg.setPlaceholderText(_translate("MainWindowRegistro", "Apellido"))
        self.input_Email_Reg.setPlaceholderText(_translate("MainWindowRegistro", "Correo@loscabos.tecnm.mx"))
        self.input_Password_Reg.setPlaceholderText(_translate("MainWindowRegistro", "Contraseña"))
        self.btn_Registrarme.setText(_translate("MainWindowRegistro", "REGISTRAR"))
        self.label_6.setText(_translate("MainWindowRegistro", "<html><head/><body><p align=\"center\">_________________________________<br/></p></body></html>"))
        self.label_5.setText(_translate("MainWindowRegistro", "<html><head/><body><p align=\"center\"><span style=\" font-size:10pt;\">O</span></p></body></html>"))
        self.label_7.setText(_translate("MainWindowRegistro", "<html><head/><body><p align=\"center\">_________________________________<br/></p></body></html>"))
        self.btn_irIniciarSesion.setText(_translate("MainWindowRegistro", "¿Ya tienes cuenta? !Inicia sesión¡"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindowRegistro = QtWidgets.QMainWindow()
    ui = Ui_MainWindowRegistro()
    ui.setupUi(MainWindowRegistro)
    MainWindowRegistro.show()
    sys.exit(app.exec_())