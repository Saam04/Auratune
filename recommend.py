import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
import joblib
import numpy as np

# Load preprocessed dataset
df = pd.read_csv("dataset/preprocessed_songs.csv")

# Convert 'lyrics_tfidf' back to lists (split by commas)
df['lyrics_tfidf'] = df['lyrics_tfidf'].apply(lambda x: np.array(x.split(','), dtype=float))

# Load TF-IDF model
tfidf = joblib.load("models/tfidf_vectorizer.pkl")

# Recommendation function
def get_recommendations(song_title, top_n=5):
    # Convert input title to lowercase
    song_title = song_title.lower()

    # Convert all dataset titles to lowercase for comparison
    df['title_lower'] = df['title'].str.lower()

    if song_title not in df['title_lower'].values:
        return "❌ Song not found in dataset!"

    # Find the song index (based on lowercase title)
    song_idx = df[df['title_lower'] == song_title].index[0]

    # Compute similarity between input song and all others
    similarity_scores = cosine_similarity(
        [df.loc[song_idx, 'lyrics_tfidf']], list(df['lyrics_tfidf'])
    )

    # Add similarity scores to DataFrame
    df['similarity'] = similarity_scores[0]

    # Sort by similarity and get top N recommendations
    recommendations = df.sort_values(by='similarity', ascending=False)[1:top_n+1]
    print('you might also like these songs ')
    return recommendations[['title', 'artist', 'genre']]

# Test recommendation
if __name__ == "__main__":
    song_name = input("Enter a song name: ")
    print(get_recommendations(song_name))

