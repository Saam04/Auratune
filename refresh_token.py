import requests
import os
from dotenv import load_dotenv

# Load credentials from .env file
load_dotenv()

CLIENT_ID = os.getenv("SPOTIPY_CLIENT_ID")
CLIENT_SECRET = os.getenv("SPOTIPY_CLIENT_SECRET")
REFRESH_TOKEN = "AQC0YRvHj_-RFWJ1XIjUmbDHAn4cm1IbhCnNbhv9zumHfvKgRpBhczVBMvuLqbDEepuT3FQn0VUL0OiKCD0ltNm3Kyg6VFN6kQiCG572cVnatDa5Y28xhrQc2yLTGAl1zxE"  # Paste your refresh token

TOKEN_URL = "https://accounts.spotify.com/api/token"

# Request to refresh access token
payload = {
    "grant_type": "refresh_token",
    "refresh_token": REFRESH_TOKEN,
    "client_id": CLIENT_ID,
    "client_secret": CLIENT_SECRET
}

response = requests.post(TOKEN_URL, data=payload)
print(response.json())  # New access token
