import requests
url = "https://pinterest-video-and-image-downloader.p.rapidapi.com/pinterest"
def pinterest_save(link):
    # url = "https://pinterest-video-and-image-downloader.p.rapidapi.com/pinterest"
    querystring = {"url": link}

    headers = {
        "x-rapidapi-key": "4360836b63msh9edf45be1d447e0p105946jsn831c2c920c00",
        "x-rapidapi-host": "pinterest-video-and-image-downloader.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers, params=querystring)

    return response.json()["data"]["url"]

# import requests
# url = "https://shazam-api7.p.rapidapi.com/charts/get-top-songs-in-city"

# querystring = {"country_code":"US","city_name":"Chicago","limit":"10"}

# headers = {
# 	"x-rapidapi-key": "4360836b63msh9edf45be1d447e0p105946jsn831c2c920c00",
# 	"x-rapidapi-host": "shazam-api7.p.rapidapi.com"
# }

# response = requests.get(url, headers=headers, params=querystring)
# print(response.status_code)