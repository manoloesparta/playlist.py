
class Goal:
    def __init__(self, playlist_goal, spotify_user):
        self.playlist_goal = playlist_goal
        self.spotify_user = spotify_user

    def remove(self):
        data = self.spotify_user.user.user_playlist_tracks(
            self.spotify_user.username, self.playlist_goal)
        actual_tracks = data['items']

        removed = []
        for i in actual_tracks:
            removed.append(i['track']['id'])

       	self.spotify_user.user.user_playlist_remove_all_occurrences_of_tracks(
       	    self.spotify_user.username, self.playlist_goal, removed)

    def update(self, tracks_uri):
        self.remove()
        self.spotify_user.user.user_playlist_add_tracks(
            self.spotify_user.username, self.playlist_goal, tracks_uri)
