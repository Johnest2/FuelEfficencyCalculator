from typing import Dict, Tuple

import event
from PyQt5.QtWidgets import (QGridLayout, QMainWindow, QMessageBox, QTabWidget,
                             QWidget)

from .dataTab import DataTab
from .osmTab import OsmMapsTab
from .settingsTab import SettingsTab


class MainWindow(QMainWindow):
    def __init__(self, settingsDict) -> None:
        super().__init__()

        self.setWindowTitle("Fuel Efficency Calculator")
        self.setGeometry(0,0,1200,900)
        
        mainWidget=QWidget()

        #Set layout and general settings for main window
        grid=QGridLayout()
        grid.setSpacing(10)

        #Create and add tabs
        tabs=QTabWidget()
        dataTab=DataTab(settingsDict)
        settingsTab=SettingsTab()
        osmMapsTab=OsmMapsTab(settingsDict)
        tabs.addTab(dataTab, "Data")
        tabs.addTab(osmMapsTab, "OpenStreet Maps")
        tabs.addTab(settingsTab, "Settings")
        tabs.setDocumentMode(True)
        tabs.setMovable(True)
        # tabs.setTabPosition(QTabWidget.West)
        grid.addWidget(tabs, 1,1)

        #SetMenubar
        
        #make everyting visable
        mainWidget.setLayout(grid)
        self.setCentralWidget(mainWidget)
        self.showMaximized()
        self.show()

        #Add events for Info and Error Messages
        event.subscribe("displayErrorMsg", self._displayError)
        event.subscribe("displayInfoMsg", self._displayInfo)


    def _displayError(self, errorMessage:str) -> None:
        if not errorMessage:
            return

        msg=QMessageBox()
        msg.setIcon(QMessageBox.Critical)
        msg.setText(errorMessage)
        msg.setWindowTitle("Error")
        msg.setStandardButtons(QMessageBox.Ok)
        msg.exec_()
    
    #used to set InfoMessage. Requiered is a dict with the following allowed key: infoMessage, windowTitle, informativeText, detailedText
    def _displayInfo(self, content: Dict) -> None:
        if not content["infoMessage"] or not content:
            return

        msg=QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setText(content["infoMessage"])

        if not content["windowTitle"]:
            msg.setWindowTitle("Information")
        else:
            msg.setWindowTitle(content["windowTitle"])
        
        if not content["informativeText"]:
            msg.setInformativeText("This is additional information")
        else:
            msg.setInformativeText(content["informativeText"])

        if not content["detailedText"]:
            msg.setDetailedText("The details are as follows:")
        else:
            msg.setDetailedText(content["detailedText"])

        msg.setStandardButtons(QMessageBox.Ok)
        msg.exec_()
