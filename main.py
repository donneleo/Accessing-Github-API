import requests
import json

def getAPI(URL):

    PARAMS = {}
    r = requests.get(url = URL, params = PARAMS)
    data = r.json()
    for info in data:
        if(info["language"] == None):
            info["language"] = "This is an essay"
        print(info["name"], ":", info["language"])
    print("\n")

def getNumberCommits(newURL):

    PARAMS = {}
    s = requests.get(url = newURL, params = PARAMS)
    data = s.json()
    for each in data:
        print("Date/Time:", each["commit"]["author"]["date"], "What was Changed:", each["commit"]["message"])

URL = ("https://api.github.com/users/donneleo/repos")
getAPI(URL)

newURL = ("https://api.github.com/repos/donneleo/3rd-Year-College-Work/commits")
getNumberCommits(newURL)