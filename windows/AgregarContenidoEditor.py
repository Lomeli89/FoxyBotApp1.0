
from PyQt5 import QtCore, QtGui, QtWidgets

from windows import Conexion


class Ui_agregarContenidoEditor(object):
    def setupUi(self, agregarContenido):
        agregarContenido.setObjectName("agregarContenido")
        agregarContenido.resize(538, 469)
        agregarContenido.setStyleSheet("background-color: rgb(217, 217, 217);")
        self.label = QtWidgets.QLabel(agregarContenido)
        self.label.setGeometry(QtCore.QRect(40, 20, 141, 21))
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(agregarContenido)
        self.lineEdit.setGeometry(QtCore.QRect(30, 50, 471, 41))
        self.lineEdit.setStyleSheet("QLineEdit{\n"
"    \n"
"    \n"
"    \n"
"    \n"
"    background-color: rgb(179, 179, 179);\n"
"    padding-top:1px;\n"
"    border-radius:20px;\n"
"    \n"
"    border-color: rgb(0, 46, 109);\n"
"}")
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(agregarContenido)
        self.lineEdit_2.setGeometry(QtCore.QRect(30, 130, 471, 41))
        self.lineEdit_2.setStyleSheet("QLineEdit{\n"
"    \n"
"    \n"
"    \n"
"    \n"
"    background-color: rgb(179, 179, 179);\n"
"    padding-top:1px;\n"
"    border-radius:20px;\n"
"    \n"
"    border-color: rgb(0, 46, 109);\n"
"}")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(agregarContenido)
        self.lineEdit_3.setGeometry(QtCore.QRect(30, 200, 471, 101))
        self.lineEdit_3.setStyleSheet("QLineEdit{\n"
"    \n"
"    \n"
"    \n"
"    \n"
"    background-color: rgb(179, 179, 179);\n"
"    padding-top:1px;\n"
"    border-radius:20px;\n"
"    \n"
"    border-color: rgb(0, 46, 109);\n"
"}")
        self.lineEdit_3.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_4 = QtWidgets.QLineEdit(agregarContenido)
        self.lineEdit_4.setGeometry(QtCore.QRect(30, 350, 471, 41))
        self.lineEdit_4.setStyleSheet("QLineEdit{\n"
"    \n"
"    \n"
"    \n"
"    \n"
"    background-color: rgb(179, 179, 179);\n"
"    padding-top:1px;\n"
"    border-radius:20px;\n"
"    \n"
"    border-color: rgb(0, 46, 109);\n"
"}")
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.label_2 = QtWidgets.QLabel(agregarContenido)
        self.label_2.setGeometry(QtCore.QRect(40, 100, 141, 21))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(agregarContenido)
        self.label_3.setGeometry(QtCore.QRect(40, 180, 141, 16))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(agregarContenido)
        self.label_4.setGeometry(QtCore.QRect(40, 320, 141, 16))
        self.label_4.setObjectName("label_4")
        self.btn_Nuevo = QtWidgets.QPushButton(agregarContenido)
        self.btn_Nuevo.setGeometry(QtCore.QRect(280, 420, 115, 30))
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
        self.btn_Nuevo_2 = QtWidgets.QPushButton(agregarContenido)
        self.btn_Nuevo_2.setGeometry(QtCore.QRect(410, 420, 115, 30))
        self.btn_Nuevo_2.setMinimumSize(QtCore.QSize(0, 30))
        self.btn_Nuevo_2.setStyleSheet("QPushButton {\n"
"    \n"
"    font: 14pt \"Calibri\";\n"
"    color:  rgb(0, 46, 109);\n"
"    \n"
"    background-color: rgb(255, 255, 255);\n"
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
        self.btn_Nuevo_2.setFlat(False)
        self.btn_Nuevo_2.setObjectName("btn_Nuevo_2")

        self.retranslateUi(agregarContenido)
        self.btn_Nuevo_2.clicked.connect(agregarContenido.close) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(agregarContenido)

        self.btn_Nuevo.clicked.connect(self.guardarContenido)

    def guardarContenido(self):
        self.datos = Conexion.DataBase()

        temp_nombre_solucion = self.lineEdit.text()
        temp_nombre_servicio = self.lineEdit_2.text()
        temp_solucion = self.lineEdit_3.text()
        temp_palabra_clave = self.lineEdit_4.text()


        print(temp_nombre_solucion, temp_solucion, temp_nombre_servicio, temp_palabra_clave)

        self.datos.gContenido(temp_nombre_solucion,temp_solucion,temp_nombre_servicio,temp_palabra_clave)
        self.lineEdit.setText("")
        self.lineEdit_2.setText("")
        self.lineEdit_3.setText("")
        self.lineEdit_4.setText("")

        print("Guardado correctamente")



    def retranslateUi(self, agregarContenido):
        _translate = QtCore.QCoreApplication.translate
        agregarContenido.setWindowTitle(_translate("agregarContenido", "Dialog"))
        self.label.setText(_translate("agregarContenido", "TÍTULO DE SOLUCIÓN:"))
        self.lineEdit.setPlaceholderText(_translate("agregarContenido", "Escriba el título de la solucion (ej. Reinscripciones)"))
        self.lineEdit_2.setPlaceholderText(_translate("agregarContenido", "Escriba un área de servicio"))
        self.lineEdit_3.setPlaceholderText(_translate("agregarContenido", "Describa la solución"))
        self.lineEdit_4.setPlaceholderText(_translate("agregarContenido", "Escriba palabras que puedan llegar a mencionar los usuarios (ej. reinscribirse)"))
        self.label_2.setText(_translate("agregarContenido", "ÁREA DE SERVICIO:"))
        self.label_3.setText(_translate("agregarContenido", "SOLUCIÓN:"))
        self.label_4.setText(_translate("agregarContenido", "PALABRA CLAVE:"))
        self.btn_Nuevo.setText(_translate("agregarContenido", "Guardar"))
        self.btn_Nuevo_2.setText(_translate("agregarContenido", "Cancelar"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    agregarContenido = QtWidgets.QDialog()
    ui = Ui_agregarContenidoEditor()
    ui.setupUi(agregarContenido)
    agregarContenido.show()
    sys.exit(app.exec_())
