#!/usr/bin/env python3.9

import ctypes
import os
import sys
from pathlib import Path

from PyQt5.QtWidgets import QApplication

from gui import MainWindow


def main(args):
    app=QApplication(args)

    try:
        from ctypes import windll  # Only exists on Windows.
        myappid="FuelEfficencyCalculator"
        windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)
    except ImportError:
        pass
    

    appDataDir = Path(os.getenv("APPDATA")).joinpath("FuelEfficencyCalculator")
    if not appDataDir.exists():
        appDataDir.mkdir

    mainWindow=MainWindow()


    sys.exit(app.exec_())


if __name__ == "__main__":
    main(sys.argv)
