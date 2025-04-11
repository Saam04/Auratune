from dotenv import load_dotenv
import os

load_dotenv()

my_variable = os.getenv("SPOTIFY_CLIENT_ID")

if my_variable:
    print(f"SPOTIFY_CLIENT_ID {my_variable}")
else:
    print("SPOTIFY_CLIENT_ID is not set.")