import sys
from PyQt5.QtGui import QGuiApplication
from PyQt5.QtQml import QQmlApplicationEngine
from PyQt5.QtCore import QObject, pyqtSlot, QMetaObject, Q_ARG, Q_RETURN_ARG, QVariant

class Controller(QObject):
    def __init__(self):
        QObject.__init__(self)
        self._root = None

    def setRoot(self, root):
        self._root = root

    @pyqtSlot("QString")
    def myPythonFunction(self, arg):
        print("myPythonFunction has been called with:", arg)
        msg = "Hello from Python"
        returnedValue = QMetaObject.invokeMethod(self._root, "myQmlFunction", Q_RETURN_ARG(QVariant), Q_ARG(QVariant, msg))
        print("myQmlFunction returned:", returnedValue)

if __name__ == "__main__":
    root = None
    controller = Controller()
    app = QGuiApplication(sys.argv)
    engine = QQmlApplicationEngine()
    engine.rootContext().setContextProperty("controller", controller)
    engine.load("view.qml")
    if not engine.rootObjects():
        sys.exit(-1)
    root = engine.rootObjects()[0]
    controller.setRoot(root)
    sys.exit(app.exec_())
