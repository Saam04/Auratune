import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Check values
print("Client ID:", os.getenv("SPOTIFY_CLIENT_ID"))
print("Client Secret:", os.getenv("SPOTIFY_CLIENT_SECRET"))
