import spotipy
from spotipy import util
from random import randint

def selectSongs(Spotify, albums_selected, albums_selected_names, albums_selected_artist):

	tracks_ids = []
	tracks_names = []

	for i in range(len(albums_selected)):

		set_list = Spotify.album_tracks(albums_selected[i])

		print('ALBUM ', albums_selected_names[i],'BY', albums_selected_artist[i], 'LOADED')

		mini = randint(0, len(set_list['items']) - 1)
		leng = len(set_list)

		tracks_ids.append(set_list['items'][mini]['id'])
		tracks_names.append(set_list['items'][mini]['name'])

	return {'tracks_id': tracks_ids, 'tracks_name': tracks_names}