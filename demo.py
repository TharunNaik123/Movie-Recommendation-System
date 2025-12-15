from recommender import MovieRecommender


# Initialize recommender
recommender = MovieRecommender('data/movies.csv')


# Test movie
movie_name = "Toy Story (1995)"


print(f"Recommendations for '{movie_name}':")
recommendations = recommender.recommend(movie_name)


for movie in recommendations:
print(movie)


### examples 
Recommendations for 'Toy Story (1995)':
['Bug's Life, A (1998)', 'Monsters, Inc. (2001)', 'Antz (1998)', 'Toy Story 2 (1999)', 'Shrek (2001)']
