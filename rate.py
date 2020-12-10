import requests
import json

def getRateLimit(URL):
    PARAMS = {}
    r = requests.get(url = URL, params = PARAMS)
    data = r.json()
    print (data)

url = "https://api.github.com/rate_limit"
getRateLimit(url)
