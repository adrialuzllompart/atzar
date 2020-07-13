import numpy as np
import pandas as pd
import requests
import json
import spotipy
#

def authenticate(username='adrialuz', scope='playlist-modify-public'):

	with open('/Users/aluz/Desktop/repos/festival-playlists/auth.json') as f:
	    credentials = json.load(f)

	spotify_client_id = credentials['spotify']['client_id']
	spotify_client_secret = credentials['spotify']['client_secret']

	token = spotipy.util.prompt_for_user_token(username, scope, spotify_client_id, spotify_client_secret,
	                                          'http://localhost')

	sp = spotipy.Spotify(auth=token)

	sp.trace = False

	return sp

def empty_playlist(sp, username='adrialuz', weekly_selection_playlist_id='2KnSRUQZBENzQ0VMEVTwsb'):
	
	tracks_to_remove = []

	tracks = sp.playlist(weekly_selection_playlist_id, fields='tracks,next')['tracks']

	for t in range(len(tracks['items'])):
	    tracks_to_remove.append(tracks['items'][t]['track']['id'])

	sp.user_playlist_remove_all_occurrences_of_tracks(username, weekly_selection_playlist_id, tracks_to_remove)
	print('Succesfully removed all tracks from previous week.')

def get_random_selection(sp, starred_playlist_id='74ezAopojjumaLWeWVUy0f', n_tracks=30):

	all_tracks = []

	tracks = sp.playlist(starred_playlist_id, fields='tracks,next')['tracks']

	for t in range(len(tracks['items'])):
	    all_tracks.append(tracks['items'][t]['track']['id'])

	while tracks['next']:
	    tracks = sp.next(tracks)
	    for t in range(len(tracks['items'])):
	        all_tracks.append(tracks['items'][t]['track']['id'])

	weekly_selection = np.random.choice(all_tracks, size=n_tracks, replace=False)

	return weekly_selection

def add_selection(sp, weekly_selection, username='adrialuz', weekly_selection_playlist_id='2KnSRUQZBENzQ0VMEVTwsb'):

	sp.user_playlist_add_tracks(username, weekly_selection_playlist_id, weekly_selection)
	print('Weekly Selection playlist has been updated!')


sp = authenticate()
empty_playlist(sp)
weekly_selection = get_random_selection(sp)
add_selection(sp, weekly_selection)