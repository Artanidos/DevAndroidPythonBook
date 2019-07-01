import sys
from PyQt5.QtGui import QGuiApplication
from PyQt5.QtQml import QQmlApplicationEngine


app = QGuiApplication(sys.argv)
engine = QQmlApplicationEngine("view.qml")
if not engine.rootObjects():
    sys.exit(-1)
sys.exit(app.exec_())
