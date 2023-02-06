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
            status = responseJson.get('status')
            print(status)
            print("**********")
            return True
        except requests.exceptions.RequestException as e:  # This is the correct syntax
            print(e)
            #raise SystemExit(e)
            return False
        

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
