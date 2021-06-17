import json
import requests

def covidf():
    url = "https://api.covid19api.com/summary"
    response = requests.get(url)
    json_data = response.json()
    NewC = (str(json_data["Global"]["NewConfirmed"]))
    TC = (str(json_data["Global"]["TotalConfirmed"]))
    ND = (str(json_data["Global"]["NewDeaths"]))
    TD = (str(json_data["Global"]["TotalDeaths"]))
    NR = (str(json_data["Global"]["NewRecovered"]))
    TR = (str(json_data["Global"]["TotalRecovered"]))
    CovMsg=("**Heres some global stats:** " + "New Confirmed Cases: " + NewC + ". Total Confirmed Cases: " + TC + ". New Deaths: " + ND + ". Total Deaths: "+ TD + ". New Recovered: "+ NR+ ". Total Recovered: " + TR)
    return CovMsg    



