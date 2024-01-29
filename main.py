from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware

from spotifyAUTH import get_token
from GetSongsName import get_tracks
from yt_download_song import download_video

app = FastAPI()

origins = ["http://localhost:5173"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

token = get_token()


@app.get("/")
async def fun1(playlist_url: str):
    try:
        # playlist_url = "https://open.spotify.com/playlist/3c9WHcjzTyx8ojpCliUOvY"
        track = get_tracks(token, playlist_url)
        successfully_downloaded_videos = []

        for song in track:
            downloaded_video = download_video(song['name'], song['artist'])
            if downloaded_video:
                successfully_downloaded_videos.append(downloaded_video)

        return {"successfully_downloaded_videos": successfully_downloaded_videos}
        # return {"tracks": track}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@app.get('/download')
async def fun(name: str, artist: str):
    try:
        # download_video(name, artist)
        download_video(name, artist)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


