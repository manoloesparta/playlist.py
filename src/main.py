from os import environ as ev
from playlist.spotify import SpotifyUser
from playlist.source import Source
from playlist.goal import Goal

def main():
    username = ev['USERNAME']
    client_id, client_secret = ev['CLIENT_ID'], ev['CLIENT_SECRET']
    spotify_user = SpotifyUser(username, client_id, client_secret)

    playlist_src, playlist_goal = ev['PLAYLIST_SRC'], ev['PLAYLIST_GOAL']
    source = Source(playlist_src, spotify_user)
    goal = Goal(playlist_goal, spotify_user)

    goal.update(source)

if __name__ == '__main__':
    main()