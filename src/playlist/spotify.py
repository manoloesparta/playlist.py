from os import environ as ev, remove
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
        """
        Sets local enviroment variables to given values
        in order to spotipy to work
        """
        ev['SPOTIPY_CLIENT_ID'] = self.client_id
        ev['SPOTIPY_CLIENT_SECRET'] = self.client_secret
        ev['SPOTIPY_REDIRECT_URI'] = 'http://google.com/'

    def auth(self):
        """
        Authentifies the user loading the .cache file or
        by creating a new one
        """
        try:
            token = util.prompt_for_user_token(self.username, self.scope)
        except:
            remove(f'.cache-{self.username}')
            token = util.prompt_for_user_token(self.username, self.scope)

        self.user = Spotify(auth=token)
