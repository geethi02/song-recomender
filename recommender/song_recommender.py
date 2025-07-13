
import pandas as pd

class SongRecommender:
    def __init__(self, csv_path):
        self.data = pd.read_csv(csv_path)

    def recommend(self, genre=None, artist=None, mood=None):
        result = self.data
        if genre:
            result = result[result['genre'].str.lower() == genre.lower()]
        if artist:
            result = result[result['artist'].str.lower() == artist.lower()]
        if mood:
            result = result[result['mood'].str.lower() == mood.lower()]
        return result['song'].tolist()
