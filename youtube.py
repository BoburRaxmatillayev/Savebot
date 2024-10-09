# import requests

# def download_video(video_url, file_name):
#     response = requests.get(video_url, stream=True)
#     if response.status_code == 200:
#         with open(file_name, 'wb') as f:
#             for chunk in response.iter_content(chunk_size=1024):
#                 if chunk:
#                     f.write(chunk)
#         return file_name
#     return None




# def youtube_save(link):
#     # YouTube video ID'sini linkdan ajratib olish
#     video_id = link.split("v=")[-1].split("&")[0]
    
#     url = "https://yt-api.p.rapidapi.com/dl"
    
#     querystring = {"id": video_id}
    
#     headers = {
#         "x-rapidapi-key": "4360836b63msh9edf45be1d447e0p105946jsn831c2c920c00",
#         "x-rapidapi-host": "yt-api.p.rapidapi.com"
#     }
    
#     # API so'rovini yuborish
#     response = requests.get(url, headers=headers, params=querystring)
    
#     # JSON javobni olish
#     data = response.json()
    
#     # Adaptive formats dan birinchi URL'ni olish
#     video_url = data.get("adaptiveFormats", [{}])[0].get("url")
    
#     # URL'ni qaytarish
#     return video_url


import requests
from pprint import pprint
url = "https://youtube-quick-video-downloader.p.rapidapi.com/api/youtube/links"
def youtube_save(link):

    payload = {"url": link}
    headers = {
        "x-rapidapi-key": "4360836b63msh9edf45be1d447e0p105946jsn831c2c920c00",
        "x-rapidapi-host": "youtube-quick-video-downloader.p.rapidapi.com",
        "Content-Type": "application/json",
        "X-Forwarded-For": "70.41.3.18"
    }

    response = requests.post(url, json=payload, headers=headers)

    return response.json()[0]["urls"][0]["url"]
#     pprint(response.json()[0]["urls"][13]["url"])
# youtube_save("https://youtu.be/LK3RCf9qqGM?si=SvOhRpY-Zaueevfl")