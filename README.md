# Atzar

*A weekly journey through my Spotify library, bringing forgotten songs back to life.*

**Atzar** (Catalan for *randomness*) is a Python project that automatically updates a [Spotify playlist](https://open.spotify.com/playlist/2KnSRUQZBENzQ0VMEVTwsb?si=9980cdff18ef437b) every Monday with a random selection of tracks from my [Starred playlist](https://open.spotify.com/playlist/74ezAopojjumaLWeWVUy0f?si=75822b89c7f247ce).  

As of August 2025, I have nearly 9,000 starred songs on Spotify — tracks I've added over the years but rarely get to revisit. **Atzar** is my way of bringing those songs back into rotation, letting me rediscover music, memories, and moments of nostalgia from the past.

The project:

- Authenticates with Spotify using a refresh token.
- Retrieves all tracks from my Starred playlist.
- Randomly selects a subset of tracks.
- Clears the weekly playlist and adds the new selection.
- Runs automatically every Monday via GitHub Actions.
- Uses modular Python code (`auth.py`, `playlist.py`, `main.py`) and `Poetry` for dependency management.
- Includes unit tests for core playlist functions.
