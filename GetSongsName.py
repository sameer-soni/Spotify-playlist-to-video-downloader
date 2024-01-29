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
        track_info = {
            "name": track['track']['name'],
            "artist": track['track']['artists'][0]['name'],
            "img": track['track']['album']['images'][0]['url'] if track['track']['album']['images'] else None

        }

        track_list.append((track_info))
    return track_list