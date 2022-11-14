# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'VentanaVisitante.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets

from PyQt5.QtWidgets import QWidget,QApplication, QListWidget, QDialog,QListWidgetItem,QWidgetItem

from RecWid import Widget as recWidget
from SenWid import Widget as senWidget


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1016, 550)
        MainWindow.setMinimumSize(QtCore.QSize(1000, 500))
        MainWindow.setStyleSheet("background-color: rgb(45, 45, 45);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
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
        self.btn_chat.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
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
        self.label_2.setGeometry(QtCore.QRect(80, 20, 47, 13))
        self.label_2.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 11.5pt \"Calibri\";")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.frame_3)
        self.label_3.setGeometry(QtCore.QRect(80, 31, 61, 20))
        self.label_3.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 25 11pt \"Calibri Light\";\n"
"background-color: transparent;")
        self.label_3.setObjectName("label_3")
        self.btn_iniciarSesion = QtWidgets.QPushButton(self.frame_3)
        self.btn_iniciarSesion.setGeometry(QtCore.QRect(30, 440, 171, 30))
        self.btn_iniciarSesion.setMinimumSize(QtCore.QSize(0, 30))
        self.btn_iniciarSesion.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_iniciarSesion.setStyleSheet("QPushButton {\n"
"    font: 9pt \"Calibri\";\n"
"    color: rgb(255, 255, 255);\n"
"    padding-left:-47px;\n"
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
        self.btn_iniciarSesion.setFlat(False)
        self.btn_iniciarSesion.setObjectName("btn_iniciarSesion")
        self.btn_registro = QtWidgets.QPushButton(self.frame_3)
        self.btn_registro.setGeometry(QtCore.QRect(30, 470, 171, 30))
        self.btn_registro.setMinimumSize(QtCore.QSize(0, 30))
        self.btn_registro.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_registro.setStyleSheet("QPushButton {\n"
"    font: 9pt \"Calibri\";\n"
"    color: rgb(255, 255, 255);\n"
"    padding-left:-59px;\n"
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
        self.btn_registro.setFlat(False)
        self.btn_registro.setObjectName("btn_registro")
        self.btn_about = QtWidgets.QPushButton(self.frame_3)
        self.btn_about.setGeometry(QtCore.QRect(20, 120, 171, 30))
        self.btn_about.setMinimumSize(QtCore.QSize(0, 30))
        self.btn_about.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
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
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.page_1)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
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
        self.frame_input_messages.setGeometry(QtCore.QRect(10, 400, 731, 71))
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
        self.listView = QtWidgets.QListView(self.frame)
        self.listView.setGeometry(QtCore.QRect(20, 20, 721, 351))
        self.listView.setObjectName("listView")
        self.horizontalLayout_3.addWidget(self.frame)
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
        self.verticalLayout_5.addWidget(self.stackedWidget)
        self.horizontalLayout_2.addWidget(self.frame_pages)
        self.verticalLayout.addWidget(self.Content)
        MainWindow.setCentralWidget(self.centralwidget)

        self.btn_iniciarSesion.clicked.connect(MainWindow.close)
        self.btn_iniciarSesion.clicked.connect(self.abrirIngreso)

        self.btn_registro.clicked.connect(MainWindow.close)
        self.btn_registro.clicked.connect(self.abrirRegistro)

        self.btn_chat.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_1))
        self.btn_about.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_2))

        self.pushButton.clicked.connect(self.sendMessage)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def abrirIngreso(self):
        self.ventana = QtWidgets.QMainWindow()
        from ventanas.VentanaIngreso import Ui_VentanaIngreso
        self.ui = Ui_VentanaIngreso()
        self.ui.setupUi(self.ventana)
        self.ventana.show()

    def abrirRegistro(self):
        self.ventana = QtWidgets.QMainWindow()
        from ventanas.VentanaRegistro import Ui_VentanaRegistro
        self.ui = Ui_VentanaRegistro()
        self.ui.setupUi(self.ventana)
        self.ventana.show()

    def sendMessage(self):
        sendW = senWidget()
        sendW.label_2.setText(str(self.lineEdit.text()))
        item = QListWidgetItem()
        item.setSizeHint(sendW.sizeHint())
        self.listView.addAction(item)
        self.listView.addAction(item, sendW)
        self.listView.setMinimumWidth(sendW.width())
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.btn_chat.setText(_translate("MainWindow", "Chat"))
        self.label_2.setText(_translate("MainWindow", "Usuario"))
        self.label_3.setText(_translate("MainWindow", "Visitante"))
        self.btn_iniciarSesion.setText(_translate("MainWindow", "Iniciar Sesión"))
        self.btn_registro.setText(_translate("MainWindow", "Registrarse"))
        self.btn_about.setText(_translate("MainWindow", "Sobre Foxy Bot"))
        self.pushButton.setText(_translate("MainWindow", "Enviar"))
        self.lineEdit.setPlaceholderText(_translate("MainWindow", "¡Escribe aquí tus dudas!"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
