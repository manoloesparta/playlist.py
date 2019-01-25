from os import environ as ev
from playlist.spotify import SpotifyUser
from playlist.source import Source
from playlist.goal import Goal

def main():

    try:
        username = ev['USERNAME']
        client_id, client_secret, redirect_uri = ev['CLIENT_ID'], ev['CLIENT_SECRET'], ev['REDIRECT_URI']
        playlist_src, playlist_goal = ev['PLAYLIST_SRC'], ev['PLAYLIST_GOAL']

    except KeyError as k:
        print(k, 'must be defined in the environment or you need to define the variables with your custom data')
    
    spotify_user = SpotifyUser(username, client_id, client_secret, redirect_uri)
    source = Source(playlist_src, spotify_user)
    goal = Goal(playlist_goal, spotify_user)

    goal.update(source)

if __name__ == '__main__':
    main()