from os import environ, remove
from spotipy import util, Spotify

class SpotifyUser:
    def __init__(self, username, client_id, client_secret):
        self.username = username
        self.client_id = client_id
        self.client_secret = client_secret
        self.scope = 'playlist-modify-private'
        
        self.set_enviroment()
        self.auth()

    def set_enviroment(self):
        environ['SPOTIPY_CLIENT_ID'] = self.client_id
        environ['SPOTIPY_CLIENT_SECRET'] = self.client_secret
        environ['SPOTIPY_REDIRECT_URI'] = 'http://google.com/'

    def auth(self):
        try:
            token = util.prompt_for_user_token(self.username, self.scope)
        except:
            remove(f'.cache-{self.username}')
            token = util.prompt_for_user_token(self.username, self.scope)

        self.user = Spotify(auth=token)