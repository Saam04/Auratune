import requests
from spotify_api import refresh_access_token  # Import auto-refresh function

# Get the latest access token automatically
ACCESS_TOKEN = refresh_access_token()

if ACCESS_TOKEN:
    headers = {"Authorization": f"Bearer {ACCESS_TOKEN}"}
    
    # Fetch User Profile
    response = requests.get("https://api.spotify.com/v1/me", headers=headers)

    # Print debugging info
    print("Status Code:", response.status_code)
    print("Response Content:", response.text)  # Print raw response

    # Handle errors
    if response.status_code == 200:
        try:
            print(response.json())  # Only parse JSON if response is valid
        except requests.exceptions.JSONDecodeError:
            print("❌ Error: Invalid JSON response from Spotify")
    else:
        print(f"❌ Error: Received {response.status_code} from Spotify API")
else:
    print("❌ Failed to get access token.")
