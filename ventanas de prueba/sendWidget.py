from PyQt5.QtWidgets import QWidget
from Send import Ui_Form as form

class Widget(QWidget, form):
    def __init__(self,parent = None):
        super(Widget, self).__init__(parent)
        QWidget.__init__(self)
        self.setupUi(self)