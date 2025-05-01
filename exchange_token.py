import requests
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

CLIENT_ID = os.getenv("SPOTIPY_CLIENT_ID")
CLIENT_SECRET = os.getenv("SPOTIPY_CLIENT_SECRET")
REDIRECT_URI = "http://127.0.0.1:8080/callback"  # Same as used in authentication

AUTH_CODE = os.getenv("AUTH_CODE")
# Spotify Token URL
TOKEN_URL = "https://accounts.spotify.com/api/token"

# Request body
payload = {
    "grant_type": "authorization_code",
    "code": AUTH_CODE,
    "redirect_uri": REDIRECT_URI,
    "client_id": CLIENT_ID,
    "client_secret": CLIENT_SECRET,
}

# Make the request
response = requests.post(TOKEN_URL, data=payload)

# Print the response
print(response.json())  # This will contain the access_token and refresh_token
