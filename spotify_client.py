import os
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from dotenv import load_dotenv

# Load API credentials from .env file
dotenv_path = os.path.join(os.path.dirname(__file__), ".env")
load_dotenv(dotenv_path)

SPOTIPY_CLIENT_ID = os.getenv("923bbee7b8b14310944309935ef5477b")
SPOTIPY_CLIENT_SECRET = os.getenv("0f8579122e3743b7ada7d887226c7edc")
SPOTIPY_REDIRECT_URI = os.getenv("http://127.0.0.1:8080/callback")

# Debugging: Print values to check if they are loading
print(f"🔍 SPOTIPY_CLIENT_ID: {SPOTIPY_CLIENT_ID}")
print(f"🔍 SPOTIPY_CLIENT_SECRET: {SPOTIPY_CLIENT_SECRET}")
print(f"🔍 SPOTIPY_REDIRECT_URI: {SPOTIPY_REDIRECT_URI}")

# Authenticate with Spotify API
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    client_id=SPOTIPY_CLIENT_ID,
    client_secret=SPOTIPY_CLIENT_SECRET,
    redirect_uri=SPOTIPY_REDIRECT_URI,
    scope="user-read-currently-playing"
))

def get_current_song():
    """Fetch the currently playing song from Spotify."""
    current_track = sp.current_playback()
    if current_track and current_track.get("is_playing"):
        song_name = current_track["item"]["name"]
        artist_name = current_track["item"]["artists"][0]["name"]
        return song_name, artist_name
    return None

if __name__ == "__main__":
    song = get_current_song()
    if song:
        print(f"🎵 Now Playing: {song[0]} - {song[1]}")
    else:
        print("No song is currently playing.")
