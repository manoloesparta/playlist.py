from os import environ
from updateplaylist.auth import auth
from updateplaylist.remove import removeSongs
from updateplaylist.albums import getAlbums
from updateplaylist.selectAlbums import selectAlbums
from updateplaylist.selectSongs import selectSongs

playlist_retrieved = environ['playlist_retrieved']
playlist_goal = environ['playlist_goal']

username = environ['username']
scope = 'playlist-modify-private'

def main():

	Spotify = auth(username, scope)

	removeSongs(Spotify, username, playlist_goal)

	albums = getAlbums(Spotify, username, playlist_retrieved)
	albums = selectAlbums(albums['albums_uri'], albums['albums_name'],albums['albums_artist'])

	tracks = selectSongs(Spotify, albums['albums_selected'], albums['albums_selected_name'], albums['albums_selected_artist'])

	Spotify.user_playlist_add_tracks(username, playlist_goal, tracks['tracks_id'])


if __name__ == '__main__':

	main()