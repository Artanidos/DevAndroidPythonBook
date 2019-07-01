from PyQt5.QtGui import QGuiApplication
from PyQt5.QtQml import QQmlApplicationEngine
from PyQt5.QtQuick import QQuickView, QQuickWindow, QQuickItem
from PyQt5.QtCore import QUrl
import sys

if len(sys.argv) < 2:
    print("Usage: python main.py <url>")
    sys.exit(-1)

app = QGuiApplication(sys.argv)

url = sys.argv[1]
engine = QQmlApplicationEngine()
engine.load(QUrl(url))
if not engine.rootObjects():
    sys.exit(-1)
root = engine.rootObjects()[0]
    
if isinstance(root, QQuickItem):
    view = QQuickView()
    view.setResizeMode(QQuickView.SizeRootObjectToView)
    view.setSource(QUrl(url))
    view.show()
elif not isinstance(root, QQuickWindow):
    sys.exit(-1)
    
sys.exit(app.exec())
