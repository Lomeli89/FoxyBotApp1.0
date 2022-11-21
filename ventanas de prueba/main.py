from PyQt5.QtWidgets import QDialog, QApplication, QListWidgetItem
from  ChatChat import Ui_Dialog as dialog
from recibeWidget import  Widget as recWidget
from sendWidget import Widget as senWidget

class Dialog(QDialog, dialog):
    def __init__(self, parent=None):
        super(Dialog, self).__init__(parent)
        QDialog.__init__(self)
        self.setupUi(self)
        self.pushButton.clicked.connect(self.sendMessage)

    #logica

    def sendMessage(self):
        sendW = senWidget()
        sendW.label_2.setText(str(self.lineEdit.text()))
        item = QListWidgetItem()
        item.setSizeHint(sendW.sizeHint())
        self.listWidget.addItem(item)
        self.listWidget.setItemWidget(item, sendW)
        self.listWidget.setMinimumWidth(sendW.width())
        self.lineEdit.setText('')





def main():
    from sys import argv
    app = QApplication(argv)
    dialog = Dialog()
    dialog.show()
    app.exec_()

if __name__ == '__main__':
    main()