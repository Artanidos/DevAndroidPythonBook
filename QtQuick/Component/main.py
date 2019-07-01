import sys
from PyQt5.QtGui import QGuiApplication, QColor, QPainter
from PyQt5.QtQml import QQmlApplicationEngine, qmlRegisterType
from PyQt5.QtQuick import QQuickPaintedItem
from PyQt5.QtCore import pyqtProperty, pyqtSignal


class Circle(QQuickPaintedItem):
    radiusChanged = pyqtSignal()

    def __init__(self, parent = None):
        QQuickPaintedItem.__init__(self, parent)
        self._color = QColor(53, 53, 53)
        self._radius = 0

    def paint(self, painter):
        painter.setRenderHints(QPainter.Antialiasing, True)
        painter.setBrush(self._color)
        painter.drawEllipse(0, 0, self._radius * 2, self._radius * 2)

    @pyqtProperty('QColor')
    def color(self):
        return self._color

    @color.setter
    def color(self, color):
        self._color = color

    @pyqtProperty('int', notify = radiusChanged)
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, radius):
        self._radius = radius
        self.setHeight(radius * 2)
        self.setWidth(radius * 2)
        self.radiusChanged.emit()    


if __name__ == "__main__":
    app = QGuiApplication(sys.argv)

    qmlRegisterType(Circle, 'Shapes', 1, 0, 'Circle')

    engine = QQmlApplicationEngine("view.qml")
    if not engine.rootObjects():
        sys.exit(-1)
    sys.exit(app.exec_())
