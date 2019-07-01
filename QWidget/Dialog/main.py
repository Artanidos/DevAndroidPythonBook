import sys
from PyQt5.QtWidgets import QApplication
from PyQt5.uic import loadUiType

UIClass, QtBaseClass = loadUiType("dialog.ui")

class MyApp(UIClass, QtBaseClass):
    def __init__(self):
        UIClass.__init__(self)
        QtBaseClass.__init__(self)
        self.setupUi(self)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())    