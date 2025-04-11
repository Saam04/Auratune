import os
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.preprocessing import MinMaxScaler
import joblib
import numpy as np

# Ensure necessary folders exist
os.makedirs("models", exist_ok=True)
os.makedirs("dataset", exist_ok=True)

# Load dataset
df = pd.read_csv("dataset/songs_dataset.csv")

# Handle missing values
df = df.dropna()

# Convert lyrics into numerical vectors using TF-IDF
tfidf = TfidfVectorizer(stop_words='english')
tfidf_matrix = tfidf.fit_transform(df['lyrics'])

# Convert sparse matrix to proper format
df['lyrics_tfidf'] = list(tfidf_matrix.toarray())

# Normalize BPM values
scaler = MinMaxScaler()
df[['bpm']] = scaler.fit_transform(df[['bpm']])

# Convert lists into strings (so they save correctly in CSV)
df['lyrics_tfidf'] = df['lyrics_tfidf'].apply(lambda x: ','.join(map(str, x)))

# Save preprocessed data and models
df.to_csv("dataset/preprocessed_songs.csv", index=False)
joblib.dump(tfidf, "models/tfidf_vectorizer.pkl")

print("✅ Preprocessing completed! Data saved as 'preprocessed_songs.csv'.")
