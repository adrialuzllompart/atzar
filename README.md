# Atzar

**Atzar** (Catalan for *randomness*) is a Python project that automatically updates a Spotify playlist every Monday with a random selection of tracks from my Starred playlist.

The project:
- Authenticates with Spotify using a refresh token.
- Retrieves all tracks from my Starred playlist.
- Randomly selects a subset of tracks.
- Clears the weekly playlist and adds the new selection.
- Runs automatically every Monday via GitHub Actions.
- Uses modular Python code (`auth.py`, `playlist.py`, `main.py`) and `Poetry` for dependency management.
- Includes unit tests for core playlist functions.
