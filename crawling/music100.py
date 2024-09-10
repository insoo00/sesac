import requests

# trackId 구하기
trackIdUrl = "https://apis.naver.com/vibeWeb/musicapiweb/vibe/v1/chart/track/total"
params = {'start': '1', 'display': '100'}

headers = {"Content-Type": "application/json", "Accept": "application/json"}
response = requests.get(trackIdUrl, headers=headers, params=params)
data = response.json()
tracks = data['response']['result']['chart']['items']['tracks']
trackIds = []

for track in tracks:
    trackIds.append(track['trackId'])



# trackId로 trackTitle과 lyric 구하기
for rank, trackId in enumerate(trackIds):
    trackInfoUrl = f"https://apis.naver.com/vibeWeb/musicapiweb/track/{trackId}"
    lyricUrl = f"https://apis.naver.com/vibeWeb/musicapiweb/vibe/v4/lyric/{trackId}"

    trackInfo = requests.get(trackInfoUrl, headers=headers)
    trackTitle = trackInfo.json()['response']['result']['track']['trackTitle']

    lyricInfo = requests.get(lyricUrl, headers=headers)
    lyric = lyricInfo.json()['response']['result']['lyric']['normalLyric']['text']

    print(f'\nTop{rank} \n노래제목: {trackTitle} \n가사: \n{lyric}')
    





