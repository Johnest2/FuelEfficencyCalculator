# -*- coding: utf-8 -*-
import numpy as np


class CalcTimeSaving():
    def __init__(self):
        self.intervall=1
        self.refSpeed=130

    def doCalculation(self, minSpeed:int, maxSpeed:int, distance:float):
        speedArry=np.arange(minSpeed, maxSpeed, self.intervall)
        timeSavingArray=[]

        for speed in speedArry:
            timeSavingArray.append( ((distance*(self.refSpeed - speed)) / (speed*self.refSpeed))*60 )

        return [speedArry, timeSavingArray]

