def removeSongs(Spotify, username, playlist_goal):
	results = Spotify.user_playlist_tracks(username, playlist_goal)
	tracks = results['items']
	
	removed = []
	for i in tracks:
		removed.append(i['track']['id'])

	Spotify.user_playlist_remove_all_occurrences_of_tracks(username, playlist_goal, removed)