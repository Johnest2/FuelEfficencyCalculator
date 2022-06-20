# -*- coding: utf-8 -*-
import collections
import json
from time import sleep
from typing import Any

import event
import openrouteservice
from geopy.extra.rate_limiter import RateLimiter
from geopy.geocoders import Nominatim
from numpy import nested_iters
from openrouteservice.directions import directions


#This uses openrouteserives for python: https://github.com/GIScience/openrouteservice-py
class RouteManager():
    def __init__(self, apiKey: str) -> None:
        # TODO: #8 Make apiKey updatable after new key is inserted the programm needs to be restarted to reach this line here.
        self.client=openrouteservice.Client(key=apiKey)
        self.geocoder=Nominatim(user_agent='FuelEfficencyCalc')
        self.geocode=RateLimiter(self.geocoder.geocode, min_delay_seconds=1, return_value_on_exception=None)

    def getRoute(self, startLocation:tuple, targetLocation:tuple):
        #TODO #12 Check if valid input in form of the expectted coordinate touple
        for elm in startLocation:
            pass

        for elm in targetLocation:
            pass

        #profile='driving-car', optimize_waypoints=True
        #TODO: #10 Catch and handle exceptions
        try:
            return self.client.directions((startLocation,targetLocation), profile='driving-car') #TODO #9 Create setting for vehile in settings and loard here,
        except Exception as e:
            
            return None

    # Return the distance in km
    def getTotalDistanceOfRoute(self, routeDict:dict):
        try:
            return routeDict["routes"][0]["summary"]["distance"]/1000
        except Exception as e:
            event.postEvent("displayErrorMsg", 'Calucaltion of route distance failed with the following error Message:' + str(e))
            return None
    # Returns the distance in km for the highway
    def getHighwayDistanceOfRoute(self, routeDict:dict) -> float:
        distance=0
        try:
            for step in routeDict['routes'][0]['segments'][0]['steps']: # Get all steps from routeDict
                if step['type'] == 6: # filter only for steps with type 6, which corresponds to highways
                    distance += step['distance']
        except Exception as e:
            event.postEvent("displayErrorMsg", 'Calucaltion of highway route distance failed with the following error Message:' + str(e))
        
        return distance/1000

    #Returns latidute, longitude location of Adress
    def getCoordinatesOfLocation(self, location:str):
        try:
            location=self.geocode(location)
            return (location.longitude, location.latitude)
        except Exception as e:
            event.postEvent("displayErrorMsg", 'Calucaltion of coordinated failed with the following error Message:' + str(e))

            return None
