import requests
import json
def next1f():
    url = "https://fdo.rocketlaunch.live/json/launches/next/5"

    response = requests.get(url)
    data = response.json()
    next1 = (data["result"][0]["launch_description"])
    return next1
#print(data["result"][0]["name"])
#print(data["result"][0]["vehicle"]["name"])
#print(data["result"][0]["provider"]["name"])
def next5f():
    url = "https://fdo.rocketlaunch.live/json/launches/next/5"

    response = requests.get(url)
    data = response.json()
    next1 = (data["result"][0]["launch_description"])
    next2 = (data["result"][1]["launch_description"])
    next3 = (data["result"][2]["launch_description"])
    next4 = (data["result"][3]["launch_description"])
    next5 = (data["result"][4]["launch_description"])
    First = "First"


    next5l = ("**First:** " + next1 + "\n" + "**Second:** " + next2 + "\n" "**Third:** " +
              next3 + "\n" + "**Fourth:** " + next4 + "\n" "**Fifth:** " + next5 + "\n")
    return next5l
