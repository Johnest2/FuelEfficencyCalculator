from PyQt6.QtWidgets import QGridLayout, QMainWindow, QTabWidget, QWidget

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
