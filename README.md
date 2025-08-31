# Atzar

*A weekly journey through my Spotify library, bringing forgotten songs back to life.*

**Atzar** (Catalan for *randomness*) is a Python project that automatically updates a [Spotify playlist](https://open.spotify.com/playlist/2KnSRUQZBENzQ0VMEVTwsb?si=9980cdff18ef437b) every Monday with a random selection of tracks from [my Starred playlist](https://open.spotify.com/playlist/74ezAopojjumaLWeWVUy0f?si=75822b89c7f247ce).  

As of August 2025, I have nearly 9,000 starred songs on Spotify — tracks I've added over the years but rarely get to revisit. **Atzar** is my way of bringing those songs back into rotation, letting me rediscover music and go down memory lane.  

The project:

- Authenticates with Spotify using a refresh token.
- Retrieves all tracks from my Starred playlist.
- Randomly selects a subset of tracks.
- Clears the weekly playlist and adds the new selection.
- Runs automatically every Monday via GitHub Actions.
- Uses modular Python code (`auth.py`, `playlist.py`, `main.py`) and `Poetry` for dependency management.
- Includes unit tests for core playlist functions.

---

## 🛠 How to use this for your own playlists

If you'd like to adapt **Atzar** for your own Spotify library:

1. **Create a Spotify Developer App**  
- Go to [Spotify Developer Dashboard](https://developer.spotify.com/dashboard/).  
- Create an app and note down your **Client ID** and **Client Secret**.  
- Set a redirect URI (e.g. `http://localhost:8888/callback`).  

2. **Get a refresh token**  
- Authenticate once with Spotify to generate a refresh token.  
- This project assumes you've already obtained it.   

3. **Set environment variables** (in a `.env` file locally, or as GitHub Actions secrets for automation):  
```bash
SPOTIPY_CLIENT_ID=your_client_id
SPOTIPY_CLIENT_SECRET=your_client_secret
SPOTIPY_REDIRECT_URI=http://localhost:8888/callback
SPOTIPY_REFRESH_TOKEN=your_refresh_token

STARRED_PLAYLIST_ID=your_source_playlist_id
WEEKLY_SELECTION_PLAYLIST_ID=your_destination_playlist_id
```

4. **Run manually** 
```
poetry install
poetry run python -m atzar.main
```
This clears your destination playlist and fills it with 30 random tracks from your source playlist.

5. **Automate with GitHub Actions**
- Add the same variables as repository secrets in GitHub.
- Push to GitHub, and the workflow will run automatically every Monday (you may change when the workflow runs by modifying the cron setup in `.github/workflows/update.yml`).