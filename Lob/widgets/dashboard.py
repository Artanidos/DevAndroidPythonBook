#############################################################################
# Copyright (C) 2020 Olaf Japp
#
# self file is part of Lob.
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
from widgets.flatbutton import FlatButton
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QGridLayout, QLabel, QTextBrowser, QFileDialog
from PyQt5.QtGui import QFont, QDesktopServices
from PyQt5.QtCore import QUrl, Qt, pyqtSignal, pyqtSlot
from PyQt5.QtNetwork import QNetworkAccessManager, QNetworkRequest, QNetworkReply
import resources

class Dashboard(QWidget):
    createSite = pyqtSignal()

    def __init__(self):
        QWidget.__init__(self)

        vbox = QVBoxLayout()
        layout = QGridLayout()
        title = QLabel()
        title.setText("Dashboard")
        fnt = title.font()
        fnt.setPointSize(20)
        fnt.setBold(True)
        title.setFont(fnt)

        self.browser = QTextBrowser()
        self.browser.setOpenLinks(False)

        self.create_button = FlatButton(":/images/create_normal.png", ":/images/create_hover.png", ":/images/create_pressed.png")
        self.create_button.setToolTip("Add a client")

        self.info = QLabel()
        self.info.setText("Welcome to Lob...")

        space = QWidget()
        space2 = QWidget()
        space3 = QWidget()
        space.setMinimumHeight(30)
        space2.setMinimumHeight(30)
        space3.setMinimumHeight(30)
        layout.addWidget(title, 0, 0, 1, 3)
        layout.addWidget(self.info, 1, 0, 1, 3)
        layout.addWidget(space, 2, 0)
        layout.addWidget(self.create_button, 3, 0, 1, 1, Qt.AlignCenter)
       
        vbox.addLayout(layout)
        vbox.addSpacing(40)
        vbox.addWidget(self.browser)
        self.setLayout(vbox)

        self.create_button.clicked.connect(self.createClicked)
  
    @pyqtSlot()
    def createClicked(self):
        self.createSite.emit()
