import streamlit as st
import random

st.title("🎵 Song Mood Generator")

# Input
lyrics = st.text_area("Enter lyrics, a topic, or a phrase:")

# Mood selection
mood = st.radio("Select a mood:", ["Happy", "Sad", "Dramatic", "Energetic"])

# Generate suggestion
if st.button("Generate"):
    emojis = {
        "Happy": "😄🎶🌞",
        "Sad": "😢🎵🌧️",
        "Dramatic": "🎭🎶🔥",
        "Energetic": "⚡🎵💃"
    }
    chords = {
        "Happy": ["C", "G", "Am", "F"],
        "Sad": ["Am", "Em", "F", "Dm"],
        "Dramatic": ["Dm", "G", "C", "Bb"],
        "Energetic": ["E", "B", "C#m", "A"]
    }

    chosen_chords = random.sample(chords[mood], k=3)
    st.subheader("🎶 Suggested chords:")
    st.write(" - ".join(chosen_chords))
    st.subheader("Mood Emojis:")
    st.write(emojis[mood])
    st.subheader("Fun description:")
    st.write(f"Sing '{lyrics}' in a {mood.lower()} style with these chords!")
