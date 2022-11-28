from PyQt5.QtWidgets import QDialog, QApplication, QListWidgetItem
from  ChatChat import Ui_Dialog as dialog
from windows.recibeWidget import  Widget as recWidget
from windows.sendWidget import Widget as senWidget
from threading import Thread
import socket

sock = None

class Dialog(QDialog, dialog):
    def __init__(self, parent=None):
        super(Dialog, self).__init__(parent)
        QDialog.__init__(self)
        self.setupUi(self)
        self.pushButton.clicked.connect(self.sendMessage)
        self.reclineEdit.setHidden(True)
        self.reclineEdit.textChanged.connect(self.recMessage)

    #logica

    def sendMessage(self):
        sendW = senWidget()
        sendW.label_2.setText(str(self.lineEdit.text()))
        if sock != None:
            label_2 = self.lineEdit.text().decode('utf-8')
            sock.send(label_2)

        item = QListWidgetItem()
        item.setSizeHint(sendW.sizeHint())
        self.listWidget.addItem(item)
        self.listWidget.setItemWidget(item, sendW)
        self.listWidget.setMinimumWidth(sendW.width())
    def recMessage(self,text):
        recW = recWidget()
        recW.label_2.setText(str(text))
        item = QListWidgetItem()
        item.setSizeHint(recW.sizeHint())
        self.listWidget.addItem(item)
        self.listWidget.setItemWidget(item, recW)
        self.listWidget.setMinimumWidth(recW.width())
class clientThread(Thread):
    def __init__(self, widow):
        Thread.__init__(self)
        self.window = widow
    def run(self):
        global sock
        sock = socket.socket()
        host = "localhost"
        port = 8000
        print("esperando conexión...")
        try:
            sock.connect((host, port))
            while True:
                message = sock.recv(1024)
                clearM = message.decode('utf-8')
                self.window.reclineEdit.setText(str(clearM))
        except socket.error as e:
            print(str(e))
def main():
    from sys import argv
    app = QApplication(argv)
    dialog = Dialog()
    dialog.show()
    client = clientThread(dialog)
    client.start()
    app.exec_()

if __name__ == '__main__':
    main()