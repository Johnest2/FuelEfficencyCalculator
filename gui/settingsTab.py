from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import (QGridLayout, QInputDialog, QLabel, QLineEdit,
                             QPushButton, QScrollArea, QVBoxLayout, QWidget)


class SettingsTab(QWidget):
    triggerSetApiKey=pyqtSignal(str, name='triggerSetApiKey')

    def __init__(self):
        super().__init__()

        vbox = QVBoxLayout()
        self.setLayout(vbox)

        vbox.addWidget(QLabel("API Key Label"))
        insertApiKeyBtn=QPushButton("Insert OpenRouteService API Key")
        insertApiKeyBtn.clicked.connect(self._insertApiKey)
        vbox.addWidget(insertApiKeyBtn)
    

    def _insertApiKey(self):
        text, okPressed = QInputDialog.getText(self, "Insert OpenRouteService API Key","API-Key:", QLineEdit.Normal, "")
        if okPressed and text != '':
            self.triggerSetApiKey.emit(str(text))
        