#!/usr/bin/env python3.9

import ctypes
import imp
import os
import sys
from pathlib import Path

from appdirs import AppDirs
from PyQt5.QtWidgets import QApplication

from gui import MainWindow
from settings import Settings
from settingsManager import SettingsManager


def main(args):
    app=QApplication(args)
    myappid="FuelEfficencyCalculator"
    
    try:
        from ctypes import windll  # Only exists on Windows.
        windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)
    except ImportError:
        pass
    
    dirs=AppDirs(myappid,"FuelDev")
    settings=Settings()
    settingsManager=SettingsManager(settings, myappid, dirs.user_data_dir)

    mainWindow=MainWindow()


    sys.exit(app.exec_())


if __name__ == "__main__":
    main(sys.argv)
