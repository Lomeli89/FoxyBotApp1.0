from PyQt5.QtWidgets import QWidget

from ChatUser import Ui_Form as form

class Widget(QWidget,form):
    def __init__(self, parent, none):
        super(Widget, self).__init__(parent)
        QWidget.__init__(self)
        self.SetupUi(self)