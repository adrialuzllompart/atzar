import os
from dotenv import load_dotenv
from spotipy import Spotify
from spotipy.oauth2 import SpotifyOAuth

# Load local .env if present (ignored in GitHub Actions)
load_dotenv()

def authenticate(scope="playlist-modify-public") -> Spotify:
    refresh_token = os.getenv("SPOTIPY_REFRESH_TOKEN")
    client_id = os.getenv("SPOTIPY_CLIENT_ID")
    client_secret = os.getenv("SPOTIPY_CLIENT_SECRET")
    redirect_uri = os.getenv("SPOTIPY_REDIRECT_URI")

    if not all([refresh_token, client_id, client_secret, redirect_uri]):
        raise ValueError("Missing one of the required Spotify credentials")

    sp_oauth = SpotifyOAuth(
        client_id=client_id,
        client_secret=client_secret,
        redirect_uri=redirect_uri,
        scope=scope,
        cache_path=None  # don't store tokens on disk
    )

    # Use refresh token to get a new access token
    token_info = sp_oauth.refresh_access_token(refresh_token)
    sp = Spotify(auth=token_info["access_token"])
    return sp
