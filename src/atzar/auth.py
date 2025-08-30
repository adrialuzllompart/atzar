import os
from spotipy import Spotify
from spotipy.oauth2 import SpotifyOAuth
from dotenv import load_dotenv

def authenticate(scope="playlist-modify-public") -> Spotify:
    """Authenticate and return a Spotify client."""
    load_dotenv()
    token_info = {
        "refresh_token": os.getenv("SPOTIPY_REFRESH_TOKEN"),
        "client_id": os.getenv("SPOTIPY_CLIENT_ID"),
        "client_secret": os.getenv("SPOTIPY_CLIENT_SECRET"),
        "redirect_uri": os.getenv("SPOTIPY_REDIRECT_URI"),
    }
    sp = Spotify(auth_manager=SpotifyOAuth(
        client_id=token_info["client_id"],
        client_secret=token_info["client_secret"],
        redirect_uri=token_info["redirect_uri"],
        scope=scope,
        cache_path=None  # don't store token locally
    ))
    sp.auth_manager.refresh_access_token(token_info["refresh_token"])
    return sp
