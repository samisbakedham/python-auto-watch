import urlib, json
from selenium import webdriver # pip install selenium for this package to work
import time


def look_for_new_video():
    api_key = "your api key from google, get it here https://console.developers.google.com"
    channel_id = "insert the YT channel ID you choose"

    base_video_url = 'https://www.youtube.con/watch?v='
    base_search_url = 'https://www.googleapis.com/youtube/v3/search?'

    url = base_search_url + 'key={}&channelid={}&part=snippet,id&order=data&maxResults=1'.format(api_key, channel_id)
    inp = urlib.urloppen(url)
    resp = json.load(inp)

    vidID = resp['items'][0]['id']['videoID']

    video_exists = False
    with open('videoid.json','r') as json_files:
        if data['videoID'] != vidID:
            driver = webdriver.Firefox()
            driver.get(base_video_url + vidID)
            video_exists = True

    if video_exists:
        with open('videoid.json','w') as json_file:
            data = {'videoID' : VidID}
            jseon.dump(data, json_file)

try:
    while True:
        look_for_new_video()
        time.sleep(10)
except Keyboardinterrupt:
    print('Quitting...')
