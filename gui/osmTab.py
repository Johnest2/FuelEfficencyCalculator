import functools
import os
from typing import Dict

import logic
from logic import *
from PyQt5 import QtCore, QtGui, QtWebChannel, QtWebEngineWidgets, QtWidgets
from PyQt5.QtCore import QUrl
from PyQt5.QtWebChannel import QWebChannel
from PyQt5.QtWebEngineCore import QWebEngineUrlRequestInterceptor
from PyQt5.QtWidgets import (QLabel, QLineEdit, QPushButton, QSizePolicy,
                             QVBoxLayout, QWidget)


#TODO: #5 Add input for navigational route planning
class OsmMapsTab(QWidget):
    def __init__(self, settingsDict: Dict) -> None:
        super().__init__()

        self.settingsDict=settingsDict

        vbox = QVBoxLayout()
        self.setLayout(vbox)

        self.startLocation=QLineEdit()
        self.startLocation.setText("Start Loaction")
        self.targetLocation=QLineEdit()
        self.targetLocation.setText("Target Location")
        calcRouteButton=QPushButton("Calculate Route")
        calcRouteButton.clicked.connect(self._calcRoute)
        vbox.addWidget(self.startLocation)
        vbox.addWidget(self.targetLocation)
        vbox.addWidget(calcRouteButton)

        label = self.label = QtWidgets.QLabel()
        sp = QtWidgets.QSizePolicy()
        sp.setVerticalStretch(0)
        label.setSizePolicy(sp)
        vbox.addWidget(label)
        view = self.view = QtWebEngineWidgets.QWebEngineView()
        channel = self.channel = QtWebChannel.QWebChannel()

        channel.registerObject("MainWindow", self)
        view.page().setWebChannel(channel)

        file = os.path.join(
            os.path.dirname(os.path.realpath(__file__)),
            "assets/map.html",
        )
        interceptor = Interceptor()
        self.view.page().profile().setUrlRequestInterceptor(interceptor)
        self.view.load(QtCore.QUrl.fromLocalFile(file))

        vbox.addWidget(view)

        button = QtWidgets.QPushButton("Go to Paris")
        panToParis = functools.partial(self.panMap, 2.3272, 48.8620)
        button.clicked.connect(panToParis)
        vbox.addWidget(button)


    @QtCore.pyqtSlot(float, float)
    def onMapMove(self, lat:float, lng:float) -> None:
        self.label.setText("Lng: {:.5f}, Lat: {:.5f}".format(lng, lat))

    def panMap(self, lng:float, lat:float) -> None:
        page = self.view.page()
        page.runJavaScript("map.panTo(L.latLng({}, {}));".format(lat, lng))

    def _calcRoute(self) -> None:
        # if self.startLocation.text()=="" or self.targetLocation.text()=="":
        #     raise Exception("Invalid input")
        #TODO Check if valid text input

        routeManager=logic.RouteManager(self.settingsDict["openRouteServiceApiKey"])
        coordStartLoc=routeManager.getCoordinatesOfLocation(self.startLocation.text())
        coordTargetLoc=routeManager.getCoordinatesOfLocation(self.targetLocation.text())
        routeDict=routeManager.getRoute(coordStartLoc, coordTargetLoc)
        if routeDict is None:
            return
        # print(f'Total Distance of the route: {routeManager.getTotalDistanceOfRoute(routeDict) : .2f}')
        
        
        #TODO #6 Draw route in map

class Interceptor(QWebEngineUrlRequestInterceptor):
    def interceptRequest(self, info) -> None:
        info.setHttpHeader(b"Accept-Language", b"en-US,en;q=0.9,es;q=0.8,de;q=0.7")
