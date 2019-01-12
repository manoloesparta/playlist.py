from random import randint
from tqdm import tqdm

class Source:
    def __init__(self, playlist_src, spotify_user):
        self.playlist_src = playlist_src
        self.spotify_user = spotify_user
        self.albums_uri = []
        self.tracks_uri = []

        self.load_albums()
        self.select_albums()
        self.select_songs()

    def load_albums(self):
        results = self.spotify_user.user.user_playlist_tracks(
            self.spotify_user.username, self.playlist_src)
        tracks = results['items']
        while results['next']:
            results = self.spotify_user.user.next(results)
            tracks.extend(results['items'])

        for track in tracks:
            self.albums_uri.append(track['track']['album']['id'])

    def select_albums(self):
        random_nums = []
        temp_albums = []

        for _ in range(100):
            choice = randint(0, len(self.albums_uri) - 1)
            while choice in random_nums:
                choice = randint(0, len(self.albums_uri) - 1)
            random_nums.append(choice)
            temp_albums.append(self.albums_uri[choice])

        self.albums_uri = temp_albums

    def select_songs(self):
        for i in tqdm(range(len(self.albums_uri))):
            set_list = self.spotify_user.user.album_tracks(
                self.albums_uri[i])
            mini = randint(0, len(set_list['items']) - 1)
            self.tracks_uri.append(set_list['items'][mini]['id'])
