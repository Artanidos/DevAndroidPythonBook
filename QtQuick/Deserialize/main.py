import sys
from PyQt5.QtCore import pyqtProperty, QCoreApplication, QObject, QUrl, Q_CLASSINFO
from PyQt5.QtQml import qmlRegisterType, QQmlComponent, QQmlEngine, QQmlListProperty


class FavouriteCars(QObject):
    Q_CLASSINFO('DefaultProperty', 'cars')

    def __init__(self, parent = None):
        super().__init__(parent)
        self._cars = []

    @pyqtProperty(QQmlListProperty)
    def cars(self):
        return QQmlListProperty(Car, self, self._cars)


class Car(QObject):
    def __init__(self, parent = None):
        super().__init__(parent)
        self._name = ''
        self._horse_power = 0

    @pyqtProperty('QString')
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    @pyqtProperty(int)
    def horsePower(self):
        return self._horse_power

    @horsePower.setter
    def horsePower(self, horsePower):
        self._horse_power = horsePower


if __name__ == "__main__":
    app = QCoreApplication(sys.argv)

    qmlRegisterType(Car, 'Cars', 1, 0, 'Car')
    qmlRegisterType(FavouriteCars, 'Cars', 1, 0, 'FavouriteCars')

    engine = QQmlEngine()

    component = QQmlComponent(engine)
    component.loadUrl(QUrl('cars.qml'))

    fav = component.create()
    if fav is not None:
        for car in fav.cars:
            print("Car:", car.name, car.horsePower, "HP")
