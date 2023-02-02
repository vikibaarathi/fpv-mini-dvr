import requests
import json
class RHManager:

    rhstatus = False
    currentHeat = 0
    raceStatus = 0

        

    @staticmethod
    def getCurrentHeat():
        config_json = open("config.json")
        config =  json.load(config_json)
        baseUrl = config.get('rotorHazardEndpoint')
        response = requests.get(baseUrl + "/api/status")
        responseJson = response.json()
        status = responseJson.get('status')
        state = status.get('state')
        currentHeat = state.get('current_heat')
        return str(currentHeat)
