import requests
import json
class RHManager:

    rhstatus = False
    currentHeat = 0
    raceStatus = 0

    @staticmethod    
    def getRaceStatus():
        config_json = open("config.json")
        config =  json.load(config_json)
        try:
            baseUrl = config.get('rotorHazardEndpoint')
            response = requests.get(baseUrl + "/api/status")
            responseJson = response.json()
            status = responseJson['status']['state']

            return status
        except requests.exceptions.RequestException as e:  # This is the correct syntax
            print(e)
            return e
        

    @staticmethod
    def getRaceCurrent():
        config_json = open("config.json")
        config =  json.load(config_json)
        try:            
            baseUrl = config.get('rotorHazardEndpoint')
            response = requests.get(baseUrl + "/api/race/current")
            responseJson = response.json()
            print(responseJson)
            print("**********")
            return True
        except requests.exceptions.RequestException as e:  # This is the correct syntax
            print(e)
            #raise SystemExit(e)
            return False


    @staticmethod
    def getRaceState(self):
        try:
            state = self.getRaceStatus()
            raceStatus = state['race_status']
            
            match raceStatus:
                case 0:
                    return "Racer Standby"
                case 1:
                    return "Race Started"
                case 2:
                    return "Race Stopped"
                case 3:
                    return "Get Ready"
                case _:
                    return "RH Malfunction"

        except:
            return "RH Disabled"
            

    ##Race status Conditions
    # 0 - Race Standby
    # 3 - Staging
    # 1 - Started
    # 2 - Race STopped
