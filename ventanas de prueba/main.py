from PyQt5.QtWidgets import QDialog, QApplication
from  ChatChat import Ui_Dialog as dialog
from recibeWidget import  Widget as recWidget
from sendWidget import Widget as senWidget

class Dialog(QDialog, dialog):
    def __init__(self,parent = None):
        super(Dialog, self).__init__(parent)
        QDialog.__init__(self)
        self.setupUi(self)

    #logica

    def sendMessage(self):
        sendW = senWidget()
        self.sendMessage().setText(str(self.lineEdit.text()))






def main():
    from sys import argv
    app = QApplication(argv)
    dialog = Dialog()
    dialog.show()
    app.exec_()

if __name__ == '__main__':
    main()