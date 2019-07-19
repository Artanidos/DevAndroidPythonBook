import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QWidget
from PyQt5.QtCore import Qt, QUrl
from PyQt5.QtQuick import QQuickView


class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setWindowTitle("Qt Combo Demo")
        widget= QWidget()
        layout = QVBoxLayout()
        view = QQuickView()
        container = QWidget.createWindowContainer(view, self)
        container.setMinimumSize(200, 200)
        container.setMaximumSize(200, 200)
        view.setSource(QUrl("view.qml"))
        label = QLabel("Hello World")
        label.setAlignment(Qt.AlignCenter)
        layout.addWidget(label)
        layout.addWidget(container)
        widget.setLayout(layout)
        self.setCentralWidget(widget)
        

if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec())