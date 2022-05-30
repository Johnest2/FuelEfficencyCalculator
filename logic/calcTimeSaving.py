# -*- coding: utf-8 -*-
import numpy as np


class CalcTimeSaving():
    def __init__(self):
        self.intervall=5
        self.refSpeed=130

    def doCalculation(self, minSpeed:int, maxSpeed:int, distance:float):
        intervall=5
        refSpeed=130
        speedArry=np.arange(minSpeed, maxSpeed, intervall)
        timeSavingArray=[]

        for speed in speedArry:
            timeSavingArray.append( ((distance*(refSpeed - speed)) / (speed*refSpeed))*60 )

        return [speedArry, timeSavingArray]

