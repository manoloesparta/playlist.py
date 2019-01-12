def getAlbums(Spotify, username, playlist_retrieved):
	results = Spotify.user_playlist_tracks(username, playlist_retrieved)
	tracks = results['items']
	while results['next']:
		results = Spotify.next(results)
		tracks.extend(results['items'])

	albums_uri = []
	albums_name = []
	albums_artist = []
	for i in tracks:
		albums_uri.append(i['track']['album']['id'])
		albums_name.append(i['track']['album']['name'])
		albums_artist.append(i['track']['artists'][0]['name'])

	return {'albums_uri':albums_uri, 'albums_name':albums_name, 'albums_artist':albums_artist}