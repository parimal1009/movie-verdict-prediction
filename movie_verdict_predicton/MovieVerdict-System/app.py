import streamlit as st
import pickle
import base64

st.title("Movie Verdict Prediction")
# Load the GIF file
with open("giphy.gif", "rb") as f:
    gif_data = f.read()
    # Encode the binary data as base64
    gif_base64 = base64.b64encode(gif_data).decode()

# Display the GIF
st.image(gif_data, caption='Your GIF Caption', use_column_width=True)

# Streamlit app content

# Add more Streamlit components here

# Load the pre-trained model
with open("Random Forest_model.pkl", 'rb') as file:
    model = pickle.load(file)

# Function to make predictions
def predict_verdict(popularity, trend_popularity, actors_popularity, twitter_score, genre):
    # Encode genre
    genre_mapping = {
        "Action": 1, "Adventure": 2, "Animation": 3, "Biography": 4, "Comedy": 5,
        "Drama": 6, "Fantasy": 7, "History": 8, "Horror": 9, "Music": 10,
        "Musical": 11, "Mystery": 12, "Romance": 13, "Sci-Fi": 14, "Short": 15,
        "Sport": 16, "Thriller": 17, "War": 18, "Western": 19
    }
    genre_encoded = genre_mapping.get(genre, 0)  # Default to 0 if genre not found

    # Make prediction
    prediction = model.predict([[popularity, trend_popularity, actors_popularity, twitter_score, genre_encoded]])
    return prediction[0]

# Sidebar inputs
st.sidebar.header("Enter Movie Details")
popularity = st.sidebar.text_input("TMDB Popularity", value="0.0")
trend_popularity = st.sidebar.text_input("Mean Google Trend Popularity", value="0.0")
actors_popularity = st.sidebar.text_input("Actors Popularity", value="0.0")
twitter_score = st.sidebar.text_input("Youtube Score", value="0.0")
genre = st.sidebar.selectbox("Movie Genre", ["Action", "Adventure", "Animation", "Biography", "Comedy", "Drama", "Fantasy", "History", "Horror", "Music", "Musical", "Mystery", "Romance", "Sci-Fi", "Short", "Sport", "Thriller", "War", "Western"])

# Convert input values to float
popularity = float(popularity)
trend_popularity = float(trend_popularity)
actors_popularity = float(actors_popularity)
twitter_score = float(twitter_score)

# Predict button
if st.sidebar.button("Predict"):
    verdict = predict_verdict(popularity, trend_popularity, actors_popularity, twitter_score, genre)
    if verdict == 0:
        st.title("FLOP, Need to Work on Positive Marketing.")
    else:
        st.title("HIT, Sit Back and Enjoy. People are Liking it")
