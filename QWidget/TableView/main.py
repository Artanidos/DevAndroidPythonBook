import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableView
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QStandardItem, QStandardItemModel


class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setWindowTitle("Qt Demo")

        model = QStandardItemModel(4, 4)
        for row in range(4):
            for column in range(4):
                item = QStandardItem("row " + str(row) + ", column " + str(column))
                model.setItem(row, column, item)

        self.table = QTableView()
        self.table.setModel(model)
        self.setCentralWidget(self.table)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec_())