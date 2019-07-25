import sys
import os
from PyQt5.QtWidgets import (QApplication, QMainWindow, QSplitter, QTextEdit, QAction, 
                             QMessageBox, QFileDialog, QDialog, QStyleFactory)
from PyQt5.QtCore import Qt, QCoreApplication, QSettings, QByteArray, QUrl
from PyQt5.QtGui import QIcon, QKeySequence
from PyQt5.QtWebEngineWidgets import QWebEngineView
import markdown2


class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.cur_file = ""
        self.splitter = QSplitter()
        self.text_edit = QTextEdit("")
        self.preview = QWebEngineView()
        self.preview.setMinimumWidth(300)
        self.setWindowTitle("Markdown [*]")
        self.splitter.addWidget(self.text_edit)
        self.splitter.addWidget(self.preview)
        self.setCentralWidget(self.splitter)
        self.createMenus()
        self.createStatusBar()
        self.readSettings()
        self.text_edit.document().contentsChanged.connect(self.documentWasModified)
        self.text_edit.textChanged.connect(self.textChanged)

    def closeEvent(self, event):
        if self.maybeSave():
            self.writeSettings()
            event.accept()
        else:
            event.ignore()

    def documentWasModified(self):
        self.setWindowModified(self.text_edit.document().isModified())

    def createMenus(self):
        new_icon = QIcon("./assets/new.png")
        open_icon = QIcon("./assets/open.png")
        save_icon = QIcon("./assets/save.png")
        save_as_icon = QIcon("./assets/save_as.png")
        exit_icon = QIcon("./assets/exit.png")

        new_act = QAction(new_icon, "&New", self)
        new_act.setShortcuts(QKeySequence.New)
        new_act.setStatusTip("Create a new file")
        new_act.triggered.connect(self.newFile)
        
        open_act = QAction(open_icon, "&Open", self)
        open_act.setShortcuts(QKeySequence.Open)
        open_act.setStatusTip("Open an existing file")
        open_act.triggered.connect(self.open)
        
        save_act = QAction(save_icon, "&Save", self)
        save_act.setShortcuts(QKeySequence.Save)
        save_act.setStatusTip("Save the document to disk")
        save_act.triggered.connect(self.save)

        save_as_act = QAction(save_as_icon, "Save &As...", self)
        save_as_act.setShortcuts(QKeySequence.SaveAs)
        save_as_act.setStatusTip("Save the document under a new name")
        save_as_act.triggered.connect(self.saveAs)

        exit_act = QAction(exit_icon, "E&xit", self)
        exit_act.setShortcuts(QKeySequence.Quit)
        exit_act.setStatusTip("Exit the application")
        exit_act.triggered.connect(self.close)

        about_act = QAction("&About", self)
        about_act.triggered.connect(self.about)
        about_act.setStatusTip("Show the application's About box")

        file_menu = self.menuBar().addMenu("&File")
        file_menu.addAction(new_act)
        file_menu.addAction(open_act)
        file_menu.addAction(save_act)
        file_menu.addAction(save_as_act)
        file_menu.addSeparator()
        file_menu.addAction(exit_act)

        help_menu = self.menuBar().addMenu("&Help")
        help_menu.addAction(about_act)

        file_tool_bar = self.addToolBar("File")
        file_tool_bar.addAction(new_act)
        file_tool_bar.addAction(open_act)
        file_tool_bar.addAction(save_act)

    def createStatusBar(self):
        self.statusBar().showMessage("Ready")

    def about(self):
        QMessageBox.about(self, "About Markdown",
            "This app demonstrates how to "
               "write modern GUI applications using Qt, with a menu bar, "
               "toolbars, and a status bar.")

    def newFile(self):
        if self.maybeSave():
            self.text_edit.clear()
        self.setCurrentFile("")

    def open(self):
        if self.maybeSave():
            fileName = QFileDialog.getOpenFileName(self)[0]
        if fileName:
            self.loadFile(fileName)

    def save(self):
        if not self.cur_file:
            return self.saveAs()
        else:
            return self.saveFile(self.cur_file)

    def saveAs(self):
        dialog = QFileDialog(self)
        dialog.setWindowModality(Qt.WindowModal)
        dialog.setAcceptMode(QFileDialog.AcceptSave)
        if dialog.exec() != QDialog.Accepted:
            return False
        return self.saveFile(dialog.selectedFiles()[0])

    def maybeSave(self):
        if not self.text_edit.document().isModified():
            return True
        ret = QMessageBox.warning(self, "Qt Demo",
                                "The document has been modified.\n"
                                "Do you want to save your changes?",
                                QMessageBox.Save | QMessageBox.Discard | QMessageBox.Cancel)
        if ret == QMessageBox.Save:
            return self.save()
        elif ret == QMessageBox.Cancel:
            return False
        return True

    def loadFile(self, fileName):
        with open(fileName, mode= "r") as f:
            text = f.read()

        QApplication.setOverrideCursor(Qt.WaitCursor)
        self.setCurrentFile(fileName)
        self.text_edit.setPlainText(text)
        self.text_edit.document().setModified(False)
        self.setWindowModified(False)
        QApplication.restoreOverrideCursor()        
        self.statusBar().showMessage("File loaded", 2000)

    def saveFile(self, fileName):
        QApplication.setOverrideCursor(Qt.WaitCursor)
        with open(fileName, "w") as f:
            f.write(self.text_edit.toPlainText())
        QApplication.restoreOverrideCursor()

        self.setCurrentFile(fileName)
        self.text_edit.document().setModified(False)
        self.setWindowModified(False)
        self.statusBar().showMessage("File saved", 2000)

    def setCurrentFile(self, fileName):
        self.cur_file = fileName
        shown_name = self.cur_file
        if not self.cur_file:
            shown_name = "untitled.txt"
        self.setWindowFilePath(shown_name)

    def writeSettings(self):
        settings = QSettings(QCoreApplication.organizationName(), QCoreApplication.applicationName())
        settings.setValue("geometry", self.saveGeometry())

    def readSettings(self):
        settings = QSettings(QCoreApplication.organizationName(), QCoreApplication.applicationName());
        geometry = settings.value("geometry", QByteArray())
        if not geometry:
            availableGeometry = QApplication.desktop().availableGeometry(self)
            self.resize(availableGeometry.width() / 3, availableGeometry.height() / 2)
            self.move((availableGeometry.width() - self.width()) / 2,
                (availableGeometry.height() - self.height()) / 2)
        else:
            self.restoreGeometry(geometry)

    def textChanged(self):
        path = os.getcwd()
        html = "<html><head><link href=\"assets/pastie.css\" rel=\"stylesheet\" type=\"text/css\"/></head><body>"
        html += markdown2.markdown(self.text_edit.toPlainText(), ..., extras=["fenced-code-blocks"])
        html += "</body></html>"
        self.preview.setHtml(html, baseUrl = QUrl("file://" + path + "/"))


if __name__ == "__main__":
    sys.argv.append("--disable-web-security")
    app = QApplication(sys.argv)
    QCoreApplication.setOrganizationName("Book")
    QCoreApplication.setApplicationName("MarkdownEditor")
    win = MainWindow()
    win.show()
    sys.exit(app.exec_())