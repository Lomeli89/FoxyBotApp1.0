from PyQt5.QtWidgets import QDialog, QApplication, QListWidgetItem
from recibeWidget import Widget as recWidget
from sendWidget import Widget as senWidget
from windows import Conexion
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindowAdmin(object):
    def setupUi(self, MainWindowAdmin):
        MainWindowAdmin.setObjectName("MainWindowAdmin")
        MainWindowAdmin.resize(1002, 600)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindowAdmin.sizePolicy().hasHeightForWidth())
        MainWindowAdmin.setSizePolicy(sizePolicy)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../../../.designer/img/298809902_539628011298194_5839572564237821349_n.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindowAdmin.setWindowIcon(icon)
        MainWindowAdmin.setStyleSheet("background-color: rgb(45, 45, 45);")
        self.centralwidget = QtWidgets.QWidget(MainWindowAdmin)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frame_6 = QtWidgets.QFrame(self.centralwidget)
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.frame_6)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, -1)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.frame_7 = QtWidgets.QFrame(self.frame_6)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_7.sizePolicy().hasHeightForWidth())
        self.frame_7.setSizePolicy(sizePolicy)
        self.frame_7.setStyleSheet("background-color: rgb(0, 46, 109);")
        self.frame_7.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_7.setObjectName("frame_7")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.frame_7)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 6)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.contenido = QtWidgets.QHBoxLayout()
        self.contenido.setSpacing(0)
        self.contenido.setObjectName("contenido")
        self.frame_izquierdo = QtWidgets.QVBoxLayout()
        self.frame_izquierdo.setSpacing(0)
        self.frame_izquierdo.setObjectName("frame_izquierdo")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setContentsMargins(-1, -1, -1, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.frame = QtWidgets.QFrame(self.frame_7)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setMaximumSize(QtCore.QSize(212, 16777215))
        self.frame.setStyleSheet("background-color: rgb(0, 46, 109);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_3.setContentsMargins(-1, 0, -1, -1)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.frame_3 = QtWidgets.QFrame(self.frame)
        self.frame_3.setMaximumSize(QtCore.QSize(16777215, 150))
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame_3)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_4 = QtWidgets.QLabel(self.frame_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        self.label_4.setMaximumSize(QtCore.QSize(51, 41))
        self.label_4.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.label_4.setText("")
        self.label_4.setPixmap(QtGui.QPixmap("../../../.designer/img/ico.png"))
        self.label_4.setScaledContents(True)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_2.addWidget(self.label_4)
        self.label_user_2 = QtWidgets.QLabel(self.frame_3)
        self.label_user_2.setMaximumSize(QtCore.QSize(50, 50))
        self.label_user_2.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 11.5pt \"Calibri\";")
        self.label_user_2.setText("")
        self.label_user_2.setPixmap(QtGui.QPixmap("../img/ico.png"))
        self.label_user_2.setScaledContents(True)
        self.label_user_2.setObjectName("label_user_2")
        self.horizontalLayout_2.addWidget(self.label_user_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.frame_5 = QtWidgets.QFrame(self.frame_3)
        self.frame_5.setMaximumSize(QtCore.QSize(16777215, 50))
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.frame_5)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.label_user = QtWidgets.QLabel(self.frame_5)
        self.label_user.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 11.5pt \"Calibri\";")
        self.label_user.setObjectName("label_user")
        self.verticalLayout_8.addWidget(self.label_user)
        self.label_estudiante = QtWidgets.QLabel(self.frame_5)
        self.label_estudiante.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 25 11pt \"Calibri Light\";\n"
"background-color: transparent;")
        self.label_estudiante.setObjectName("label_estudiante")
        self.verticalLayout_8.addWidget(self.label_estudiante)
        self.horizontalLayout_3.addWidget(self.frame_5)
        self.horizontalLayout_2.addLayout(self.horizontalLayout_3)
        self.verticalLayout_3.addWidget(self.frame_3)
        self.btn_chat = QtWidgets.QPushButton(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_chat.sizePolicy().hasHeightForWidth())
        self.btn_chat.setSizePolicy(sizePolicy)
        self.btn_chat.setMinimumSize(QtCore.QSize(0, 30))
        self.btn_chat.setMaximumSize(QtCore.QSize(171, 30))
        self.btn_chat.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_chat.setStyleSheet("QPushButton {\n"
"    \n"
"    \n"
"    font: 75 11.5pt \"SansSerif\";\n"
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
        self.verticalLayout_3.addWidget(self.btn_chat)
        self.btn_servicios = QtWidgets.QPushButton(self.frame)
        self.btn_servicios.setMinimumSize(QtCore.QSize(0, 30))
        self.btn_servicios.setMaximumSize(QtCore.QSize(171, 30))
        self.btn_servicios.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_servicios.setStyleSheet("QPushButton {\n"
"    font: 75 11.5pt \"SansSerif\";\n"
"    color: rgb(255, 255, 255);\n"
"    padding-left:10px;\n"
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
        self.btn_servicios.setFlat(False)
        self.btn_servicios.setObjectName("btn_servicios")
        self.verticalLayout_3.addWidget(self.btn_servicios)
        self.btn_editores = QtWidgets.QPushButton(self.frame)
        self.btn_editores.setMinimumSize(QtCore.QSize(0, 30))
        self.btn_editores.setMaximumSize(QtCore.QSize(171, 30))
        self.btn_editores.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_editores.setStyleSheet("QPushButton {\n"
"    font: 75 11.5pt \"SansSerif\";\n"
"    color: rgb(255, 255, 255);\n"
"    padding-left:2px;\n"
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
        self.btn_editores.setFlat(False)
        self.btn_editores.setObjectName("btn_editores")
        self.verticalLayout_3.addWidget(self.btn_editores)
        self.btn_about = QtWidgets.QPushButton(self.frame)
        self.btn_about.setMinimumSize(QtCore.QSize(0, 30))
        self.btn_about.setMaximumSize(QtCore.QSize(171, 30))
        self.btn_about.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_about.setStyleSheet("QPushButton {\n"
"    font: 75 11.5pt \"SansSerif\";\n"
"    color: rgb(255, 255, 255);\n"
"    padding-left:-20px;\n"
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
        self.verticalLayout_3.addWidget(self.btn_about)
        self.frame_4 = QtWidgets.QFrame(self.frame)
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.verticalLayout_3.addWidget(self.frame_4)
        self.btn_cerrarSesion = QtWidgets.QPushButton(self.frame)
        self.btn_cerrarSesion.setMinimumSize(QtCore.QSize(0, 30))
        self.btn_cerrarSesion.setMaximumSize(QtCore.QSize(171, 30))
        self.btn_cerrarSesion.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_cerrarSesion.setStyleSheet("QPushButton {\n"
"    font: 75 11.5pt \"SansSerif\";\n"
"    color: rgb(255, 255, 255);\n"
"    padding-left:-29px;\n"
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
        self.verticalLayout_3.addWidget(self.btn_cerrarSesion)
        self.verticalLayout_2.addWidget(self.frame)
        self.frame_izquierdo.addLayout(self.verticalLayout_2)
        self.contenido.addLayout(self.frame_izquierdo)
        self.horizontalLayout_5.addLayout(self.contenido)
        self.horizontalLayout_4.addWidget(self.frame_7)
        self.frame_8 = QtWidgets.QFrame(self.frame_6)
        self.frame_8.setStyleSheet("background-color: rgb(167, 182, 203);")
        self.frame_8.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_8.setObjectName("frame_8")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.frame_8)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.stackedWidget = QtWidgets.QStackedWidget(self.frame_8)
        self.stackedWidget.setStyleSheet("QFrame{\n"
"    background-color: rgb(217, 217, 217);\n"
"    \n"
"\n"
"}")
        self.stackedWidget.setObjectName("stackedWidget")
        self.page_chat = QtWidgets.QWidget()
        self.page_chat.setObjectName("page_chat")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.page_chat)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame_2 = QtWidgets.QFrame(self.page_chat)
        self.frame_2.setStyleSheet("")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.frame_2)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.frame_11 = QtWidgets.QFrame(self.frame_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_11.sizePolicy().hasHeightForWidth())
        self.frame_11.setSizePolicy(sizePolicy)
        self.frame_11.setStyleSheet("background-color: rgb(45, 45, 45);\n"
"border-bottom-left-radius : 5px;\n"
"border-bottom-right-radius : 5px\n"
"")
        self.frame_11.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_11.setObjectName("frame_11")
        self.verticalLayout_12 = QtWidgets.QVBoxLayout(self.frame_11)
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.label = QtWidgets.QLabel(self.frame_11)
        self.label.setStyleSheet("margin-left: 10px; \n"
"font: 9pt \"MS Sans Serif\";\n"
"background-color: rgb(45, 45, 45);")
        self.label.setObjectName("label")
        self.verticalLayout_12.addWidget(self.label)
        self.verticalLayout_4.addWidget(self.frame_11)
        self.frame_9 = QtWidgets.QFrame(self.frame_2)
        self.frame_9.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_9.setObjectName("frame_9")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.frame_9)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout()
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.groupBox = QtWidgets.QGroupBox(self.frame_9)
        self.groupBox.setStyleSheet("background-color: rgb(217, 217, 217);")
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.listWidget = QtWidgets.QListWidget(self.groupBox)
        self.listWidget.setStyleSheet("")
        self.listWidget.setObjectName("listWidget")
        self.verticalLayout_11.addWidget(self.listWidget)
        self.verticalLayout_10.addWidget(self.groupBox)
        self.verticalLayout_9.addLayout(self.verticalLayout_10)
        self.frame_10 = QtWidgets.QFrame(self.frame_9)
        self.frame_10.setMaximumSize(QtCore.QSize(16777215, 70))
        self.frame_10.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_10.setObjectName("frame_10")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.frame_10)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setSpacing(0)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.label_5 = QtWidgets.QLabel(self.frame_10)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy)
        self.label_5.setMinimumSize(QtCore.QSize(50, 50))
        self.label_5.setMaximumSize(QtCore.QSize(50, 50))
        self.label_5.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.label_5.setStyleSheet("")
        self.label_5.setText("")
        self.label_5.setPixmap(QtGui.QPixmap("../../../../Downloads/icoUser.png"))
        self.label_5.setScaledContents(True)
        self.label_5.setWordWrap(True)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_9.addWidget(self.label_5)
        self.lineEdit = QtWidgets.QLineEdit(self.frame_10)
        self.lineEdit.setMaximumSize(QtCore.QSize(560, 35))
        self.lineEdit.setStyleSheet("QLineEdit{\n"
"    background-color: rgb(217, 217, 217);\n"
"    font: 9pt \"MS Sans Serif\";\n"
"    border: 2px solid rgb(158, 158, 158);\n"
"    border-radius: 15px;\n"
"    \n"
"}")
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout_9.addWidget(self.lineEdit)
        self.btn_enviar = QtWidgets.QPushButton(self.frame_10)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_enviar.sizePolicy().hasHeightForWidth())
        self.btn_enviar.setSizePolicy(sizePolicy)
        self.btn_enviar.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_enviar.setStyleSheet("QPushButton {\n"
"    \n"
"    \n"
"    background-color:transparent;\n"
"font: 9pt \"MS Sans Serif\";\n"
"\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(250, 250, 250);\n"
"}\n"
"\n"
"\n"
"")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("../../../.designer/img/botonSend.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_enviar.setIcon(icon1)
        self.btn_enviar.setObjectName("btn_enviar")
        self.horizontalLayout_9.addWidget(self.btn_enviar)
        self.horizontalLayout_8.addLayout(self.horizontalLayout_9)
        self.verticalLayout_9.addWidget(self.frame_10)
        self.verticalLayout_4.addWidget(self.frame_9)
        self.verticalLayout.addWidget(self.frame_2)
        self.stackedWidget.addWidget(self.page_chat)
        self.page_servicios = QtWidgets.QWidget()
        self.page_servicios.setStyleSheet("background-color: rgb(217, 217, 217);")
        self.page_servicios.setObjectName("page_servicios")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.page_servicios)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.frame_16 = QtWidgets.QFrame(self.page_servicios)
        self.frame_16.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_16.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_16.setObjectName("frame_16")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.frame_16)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.pushButton = QtWidgets.QPushButton(self.frame_16)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_7.addWidget(self.pushButton)
        self.label_3 = QtWidgets.QLabel(self.frame_16)
        self.label_3.setStyleSheet("font: 75 11.5pt \"SansSerif\";")
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_7.addWidget(self.label_3)

        self.btn_eliminar = QtWidgets.QPushButton(self.frame_16)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_eliminar.sizePolicy().hasHeightForWidth())
        self.btn_eliminar.setSizePolicy(sizePolicy)
        self.btn_eliminar.setMinimumSize(QtCore.QSize(0, 30))
        self.btn_eliminar.setMaximumSize(QtCore.QSize(100, 16777215))
        self.btn_eliminar.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_eliminar.setStyleSheet("QPushButton {\n"
"    \n"
"    font: 14pt \"Calibri\";\n"
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
        self.btn_eliminar.setFlat(False)
        self.btn_eliminar.setObjectName("btn_eliminar")
        self.horizontalLayout_7.addWidget(self.btn_eliminar)
        self.btn_Nuevo = QtWidgets.QPushButton(self.frame_16)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_Nuevo.sizePolicy().hasHeightForWidth())
        self.btn_Nuevo.setSizePolicy(sizePolicy)
        self.btn_Nuevo.setMinimumSize(QtCore.QSize(0, 30))
        self.btn_Nuevo.setMaximumSize(QtCore.QSize(100, 16777215))
        self.btn_Nuevo.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
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
        self.horizontalLayout_7.addWidget(self.btn_Nuevo)
        self.verticalLayout_7.addLayout(self.horizontalLayout_7)
        self.tableWidget = QtWidgets.QTableWidget(self.frame_16)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(4)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignVCenter)
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        self.verticalLayout_7.addWidget(self.tableWidget)
        self.verticalLayout_6.addWidget(self.frame_16)
        self.stackedWidget.addWidget(self.page_servicios)
        self.page_editores = QtWidgets.QWidget()
        self.page_editores.setObjectName("page_editores")
        self.verticalLayout_27 = QtWidgets.QVBoxLayout(self.page_editores)
        self.verticalLayout_27.setObjectName("verticalLayout_27")
        self.frame_26 = QtWidgets.QFrame(self.page_editores)
        self.frame_26.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_26.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_26.setObjectName("frame_26")
        self.verticalLayout_29 = QtWidgets.QVBoxLayout(self.frame_26)
        self.verticalLayout_29.setObjectName("verticalLayout_29")
        self.frame_27 = QtWidgets.QFrame(self.frame_26)
        self.frame_27.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_27.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_27.setObjectName("frame_27")
        self.verticalLayout_28 = QtWidgets.QVBoxLayout(self.frame_27)
        self.verticalLayout_28.setObjectName("verticalLayout_28")
        self.horizontalLayout_17 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_17.setObjectName("horizontalLayout_17")
        self.pushButton_2 = QtWidgets.QPushButton(self.frame_27)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_2.sizePolicy().hasHeightForWidth())
        self.pushButton_2.setSizePolicy(sizePolicy)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout_17.addWidget(self.pushButton_2)
        self.label_12 = QtWidgets.QLabel(self.frame_27)
        self.label_12.setStyleSheet("font: 75 11.5pt \"SansSerif\";")
        self.label_12.setObjectName("label_12")
        self.horizontalLayout_17.addWidget(self.label_12)
        self.btn_eliminar_3 = QtWidgets.QPushButton(self.frame_27)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_eliminar_3.sizePolicy().hasHeightForWidth())
        self.btn_eliminar_3.setSizePolicy(sizePolicy)
        self.btn_eliminar_3.setMinimumSize(QtCore.QSize(0, 30))
        self.btn_eliminar_3.setMaximumSize(QtCore.QSize(100, 16777215))
        self.btn_eliminar_3.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_eliminar_3.setStyleSheet("QPushButton {\n"
"    \n"
"    font: 14pt \"Calibri\";\n"
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
        self.btn_eliminar_3.setFlat(False)
        self.btn_eliminar_3.setObjectName("btn_eliminar_3")
        self.horizontalLayout_17.addWidget(self.btn_eliminar_3)

        self.verticalLayout_28.addLayout(self.horizontalLayout_17)
        self.tableWidget_3 = QtWidgets.QTableWidget(self.frame_27)
        self.tableWidget_3.setObjectName("tableWidget_3")
        self.tableWidget_3.setColumnCount(6)
        self.tableWidget_3.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignVCenter)
        self.tableWidget_3.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(5, item)
        self.verticalLayout_28.addWidget(self.tableWidget_3)
        self.verticalLayout_29.addWidget(self.frame_27)
        self.verticalLayout_27.addWidget(self.frame_26)
        self.stackedWidget.addWidget(self.page_editores)
        self.page_about = QtWidgets.QWidget()
        self.page_about.setObjectName("page_about")
        self.verticalLayout_14 = QtWidgets.QVBoxLayout(self.page_about)
        self.verticalLayout_14.setObjectName("verticalLayout_14")
        self.verticalLayout_13 = QtWidgets.QVBoxLayout()
        self.verticalLayout_13.setObjectName("verticalLayout_13")
        self.frame_12 = QtWidgets.QFrame(self.page_about)
        self.frame_12.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_12.setObjectName("frame_12")
        self.verticalLayout_15 = QtWidgets.QVBoxLayout(self.frame_12)
        self.verticalLayout_15.setObjectName("verticalLayout_15")
        self.frame_15 = QtWidgets.QFrame(self.frame_12)
        self.frame_15.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_15.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_15.setObjectName("frame_15")
        self.verticalLayout_15.addWidget(self.frame_15)
        self.label_2 = QtWidgets.QLabel(self.frame_12)
        self.label_2.setStyleSheet("font: 75 35pt \"MS Sans Serif\";\n"
"color: rgb(167, 182, 203);")
        self.label_2.setObjectName("label_2")
        self.verticalLayout_15.addWidget(self.label_2)
        self.frame_14 = QtWidgets.QFrame(self.frame_12)
        self.frame_14.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_14.setObjectName("frame_14")
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout(self.frame_14)
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.label_6 = QtWidgets.QLabel(self.frame_14)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy)
        self.label_6.setMaximumSize(QtCore.QSize(90, 100))
        self.label_6.setText("")
        self.label_6.setPixmap(QtGui.QPixmap("../../../.designer/img/sdwhitw1.png"))
        self.label_6.setScaledContents(True)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_11.addWidget(self.label_6)
        self.verticalLayout_15.addWidget(self.frame_14)
        self.frame_13 = QtWidgets.QFrame(self.frame_12)
        self.frame_13.setMaximumSize(QtCore.QSize(16777215, 100))
        self.frame_13.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_13.setObjectName("frame_13")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout(self.frame_13)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.verticalLayout_15.addWidget(self.frame_13)
        self.verticalLayout_13.addWidget(self.frame_12)
        self.verticalLayout_14.addLayout(self.verticalLayout_13)
        self.stackedWidget.addWidget(self.page_about)
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.page)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.frame_17 = QtWidgets.QFrame(self.page)
        self.frame_17.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_17.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_17.setObjectName("frame_17")
        self.verticalLayout_16 = QtWidgets.QVBoxLayout(self.frame_17)
        self.verticalLayout_16.setObjectName("verticalLayout_16")
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.pushButton_3 = QtWidgets.QPushButton(self.frame_17)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_3.sizePolicy().hasHeightForWidth())
        self.pushButton_3.setSizePolicy(sizePolicy)
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout_12.addWidget(self.pushButton_3)
        self.label_7 = QtWidgets.QLabel(self.frame_17)
        self.label_7.setStyleSheet("font: 75 11.5pt \"SansSerif\";")
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_12.addWidget(self.label_7)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.frame_17)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.horizontalLayout_12.addWidget(self.lineEdit_2)
        self.btn_Nuevo_2 = QtWidgets.QPushButton(self.frame_17)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_Nuevo_2.sizePolicy().hasHeightForWidth())
        self.btn_Nuevo_2.setSizePolicy(sizePolicy)
        self.btn_Nuevo_2.setMinimumSize(QtCore.QSize(0, 30))
        self.btn_Nuevo_2.setMaximumSize(QtCore.QSize(100, 16777215))
        self.btn_Nuevo_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_Nuevo_2.setStyleSheet("QPushButton {\n"
"    \n"
"    font: 14pt \"Calibri\";\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgb(0, 46, 109);\n"
"    border: 0px solid;\n"
"    border-radius:7px;\n"
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
        self.btn_Nuevo_2.setFlat(False)
        self.btn_Nuevo_2.setObjectName("btn_Nuevo_2")
        self.horizontalLayout_12.addWidget(self.btn_Nuevo_2)
        self.verticalLayout_16.addLayout(self.horizontalLayout_12)
        self.tableWidget_2 = QtWidgets.QTableWidget(self.frame_17)
        self.tableWidget_2.setObjectName("tableWidget_2")
        self.tableWidget_2.setColumnCount(4)
        self.tableWidget_2.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignVCenter)
        self.tableWidget_2.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(3, item)
        self.verticalLayout_16.addWidget(self.tableWidget_2)
        self.verticalLayout_5.addWidget(self.frame_17)
        self.stackedWidget.addWidget(self.page)
        self.horizontalLayout_6.addWidget(self.stackedWidget)
        self.horizontalLayout_4.addWidget(self.frame_8)
        self.horizontalLayout.addWidget(self.frame_6)
        MainWindowAdmin.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindowAdmin)
        self.stackedWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindowAdmin)

        self.btn_chat.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_chat))
        self.btn_about.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_about))
        self.btn_servicios.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_servicios))
        self.btn_editores.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_editores))
        self.btn_cerrarSesion.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(MainWindowAdmin.close()))


        self.btn_enviar.clicked.connect(self.sendMessage)
        self.btn_Nuevo.clicked.connect(self.nuevoServicio)
        self.pushButton.clicked.connect(self.mostrar_soluciones)
        self.btn_Nuevo_2.clicked.connect(self.buscar_solucion_eliminar)
        self.pushButton_3.clicked.connect(self.eliminar_solucion_1)
        self.pushButton_2.clicked.connect(self.mUsuarios_1)
        self.btn_eliminar.clicked.connect(self.editar_solucion)
        self.btn_eliminar_3.clicked.connect(self.editar_user)

        self.btn_cerrarSesion.clicked.connect(self.cerrar_sesion)
        self.btn_cerrarSesion.clicked.connect(MainWindowAdmin.close)
        self.bienvenidaAutomatica()

    def cerrar_sesion(self):
        self.ventana = QtWidgets.QMainWindow()
        from windows.LoginWindow import Ui_MainWindowLogin
        self.ui = Ui_MainWindowLogin()
        self.ui.setupUi(self.ventana)
        self.ventana.show()

    def editar_user(self):
        self.ventana = QtWidgets.QDialog()
        from windows.EditarEditor import Ui_editarEditor
        self.ui = Ui_editarEditor()
        self.ui.setupUi(self.ventana)
        self.ventana.show()

    def editar_solucion(self):
        self.ventana = QtWidgets.QDialog()
        from windows.EditarContenido import Ui_WindowEditarContenido
        self.ui = Ui_WindowEditarContenido()
        self.ui.setupUi(self.ventana)
        self.ventana.show()

    def mostrar_soluciones(self):
        self.datos = Conexion.DataBase()
        datos1 = self.datos.mContenido()
        i = len(datos1)
        self.tableWidget.setRowCount(i)
        tablerow = 0
        for row in datos1:
            self.fila = row[0]
            self.tableWidget.setItem(tablerow, 0, QtWidgets.QTableWidgetItem(row[1]))
            self.tableWidget.setItem(tablerow, 1, QtWidgets.QTableWidgetItem(row[2]))
            self.tableWidget.setItem(tablerow, 2, QtWidgets.QTableWidgetItem(row[3]))
            self.tableWidget.setItem(tablerow, 3, QtWidgets.QTableWidgetItem(row[4]))
            tablerow += 1

    def mUsuarios_1(self):
        self.datos = Conexion.DataBase()
        datos1 = self.datos.mUsuarios()
        i = len(datos1)
        self.tableWidget_3.setRowCount(i)
        tablerow = 0
        for row in datos1:
            self.newFila = row[0]
            self.tableWidget_3.setItem(tablerow, 0, QtWidgets.QTableWidgetItem(row[1]))
            self.tableWidget_3.setItem(tablerow, 1, QtWidgets.QTableWidgetItem(row[2]))
            self.tableWidget_3.setItem(tablerow, 2, QtWidgets.QTableWidgetItem(row[3]))
            self.tableWidget_3.setItem(tablerow, 3, QtWidgets.QTableWidgetItem(row[4]))
            self.tableWidget_3.setItem(tablerow, 4, QtWidgets.QTableWidgetItem(row[5]))
            self.tableWidget_3.setItem(tablerow, 5, QtWidgets.QTableWidgetItem(row[6]))
            tablerow += 1
            print("pasas")


    def buscar_solucion_eliminar(self):
        pregunta_nombre_1 = self.lineEdit_2.text().upper()
        pregunta_nombre = str("'"+pregunta_nombre_1+"'")
        Conexion.DataBase()
        self.datos_1 = Conexion.DataBase()
        datos1 = self.datos_1.buscar_solucion(pregunta_nombre)
        self.tableWidget_2.setRowCount(len(datos1))
        if len(datos1) == 0:
            print("no existe")
        else:
            print("solucion seleccionada")
        tablerow = 0
        print("pasas")
        for row in datos1:
            print("pasas")
            self.solucion_a_borrar = row[1]
            self.tableWidget_2.setItem(tablerow, 0, QtWidgets.QTableWidgetItem(row[1]))
            self.tableWidget_2.setItem(tablerow, 1, QtWidgets.QTableWidgetItem(row[2]))
            self.tableWidget_2.setItem(tablerow, 2, QtWidgets.QTableWidgetItem(row[3]))
            self.tableWidget_2.setItem(tablerow, 3, QtWidgets.QTableWidgetItem(row[4]))
            tablerow += 1


    def eliminar_solucion_1(self):
        print("desicion")
        datos_solucion_borrar = self.solucion_a_borrar
        datos_solucion_borrar = ("'"+ datos_solucion_borrar + "'")
        self.row_Flag = self.tableWidget_2.currentRow()
        print(self.row_Flag)
        if self.row_Flag == 0:
            print("borrando...")
            self.tableWidget_2.removeRow(0)
            print("borrando...")
            self.datos_1 = Conexion.DataBase()
            print("borrando...")
            self.datos_1.eliminar_solucion("'"+ datos_solucion_borrar +"'")
            print("borrando...")
            self.lineEdit_2.setText('')
        else:
            print("imposible borrar")



    def sendMessage2(self):
        sendW = senWidget()
        sendW.label_2.setText(str(self.lineEdit.text()))
        print(f"Contenido de lineEdit : {self.lineEdit.text()}")
        print(f"Contenido de sendW : {str(sendW.label_2.text())}")
        item = QListWidgetItem()
        item.setSizeHint(sendW.sizeHint())
        self.listWidget.addItem(item)
        self.listWidget.setItemWidget(item, sendW)
        self.listWidget.setMinimumWidth(sendW.width())
        print("texto enviado correctamente")
        self.lineEdit.setText('')
        print("campo de texto limpio")
        # respuesta hola >> hi
        if str(sendW.label_2.text()) == "1+1":
            print("texto recibido")
            recW = recWidget()
            text3 = text_temp
            recW.label_4.setText(str(text3))
            recW.label_4.text()
            item = QListWidgetItem()
            item.setSizeHint(recW.sizeHint())
            self.listWidget.addItem(item)
            self.listWidget.setItemWidget(item, recW)
            self.listWidget.setMinimumWidth(recW.width())
            print(f"contenido de recibido {recW.label_4.text()}")

        elif str(sendW.label_2.text()) == "xd":
            print("texto recibido")
            recW = recWidget()
            text3 = " jajajajaja "
            recW.label_4.setText(str(text3))
            recW.label_4.text()
            item = QListWidgetItem()
            item.setSizeHint(recW.sizeHint())
            self.listWidget.addItem(item)
            self.listWidget.setItemWidget(item, recW)
            self.listWidget.setMinimumWidth(recW.width())
            print(f"contenido de recibido {recW.label_4.text()}")
        else:
            print("No logro entender tu mensaje, por favor se presciso con lo que quieres decirme")
            print("texto recibido")
            recW = recWidget()
            text3 = text_temp2
            recW.label_4.setText(str(text3))
            recW.label_4.text()
            item = QListWidgetItem()
            item.setSizeHint(recW.sizeHint())
            self.listWidget.addItem(item)
            self.listWidget.setItemWidget(item, recW)
            self.listWidget.setMinimumWidth(recW.width())
            print(f"contenido de recibido {recW.label_4.text()}")

    def sendMessage(self):
        id_pregunta = self.lineEdit.text()
        id_pregunta_1 = str("'" + id_pregunta + "'")
        from windows import Conexion
        sendW = senWidget()
        sendW.label_2.setText(str(id_pregunta_1))
        item = QListWidgetItem()
        item.setSizeHint(sendW.sizeHint())
        self.listWidget.addItem(item)
        self.listWidget.setItemWidget(item, sendW)
        self.listWidget.setMinimumWidth(sendW.width())
        print("texto enviado correctamente")
        self.lineEdit.setText('')
        print("campo de texto limpio")
        self.datos = Conexion.DataBase()
        self.pregunta = self.datos.buscar_solucion(id_pregunta_1)
        print(self.pregunta)
        print("paso")

        if len(self.pregunta) != 0:
            print("texto recibido")
            recW = recWidget()
            recW.label_4.setText(str(self.pregunta[0][2]))
            recW.label_4.text()
            item = QListWidgetItem()
            item.setSizeHint(recW.sizeHint())
            self.listWidget.addItem(item)
            self.listWidget.setItemWidget(item, recW)
            self.listWidget.setMinimumWidth(recW.width())
            print(f"contenido de recibido 1 {recW.label_4.text()}")

        elif str(sendW.label_2.text()) == "Hola":
            print("texto recibido")
            recW = recWidget()
            text3 = " Hola "
            recW.label_4.setText(str(text3))
            recW.label_4.text()
            item = QListWidgetItem()
            item.setSizeHint(recW.sizeHint())
            self.listWidget.addItem(item)
            self.listWidget.setItemWidget(item, recW)
            self.listWidget.setMinimumWidth(recW.width())
            print(f"contenido de recibido {recW.label_4.text()}")
        else:
            print("No logro entender tu mensaje, por favor se presciso con lo que quieres decirme")
            print("texto recibido")
            recW = recWidget()
            text3 = text_temp2
            recW.label_4.setText(str(text3))
            recW.label_4.text()
            item = QListWidgetItem()
            item.setSizeHint(recW.sizeHint())
            self.listWidget.addItem(item)
            self.listWidget.setItemWidget(item, recW)
            self.listWidget.setMinimumWidth(recW.width())
            print(f"contenido de recibido {recW.label_4.text()}")



    def bienvenidaAutomatica(self):
        print("texto recibido")
        recW = recWidget()
        text = "Hola Bienvenido, soy FoxyBot, estoy para ayudarte con alguna duda que tengas, puedes ingresar y probar con esta opcion que tengo implementado: - Reinscripción."
        recW.label_4.setText(str(text))
        recW.label_4.text()
        item = QListWidgetItem()
        item.setSizeHint(recW.sizeHint())
        self.listWidget.addItem(item)
        self.listWidget.setItemWidget(item, recW)
        self.listWidget.setMinimumWidth(recW.width())
        print(f"contenido de recibido {recW.label_4.text()}")

    def nuevoServicio(self):
        self.ventana = QtWidgets.QMainWindow()
        from windows.AgregarContenidoEditor import Ui_agregarContenidoEditor
        self.ui = Ui_agregarContenidoEditor()
        self.ui.setupUi(self.ventana)
        self.ventana.show()

    def retranslateUi(self, MainWindowAdmin):
        _translate = QtCore.QCoreApplication.translate
        MainWindowAdmin.setWindowTitle(_translate("MainWindowAdmin", "Admin"))
        self.label_user.setText(_translate("MainWindowAdmin", "Usuario"))
        self.label_estudiante.setText(_translate("MainWindowAdmin", "Administrador"))
        self.btn_chat.setText(_translate("MainWindowAdmin", "Chat"))
        self.btn_servicios.setText(_translate("MainWindowAdmin", "Gestión de Contenido"))
        self.btn_editores.setText(_translate("MainWindowAdmin", "Gestión de editores"))
        self.btn_about.setText(_translate("MainWindowAdmin", "Sobre Foxy Bot"))
        self.btn_cerrarSesion.setText(_translate("MainWindowAdmin", "Cerrar Sesión"))
        self.label.setText(_translate("MainWindowAdmin", "<html><head/><body><p><span style=\" color:#ffffff;\">FOXYBOT</span></p></body></html>"))
        self.lineEdit.setPlaceholderText(_translate("MainWindowAdmin", "¡Escribe aquí tus dudas!"))
        self.btn_enviar.setText(_translate("MainWindowAdmin", "Enviar"))
        self.pushButton.setText(_translate("MainWindowAdmin", "Actualizar"))
        self.label_3.setText(_translate("MainWindowAdmin", "<html><head/><body><p><span style=\" font-size:18pt;\">Gestión de contenido</span></p></body></html>"))

        self.btn_eliminar.setText(_translate("MainWindowAdmin", "Editar"))
        self.btn_Nuevo.setText(_translate("MainWindowAdmin", "+Nuevo"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindowAdmin", "Título"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindowAdmin", "Solución"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindowAdmin", "Área de servicio"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindowAdmin", "Palabra clave"))
        self.pushButton_2.setText(_translate("MainWindowAdmin", "Actualizar"))
        self.label_12.setText(_translate("MainWindowAdmin", "<html><head/><body><p><span style=\" font-family:\'sans-serif\'; font-size:18pt;\">Gestión de Editores</span></p></body></html>"))
        self.btn_eliminar_3.setText(_translate("MainWindowAdmin", "Editar"))

        item = self.tableWidget_3.horizontalHeaderItem(0)
        item.setText(_translate("MainWindowAdmin", "Nombre"))
        item = self.tableWidget_3.horizontalHeaderItem(1)
        item.setText(_translate("MainWindowAdmin", "Apellido"))
        item = self.tableWidget_3.horizontalHeaderItem(2)
        item.setText(_translate("MainWindowAdmin", "Correo"))
        item = self.tableWidget_3.horizontalHeaderItem(3)
        item.setText(_translate("MainWindowAdmin", "Roles: Editor = 1 , Estudiante = 0"))
        item = self.tableWidget_3.horizontalHeaderItem(4)
        item.setText(_translate("MainWindowAdmin", "Contraseña"))
        item = self.tableWidget_3.horizontalHeaderItem(5)
        item.setText(_translate("MainWindowAdmin", "Numero Empleado"))
        self.label_2.setText(_translate("MainWindowAdmin", "<html><head/><body><p align=\"center\">FOXYBOT Versión 1.0</p></body></html>"))
        self.pushButton_3.setText(_translate("MainWindowAdmin", "ELIMINAR"))
        self.label_7.setText(_translate("MainWindowAdmin", "<html><head/><body><p><span style=\" font-size:18pt;\">Buscar conenido por título:</span></p></body></html>"))
        self.btn_Nuevo_2.setText(_translate("MainWindowAdmin", "BUSCAR"))
        item = self.tableWidget_2.horizontalHeaderItem(0)
        item.setText(_translate("MainWindowAdmin", "Título"))
        item = self.tableWidget_2.horizontalHeaderItem(1)
        item.setText(_translate("MainWindowAdmin", "Solución"))
        item = self.tableWidget_2.horizontalHeaderItem(2)
        item.setText(_translate("MainWindowAdmin", "Área de servicio"))
        item = self.tableWidget_2.horizontalHeaderItem(3)
        item.setText(_translate("MainWindowAdmin", "Palabra clave"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindowAdmin = QtWidgets.QMainWindow()
    ui = Ui_MainWindowAdmin()
    ui.setupUi(MainWindowAdmin)
    MainWindowAdmin.show()
    sys.exit(app.exec_())
