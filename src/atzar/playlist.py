import numpy as np
import logging

logger = logging.getLogger(__name__)

def clear_playlist(sp, playlist_id: str) -> None:
    """Remove all tracks from the given playlist."""
    tracks = sp.playlist_items(playlist_id)
    track_ids = [item["track"]["id"] for item in tracks["items"] if item["track"]]

    while tracks["next"]:
        tracks = sp.next(tracks)
        track_ids.extend([item["track"]["id"] for item in tracks["items"] if item["track"]])

    if track_ids:
        sp.playlist_remove_all_occurrences_of_items(playlist_id, track_ids)
        logger.info("Cleared playlist.")
    else:
        logger.info("Playlist already empty.")

def get_random_tracks(sp, playlist_id: str, n: int = 30) -> list[str]:
    """Return n random track IDs from a playlist."""
    all_tracks = []
    results = sp.playlist_items(playlist_id)

    while results:
        all_tracks.extend([item["track"]["id"] for item in results["items"] if item["track"]])
        results = sp.next(results) if results["next"] else None

    return np.random.choice(all_tracks, size=n, replace=False).tolist()

def add_tracks(sp, playlist_id: str, track_ids: list[str]) -> None:
    """Add tracks to playlist."""
    sp.playlist_add_items(playlist_id, track_ids)
    logger.info("Added %d tracks.", len(track_ids))
