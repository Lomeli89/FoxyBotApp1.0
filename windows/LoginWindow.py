
from PyQt5 import QtCore, QtGui, QtWidgets
import Conexion
import re
import bcrypt


class Ui_MainWindowLogin(object):
    def setupUi(self, MainWindowLogin, ):
        MainWindowLogin.setObjectName("MainWindowLogin")
        MainWindowLogin.resize(879, 646)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../img/298809902_539628011298194_5839572564237821349_n.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindowLogin.setWindowIcon(icon)
        MainWindowLogin.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.centralwidget = QtWidgets.QWidget(MainWindowLogin)
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
        self.input_Email = QtWidgets.QLineEdit(self.frame_3)
        self.input_Email.setMaximumSize(QtCore.QSize(271, 31))
        self.input_Email.setStyleSheet("QLineEdit{\n"
"    \n"
"    font: 9pt \"MS Sans Serif\";\n"
"    border: 2px solid rgb(158, 158, 158);\n"
"    border-radius: 15px;\n"
"    \n"
"}")
        self.input_Email.setMaxLength(70)
        self.input_Email.setObjectName("input_Email")
        self.horizontalLayout.addWidget(self.input_Email)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.input_Password = QtWidgets.QLineEdit(self.frame_3)
        self.input_Password.setMaximumSize(QtCore.QSize(271, 31))
        self.input_Password.setStyleSheet("QLineEdit{\n"
"    \n"
"    font: 9pt \"MS Sans Serif\";\n"
"    border: 2px solid rgb(158, 158, 158);\n"
"    border-radius: 15px;\n"
"    \n"
"}")
        self.input_Password.setText("")
        self.input_Password.setMaxLength(60)
        self.input_Password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.input_Password.setObjectName("input_Password")
        self.horizontalLayout_4.addWidget(self.input_Password)
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.btn_iniciarSesion = QtWidgets.QPushButton(self.frame_3)
        self.btn_iniciarSesion.setMaximumSize(QtCore.QSize(121, 31))
        self.btn_iniciarSesion.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_iniciarSesion.setStyleSheet("\n"
"border-radius:15px;\n"
"font: 8pt \"MS Sans Serif\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(1, 45, 108);")
        self.btn_iniciarSesion.setObjectName("btn_iniciarSesion")
        self.horizontalLayout_5.addWidget(self.btn_iniciarSesion)
        self.verticalLayout_2.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.btn_irRegistrate = QtWidgets.QPushButton(self.frame_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_irRegistrate.sizePolicy().hasHeightForWidth())
        self.btn_irRegistrate.setSizePolicy(sizePolicy)
        self.btn_irRegistrate.setMaximumSize(QtCore.QSize(185, 31))
        self.btn_irRegistrate.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_irRegistrate.setStyleSheet("background-color: transparent;\n"
"font: 75 9pt \"MS Sans Serif\";")
        self.btn_irRegistrate.setObjectName("btn_irRegistrate")
        self.horizontalLayout_7.addWidget(self.btn_irRegistrate)
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
        self.btn_PruebaFoxyBot = QtWidgets.QPushButton(self.frame_3)
        self.btn_PruebaFoxyBot.setMaximumSize(QtCore.QSize(161, 31))
        self.btn_PruebaFoxyBot.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_PruebaFoxyBot.setStyleSheet("\n"
"border: 2px solid rgb(1, 45, 108);\n"
"border-radius: 15px;\n"
"font: 10pt \"Nirmala UI\";\n"
"color: rgb(1, 45, 108);\n"
"background-color: transparent;")
        self.btn_PruebaFoxyBot.setObjectName("btn_PruebaFoxyBot")
        self.horizontalLayout_8.addWidget(self.btn_PruebaFoxyBot)
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
        MainWindowLogin.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindowLogin)
        QtCore.QMetaObject.connectSlotsByName(MainWindowLogin)

        ##################eventos###############################
        self.btn_iniciarSesion.clicked.connect(self.inicio)

    def inicio(self):

        self.datos = Conexion.DataBase()


        temp_entradas_email = self.input_Email.text()
        temp_entradas_pass = self.input_Password.text()

        temp_entradas_email_1 = str("'"+ temp_entradas_email + "'")
        temp_entradas_pass_1 = str("'"+ temp_entradas_pass + "'")

        si1 = 0
        si2 = 0

        dato1 = self.datos.busca_user(temp_entradas_email_1)
        dato2 = self.datos.busca_contra(temp_entradas_pass_1)


        if self.input_Email.text() == "" or self.input_Password.text() == "":
            self.info_campos_texto()
        else:
            if dato1[0][0] == temp_entradas_email:
                if dato2[0][0] == temp_entradas_pass:
                    MainWindowLogin.close()
                    self.abrir_Estudiante()
                else:
                    self.error_entrada()
            else:
             print("R")




    def vfnIngreso(self):
        varEmail = str
        varPass = str
        varEmail(str(self.input_Email.text()))
        varPass(str(self.input_Password.text()))
        if str(self.input_Email.text()) == "19380605@loscabos.tecnm.mx" and str(
                self.input_Password.text()) == "1234":
            print("Ingresado exitosamente")
            self.input_Email.setText("")
            MainWindowLogin.close()
            self.abrir_Estudiante()
        elif str(self.input_Email.text()) == "admin" and str(self.input_Password.text()) == "1234":
            self.input_Email.setText("")
            MainWindowLogin.close()
            self.abrir_Admin()
        else:
            import tkinter
            from tkinter import messagebox
            error = tkinter.messagebox.showerror("Error", "datos incorrectos")

    def abrir_Admin(self):
        self.ventana = QtWidgets.QMainWindow()
        from windows.AdminWindow import Ui_MainWindowAdmin
        self.ui = Ui_MainWindowAdmin()
        self.ui.setupUi(self.ventana)
        self.ventana.show()
    def abrir_Estudiante(self):
        self.ventana = QtWidgets.QMainWindow()
        from windows.EstudianteWindow import Ui_MainWindowEstudiante
        self.ui = Ui_MainWindowEstudiante()
        self.ui.setupUi(self.ventana)
        self.ventana.show()
    def info_campos_texto(self):
        import tkinter
        from tkinter import messagebox
        informacion = tkinter.messagebox.showinfo("Sin datos", "No hay datos en los campos de texto")
    def error_entrada(self):
        import tkinter
        from tkinter import messagebox
        error = tkinter.messagebox.showerror("Error", "Datos o dato incorrecto")

    def retranslateUi(self, MainWindowLogin):
        _translate = QtCore.QCoreApplication.translate
        MainWindowLogin.setWindowTitle(_translate("MainWindowLogin", "MainWindow"))
        self.input_Email.setPlaceholderText(_translate("MainWindowLogin", "numerocontrol@loscabos.tecnm.mx"))
        self.input_Password.setPlaceholderText(_translate("MainWindowLogin", "Contraseña"))
        self.btn_iniciarSesion.setText(_translate("MainWindowLogin", "INICIAR SESIÓN"))
        self.btn_irRegistrate.setText(_translate("MainWindowLogin", "¿Eres nuevo? ¡Regístrate!"))
        self.label_6.setText(_translate("MainWindowLogin", "<html><head/><body><p align=\"center\">_________________________________<br/></p></body></html>"))
        self.label_5.setText(_translate("MainWindowLogin", "<html><head/><body><p align=\"center\"><span style=\" font-size:10pt;\">O</span></p></body></html>"))
        self.label_7.setText(_translate("MainWindowLogin", "<html><head/><body><p align=\"center\">_________________________________<br/></p></body></html>"))
        self.btn_PruebaFoxyBot.setText(_translate("MainWindowLogin", "¡PRUEBA A FOXY BOT!"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindowLogin = QtWidgets.QMainWindow()
    ui = Ui_MainWindowLogin()
    ui.setupUi(MainWindowLogin)
    MainWindowLogin.show()
    sys.exit(app.exec_())
