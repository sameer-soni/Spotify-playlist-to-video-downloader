import spotifyAUTH
from requests import get
import json


def get_tracks(token, playlist_url):
    playlist_id = playlist_url.split('/')[-1]

    url = f"https://api.spotify.com/v1/playlists/{playlist_id}"
    headers = spotifyAUTH.get_auth_header(token)

    result = get(url, headers=headers)
    json_r = json.loads(result.content)

    tracks= json_r['tracks']['items']
    track_list = []
    for track in tracks:
        # track_list.append(track['track']['name'])
        # art = track['track']['artists']
        #
        # for a in art:
        #     print(a['name'])
        track_info = {
            "name": track['track']['name'],
            # "artist": next(iter(artist['name'] for artist in track['track']['artists'])),
            "artist": track['track']['artists'][0]['name'],
            # "img": next(iter(img['url'] for album in track['track']['album'] for img in album['images'][0]))
            "img": track['track']['album']['images'][0]['url'] if track['track']['album']['images'] else None

        }

        track_list.append((track_info))

    # print(track_list)
    # print(track_list[0]['artist'])
    return track_list

# for track in tracks:
#     print(track['track']['name'])
# from spotifyAUTH import get_token
# token = get_token()
# get_tracks(token,"https://open.spotify.com/playlist/3c9WHcjzTyx8ojpCliUOvY")