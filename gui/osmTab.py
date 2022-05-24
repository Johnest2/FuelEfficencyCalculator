import functools
import os

from PyQt6 import QtCore
from PyQt6.QtCore import QUrl
from PyQt6.QtWebChannel import QWebChannel
from PyQt6.QtWebEngineCore import QWebEngineUrlRequestInterceptor
from PyQt6.QtWebEngineWidgets import QWebEngineView
from PyQt6.QtWidgets import QLabel, QSizePolicy, QVBoxLayout, QWidget


class OsmMapsTab(QWidget):
    def __init__(self):
        super().__init__()
        vbox=QVBoxLayout()
        self.setLayout(vbox)

        self.label = QLabel()
        sp = QSizePolicy()
        sp.setVerticalStretch(0)
        self.label.setSizePolicy(sp)
        vbox.addWidget(self.label)
        self.view = QWebEngineView()
        # self.channel = QWebChannel()

        # self.channel.registerObject("OsmMapsTab", self)
        # self.view.page().setWebChannel(self.channel)

        file = os.path.join(
            os.path.dirname(os.path.realpath(__file__)),
            "assets\map.html",
        )

        interceptor = Interceptor()
        self.view.page().profile().setUrlRequestInterceptor(interceptor)
        self.view.load(QUrl.fromLocalFile(file))
        self.view.show()

        vbox.addWidget(self.view)


class Interceptor(QWebEngineUrlRequestInterceptor):
    def interceptRequest(self, info):
        info.setHttpHeader(b"Accept-Language", b"en-US,en;q=0.9,es;q=0.8,de;q=0.7")
