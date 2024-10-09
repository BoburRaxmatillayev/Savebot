# # import requests
# # from pprint import pprint

# # url = "https://all-media-downloader.p.rapidapi.com/rapid_download/download"

# # def insta_save(link):
# #     # So'rovda foydalaniladigan ma'lumotlar
# #     payload = {
# #         'url': link
# #     }
    
# #     headers = {
# #         "x-rapidapi-key": "4360836b63msh9edf45be1d447e0p105946jsn831c2c920c00",
# #         "x-rapidapi-host": "all-media-downloader.p.rapidapi.com",
# #     }

# #     # `files` o'rniga `data` ishlatilmoqda
# #     response = requests.post(url, data=payload, headers=headers)

# #     rasmlar = []
# #     try:
# #         for i in response.json()["data"]["shortcode_media"]["edge_sidecar_to_children"]["edges"]:
# #             try:
# #                 rasmlar.append(i['node']['display_resources'][-1]['src'])
# #             except KeyError:
# #                 pass
# #         return {"images": rasmlar}
# #     except KeyError:
# #         try:
# #             return {"video": response.json()["data"]['shortcode_media']["video_url"]}
# #         except KeyError:
# #             return {"error": "Hech qanday media topilmadi"}
# #     pprint(response.json()["data"]["mediaList"][0]["media_quality"][0])
# # result = insta_save("https://www.instagram.com/p/C1Uf5XpI2Ff/?utm_source=ig_web_copy_link&igsh=MzRlODBiNWFlZA==")
# # print(result)

# # print(result)


# # import requests
# # from pprint import pprint 
# # url = "https://instagram-media-downloader.p.rapidapi.com/rapid/post_v2.php"

# # def insta_save(link):

# #     querystring = {"url":link}

# #     headers = {
# #         "X-RapidAPI-Key": "138577ad99msh285e033da25ed1bp12cefbjsne90ad86c1843",
# #         "X-RapidAPI-Host": "instagram-media-downloader.p.rapidapi.com"
# #     }

# #     response = requests.get(url, headers=headers, params=querystring)

# #     try:
# #         result = ("video",response.json()["items"][0]["video_versions"][0]["url"])
# #     except:
# #         result = ("rasm",response.json()["items"][0]["image_versions2"]["candidates"][0]["url"])
    
# #     return result



# # import requests
# # from pprint import pprint 
# # url = "https://instagram-media-downloader.p.rapidapi.com/rapid/post_v2.php"

# # # def insta_save(link):

# # querystring = {"url":"https://www.instagram.com/reel/C63i_3Ns9hQ/?igsh=MTM0bDc2cjc2bGI3aA=="}

# # headers = {
# #     "X-RapidAPI-Key": "138577ad99msh285e033da25ed1bp12cefbjsne90ad86c1843",
# #     "X-RapidAPI-Host": "instagram-media-downloader.p.rapidapi.com"
# # }

# # response = requests.get(url, headers=headers, params=querystring)

# # print(response.status_code)
#     # insta_save("")

#     # try:
#     #     result = ("video",response.json()["items"][0]["video_versions"][0]["url"])
#     # except:
#     #     result = ("rasm",response.json()["items"][0]["image_versions2"]["candidates"][0]["url"])
    
#     # return result


# # import requests
# # from pprint import pprint
# # url = "https://instagram-bulk-scraper-latest.p.rapidapi.com/media_info_from_shortcode/CwqI-QTpUG2"
# # def insta_save(link):
# #     querystring = {"url":"https://www.instagram.com/reel/C63i_3Ns9hQ/?igsh=MTM0bDc2cjc2bGI3aA=="}
# #     headers = {
# #         "x-rapidapi-key": "4360836b63msh9edf45be1d447e0p105946jsn831c2c920c00",
# #         "x-rapidapi-host": "instagram-bulk-scraper-latest.p.rapidapi.com"
# #     }

# #     response = requests.get(url, headers=headers, params=querystring)
# #     pprint(response.json())
# #     # ["data"][0]["thumbnail_url"]
# # #     pprint(response.json()["data"][0]["download_url"])
# # insta_save("https://www.instagram.com/reel/C63i_3Ns9hQ/?igsh=MTM0bDc2cjc2bGI3aA==")


# # import requests
# # from pprint import pprint
# # url = "https://instagram-downloader.p.rapidapi.com/index"
# # def isnta_save(link):
# #     querystring = {"url":link}

# #     headers = {
# #         "x-rapidapi-key": "4360836b63msh9edf45be1d447e0p105946jsn831c2c920c00",
# #         "x-rapidapi-host": "instagram-downloader.p.rapidapi.com"
# #     }

# #     response = requests.get(url, headers=headers, params=querystring)

# #     pprint(response.json())
# # isnta_save("https://www.instagram.com/reel/C63i_3Ns9hQ/?igsh=MTM0bDc2cjc2bGI3aA==")

import requests
def insta_save(link):
    url = "https://instagram-downloader-download-instagram-videos-stories1.p.rapidapi.com/get-info-rapidapi"

    querystring = {"url":link}

    headers = {
        "x-rapidapi-key": "4360836b63msh9edf45be1d447e0p105946jsn831c2c920c00",
        "x-rapidapi-host": "instagram-downloader-download-instagram-videos-stories1.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers, params=querystring)
    rasmlar = []
    try:
        for i in response.json()["medias"]:
            try:
                rasmlar.append(i["download_url"])
            except KeyError:
                pass
        return {"images": rasmlar}
    except KeyError:
        try:
            return {"video": response.json()["download_url"]}
        except KeyError:
            return {"error": "Hech qanday media topilmadi"}
# ["medias"]
# ["download_url"]
    # print(response.json()["medias"])
    # print(response.json()["download_url"])

# result = insta_save("https://www.instagram.com/reel/C_6GObWCR0s/?igsh=MTJ5NXRkNm94MXBxNw==")
# print(result)
