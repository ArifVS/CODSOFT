# Sample data
import pandas as pd
movies = pd.DataFrame({
    'Movie': ['Movie1', 'Movie2', 'Movie3', 'Movie4', 'Movie5'],
    'Action': [1, 1, 0, 1, 0],
    'Comedy': [0, 1, 1, 0, 1],
    'Drama': [0, 0, 1, 1, 1],
})

# User preferences
user_preferences = {'Action': 5, 'Comedy': 3, 'Drama': 4}

# Calculate similarity
def content_based_recommendations(user_prefs, movies):
    movie_scores = []
    for index, row in movies.iterrows():
        score = sum([user_prefs[feature] * row[feature] for feature in user_prefs])
        movie_scores.append((row['Movie'], score))
    movie_scores.sort(key=lambda x: x[1], reverse=True)
    return movie_scores

print(content_based_recommendations(user_preferences, movies))
