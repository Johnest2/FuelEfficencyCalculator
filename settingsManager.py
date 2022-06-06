
import json
from os.path import exists

import keyring
import keyring.util.platform_ as keyring_platform

from PyQt5.QtCore import pyqtSignal

keyringEntry_OpenRouteApiKey='openRouteServiceApiKey'
class SettingsManager():
    def __init__(self, settings, appName, userDataDir):
        self.settings=settings
        self.keyringNamespace=appName
        
        self.settings.openRouteServiceApiKey=keyring.get_password(self.keyringNamespace, keyringEntry_OpenRouteApiKey)

        #TODO #7 save user Settings in json file
        # with open(userDataDir+"\\userData.json", 'w') as userDataFile:
        #     x = {
        #         "name": "John",
        #         "age": 30,
        #         "city": "New York"
        #         }
        #     json.dump(x, userDataFile)

        updateOpenRouteApiKey=pyqtSignal(name='triggerSetApiKey')
        updateOpenRouteApiKey.connect(self.setOpenRouteSeriveProfile)



    def setOpenRouteServiceApiKey(self, apiKey):
        keyring.set_password(self.keyringNamespace, keyringEntry_OpenRouteApiKey, apiKey)
        self.settings.openRouteServiceApieKey=apiKey

    def setMinMaxSpeed(self, minSpeed, maxSpeed):
        pass
    
    def setOpenRouteSeriveProfile(self, profile):
        pass
