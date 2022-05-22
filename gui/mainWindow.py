from PyQt6.QtWidgets import QGridLayout, QMainWindow, QTabWidget, QWidget

from .dataTab import DataTab
from .settingsTab import SettingsTab


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Fuel Efficency Calculator")
        self.setGeometry(0,0,1200,900)
        
        mainWidget=QWidget()

        #Set layout and general settings for main window
        self.grid=QGridLayout()
        self.grid.setSpacing(10)

        #Create and add tabs
        self.tabs=QTabWidget()
        self.dataTab=DataTab()
        self.settingsTab=SettingsTab()
        self.tabs.addTab(self.dataTab, "Data")
        self.tabs.addTab(self.settingsTab, "Settings")
        self.tabs.setDocumentMode(True)
        self.tabs.setMovable(True)
        # self.tabs.setTabPosition(QTabWidget.West)
        self.grid.addWidget(self.tabs, 1,1)

        #SetMenubar
        

        #make everyting visable
        mainWidget.setLayout(self.grid)
        self.setCentralWidget(mainWidget)
        self.showMaximized()
        self.show()
