from PyQt5.QtWidgets import QDialog, QListWidgetItem
from  ChatChat import Ui_Dialog as dialog
from windows.recibeWidget import  Widget as recWidget
from windows.sendWidget import Widget as senWidget


#conn = None


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
        '''if conn != None:
            label_2 = self.lineEdit.text().decode('utf-8')
            conn.send(label_2)'''
        item = QListWidgetItem()
        item.setSizeHint(sendW.sizeHint())
        self.listWidget.addItem(item)
        self.listWidget.setItemWidget(item, sendW)
        self.listWidget.setMinimumWidth(sendW.width())
        self.lineEdit.setText('')
    def recMessage(self,text):
        recW = recWidget()
        recW.label_2.setText(str(text))
        item = QListWidgetItem()
        item.setSizeHint(recW.sizeHint())
        self.listWidget.addItem(item)
        self.listWidget.setItemWidget(item, recW)
        self.listWidget.setMinimumWidth(recW.width())