import os
from spotipy import Spotify
from spotipy.oauth2 import SpotifyOAuth

def authenticate(scope="playlist-modify-public") -> Spotify:
    """Authenticate and return a Spotify client."""
    sp = Spotify(auth_manager=SpotifyOAuth(
        client_id=os.getenv("SPOTIPY_CLIENT_ID"),
        client_secret=os.getenv("SPOTIPY_CLIENT_SECRET"),
        redirect_uri=os.getenv("SPOTIPY_REDIRECT_URI"),
        scope=scope,
        cache_path=".spotify_cache"  # saves token, no login each time
    ))
    return sp
