# Update Playlist
I tend to listen a lot of albums, but I have more than a 130 albums pending to listen you can find a track from each album in this [playlist](https://open.spotify.com/user/manoloesparta/playlist/1ofx1iXeCqb5gPuEWSanfc?si=gN6ZmmDSQleNc7QLDiTXew). So this little script was made to randomize the way to choose albums to listen :D

It selects randomly 100 albums out of the 130+, and from each selected album, it selects one song randomly, appending all the songs to this other [playlist](https://open.spotify.com/user/manoloesparta/playlist/0iYFyrLsby2E0QBBPs2xWi?si=Yv6aajgYTTyMnEj4jbljWA). This is the playlist I listen daily.

## Requirements
```
git clone https://github.com/manoloesparta/playlist.py
cd playlist.py/
pip install -r requirements.txt
```
## Usage
First you need to create your new Spotify app in [this website](https://developer.spotify.com/dashboard/) in order to get your __Client ID__ and __Client ID Secret__. Then initiate your own __SpotifyUser__ object.
```python
from playlist.spotify import SpotifyUser

username = ' your spotify username '
client_id = ' your client id '
client_secret = ' your client secret id '

spotify_user = SpotifyUser(username, client_id, client_secret)
```
Get the URIs of your playlist from where you are retrieving the albums and songs, and the one you want to append them. ___(In other words your playlist source and playlist goal)___
```python
from playlist.source import Source
from playlist.goal import Goal

playlist_src = ' your playlist source URI '
playlist_goal = ' your playlist goal URI '

source = Source(playlist_src, spotify_user)
goal = Goal(playlist_goal, spotify_user)
```
Just update the playlist goal with your __Source__ object
```python
goal.update(source)
```
## Example
```python
from playlist.spotify import SpotifyUser
from playlist.source import Source
from playlist.goal import Goal

username = 'genericusername'
client_id = '9589a322e8bss2a0bfg6achdaw3cfb02'
client_secret = 'cd0629546544c959ebabcd23fd0239b'
spotify_user = SpotifyUser(username, client_id, client_secret)

playlist_src = 'pq1x1iXehjl5gPuEWS54yc' 
source = Source(playlist_src, spotify_user)

playlist_goal = '45fdyrfrey2E0QBBP8teWi'
goal = Goal(playlist_goal, spotify_user)

goal.update(source)
```
_All this data is invented_
## Docker
In order to build succesfully the docker image and run the src/main.py exactly as it is you need to build it with some enviroment variables. You can build it with this command:
```bash
docker build -t playlist.py \
--build-arg user='manoloesparta' \
--build-arg c_id='8589a322e8b142a0bf76ac9da43cfb92' \
--build-arg c_secret='cd0629c79f544c959ebbbbb23fd0239b' \
--build-arg p_src='1ofx1iXeCqb5gPuEWSanfc' \
--build-arg p_goal='0iYFyrLsby2E0QBBPs2xWi' .
```
For running the docker image:
```bash
docker run --rm -v $(pwd):/usr/src/ -it playlist.py bash
```
## License
This project is licensed under the MIT License
