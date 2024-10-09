import requests
from pprint import pprint
url = "https://all-in-one-vidoe-downloader.p.rapidapi.com/download"
def all_downloader(link):
    querystring = {"url": link}
    headers = {
        "x-rapidapi-key": "4360836b63msh9edf45be1d447e0p105946jsn831c2c920c00",
        "x-rapidapi-host": "all-in-one-vidoe-downloader.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers,params=querystring)

    pprint(response.json())
all_downloader("https://www.instagram.com/p/DAOr9zMox_0/?igsh=ZDZnODlxb2d2amt1")