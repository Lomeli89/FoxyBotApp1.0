from PyQt5.QtWidgets import QDialog, QApplication, QListWidgetItem
from  ChatChat import Ui_Dialog as dialog
from recibeWidget import  Widget as recWidget
from sendWidget import Widget as senWidget
from threading import Thread
from _thread import *
import socket
import os

#conn = None

text_temp = str("1 = escuela")
text_temp2 = str("2 = alumno")



class Dialog(QDialog, dialog):
    def __init__(self, parent=None):
        super(Dialog, self).__init__(parent)
        QDialog.__init__(self)
        self.setupUi(self)
        self.pushButton.clicked.connect(self.sendMessage)
        self.pushButton.clicked.connect(self.recMessage)
        self.reclineEdit.setHidden(True)
        self.reclineEdit.textChanged.connect(self.recMessage)


    #logica

    def sendMessage(self):
        sendW = senWidget()
        sendW.label_2.setText(str(self.lineEdit.text()))
        print(self.lineEdit.text())
        '''if conn != None:
            label_2 = self.lineEdit.text().decode('utf-8')
            conn.send(label_2)'''
        item = QListWidgetItem()
        item.setSizeHint(sendW.sizeHint())
        self.listWidget.addItem(item)
        self.listWidget.setItemWidget(item, sendW)
        self.listWidget.setMinimumWidth(sendW.width())
        print("texto enviado")
        self.lineEdit.setText('')
        print("entrada limpiada")

    def recMessage(self,text):
        print("------------incio funcion 2-----------")
        recW = recWidget()
        recW.label_2.setText(str(self.lineEdit.text()))
        #recW.label_2.setText(str(text))
        item = QListWidgetItem()
        item.setSizeHint(recW.sizeHint())
        self.listWidget.addItem(item)
        self.listWidget.setItemWidget(item, recW)
        self.listWidget.setMinimumWidth(recW.width())





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