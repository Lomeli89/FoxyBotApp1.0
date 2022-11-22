from PyQt5.QtWidgets import QDialog, QApplication, QListWidgetItem
from  ChatChat import Ui_Dialog as dialog
from recibeWidget import  Widget as recWidget
from sendWidget import Widget as senWidget
from threading import Thread
from _thread import *
import socket
import os

#conn = None

text_temp = str("2")
text_temp2 = str("No logro entender tu mensaje, por favor se presciso con lo que quieres decirme")
text = str


class Dialog(QDialog, dialog):
    def __init__(self, parent=None):
        super(Dialog, self).__init__(parent)
        QDialog.__init__(self)
        self.setupUi(self)
        self.bienvenidaAutomatica()
        self.pushButton.clicked.connect(self.sendMessage)
        self.reclineEdit.setHidden(True)
       # self.reclineEdit.textChanged.connect(self.recMessage)


    #logica

    def sendMessage(self):
        sendW = senWidget()
        sendW.label_2.setText(str(self.lineEdit.text()))
        print(f"Contenido de lineEdit : {self.lineEdit.text()}")
        print(f"Contenido de sendW : {str(sendW.label_2.text())}")
        '''if conn != None:
            label_2 = self.lineEdit.text().decode('utf-8')
            conn.send(label_2)'''
        item = QListWidgetItem()
        item.setSizeHint(sendW.sizeHint())
        self.listWidget.addItem(item)
        self.listWidget.setItemWidget(item, sendW)
        self.listWidget.setMinimumWidth(sendW.width())
        print("texto enviado correctamente")
        self.lineEdit.setText('')
        print("campo de texto limpio")
        #respuesta hola >> hi
        if str(sendW.label_2.text()) == "1+1":
            print("texto recibido")
            recW = recWidget()
            text = text_temp
            recW.label_2.setText(str(text))
            recW.label_2.text()
            item = QListWidgetItem()
            item.setSizeHint(recW.sizeHint())
            self.listWidget.addItem(item)
            self.listWidget.setItemWidget(item, recW)
            self.listWidget.setMinimumWidth(recW.width())
            print(f"contenido de recibido {recW.label_2.text()}")

        if str(sendW.label_2.text()) == "xd":
            print("texto recibido")
            recW = recWidget()
            text = " jajajajaja "
            recW.label_2.setText(str(text))
            recW.label_2.text()
            item = QListWidgetItem()
            item.setSizeHint(recW.sizeHint())
            self.listWidget.addItem(item)
            self.listWidget.setItemWidget(item, recW)
            self.listWidget.setMinimumWidth(recW.width())
            print(f"contenido de recibido {recW.label_2.text()}")
        else:
            print("No logro entender tu mensaje, por favor se presciso con lo que quieres decirme")
            print("texto recibido")
            recW = recWidget()
            text = text_temp2
            recW.label_2.setText(str(text))
            recW.label_2.text()
            item = QListWidgetItem()
            item.setSizeHint(recW.sizeHint())
            self.listWidget.addItem(item)
            self.listWidget.setItemWidget(item, recW)
            self.listWidget.setMinimumWidth(recW.width())
            print(f"contenido de recibido {recW.label_2.text()}")

    def recMessage(self,text):
        print("------------incio funcion 2-----------")
        recW = recWidget()
        #recW.label_2.setText(str(text))
        item = QListWidgetItem()
        item.setSizeHint(recW.sizeHint())
        self.listWidget.addItem(item)
        self.listWidget.setItemWidget(item, recW)
        self.listWidget.setMinimumWidth(recW.width())
    '''def resBot(self):
        while True:
            if '''

    def bienvenidaAutomatica(self):
        print("texto recibido")
        recW = recWidget()
        text = "Hola Bienvenido, soy FoxyBot, estoy para ayudarte con tus dudas acerca del area de control escolar."
        recW.label_2.setText(str(text))
        recW.label_2.text()
        item = QListWidgetItem()
        item.setSizeHint(recW.sizeHint())
        self.listWidget.addItem(item)
        self.listWidget.setItemWidget(item, recW)
        self.listWidget.setMinimumWidth(recW.width())
        print(f"contenido de recibido {recW.label_2.text()}")


'''class serverThread(Thread):
    def __init__(self, widow):
        Thread.__init__(self)
        self.window = widow
    def run(self):

        sock = socket.socket()
        host = "localhost"
        port = 8000
        sock.bind((host, port))
        print('conexion exitosa')
        sock.listen(5)
        global conn
        (conn,(ip,port)) = sock.accept()
        print('Connected to: ' + str(ip) + ':' + str(port))
        while True:
            message = conn.recv(1024)
            clearM = message.decode('utf-8')
            self.window.reclineEdit.setText(str(clearM))'''
def main():
    from sys import argv
    app = QApplication(argv)
    dialog = Dialog()
    dialog.show()
    '''server = serverThread(dialog)
    server.start()'''
    app.exec_()

if __name__ == '__main__':
    main()