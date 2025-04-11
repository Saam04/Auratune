import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import os
from spotipy.oauth2 import SpotifyOAuth

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    scope="user-library-read playlist-read-private",
    redirect_uri="http://127.0.0.1:8080/callback"
))

client_id = os.getenv("SPOTIFY_CLIENT_ID")
client_secret = os.getenv("SPOTIFY_CLIENT_SECRET")

auth_manager = SpotifyClientCredentials(client_id, client_secret)
sp = spotipy.Spotify(auth_manager=auth_manager)

try:
    sp.search(q="Beatles", type="artist")  # Test query
    print("Spotify API authentication successful!")
except Exception as e:
    print("Error:", e)
