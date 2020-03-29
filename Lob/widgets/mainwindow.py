#############################################################################
# Copyright (C) 2020 Olaf Japp
#
# This file is part of Lob.
#
#  Lob is free software: you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  Lob is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with Lob.  If not, see <http://www.gnu.org/licenses/>.
#
#############################################################################

import os
import inspect
import pathlib
import sys
import re
import shutil
from tinydb import TinyDB, Query
from datetime import datetime
from importlib import import_module
from widgets.flatbutton import FlatButton
from widgets.expander import Expander
from widgets.hyperlink import HyperLink
from widgets.dashboard import Dashboard
from widgets.settingseditor import SettingsEditor
from widgets.clienteditor import ClientEditor
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QListWidget, QListWidgetItem, QSizePolicy, QMessageBox, QVBoxLayout, QMainWindow, QWidget, QScrollArea, QDockWidget, QUndoStack, QApplication, QLabel, QLineEdit
from PyQt5.QtCore import pyqtSignal, Qt, QUrl, QRect, QCoreApplication, QDir, QSettings, QByteArray, QEvent, QPoint, QAbstractAnimation, QPropertyAnimation
from PyQt5.QtQml import QQmlEngine, QQmlComponent

import resources

class MainWindow(QMainWindow):
    siteLoaded = pyqtSignal(object)

    def __init__(self, app):
        QMainWindow.__init__(self)
        self.app = app
        self.initGui()
        self.readSettings()
        self.dashboard.setExpanded(True)
        self.showDashboard()
        self.loadDatabase()
        self.loadClients()
        self.statusBar().showMessage("Ready")
    
    def initGui(self):
        self.installEventFilter(self)
        self.dashboard = Expander("Dashboard", ":/images/dashboard_normal.png", ":/images/dashboard_hover.png", ":/images/dashboard_selected.png")
        self.content = Expander("Clients", ":/images/clients_normal.png", ":/images/clients_hover.png", ":/images/clients_selected.png")
        self.settings = Expander("Settings", ":/images/settings_normal.png", ":/images/settings_hover.png", ":/images/settings_selected.png")

        self.setWindowTitle(QCoreApplication.applicationName() + " " + QCoreApplication.applicationVersion())
        vbox = QVBoxLayout()
        vbox.addWidget(self.dashboard)
        vbox.addWidget(self.content)
        vbox.addWidget(self.settings)
        vbox.addStretch()

        content_box = QVBoxLayout()
        filter_label = QLabel("Filter")
        self.filter = QLineEdit()
        self.filter.textChanged.connect(self.filterChanged)
        self.client_list = QListWidget()
        self.client_list.setSizePolicy(QSizePolicy.Ignored, QSizePolicy.Fixed)
        self.client_list.currentItemChanged.connect(self.clientChanged)
        
        content_box.addWidget(filter_label)
        content_box.addWidget(self.filter)
        content_box.addWidget(self.client_list)
        self.content.addLayout(content_box)

        scroll_content = QWidget()
        scroll_content.setLayout(vbox)
        scroll = QScrollArea()
        scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        scroll.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        scroll.setWidget(scroll_content)
        scroll.setWidgetResizable(True)
        scroll.setMaximumWidth(200)
        scroll.setMinimumWidth(200)

        self.navigationdock = QDockWidget("Navigation", self)
        self.navigationdock.setAllowedAreas(Qt.LeftDockWidgetArea | Qt.RightDockWidgetArea)
        self.navigationdock.setWidget(scroll)
        self.navigationdock.setObjectName("Navigation")

        self.addDockWidget(Qt.LeftDockWidgetArea, self.navigationdock)

        self.showDock = FlatButton(":/images/edit_normal.png", ":/images/edit_hover.png")
        self.showDock.setToolTip("Show Navigation")
        self.statusBar().addPermanentWidget(self.showDock)

        self.dashboard.expanded.connect(self.dashboardExpanded)
        self.dashboard.clicked.connect(self.showDashboard)
        self.content.expanded.connect(self.contentExpanded)
        self.content.clicked.connect(self.showClient)
        
        self.settings.expanded.connect(self.settingsExpanded)
        self.settings.clicked.connect(self.showSettings)
        
        self.showDock.clicked.connect(self.showMenu)
        self.navigationdock.visibilityChanged.connect(self.dockVisibilityChanged)

        self.client = None
        self.client_editor = ClientEditor(self)

    def showDashboard(self):
        db = Dashboard()
        db.createSite.connect(self.addClient)
        self.setCentralWidget(db)

    def showClient(self):
        self.setCentralWidget(self.client_editor)

    def showSettings(self):
        s = SettingsEditor(self)
        self.setCentralWidget(s)

    def setCentralWidget(self, widget):
        old_widget = self.takeCentralWidget()
        super().setCentralWidget(widget)
        widget.show()

    def closeEvent(self, event):
        self.writeSettings()
        event.accept()

    def writeSettings(self):
        settings = QSettings(QSettings.IniFormat, QSettings.UserScope, QCoreApplication.organizationName(), QCoreApplication.applicationName())
        settings.setValue("geometry", self.saveGeometry())
        settings.setValue("state", self.saveState())
        settings.setValue("database", self.database)
        settings.setValue("fontSize", str(self.fontSize))
       
    def readSettings(self):
        settings = QSettings(QSettings.IniFormat, QSettings.UserScope, QCoreApplication.organizationName(), QCoreApplication.applicationName())
        geometry = settings.value("geometry", QByteArray())
        if geometry.isEmpty():
            availableGeometry = QApplication.desktop().availableGeometry(self)
            self.resize(availableGeometry.width() / 3, availableGeometry.height() / 2)
            self.move(int(((availableGeometry.width() - self.width()) / 2)), int((availableGeometry.height() - self.height()) / 2))
        else:
            self.restoreGeometry(geometry)
            self.restoreState(settings.value("state"))
        self.database = settings.value("database")
        if not self.database:
            self.database = "."
        fs = settings.value("fontSize")
        if not fs:
            fs = 10
        self.fontSize = int(fs)
        font = QFont("Sans Serif", self.fontSize)
        self.app.setFont(font)

    def dashboardExpanded(self, value):
        if value:
            self.content.setExpanded(False)
            self.settings.setExpanded(False)

    def contentExpanded(self, value):
        if value:
            self.dashboard.setExpanded(False)
            self.settings.setExpanded(False)

    def settingsExpanded(self, value):
        if value:
            self.dashboard.setExpanded(False)
            self.content.setExpanded(False)

    def showMenu(self):
        self.navigationdock.setVisible(True)

    def dockVisibilityChanged(self, visible):
        self.showDock.setVisible(not visible)

    def animate(self, item):
        panel = self.centralWidget()
        self.list = item.tableWidget()
        self.row = item.row()

        # create a cell widget to get the right position in the table
        self.cellWidget = QWidget()
        self.cellWidget.setMaximumHeight(0)
        self.list.setCellWidget(self.row, 1, self.cellWidget)
        pos = self.cellWidget.mapTo(panel, QPoint(0, 0))

        self.editor.setParent(panel)
        self.editor.move(pos)
        self.editor.resize(self.cellWidget.size())
        self.editor.show()

        self.animation = QPropertyAnimation(self.editor, "geometry".encode("utf-8"))
        self.animation.setDuration(300)
        self.animation.setStartValue(QRect(pos.x(), pos.y(), self.cellWidget.size().width(), self.cellWidget.size().height()))
        self.animation.setEndValue(QRect(0, 0, panel.size().width(), panel.size().height()))
        self.animation.start()

    def editorClosed(self):
        pos = self.cellWidget.mapTo(self.centralWidget(), QPoint(0, 0))
        # correct end values in case of resizing the window
        self.animation.setStartValue(QRect(pos.x(), pos.y(), self.cellWidget.size().width(), self.cellWidget.size().height()))
        self.animation.finished.connect(self.animationFineshedZoomOut)
        self.animation.setDirection(QAbstractAnimation.Backward)
        self.animation.start()

    def animationFineshedZoomOut(self):
        self.list.removeCellWidget(self.row, 1)
        del self.animation

        list = self.centralWidget()
        if list is MenuEditor:
            list.unregisterMenuEditor()

        del self.editor
        self.editor = None

        if self.method_after_animation == "showDashboard":
            self.showDashboard()
            self.method_after_animation = ""
        elif self.method_after_animation == "showSettings":
            self.showSettings()

        if self.content_after_animation:
            self.previewSite(self.content_after_animation)
            self.content_after_animation = None

    def filterChanged(self):
        self.loadClients()

    def loadDatabase(self):
        self.db = TinyDB(os.path.join(self.database,"lob.json"))
        self.clients = self.db.table('Clients')

    def updateClient(self):
        for i in range(self.client_list.count()):
            item = self.client_list.item(i)
            c = item.data(3)
            if c.doc_id == self.client.doc_id:
                item.setData(3, self.client)
                item.setText(self.client["name"])
                break

    def loadClients(self):
        self.client_list.clear()
        filter = self.filter.text()
        
        a = []
        for c in self.clients:
            if filter in c["name"]:
                a.append(c)

        s = sorted(a, key=namesort)
        for c in s:
            item = QListWidgetItem()
            item.setText(c["name"])
            item.setData(3, c)
            self.client_list.addItem(item)
        self.client_list.setCurrentRow(0)

    def addClient(self):
        now = datetime.now()
        newclient = {
            "number": "",
            "name": "", 
            "birthday_year": 1990,
            "birthday_month": 1,
            "birthday_day": 1,
            "profession": "",
            "address": "",
            "mobile": "",
            "email": "",
            "notes": ""
        }
        self.clients.insert(newclient)
        self.showClient()
        self.loadClients()
        q = Query()
        self.client = self.clients.get(q.name=="")
        self.client["name"] = ""
        self.client_editor.reload()
        

    def clientChanged(self, item):
        if item:
            self.client = item.data(3)
            self.client_editor.reload()
        else:
            self.client = None
            self.client_editor.reload()

def namesort(json):
    try:
        return json['name']
    except KeyError:
        return ""
