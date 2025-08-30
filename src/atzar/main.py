import os
import logging
from dotenv import load_dotenv
from atzar.auth import authenticate
from atzar.playlist import clear_playlist, get_random_tracks, add_tracks

# Load local .env
load_dotenv()

# Logging setup
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s"
)
logger = logging.getLogger(__name__)

def main():
    try:
        logger.info("Starting weekly playlist update...")

        sp = authenticate()
        weekly_id = os.getenv("WEEKLY_SELECTION_PLAYLIST_ID")
        starred_id = os.getenv("STARRED_PLAYLIST_ID")

        logger.info("Clearing previous playlist tracks...")
        clear_playlist(sp, weekly_id)

        logger.info("Selecting 30 random tracks from starred playlist...")
        selection = get_random_tracks(sp, starred_id, n=30)

        logger.info("Adding selected tracks to weekly playlist...")
        add_tracks(sp, weekly_id, selection)

        logger.info("Weekly playlist updated successfully!")

    except Exception as e:
        logger.exception("Error updating weekly playlist")
        raise  # ensures GitHub Actions marks workflow as failed

if __name__ == "__main__":
    main()
