import imp
import sys

import numpy as np
import pyqtgraph as pg
import pyqtgraph.exporters
from logic import *
from PyQt6.QtWidgets import (QGridLayout, QHBoxLayout, QLabel, QLineEdit,
                             QPushButton, QScrollArea, QWidget)

_inputHight=26

class DataTab(QWidget):
    def __init__(self):
        super().__init__()
        hbox=QHBoxLayout()

        self.setLayout(hbox)
        scrollArea = QScrollArea(self)
        scrollArea.setWidgetResizable(True)  
        hbox.addWidget(scrollArea)

        widget=QWidget()
        scrollArea.setWidget(widget)

        grid=QGridLayout()
        widget.setLayout(grid)
        grid.setSpacing(10)

        # Add empty plot
        self.plot = pg.PlotWidget()
        grid.addWidget(self.plot, 0, 0, 1, 4)

        # Add Inputs
        self.minSpeedInput=QLineEdit()
        self.minSpeedInput.setMaximumHeight(_inputHight)
        grid.addWidget(self.minSpeedInput, 1,1)
        grid.addWidget(QLabel("Min Speed"), 1,0)

        self.maxSpeedInput=QLineEdit()
        self.maxSpeedInput.setMaximumHeight(_inputHight)
        grid.addWidget(self.maxSpeedInput, 1,3)
        grid.addWidget(QLabel("Max Speed"), 1,2)
        
        self.distance=QLineEdit()
        self.distance.setMaximumHeight(_inputHight)
        grid.addWidget(self.distance, 2,1)
        grid.addWidget(QLabel("distance"), 2,0)

        # Add Refrseh button
        refresh = QPushButton("Refresh")
        refresh.clicked.connect(self.__refreshPlot)
        grid.addWidget(refresh,3, 0, 1, 4)

    def __refreshPlot(self):
        if self.minSpeedInput.text()=="" or self.maxSpeedInput.text=="" or self.distance.text()=="":
            raise Exception("Invalid input!")


        # ToDo Catch more wrong user input and add nice error message

        [speedArry, timeSavingArray]=CalcTimeSaving.doCalculation(int(self.minSpeedInput.text()), int(self.maxSpeedInput.text()), int(self.distance.text()))
        self.plot.plot(speedArry, timeSavingArray)




        

