from os import environ
from playlist.auth import auth
from playlist.remove import removeSongs
from playlist.albums import getAlbums
from playlist.selectAlbums import selectAlbums
from playlist.selectSongs import selectSongs

playlist_retrieved = '1ofx1iXeCqb5gPuEWSanfc'
playlist_goal = '0iYFyrLsby2E0QBBPs2xWi'

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
