
import event
from PyQt5.QtWidgets import (QGridLayout, QInputDialog, QLabel, QLineEdit,
                             QPushButton, QScrollArea, QVBoxLayout, QWidget)


class SettingsTab(QWidget):
    def __init__(self) -> None:
        super().__init__()

        vboxLayout = QVBoxLayout()

        vboxLayout.addWidget(QLabel("API Key Label"))
        insertApiKeyBtn=QPushButton("Insert OpenRouteService API Key")
        insertApiKeyBtn.clicked.connect(self._insertApiKey)
        vboxLayout.addWidget(insertApiKeyBtn)

        self.setLayout(vboxLayout)


    def _insertApiKey(self) -> None:
        text, okPressed = QInputDialog.getText(self, "Insert OpenRouteService API Key","API-Key:", QLineEdit.Normal, "")
        if okPressed and text != '':
            event.postEvent("newApiKeyInserted", text)
        