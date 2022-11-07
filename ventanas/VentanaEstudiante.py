from PyQt5 import QtCore, QtGui, QtWidgets
from VentanaIngreso import *

class Ui_VentanaEstudiante(object):
    def setupUi(self, VentanaEstudiante):
        VentanaEstudiante.setObjectName("VentanaEstudiante")
        VentanaEstudiante.resize(1028, 538)
        VentanaEstudiante.setMinimumSize(QtCore.QSize(1000, 500))
        VentanaEstudiante.setStyleSheet("background-color: rgb(45, 45, 45);")
        self.centralwidget = QtWidgets.QWidget(VentanaEstudiante)
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
        self.btn_chat.setGeometry(QtCore.QRect(20, 90, 171, 30))
        self.btn_chat.setMinimumSize(QtCore.QSize(0, 30))
        self.btn_chat.setStyleSheet("QPushButton {\n"
"    font: 11.5pt \"Calibri\";\n"
"    color: rgb(255, 255, 255);\n"
"    padding-left:-90px;\n"
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
"    \n"
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
        self.btn_about.setGeometry(QtCore.QRect(20, 300, 171, 30))
        self.btn_about.setMinimumSize(QtCore.QSize(0, 30))
        self.btn_about.setStyleSheet("QPushButton {\n"
"    font: 11.5pt \"Calibri\";\n"
"    color: rgb(255, 255, 255);\n"
"    padding-left:-27px;\n"
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
        self.btn_about_2 = QtWidgets.QPushButton(self.frame_3)
        self.btn_about_2.setGeometry(QtCore.QRect(20, 150, 171, 30))
        self.btn_about_2.setMinimumSize(QtCore.QSize(0, 30))
        self.btn_about_2.setStyleSheet("QPushButton {\n"
"    font: 11.5pt \"Calibri\";\n"
"    color: rgb(255, 255, 255);\n"
"    padding-left:-27px;\n"
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
        self.btn_about_2.setFlat(False)
        self.btn_about_2.setObjectName("btn_about_2")
        self.btn_about_3 = QtWidgets.QPushButton(self.frame_3)
        self.btn_about_3.setGeometry(QtCore.QRect(20, 180, 171, 30))
        self.btn_about_3.setMinimumSize(QtCore.QSize(0, 30))
        self.btn_about_3.setStyleSheet("QPushButton {\n"
"    font: 11.5pt \"Calibri\";\n"
"    color: rgb(255, 255, 255);\n"
"    padding-left:-27px;\n"
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
        self.btn_about_3.setFlat(False)
        self.btn_about_3.setObjectName("btn_about_3")
        self.btn_about_4 = QtWidgets.QPushButton(self.frame_3)
        self.btn_about_4.setGeometry(QtCore.QRect(20, 210, 171, 30))
        self.btn_about_4.setMinimumSize(QtCore.QSize(0, 30))
        self.btn_about_4.setStyleSheet("QPushButton {\n"
"    font: 11.5pt \"Calibri\";\n"
"    color: rgb(255, 255, 255);\n"
"    padding-left:-27px;\n"
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
        self.btn_about_4.setFlat(False)
        self.btn_about_4.setObjectName("btn_about_4")
        self.btn_about_5 = QtWidgets.QPushButton(self.frame_3)
        self.btn_about_5.setGeometry(QtCore.QRect(20, 240, 171, 30))
        self.btn_about_5.setMinimumSize(QtCore.QSize(0, 30))
        self.btn_about_5.setStyleSheet("QPushButton {\n"
"    font: 11.5pt \"Calibri\";\n"
"    color: rgb(255, 255, 255);\n"
"    padding-left:-27px;\n"
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
        self.btn_about_5.setFlat(False)
        self.btn_about_5.setObjectName("btn_about_5")
        self.btn_about_6 = QtWidgets.QPushButton(self.frame_3)
        self.btn_about_6.setGeometry(QtCore.QRect(20, 270, 171, 30))
        self.btn_about_6.setMinimumSize(QtCore.QSize(0, 30))
        self.btn_about_6.setStyleSheet("QPushButton {\n"
"    font: 11.5pt \"Calibri\";\n"
"    color: rgb(255, 255, 255);\n"
"    padding-left:-27px;\n"
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
        self.btn_about_6.setFlat(False)
        self.btn_about_6.setObjectName("btn_about_6")
        self.btn_about_7 = QtWidgets.QPushButton(self.frame_3)
        self.btn_about_7.setGeometry(QtCore.QRect(20, 120, 171, 30))
        self.btn_about_7.setMinimumSize(QtCore.QSize(0, 30))
        self.btn_about_7.setStyleSheet("QPushButton {\n"
"    font: 11.5pt \"Calibri\";\n"
"    color: rgb(255, 255, 255);\n"
"    padding-left:-27px;\n"
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
        self.btn_about_7.setFlat(False)
        self.btn_about_7.setObjectName("btn_about_7")
        self.verticalLayout_3.addWidget(self.frame_3)
        self.horizontalLayout_2.addWidget(self.frame_left_menu)
        self.frame_pages = QtWidgets.QFrame(self.Content)
        self.frame_pages.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.frame_pages.setStyleSheet("background-color: rgb(167, 182, 203);")
        self.frame_pages.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_pages.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_pages.setObjectName("frame_pages")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.frame_pages)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.stackedWidget = QtWidgets.QStackedWidget(self.frame_pages)
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
        self.frame_input_messages.setGeometry(QtCore.QRect(10, 400, 721, 71))
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
        self.lineEdit = QtWidgets.QLineEdit(self.frame_input_messages)
        self.lineEdit.setGeometry(QtCore.QRect(100, 9, 601, 51))
        self.lineEdit.setStyleSheet("QLineEdit{\n"
"    \n"
"    \n"
"    \n"
"    \n"
"    background-color: rgb(167, 182, 203);\n"
"    padding-top:1px;\n"
"    border-radius:25px;\n"
"    \n"
"    border-color: rgb(0, 46, 109);\n"
"}")
        self.lineEdit.setObjectName("lineEdit")
        self.label_5 = QtWidgets.QLabel(self.frame_input_messages)
        self.label_5.setGeometry(QtCore.QRect(10, 20, 51, 41))
        self.label_5.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.label_5.setText("")
        self.label_5.setPixmap(QtGui.QPixmap("../img/ico.png"))
        self.label_5.setScaledContents(True)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_7.addWidget(self.frame)
        self.stackedWidget.addWidget(self.page_1)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.page_2)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.frame_2 = QtWidgets.QFrame(self.page_2)
        self.frame_2.setStyleSheet("QFrame{\n"
"    background-color: rgb(217, 217, 217);\n"
"    border-radius:26px;\n"
"\n"
"}")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout_6.addWidget(self.frame_2)
        self.stackedWidget.addWidget(self.page_2)
        self.page_3 = QtWidgets.QWidget()
        self.page_3.setObjectName("page_3")
        self.stackedWidget.addWidget(self.page_3)
        self.page_4 = QtWidgets.QWidget()
        self.page_4.setObjectName("page_4")
        self.stackedWidget.addWidget(self.page_4)
        self.page_5 = QtWidgets.QWidget()
        self.page_5.setObjectName("page_5")
        self.stackedWidget.addWidget(self.page_5)
        self.page_6 = QtWidgets.QWidget()
        self.page_6.setObjectName("page_6")
        self.stackedWidget.addWidget(self.page_6)
        self.page_7 = QtWidgets.QWidget()
        self.page_7.setObjectName("page_7")
        self.stackedWidget.addWidget(self.page_7)
        self.page_8 = QtWidgets.QWidget()
        self.page_8.setObjectName("page_8")
        self.stackedWidget.addWidget(self.page_8)
        self.verticalLayout_5.addWidget(self.stackedWidget)
        self.horizontalLayout_2.addWidget(self.frame_pages)
        self.verticalLayout.addWidget(self.Content)
        VentanaEstudiante.setCentralWidget(self.centralwidget)

        self.btn_cerrarSesion.clicked.connect(self.cerrarSesion)
        self.btn_cerrarSesion.clicked.connect(VentanaEstudiante.close)

        self.retranslateUi(VentanaEstudiante)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(VentanaEstudiante)

    def cerrarSesion(self):
        self.ventana = QtWidgets.QMainWindow()
        from ventanas.VentanaIngreso import Ui_VentanaIngreso
        self.ui = Ui_VentanaIngreso()
        self.ui.setupUi(self.ventana)
        self.ventana.show()


    def retranslateUi(self, VentanaEstudiante):
        _translate = QtCore.QCoreApplication.translate
        VentanaEstudiante.setWindowTitle(_translate("VentanaEstudiante", "MainWindow"))
        self.btn_chat.setText(_translate("VentanaEstudiante", "Chat"))
        self.label_2.setText(_translate("VentanaEstudiante", "Nombre_user"))
        self.label_3.setText(_translate("VentanaEstudiante", "Estudiante"))
        self.btn_cerrarSesion.setText(_translate("VentanaEstudiante", "Cerrar Sesión"))
        self.btn_about.setText(_translate("VentanaEstudiante", "Sobre Foxy Bot"))
        self.btn_about_2.setText(_translate("VentanaEstudiante", "Solicitudes Enviadas"))
        self.btn_about_3.setText(_translate("VentanaEstudiante", "Solicitudes Resueltas"))
        self.btn_about_4.setText(_translate("VentanaEstudiante", "Solicitudes Devueltas"))
        self.btn_about_5.setText(_translate("VentanaEstudiante", "Solicitudes Devueltas"))
        self.btn_about_6.setText(_translate("VentanaEstudiante", "Ajustes"))
        self.btn_about_7.setText(_translate("VentanaEstudiante", "Solicitudes"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    VentanaEstudiante = QtWidgets.QMainWindow()
    ui = Ui_VentanaEstudiante()
    ui.setupUi(VentanaEstudiante)
    VentanaEstudiante.show()
    sys.exit(app.exec_())
