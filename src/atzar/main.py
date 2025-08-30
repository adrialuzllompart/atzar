import os
import logging
from dotenv import load_dotenv
from atzar.auth import authenticate
from atzar.playlist import clear_playlist, get_random_tracks, add_tracks

logging.basicConfig(level=logging.INFO)

def main():
    load_dotenv()
    sp = authenticate()
    weekly_id = os.getenv("WEEKLY_SELECTION_PLAYLIST_ID")
    starred_id = os.getenv("STARRED_PLAYLIST_ID")

    clear_playlist(sp, weekly_id)
    selection = get_random_tracks(sp, starred_id, n=30)
    add_tracks(sp, weekly_id, selection)

if __name__ == "__main__":
    main()
