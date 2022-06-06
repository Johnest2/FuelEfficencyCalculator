from PyQt5.QtWidgets import (QGridLayout, QMainWindow, QMessageBox, QTabWidget,
                             QWidget)

from .dataTab import DataTab
from .osmTab import OsmMapsTab
from .settingsTab import SettingsTab


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Fuel Efficency Calculator")
        self.setGeometry(0,0,1200,900)
        
        mainWidget=QWidget()

        #Set layout and general settings for main window
        grid=QGridLayout()
        grid.setSpacing(10)

        #Create and add tabs
        tabs=QTabWidget()
        dataTab=DataTab()
        settingsTab=SettingsTab()
        osmMapsTab=OsmMapsTab()
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

    def displayError(self, errorMessage):
            msg=QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText(errorMessage)
            msg.setWindowTitle("Error")
            msg.setStandardButtons(QMessageBox.Ok)
            msg.exec_()
    
    
    def displayInfo(self, infoMessage, windowTitle, infomativeText, detailedText):
                msg=QMessageBox()
                msg.setIcon(QMessageBox.Information)
                msg.setText(infoMessage)

                if not windowTitle:
                    msg.setWindowTitle("Information")
                else:
                    msg.setWindowTitle(windowTitle)
                
                if not infomativeText:
                    msg.setInformativeText("This is additional information")
                else:
                    msg.setInformativeText(infomativeText)

                if not detailedText:
                    msg.setDetailedText("The details are as follows:")
                else:
                    msg.setDetailedText(detailedText)

                msg.setStandardButtons(QMessageBox.Ok)
                msg.exec_()
