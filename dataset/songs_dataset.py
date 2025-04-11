import pandas as pd

# Create a dataset with 15 songs
data = {
    "title": [
        "Shape of You", "Blinding Lights", "Rolling in the Deep", "Someone Like You", "Levitating",
        "Believer", "Closer", "Memories", "Bad Guy", "Senorita",
        "Perfect", "Sunflower", "Dance Monkey", "Uptown Funk", "Havana"
    ],
    "artist": [
        "Ed Sheeran", "The Weeknd", "Adele", "Adele", "Dua Lipa",
        "Imagine Dragons", "The Chainsmokers", "Maroon 5", "Billie Eilish", "Shawn Mendes & Camila Cabello",
        "Ed Sheeran", "Post Malone", "Tones and I", "Mark Ronson & Bruno Mars", "Camila Cabello"
    ],
    "genre": [
        "Pop", "R&B", "Soul", "Soul", "Pop",
        "Rock", "Pop", "Pop", "Electropop", "Latin Pop",
        "Pop", "Hip-Hop", "Electropop", "Funk", "Latin Pop"
    ],
    "bpm": [
        96, 171, 105, 67, 103,
        125, 95, 90, 135, 117,
        63, 90, 98, 115, 105
    ],
    "lyrics": [
        "The club isn't the best place to find...", "I said, ooh, I'm blinded by the lights...", 
        "There's a fire starting in my heart...", "Nevermind, I'll find someone like you...", "If you wanna run away with me...",
        "First things first, I'ma say all the words...", "So baby, pull me closer in the backseat...", 
        "Here's to the ones that we got...", "White shirt now red, my bloody nose...", "I love it when you call me señorita...",
        "I found a love for me...", "Needless to say, I keep her in check...", "They say, oh my God, I see the way you shine...",
        "This hit, that ice cold, Michelle Pfeiffer...", "Havana, ooh na-na..."
    ]
}

# Convert to DataFrame
df = pd.DataFrame(data)

# Save to CSV
df.to_csv("songs_dataset.csv", index=False)

print("✅ Dataset with 15 songs created successfully! File saved as 'songs_dataset.csv'.")
