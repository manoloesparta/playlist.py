from os import environ, remove
from spotipy import util
from spotipy import Spotify

def auth(username, scope): 

	playlist_retrieved = environ['playlist_retrieved']
	playlist_goal = environ['playlist_goal']
	
	try:
		token = util.prompt_for_user_token(username, scope)
	except:
		remove(f'.cache-{username}')
		token = util.prompt_for_user_token(username, scope)

	return Spotify(auth=token)