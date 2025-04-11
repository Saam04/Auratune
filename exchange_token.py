import requests
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

CLIENT_ID = os.getenv("SPOTIPY_CLIENT_ID")
CLIENT_SECRET = os.getenv("SPOTIPY_CLIENT_SECRET")
REDIRECT_URI = "http://127.0.0.1:8080/callback"  # Same as used in authentication

# 🔹 Paste the AUTH_CODE from the redirect URL here
AUTH_CODE = "AQD3ChWs5lLGxPAlB_KtYd5wNeHZwG5MpuLGxp_oq7-5QxeSTUZFGjxS2WkKsg_mKtN8U9vMMLqpS2WPgntRUjgsbl0l9T6J0-ItRcnB1RSMZ0b06XPJsKtgW_a0oduji1uj93iM_L3xpqDLLmkzPgRSxhOLMKwLwblFOqCPwruKvb7ZSNZ0lbk_wnDtp1ZTJdJ1L4Q"

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
