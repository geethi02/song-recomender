
from recommender.song_recommender import SongRecommender

def main():
    recommender = SongRecommender("data/songs.csv")
    print("Recommendations for genre='Pop', mood='Energetic':")
    print(recommender.recommend(genre='Pop', mood='Energetic'))

if __name__ == "__main__":
    main()
