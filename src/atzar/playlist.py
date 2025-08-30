import numpy as np
import logging

logger = logging.getLogger(__name__)

def clear_playlist(sp, playlist_id: str) -> None:
    """Remove all tracks from the given playlist."""
    tracks = sp.playlist_items(playlist_id)
    track_ids = [item["track"]["id"] for item in tracks["items"] if item.get("track") and item["track"].get("id")]

    while tracks.get("next"):
        tracks = sp.next(tracks)
        track_ids.extend([item["track"]["id"] for item in tracks["items"] if item.get("track") and item["track"].get("id")])

    if track_ids:
        sp.playlist_remove_all_occurrences_of_items(playlist_id, track_ids)
        logger.info("Cleared playlist (%d tracks removed).", len(track_ids))
    else:
        logger.info("Playlist already empty.")

def get_random_tracks(sp, playlist_id: str, n: int = 30) -> list[str]:
    """Return n random track IDs from a playlist, skipping invalid tracks."""
    all_tracks = []
    results = sp.playlist_items(playlist_id)

    while results:
        for item in results["items"]:
            track = item.get("track")
            if track and track.get("id"):
                all_tracks.append(track["id"])
        results = sp.next(results) if results.get("next") else None

    if len(all_tracks) < n:
        logger.warning(
            "Requested %d tracks, but only %d valid tracks found. Returning all valid tracks.",
            n, len(all_tracks)
        )
        return all_tracks

    selection = np.random.choice(all_tracks, size=n, replace=False).tolist()
    logger.info("Selected %d random tracks.", len(selection))
    return selection

def add_tracks(sp, playlist_id: str, track_ids: list[str]) -> None:
    """Add tracks to playlist, skipping any invalid entries."""
    valid_tracks = [tid for tid in track_ids if tid]
    if not valid_tracks:
        logger.warning("No valid tracks to add to playlist.")
        return

    sp.playlist_add_items(playlist_id, valid_tracks)
    logger.info("Added %d tracks.", len(valid_tracks))
