# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'EditarEditor.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_editarEditor(object):
    def setupUi(self, editarEditor):
        editarEditor.setObjectName("editarEditor")
        editarEditor.resize(538, 469)
        editarEditor.setStyleSheet("background-color: rgb(217, 217, 217);")
        self.label = QtWidgets.QLabel(editarEditor)
        self.label.setGeometry(QtCore.QRect(40, 20, 141, 21))
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(editarEditor)
        self.lineEdit.setEnabled(False)
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
        self.lineEdit_2 = QtWidgets.QLineEdit(editarEditor)
        self.lineEdit_2.setEnabled(False)
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
        self.lineEdit_3 = QtWidgets.QLineEdit(editarEditor)
        self.lineEdit_3.setEnabled(False)
        self.lineEdit_3.setGeometry(QtCore.QRect(30, 200, 471, 41))
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
        self.lineEdit_3.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_4 = QtWidgets.QLineEdit(editarEditor)
        self.lineEdit_4.setEnabled(False)
        self.lineEdit_4.setGeometry(QtCore.QRect(30, 280, 471, 41))
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
        self.label_2 = QtWidgets.QLabel(editarEditor)
        self.label_2.setGeometry(QtCore.QRect(40, 100, 141, 21))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(editarEditor)
        self.label_3.setGeometry(QtCore.QRect(40, 180, 141, 16))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(editarEditor)
        self.label_4.setGeometry(QtCore.QRect(40, 260, 141, 16))
        self.label_4.setObjectName("label_4")
        self.btn_Nuevo = QtWidgets.QPushButton(editarEditor)
        self.btn_Nuevo.setGeometry(QtCore.QRect(280, 420, 115, 30))
        self.btn_Nuevo.setMinimumSize(QtCore.QSize(0, 30))
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
        self.btn_Nuevo_2 = QtWidgets.QPushButton(editarEditor)
        self.btn_Nuevo_2.setGeometry(QtCore.QRect(410, 420, 115, 30))
        self.btn_Nuevo_2.setMinimumSize(QtCore.QSize(0, 30))
        self.btn_Nuevo_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_Nuevo_2.setStyleSheet("QPushButton {\n"
"    \n"
"    font: 14pt \"Calibri\";\n"
"    \n"
"    color: rgb(255, 255, 255);\n"
"    \n"
"    \n"
"    background-color: rgb(255, 0, 0);\n"
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
        self.pushButton = QtWidgets.QPushButton(editarEditor)
        self.pushButton.setGeometry(QtCore.QRect(410, 60, 75, 23))
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton.setStyleSheet("background-color: transparent;\n"
"color: rgb(0, 37, 87);")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(editarEditor)
        self.pushButton_2.setGeometry(QtCore.QRect(410, 140, 75, 23))
        self.pushButton_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_2.setStyleSheet("background-color: transparent;\n"
"color: rgb(0, 37, 87);")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(editarEditor)
        self.pushButton_3.setGeometry(QtCore.QRect(410, 210, 75, 23))
        self.pushButton_3.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_3.setStyleSheet("background-color: transparent;\n"
"color: rgb(0, 37, 87);")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(editarEditor)
        self.pushButton_4.setGeometry(QtCore.QRect(410, 290, 75, 23))
        self.pushButton_4.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_4.setStyleSheet("background-color: transparent;\n"
"color: rgb(0, 37, 87);")
        self.pushButton_4.setObjectName("pushButton_4")

        self.retranslateUi(editarEditor)
        self.btn_Nuevo_2.clicked.connect(editarEditor.close) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(editarEditor)

    def retranslateUi(self, editarEditor):
        _translate = QtCore.QCoreApplication.translate
        editarEditor.setWindowTitle(_translate("editarEditor", "Dialog"))
        self.label.setText(_translate("editarEditor", "NOMBRE:"))
        self.lineEdit.setPlaceholderText(_translate("editarEditor", "Nombre completo "))
        self.lineEdit_2.setPlaceholderText(_translate("editarEditor", "Correo electrónico "))
        self.lineEdit_3.setText(_translate("editarEditor", "Describa la solución"))
        self.lineEdit_3.setPlaceholderText(_translate("editarEditor", "Número de empleado "))
        self.lineEdit_4.setPlaceholderText(_translate("editarEditor", "Seleccione un rol "))
        self.label_2.setText(_translate("editarEditor", "CORREO ELECTRÓNICO:"))
        self.label_3.setText(_translate("editarEditor", "NÚMERO DE EMPLEADO:"))
        self.label_4.setText(_translate("editarEditor", "ROL:"))
        self.btn_Nuevo.setText(_translate("editarEditor", "Guardar"))
        self.btn_Nuevo_2.setText(_translate("editarEditor", "Eliminar"))
        self.pushButton.setText(_translate("editarEditor", "Editar"))
        self.pushButton_2.setText(_translate("editarEditor", "Editar"))
        self.pushButton_3.setText(_translate("editarEditor", "Editar"))
        self.pushButton_4.setText(_translate("editarEditor", "Editar"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    editarEditor = QtWidgets.QDialog()
    ui = Ui_editarEditor()
    ui.setupUi(editarEditor)
    editarEditor.show()
    sys.exit(app.exec_())
