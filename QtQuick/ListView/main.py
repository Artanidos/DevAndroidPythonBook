import sys
from PyQt5.QtGui import QGuiApplication
from PyQt5.QtQml import QQmlApplicationEngine

items = ["Item1", "Item2", "Item3", "Item4"]

app = QGuiApplication(sys.argv)
engine = QQmlApplicationEngine()
engine.rootContext().setContextProperty("myModel", items)
engine.load("view.qml")
if not engine.rootObjects():
    sys.exit(-1)
sys.exit(app.exec_())
