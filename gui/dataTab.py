import numpy as np
import pyqtgraph as pg
from PyQt6.QtWidgets import (QGridLayout, QHBoxLayout, QLabel, QLineEdit,
                             QPushButton, QScrollArea, QWidget)

_inputHight=26

#ToDO:
# 1. Move Calculation to Logic Class
# 2. Catch invalid user inputs
class DataTab(QWidget):
    def __init__(self):
        super().__init__()
        hbox=QHBoxLayout()

        self.setLayout(hbox)
        scrollArea=QScrollArea(self)
        scrollArea.setWidgetResizable(True)  
        hbox.addWidget(scrollArea)

        widget=QWidget()
        scrollArea.setWidget(widget)

        grid=QGridLayout()
        widget.setLayout(grid)
        grid.setSpacing(10)

        # Add empty plot
        self.plot=pg.PlotWidget()
        self.plot.setBackground('w')
        self._curves = {} #This is a empy array for all the curveIds

        #Styling and Labeling
        self.plot.setTitle("Timesaving over the driven speed", size="30pt")
        self.plot.setLabel('left', 'Timesaving in min')
        self.plot.setLabel('bottom', 'Speed in km/h')
        self.plot.showGrid(x=True, y=True)

        grid.addWidget(self.plot, 0, 0, 1, 4)

        #Add Cursor
        # self.cursorVert=pg.InfiniteLine(pos=self.wave[NUM_PIXELS / 2], angle=90, pen=mkPen("g", width=0.5), movable=True)
        # self.cursorHori=pg.InfiniteLine(pos=0, angle=0, pen=mkPen("g", width=0.5), movable=True)
        # self.plot.addItem(self.cursorVert)
        # self.plot.addItem(self.cursorHori)

        # Add Inputs
        self.minSpeedInput=QLineEdit()
        self.minSpeedInput.setMaximumHeight(_inputHight)
        self.minSpeedInput.setText('60')
        grid.addWidget(self.minSpeedInput, 1,1)
        grid.addWidget(QLabel("Min Speed [km/h]"), 1,0)

        self.maxSpeedInput=QLineEdit()
        self.maxSpeedInput.setMaximumHeight(_inputHight)
        self.maxSpeedInput.setText('170')
        grid.addWidget(self.maxSpeedInput, 1,3)
        grid.addWidget(QLabel("Max Speed [km/h]"), 1,2)
        
        self.distance=QLineEdit()
        self.distance.setMaximumHeight(_inputHight)
        grid.addWidget(self.distance, 2,1)
        grid.addWidget(QLabel("distance [km]"), 2,0)

        # Add Refresh button
        refresh = QPushButton("Refresh")
        refresh.clicked.connect(self.__refreshPlot)
        grid.addWidget(refresh,3, 0, 1, 4)

    def __refreshPlot(self):
        if self.minSpeedInput.text()=="" or self.maxSpeedInput.text=="" or self.distance.text()=="":
            raise Exception("Invalid input!")

        # ToDo Catch more wrong user input and add nice error message

        [speedArry, timeSavingArray]=self.doCalculation(int(self.minSpeedInput.text()), int(self.maxSpeedInput.text()), int(self.distance.text()))
        if not self._curves:
            self._curves=self.plot.plot(speedArry, timeSavingArray)
        else:
            self._curves.setData(speedArry, timeSavingArray)

    def __clearPlot(self):
        for curve in self._curves:
            self.plot.removeItem(curve)
        
        self._curves.clear() # Ideally every element is removed right after the curve is cleared



    #ToDo This should be moved to the logics tab, but for some reason packages are not working atm
    def doCalculation(self, minSpeed:int, maxSpeed:int, distance:float):
        intervall=5
        refSpeed=130
        speedArry=np.arange(minSpeed, maxSpeed, intervall)
        timeSavingArray=[]

        for speed in speedArry:
            timeSavingArray.append( ((distance*(refSpeed - speed)) / (speed*refSpeed))*60 )

        return [speedArry, timeSavingArray]

        

