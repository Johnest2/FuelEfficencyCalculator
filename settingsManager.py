
import json
import os.path
from email.policy import default
from os.path import exists
from typing import Any, Dict

import keyring
import keyring.util.platform_ as keyring_platform

import event

keyringEntry_OpenRouteApiKey='openRouteServiceApiKey'
class SettingsManager():
    def __init__(self, appName:str, userDataDir:str) -> None:
        self.settingsDict = {
            "openRouteServiceApiKey": '',
            "openRouteServiceProfile": 'driving-car',
            "minSpeed": 60,
            "maxSpeed": 180
        }
        self.keyringNamespace=appName
        self.userDataFile=userDataDir+"\\userData.json"
        
        self.settingsDict['openRouteServiceApiKey']=keyring.get_password(self.keyringNamespace, keyringEntry_OpenRouteApiKey)

        #TODO #7 save user Settings in json file
        try:
            with open(self.userDataFile, 'x') as f:
                json.dump(self._getCleanSettingsDict(), f)
        except FileExistsError:
            with open(self.userDataFile, 'r') as f:
                loadedSettings=json.load(f)
                for k in loadedSettings.keys():
                    if k in self.settingsDict:
                        self.settingsDict[k] = loadedSettings.get(k, None)

        #Add Listener for Event system
        event.subscribe("newApiKeyInserted", self.setOpenRouteServiceApiKey)
        event.subscribe("setMinMaxSpeed", self.setMinMaxSpeed)
        event.subscribe("setOpenRouteSeriveProfile", self.setOpenRouteSeriveProfile)


    def setOpenRouteServiceApiKey(self, apiKey:str) -> None:
        keyring.set_password(self.keyringNamespace, keyringEntry_OpenRouteApiKey, apiKey)
        self.settingsDict["openRouteServiceApiKey"]=apiKey


    def setMinMaxSpeed(self, data: Dict) -> None:
        if not data["minSpeed"] or not data["maxSpeed"]:
            return
        
        self.settingsDict['minSpeed']=data["minSpeed"]
        self.settingsDict['maxSpeed']=data["maxSpeed"]
        try:
            with open(self.userDataFile, 'w') as f:
                json.dump(self._getCleanSettingsDict(), f)
        except Exception as e:
            event.postEvent("displayErrorMsg", f'Error while storing min and max speed to config file, with the following error: {e}')
        
    
    def setOpenRouteSeriveProfile(self, profile:str) -> None:
        if not profile:
            return

        self.settingsDict['orsProfile']=profile
        try:
            with open(self.userDataFile, 'w') as f:
                json.dump(self._getCleanSettingsDict(), f) 
        except Exception as e:
            event.postEvent("displayErrorMsg", f'Error while storing OpenRouteService Profile to config file, with the following error: {e}')
    
    
    def _getCleanSettingsDict(self) -> Dict:
        return {k: self.settingsDict[k] for k in self.settingsDict.keys() - {"openRouteServiceApiKey"}}
