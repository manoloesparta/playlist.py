from os import environ
from playlist.spotify import SpotifyUser
from playlist.source import Source
from playlist.goal import Goal

def main():
    username = environ['USERNAME']
    client_id = environ['CLIENT_ID']
    client_secret = environ['CLIENT_SECRET']
    spotify_user = SpotifyUser(username, client_id, client_secret)

    playlist_src = environ['PLAYLIST_SRC']
    source = Source(playlist_src, spotify_user)

    playlist_goal = environ['PLAYLIST_GOAL']
    goal = Goal(playlist_goal, spotify_user)

    goal.update(source.tracks_uri)

if __name__ == '__main__':
    main()