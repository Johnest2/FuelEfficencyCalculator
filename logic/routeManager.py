# -*- coding: utf-8 -*-
import collections
import json
from time import sleep

import openrouteservice
from geopy.extra.rate_limiter import RateLimiter
from geopy.geocoders import Nominatim
from numpy import nested_iters
from openrouteservice.directions import directions


#This uses openrouteserives for python: https://github.com/GIScience/openrouteservice-py
class RouteManager():
    def __init__(self):
        self.client=openrouteservice.Client(key='') #TODO Add API Key to settings and load here
        self.geocoder=Nominatim(user_agent='FuelEfficencyCalc')
        self.geocode=RateLimiter(self.geocoder.geocode, min_delay_seconds=1, return_value_on_exception=None)

    def getRoute(self, startLocation:tuple, targetLocation:tuple):
        #TODO Check if valid input in form of the expectted coordinate touple
        for elm in startLocation:
            pass

        for elm in targetLocation:
            pass

        #profile='driving-car', optimize_waypoints=True
        #TODO: Catch and handle exceptions
        try:
            return self.client.directions((startLocation,targetLocation), profile='driving-car') #TODO Create setting for vehile in settings and loard here,
        except Exception as e:
            print("Cannont calculate Route: " +str(e))
            return None
    def getTotalDistanceOfRoute(self, routeDict:dict):
        return routeDict["routes"][0]["summary"]["distance"]

    #Returns latidute, longitude location of Adress
    def getCoordinatesOfLocation(self, location:str):
        try:
            location=self.geocode(location)
            return (location.longitude, location.latitude)
        except Exception as e:
            print("Calculation of Coodrindates failed: " + str(e))
            return None
