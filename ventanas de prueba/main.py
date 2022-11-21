from PyQt5.QtWidgets import QDialog, QApplication, QListWidgetItem
from  ChatChat import Ui_Dialog as dialog
from recibeWidget import  Widget as recWidget
from sendWidget import Widget as senWidget
from threading import Thread
class Dialog(QDialog, dialog):
    def __init__(self, parent=None):
        super(Dialog, self).__init__(parent)
        QDialog.__init__(self)
        self.setupUi(self)
        self.pushButton.clicked.connect(self.sendMessage)
       # self.pushButton.clicked.connect(self.respuesta)
        self.lineEdit_2.setHidden(True)
        self.lineEdit_2.textChanged.connect(self.recMessage())

    #logica

    def sendMessage(self):
        sendW = senWidget()
        sendW.label_2.setText(str(self.lineEdit.text()))
        item = QListWidgetItem()
        item.setSizeHint(sendW.sizeHint())
        self.listWidget.addItem(item)
        self.listWidget.setItemWidget(item, sendW)
        self.listWidget.setMinimumWidth(sendW.width())

    class serverThread(Thread):
        def __init__(self, widow):
            self.window = widow
        def run(self):
    def recMessage(self,text):
        recW = recWidget()
        recW.label_2.setText(str(text))
        item = QListWidgetItem()
        item.setSizeHint(recW.sizeHint())
        self.listWidget.addItem(item)
        self.listWidget.setItemWidget(item, recW)
        self.listWidget.setMinimumWidth(recW.width())
        self.lineEdit.setText('')

    def respuesta(self):
        sendW = senWidget()
        sendW.label_2.getText(str(self.lineEdit.text()))
        if self.lineEdit.text() == "HOLA":
             print(f"Hola")


def main():
    from sys import argv
    app = QApplication(argv)
    dialog = Dialog()
    dialog.show()
    app.exec_()

if __name__ == '__main__':
    main()