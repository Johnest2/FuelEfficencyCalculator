import datetime
from string import Template

import logic
import numpy as np
import pyqtgraph
from logic import *
from PyQt5.QtWidgets import (QGridLayout, QHBoxLayout, QLabel, QLineEdit,
                             QPushButton, QScrollArea, QWidget)

_inputHight=26

# TODO #2 Add more statistics data
# TODO #3 Add Mouse position hover window
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
        self.plot=pyqtgraph.PlotWidget()
        self.plot.setBackground('w')
        self.curveRef = None  #This is the curveRef for the currently shown line

        #Styling and Labeling
        self.plot.setTitle("Time difference in travel time over travel speed", size="30pt", color='k')
        self.plot.setLabel('left', 'Time difference in min', size="24pt", color='k')
        self.plot.setLabel('bottom', 'Speed in km/h', size="24pt", color='k')
        self.plot.showGrid(x=True, y=True)
        grid.addWidget(self.plot, 0, 0, 1, 4)
        self.penSettings=pyqtgraph.mkPen(color='k', width=3)

        #Add cursor crosshair
        crosshairSettings=pyqtgraph.mkPen(color='c', width=1, line=':')
        self.crosshairVert=pyqtgraph.InfiniteLine(angle=90, movable=False, pen=crosshairSettings)
        self.crosshairHorz=pyqtgraph.InfiniteLine(angle=0, movable=False, pen=crosshairSettings)
        self.plot.addItem(self.crosshairVert, ignoreBounds=True)
        self.plot.addItem(self.crosshairHorz, ignoreBounds=True)
        self.proxy = pyqtgraph.SignalProxy(self.plot.scene().sigMouseMoved, rateLimit=60, slot=self.__updateCrosshair)

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
        grid.addWidget(QLabel("Distance [km]"), 2,0)

        # Add control buttons
        refresh=QPushButton("Refresh Graph")
        refresh.clicked.connect(self.__refreshPlotAndStatistics)
        grid.addWidget(refresh, 3, 0, 1, 2)

        clearGraph=QPushButton("Clear Graph")
        clearGraph.clicked.connect(self.__clearPlot)
        grid.addWidget(clearGraph, 3, 2, 1,2)

        #Add Statistics
        self.outputMaxTimeSaving=QLabel()
        self.outputMaxTimeSaving.setText("Max Time Saving:")
        grid.addWidget(self.outputMaxTimeSaving, 4, 0)



    def __refreshPlotAndStatistics(self):
        if self.minSpeedInput.text()=="" or self.maxSpeedInput.text=="" or self.distance.text()=="":
            raise Exception("Invalid input!")

        # TODO #1 Catch more wrong user input and add nice error message
        dataManager=logic.CalcTimeSaving()
        [speedArry, timeSavingArray]=dataManager.doCalculation(int(self.minSpeedInput.text()), int(self.maxSpeedInput.text()), int(self.distance.text()))
        if not self.curveRef:
            self.curveRef=self.plot.plot(speedArry, timeSavingArray, pen=self.penSettings)
        else:
            self.curveRef.setData(speedArry, timeSavingArray, pen=self.penSettings)

        tdelta=datetime.timedelta(minutes=abs(min(timeSavingArray)))

        d = {"D": tdelta.days}
        hours, rem = divmod(tdelta.seconds, 3600)
        minutes, seconds = divmod(rem, 60)
        d["H"] = '{:02d}'.format(hours)
        d["M"] = '{:02d}'.format(minutes)
        d["S"] = '{:02d}'.format(seconds)
        t = DeltaTemplate('%H:%M:%S')
        outValue=t.substitute(**d)

        self.outputMaxTimeSaving.setText("Time saving at max speed: " + str(outValue))

    def __clearPlot(self):
        if not self.curveRef:
            return

        self.plot.removeItem(self.curveRef)
        self.curveRef=None

    def __updateCrosshair(self, e):
        pos=e[0]
        if self.plot.sceneBoundingRect().contains(pos):
            mousePoint = self.plot.getPlotItem().vb.mapSceneToView(pos)
            self.crosshairVert.setPos(mousePoint.x())
            self.crosshairHorz.setPos(mousePoint.y())
class DeltaTemplate(Template):
    delimiter = "%"

        

