class Goal:
    def __init__(self, playlist_goal, spotify_user):
        self.playlist_goal = playlist_goal
        self.spotify_user = spotify_user

    def _remove(self):
        """ Removes current songs from playlist """
        data = self.spotify_user.user.user_playlist_tracks(
            self.spotify_user.username, self.playlist_goal)
        actual_tracks = data['items']

        removed = []
        for i in actual_tracks:
            removed.append(i['track']['id'])

       	self.spotify_user.user.user_playlist_remove_all_occurrences_of_tracks(
       	    self.spotify_user.username, self.playlist_goal, removed)

    def update(self, source):
        """ Updates playlist with new randomly selected songs, 
        source parameter is a Source object """
        self._remove()
        self.spotify_user.user.user_playlist_add_tracks(
            self.spotify_user.username, self.playlist_goal, source.tracks_uri)
