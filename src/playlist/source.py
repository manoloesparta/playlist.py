from random import randint
from tqdm import tqdm

class Source:
    def __init__(self, playlist_src, spotify_user):
        self.playlist_src = playlist_src
        self.spotify_user = spotify_user
        self.albums_uri = []
        self.tracks_uri = []

        self._load_albums()
        self._select_albums()
        self._select_songs()

    def _load_albums(self):
        """ Loads all the albums from self.playlist_src """
        results = self.spotify_user.user.user_playlist_tracks(
            self.spotify_user.username, self.playlist_src)
        tracks = results['items']
        while results['next']:
            results = self.spotify_user.user.next(results)
            tracks.extend(results['items'])

        for track in tracks:
            self.albums_uri.append(track['track']['album']['id'])

        self.tracks_num = 100 if len(tracks) > 100 else len(tracks)

    def _select_albums(self):
        """ Select 100 or less albums randomly from self.albums_uri """
        random_nums = []
        temp_albums = []

        for _ in range(self.tracks_num):
            choice = randint(0, len(self.albums_uri) - 1)
            while choice in random_nums:
                choice = randint(0, len(self.albums_uri) - 1)
            random_nums.append(choice)
            temp_albums.append(self.albums_uri[choice])

        self.albums_uri = temp_albums

    def _select_songs(self):
        """ Select one song of each randomly selected album of 
        self.albums_uri """
        for i in tqdm(range(len(self.albums_uri))):
            set_list = self.spotify_user.user.album_tracks(
                self.albums_uri[i])
            mini = randint(0, len(set_list['items']) - 1)
            self.tracks_uri.append(set_list['items'][mini]['id'])
