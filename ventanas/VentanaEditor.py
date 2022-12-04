from PyQt5 import QtCore, QtGui, QtWidgets
class Ui_VentanaEditor(object):
    def setupUi(self, VentanaEditor):
        VentanaEditor.setObjectName("VentanaEditor")
        VentanaEditor.resize(1000, 500)
        VentanaEditor.setMinimumSize(QtCore.QSize(1000, 500))
        VentanaEditor.setStyleSheet("background-color: rgb(45, 45, 45);")
        self.centralwidget = QtWidgets.QWidget(VentanaEditor)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.Top_Bar = QtWidgets.QFrame(self.centralwidget)
        self.Top_Bar.setMaximumSize(QtCore.QSize(16777215, 40))
        self.Top_Bar.setStyleSheet("background-color: rgb(35, 35, 35);")
        self.Top_Bar.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.Top_Bar.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Top_Bar.setObjectName("Top_Bar")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.Top_Bar)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frame_toggle = QtWidgets.QFrame(self.Top_Bar)
        self.frame_toggle.setMaximumSize(QtCore.QSize(70, 40))
        self.frame_toggle.setStyleSheet("background-color: rgb(85, 170, 255);")
        self.frame_toggle.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_toggle.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_toggle.setObjectName("frame_toggle")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame_toggle)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout.addWidget(self.frame_toggle)
        self.frame_top = QtWidgets.QFrame(self.Top_Bar)
        self.frame_top.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_top.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_top.setObjectName("frame_top")
        self.horizontalLayout.addWidget(self.frame_top)
        self.verticalLayout.addWidget(self.Top_Bar)
        self.Content = QtWidgets.QFrame(self.centralwidget)
        self.Content.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.Content.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.Content.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Content.setObjectName("Content")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.Content)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.frame_left_menu = QtWidgets.QFrame(self.Content)
        self.frame_left_menu.setMinimumSize(QtCore.QSize(212, 0))
        self.frame_left_menu.setMaximumSize(QtCore.QSize(70, 16777215))
        self.frame_left_menu.setStyleSheet("background-color: rgb(0, 46, 109);")
        self.frame_left_menu.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_left_menu.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_left_menu.setObjectName("frame_left_menu")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame_left_menu)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.frame_3 = QtWidgets.QFrame(self.frame_left_menu)
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.btn_chat = QtWidgets.QPushButton(self.frame_3)
        self.btn_chat.setGeometry(QtCore.QRect(20, 100, 171, 30))
        self.btn_chat.setMinimumSize(QtCore.QSize(0, 30))
        self.btn_chat.setStyleSheet("QPushButton {\n"
"    font: 11.5pt \"Calibri\";\n"
"    color: rgb(255, 255, 255);\n"
"    padding-left:-100px;\n"
"    background-color: rgb(0, 46, 109);\n"
"    border: 0px solid;\n"
"    border-radius:15px;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(93, 129, 163);\n"
"}\n"
"\n"
"\n"
"    \n"
"    \n"
"    \n"
"    \n"
"")
        self.btn_chat.setFlat(False)
        self.btn_chat.setObjectName("btn_chat")
        self.label_2 = QtWidgets.QLabel(self.frame_3)
        self.label_2.setGeometry(QtCore.QRect(80, 20, 101, 16))
        self.label_2.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 11.5pt \"Calibri\";")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.frame_3)
        self.label_3.setGeometry(QtCore.QRect(80, 31, 101, 20))
        self.label_3.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 25 11pt \"Calibri Light\";\n"
"background-color: transparent;")
        self.label_3.setObjectName("label_3")
        self.btn_cerrarSesion = QtWidgets.QPushButton(self.frame_3)
        self.btn_cerrarSesion.setGeometry(QtCore.QRect(20, 450, 171, 30))
        self.btn_cerrarSesion.setMinimumSize(QtCore.QSize(0, 30))
        self.btn_cerrarSesion.setStyleSheet("QPushButton {\n"
"    font: 9pt \"Calibri\";\n"
"    color: rgb(255, 255, 255);\n"
"    padding-left:-50px;\n"
"    background-color: rgb(0, 46, 109);\n"
"    border: 0px solid;\n"
"    border-radius:15px;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(93, 129, 163);\n"
"}\n"
"\n"
"\n"
"    \n"
"    \n"
"    \n"
"    \n"
"")
        self.btn_cerrarSesion.setFlat(False)
        self.btn_cerrarSesion.setObjectName("btn_cerrarSesion")
        self.btn_about = QtWidgets.QPushButton(self.frame_3)
        self.btn_about.setGeometry(QtCore.QRect(20, 180, 171, 30))
        self.btn_about.setMinimumSize(QtCore.QSize(0, 30))
        self.btn_about.setStyleSheet("QPushButton {\n"
"    font: 11.5pt \"Calibri\";\n"
"    color: rgb(255, 255, 255);\n"
"    padding-left:-40px;\n"
"    background-color: rgb(0, 46, 109);\n"
"    border: 0px solid;\n"
"    border-radius:15px;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(93, 129, 163);\n"
"}\n"
"\n"
"\n"
"    \n"
"    \n"
"    \n"
"    \n"
"")
        self.btn_about.setFlat(False)
        self.btn_about.setObjectName("btn_about")
        self.label_4 = QtWidgets.QLabel(self.frame_3)
        self.label_4.setGeometry(QtCore.QRect(30, 10, 51, 41))
        self.label_4.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.label_4.setText("")
        self.label_4.setPixmap(QtGui.QPixmap("../img/ico.png"))
        self.label_4.setScaledContents(True)
        self.label_4.setObjectName("label_4")
        self.btn_menuContenido = QtWidgets.QPushButton(self.frame_3)
        self.btn_menuContenido.setGeometry(QtCore.QRect(20, 140, 171, 30))
        self.btn_menuContenido.setMinimumSize(QtCore.QSize(0, 30))
        self.btn_menuContenido.setStyleSheet("QPushButton {\n"
"    font: 11.5pt \"Calibri\";\n"
"    color: rgb(255, 255, 255);\n"
"    padding-left:-10px;\n"
"    background-color: rgb(0, 46, 109);\n"
"    border: 0px solid;\n"
"    border-radius:15px;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(93, 129, 163);\n"
"}\n"
"\n"
"\n"
"    \n"
"    \n"
"    \n"
"    \n"
"")
        self.btn_menuContenido.setFlat(False)
        self.btn_menuContenido.setObjectName("btn_menuContenido")
        self.verticalLayout_3.addWidget(self.frame_3)
        self.horizontalLayout_2.addWidget(self.frame_left_menu)
        self.frame_pages = QtWidgets.QFrame(self.Content)
        self.frame_pages.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.frame_pages.setStyleSheet("background-color: rgb(217, 217, 217);")
        self.frame_pages.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_pages.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_pages.setObjectName("frame_pages")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.frame_pages)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.stackedWidget = QtWidgets.QStackedWidget(self.frame_pages)
        self.stackedWidget.setStyleSheet("background-color: rgb(217, 217, 217);")
        self.stackedWidget.setObjectName("stackedWidget")
        self.page_1 = QtWidgets.QWidget()
        self.page_1.setObjectName("page_1")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.page_1)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.frame = QtWidgets.QFrame(self.page_1)
        self.frame.setStyleSheet("QFrame{\n"
"    background-color: rgb(217, 217, 217);\n"
"    border-radius:26px;\n"
"\n"
"}")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.frame_input_messages = QtWidgets.QFrame(self.frame)
        self.frame_input_messages.setGeometry(QtCore.QRect(30, 410, 731, 71))
        self.frame_input_messages.setStyleSheet("QFrame{\n"
"    \n"
"    \n"
"    \n"
"    padding-top:1px;\n"
"    border-radius:25px;\n"
"}")
        self.frame_input_messages.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_input_messages.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_input_messages.setObjectName("frame_input_messages")
        self.pushButton = QtWidgets.QPushButton(self.frame_input_messages)
        self.pushButton.setGeometry(QtCore.QRect(660, 10, 51, 51))
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton.setStyleSheet("QPushButton{\n"
"    background-color: rgb(167, 182, 203);\n"
"    padding-top:1px;\n"
"    border-radius:25px;\n"
"    border-color: rgb(0, 46, 109);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(93, 129, 163);\n"
"}")
        self.pushButton.setObjectName("pushButton")
        self.label_5 = QtWidgets.QLabel(self.frame_input_messages)
        self.label_5.setGeometry(QtCore.QRect(20, 0, 61, 61))
        self.label_5.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.label_5.setStyleSheet("")
        self.label_5.setText("")
        self.label_5.setPixmap(QtGui.QPixmap("../../../Downloads/icoUser.png"))
        self.label_5.setScaledContents(True)
        self.label_5.setWordWrap(True)
        self.label_5.setObjectName("label_5")
        self.frame_4 = QtWidgets.QFrame(self.frame_input_messages)
        self.frame_4.setGeometry(QtCore.QRect(100, 11, 541, 51))
        self.frame_4.setStyleSheet("QFrame{\n"
"    \n"
"    \n"
"    \n"
"    \n"
"    \n"
"    \n"
"    background-color: rgb(148, 148, 148);\n"
"    padding-top:1px;\n"
"    border-radius:25px;\n"
"    \n"
"    border-color: rgb(0, 46, 109);\n"
"}")
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.lineEdit = QtWidgets.QLineEdit(self.frame_4)
        self.lineEdit.setGeometry(QtCore.QRect(0, 0, 541, 51))
        self.lineEdit.setStyleSheet("QLineEdit{\n"
"    \n"
"    \n"
"    \n"
"    \n"
"    background-color: rgb(217, 217, 217);\n"
"    padding-top:1px;\n"
"    border-radius:25px;\n"
"    \n"
"    border-color: rgb(0, 46, 109);\n"
"}")
        self.lineEdit.setObjectName("lineEdit")
        self.frame_4.raise_()
        self.pushButton.raise_()
        self.label_5.raise_()
        self.verticalLayout_7.addWidget(self.frame)
        self.stackedWidget.addWidget(self.page_1)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.page_2)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.label_9 = QtWidgets.QLabel(self.page_2)
        self.label_9.setObjectName("label_9")
        self.gridLayout_3.addWidget(self.label_9, 1, 3, 1, 1)
        self.label_10 = QtWidgets.QLabel(self.page_2)
        self.label_10.setObjectName("label_10")
        self.gridLayout_3.addWidget(self.label_10, 1, 4, 1, 1)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_7 = QtWidgets.QLabel(self.page_2)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_5.addWidget(self.label_7)
        self.gridLayout_3.addLayout(self.horizontalLayout_5, 1, 1, 1, 1)
        self.label_11 = QtWidgets.QLabel(self.page_2)
        self.label_11.setObjectName("label_11")
        self.gridLayout_3.addWidget(self.label_11, 1, 5, 1, 1)
        self.verticalLayout_10 = QtWidgets.QVBoxLayout()
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.label_6 = QtWidgets.QLabel(self.page_2)
        self.label_6.setObjectName("label_6")
        self.verticalLayout_10.addWidget(self.label_6)
        self.gridLayout_3.addLayout(self.verticalLayout_10, 1, 0, 1, 1)
        self.btn_Nuevo = QtWidgets.QPushButton(self.page_2)
        self.btn_Nuevo.setMinimumSize(QtCore.QSize(0, 30))
        self.btn_Nuevo.setStyleSheet("QPushButton {\n"
"    \n"
"    font: 14pt \"Calibri\";\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgb(0, 46, 109);\n"
"    border: 0px solid;\n"
"    border-radius:15px;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(93, 129, 163);\n"
"}\n"
"\n"
"\n"
"    \n"
"    \n"
"    \n"
"    \n"
"")
        self.btn_Nuevo.setFlat(False)
        self.btn_Nuevo.setObjectName("btn_Nuevo")
        self.gridLayout_3.addWidget(self.btn_Nuevo, 0, 5, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.page_2)
        self.label_8.setObjectName("label_8")
        self.gridLayout_3.addWidget(self.label_8, 0, 0, 1, 2)
        self.verticalLayout_6.addLayout(self.gridLayout_3)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_6.addItem(spacerItem)
        self.stackedWidget.addWidget(self.page_2)
        self.page_8 = QtWidgets.QWidget()
        self.page_8.setObjectName("page_8")
        self.frame_5 = QtWidgets.QFrame(self.page_8)
        self.frame_5.setGeometry(QtCore.QRect(10, 10, 781, 501))
        self.frame_5.setStyleSheet("QFrame{\n"
"    background-color: rgb(217, 217, 217);\n"
"    border-radius:26px;\n"
"\n"
"}")
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.label = QtWidgets.QLabel(self.frame_5)
        self.label.setGeometry(QtCore.QRect(370, 190, 141, 61))
        self.label.setStyleSheet("font: 16pt \"Calibri\";")
        self.label.setObjectName("label")
        self.stackedWidget.addWidget(self.page_8)
        self.verticalLayout_5.addWidget(self.stackedWidget)
        self.horizontalLayout_2.addWidget(self.frame_pages)
        self.verticalLayout.addWidget(self.Content)
        VentanaEditor.setCentralWidget(self.centralwidget)

        self.retranslateUi(VentanaEditor)
        self.stackedWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(VentanaEditor)

        self.btn_chat.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_1))
        self.btn_menuContenido.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_2))
        self.btn_about.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_8))

        self.btn_Nuevo.clicked.connect(self.nuevoContenido)
    def nuevoContenido(self):

        self.ventana = QtWidgets.QMainWindow()
        from ventanas.AgregarContenido import Ui_agregarContenido
        self.ui = Ui_agregarContenido()
        self.ui.setupUi(self.ventana)
        self.ventana.show()
    def retranslateUi(self, VentanaEditor):
        _translate = QtCore.QCoreApplication.translate
        VentanaEditor.setWindowTitle(_translate("VentanaEditor", "MainWindow"))
        self.btn_chat.setText(_translate("VentanaEditor", "Chat"))
        self.label_2.setText(_translate("VentanaEditor", "Nombre_user"))
        self.label_3.setText(_translate("VentanaEditor", "Editor"))
        self.btn_cerrarSesion.setText(_translate("VentanaEditor", "Cerrar Sesión"))
        self.btn_about.setText(_translate("VentanaEditor", "Sobre Foxy Bot"))
        self.btn_menuContenido.setText(_translate("VentanaEditor", "Menú de Contenido"))
        self.pushButton.setText(_translate("VentanaEditor", "Enviar"))
        self.lineEdit.setPlaceholderText(_translate("VentanaEditor", "¡Escribe aquí tus dudas!"))
        self.label_9.setText(_translate("VentanaEditor", "Solución"))
        self.label_10.setText(_translate("VentanaEditor", "Palabras clave"))
        self.label_7.setText(_translate("VentanaEditor", "Titulo"))
        self.label_11.setText(_translate("VentanaEditor", "Fecha de modificacion"))
        self.label_6.setText(_translate("VentanaEditor", "Area de servicios"))
        self.btn_Nuevo.setText(_translate("VentanaEditor", "+Nuevo"))
        self.label_8.setText(_translate("VentanaEditor", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Contenido: Preguntas/Respuestas de Foxy Bot </span></p></body></html>"))
        self.label.setText(_translate("VentanaEditor", "<html><head/><body><p><span style=\" font-size:18pt;\">FOXYBOT v0.1</span></p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    VentanaEditor = QtWidgets.QMainWindow()
    ui = Ui_VentanaEditor()
    ui.setupUi(VentanaEditor)
    VentanaEditor.show()
    sys.exit(app.exec_())
