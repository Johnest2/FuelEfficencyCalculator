#!/usr/bin/env python3.9

import ctypes
import os
import sys
from pathlib import Path

from PyQt5.QtWidgets import QApplication


def main(args):
    app=QApplication(args)
    myappid="FuelEfficencyCalculator"

    ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)

    appDataDir = Path(os.getenv("APPDATA")).joinpath("phoneTimer")
    if not appDataDir.exists():
        appDataDir.mkdir

    # Write main code here!


    sys.exit(app.exec_())


if __name__ == "__main__":
    main(sys.argv)
