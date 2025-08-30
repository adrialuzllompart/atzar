import pytest
from atzar.playlist import clear_playlist, get_random_tracks, add_tracks

class MockSpotify:
    def __init__(self):
        self.items_removed = []
        self.items_added = []

    def playlist_items(self, playlist_id):
        return {
            "items": [{"track": {"id": f"track{i}"}} for i in range(50)],
            "next": None
        }

    def playlist_remove_all_occurrences_of_items(self, playlist_id, track_ids):
        self.items_removed.extend(track_ids)

    def playlist_add_items(self, playlist_id, track_ids):
        self.items_added.extend(track_ids)

def test_clear_playlist():
    sp = MockSpotify()
    clear_playlist(sp, "dummy_playlist")
    assert len(sp.items_removed) == 50

def test_get_random_tracks():
    sp = MockSpotify()
    tracks = get_random_tracks(sp, "dummy_playlist", n=10)
    assert len(tracks) == 10
    assert all(track.startswith("track") for track in tracks)

def test_add_tracks():
    sp = MockSpotify()
    track_ids = ["track1", "track2", "track3"]
    add_tracks(sp, "dummy_playlist", track_ids)
    assert sp.items_added == track_ids
