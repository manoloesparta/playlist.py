import os
from spotipy import util
from spotipy import Spotify

def auth(username, scope): 

	playlist_retrieved = '1ofx1iXeCqb5gPuEWSanfc'
	playlist_goal = '0iYFyrLsby2E0QBBPs2xWi'
	
	try:
		token = util.prompt_for_user_token(username, scope)
	except:
		os.remove(f'.cache-{username}')
		token = util.prompt_for_user_token(username, scope)

	return Spotify(auth=token)