import json
import requests

def astrof():
    url = "https://api.nasa.gov/planetary/apod?api_key=oyF4ZF1NgvKcZuj64Al9TmdJslmp1AHFPCCvxbTI"
    response = requests.get(url)
    json_data = response.json()
    apod = (json_data["url"])
    caption = (json_data["explanation"])
    fulltext = apod +" "+ caption
    return fulltext
