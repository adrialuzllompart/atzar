import os
import logging
from dotenv import load_dotenv
from spotipy import Spotify
from spotipy.oauth2 import SpotifyOAuth, SpotifyOauthError

# Load local .env if present
load_dotenv()

logger = logging.getLogger(__name__)

def authenticate(scope: str = "playlist-modify-public") -> Spotify:
    """
    Authenticate with Spotify using a refresh token.
    Works locally with .env or in GitHub Actions via secrets.
    """
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

    try:
        token_info = sp_oauth.refresh_access_token(refresh_token)
        access_token = token_info.get("access_token")
        if not access_token:
            raise SpotifyOauthError("Failed to get access token from refresh token")
    except SpotifyOauthError as e:
        logger.error("Spotify authentication failed: %s", e)
        raise

    return Spotify(auth=access_token)
