import os
import requests
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

CLIENT_ID = os.getenv("SPOTIPY_CLIENT_ID")
CLIENT_SECRET = os.getenv("SPOTIPY_CLIENT_SECRET")
REFRESH_TOKEN = os.getenv("SPOTIPY_REFRESH_TOKEN")
TOKEN_URL = "https://accounts.spotify.com/api/token"

def refresh_access_token():
    """Automatically refresh the access token when expired."""
    if not CLIENT_ID or not CLIENT_SECRET or not REFRESH_TOKEN:
        print("❌ Error: Missing CLIENT_ID, CLIENT_SECRET, or REFRESH_TOKEN")
        return None

    payload = {
        "grant_type": "refresh_token",
        "refresh_token": REFRESH_TOKEN,
        "client_id": CLIENT_ID,
        "client_secret": CLIENT_SECRET
    }

    try:
        response = requests.post(TOKEN_URL, data=payload)
        
        # Print the raw response for debugging
        print("Response Status Code:", response.status_code)
        print("Raw Response:", response.text)

        token_data = response.json()
        
        if "access_token" in token_data:
            new_access_token = token_data["access_token"]
            print("✅ New Access Token:", new_access_token)
            return new_access_token
        else:
            print("❌ Error refreshing token:", token_data)
            return None
    except requests.exceptions.RequestException as e:
        print(f"❌ Request Error: {e}")
        return None
