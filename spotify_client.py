import requests

def get_user_top_tracks(token):
    url = "https://api.spotify.com/v1/me/top/tracks?limit=5"
    headers = {"Authorization": f"Bearer {token}"}
    response = requests.get(url, headers=headers)
    return response.json()

def get_audio_features(token, track_id):
    url = f"https://api.spotify.com/v1/audio-features/{track_id}"
    headers = {"Authorization": f"Bearer {token}"}
    response = requests.get(url, headers=headers)

    if response.status_code !=200:
        print(f"Failed to fetch the Audio Features of id: {track_id}")
        print("Response", response.json())
        return None
    
    data = response.json()
    if data is None or 'dancibility' not in data:
        print(f'No audio features fetched from {track_id}')
        return None
    return data

def get_track_metadata(token, track_id):
    url = f"https://api.spotify.com/v1/tracks/{track_id}"
    headers = {"Authorization": f"Bearer {token}"}
    response = requests.get(url, headers=headers)
    return response.json()
