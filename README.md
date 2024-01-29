# Spotify Playlist to Video Downloader

## Overview

This is a Python application that allows you to download songs from a Spotify playlist. It uses the FastAPI framework and PyTube for downloading those songs in its video format.

## Dependencies

Make sure you have the following installed:

- Python
- PyTube
- FastAPI
- Uvicorn
- Dotenv
- SpotifyAUTH

You can install the Python dependencies using:

```bash
pip install -r packages_listed_above
```

## Spotify Developer Account
You will need a spotify developer account to get client_id and client_secret
- Create a Spotify Developer account at [Spotify for Developers](https://developer.spotify.com/dashboard).
- Create a new app in the dashboard.
- Obtain the Client ID and Client Secret.
- Create a .env file in the project's root folder and add your credentials:
```
CLIENT_ID= your_spotify_client_id
CLIENT_SECRET= your_spotify_client_secret
```

# Running the Application
- Start the server using Uvicorn:
- Go in terminal and use command:
  ```
  uvicorn main:app --reload
  ```
- Open your browser and go to http://localhost:8000/docs. (modify the port number as yours)
- In right side of 'Parameters', click on 'Try it out' and enter the playlist_url then press 'Execute'
- In terminal which you have used to start the server, you can see that the download has started there, once completed you will get the response of all the songs that has been downloaded successfully. It will get download in the dir from where you are running the server.
