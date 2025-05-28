from auth import get_auth_url, get_token
from spotify_client import get_user_top_tracks, get_audio_features, get_track_metadata

def main():
    print("STEP 1: Visit this URL and authorize Auratune:")
    print(get_auth_url())

    code = input("\nSTEP 2: Paste the authorization code here: ").strip()
    tokens = get_token(code)

    access_token = tokens["access_token"]
    refresh_token = tokens["refresh_token"]

    print("\n Access token acquired. Fetching top tracks...")

    top_tracks = get_user_top_tracks(access_token)
    for idx, track in enumerate(top_tracks["items"]):
        print(f"\n🎵 Track #{idx + 1}")
        print(f"Name     : {track['name']}")
        print(f"Artist   : {track['artists'][0]['name']}")
        print(f"ID       : {track['id']}")
        
        features = get_audio_features(access_token, track["id"])

        if features and isinstance(features, dict) and 'dancibility' in features:
            print(f"Danceability: {features['danceability']}")
            print(f"Energy      : {features.get('energy','N/A')}")
        else:
            print("Data Features not available or invalid for this track")
            print(f'track ID: {track["id"]}')

if __name__ == "__main__":
    main()
