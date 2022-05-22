#!/usr/bin/env python3.9

import ctypes
import os
import sys
from pathlib import Path

from PyQt6.QtWidgets import QApplication

from gui.mainWindow import MainWindow


def main(args):
    app=QApplication(args)
    myappid="FuelEfficencyCalculator"

    ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)

    appDataDir = Path(os.getenv("APPDATA")).joinpath("FuelEfficencyCalculator")
    if not appDataDir.exists():
        appDataDir.mkdir

    mainWindow=MainWindow()


    sys.exit(app.exec())


if __name__ == "__main__":
    main(sys.argv)
