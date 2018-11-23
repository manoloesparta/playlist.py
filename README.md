# Update Playlist
I tend to listen a lot of albums, but I have more than a 130 albums pending to listen you can find a track from each album in this [playlist](https://open.spotify.com/user/manoloesparta/playlist/1ofx1iXeCqb5gPuEWSanfc?si=gN6ZmmDSQleNc7QLDiTXew). So this little script was made to randomize the way to choose albums to listen :D

It selects randomly 100 albums out of the 130+, and from each selected album, it selects one song randomly, appending all the songs to this other [playlist](https://open.spotify.com/user/manoloesparta/playlist/0iYFyrLsby2E0QBBPs2xWi?si=Yv6aajgYTTyMnEj4jbljWA). This is the playlist I listen daily.

## Requirements
```
git clone https://github.com/manoloesparta/updateplaylist
pip install -r requirements.txt
```
This uses spotipy library so in order to use you need to setup some enviroment variables, that you get from an application from [here](https://developer.spotify.com/dashboard/applications)
```
export SPOTIPY_CLIENT_ID='Client ID'
export SPOTIPY_CLIENT_SECRET='Client Secret'
export SPOTIPY_REDIRECT_URI='http://google.com/'
```
And some other enviroment variables setup by me in order for this to work
```
export playlist_retrieved='uri of playlist from which you are retrieving the albums'
export playlist_goal='uri of the playlist which you are appending the songs'
export username='your spotify account username'
```
_I recommend adding this to your .bash_profile_

## Usage
In order to run the program just type
```
python3 main.py
```

## License
This project is licensed under the MIT License