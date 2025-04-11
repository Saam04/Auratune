import pandas as pd

# List to store song data
songs = []

# Function to add a new song manually
def add_song():
    title = input("Enter Song Title: ")
    artist = input("Enter Artist Name: ")
    genre = input("Enter Genre: ")
    bpm = input("Enter BPM (Beats Per Minute): ")
    lyrics = input("Enter Lyrics (Short version): ")

    songs.append({"title": title, "artist": artist, "genre": genre, "bpm": bpm, "lyrics": lyrics})

# Ask user how many songs they want to add
num_songs = int(input("How many songs do you want to add? "))

for _ in range(num_songs):
    add_song()

# Convert list to DataFrame
df = pd.DataFrame(songs)

# Save to CSV file
df.to_csv("songs_dataset.csv", index=False)

print("✅ Dataset created successfully! File saved as 'songs_dataset.csv'.")
