import tmdbsimple as tmdb
tmdb.API_KEY = '83cbec0139273280b9a3f8ebc9e35ca9'
tmdb.REQUESTS_TIMEOUT = 5

movies = tmdb.Movies()
popular_movies = movies.popular(page=1)["results"]
for movie_data in popular_movies:
    title = movie_data.get("title")
    release_date = movie_data.get("release_date")
    vote_average = int(movie_data.get("vote_average") * 10)
    poster_path = "https://image.tmdb.org/t/p/w300" + movie_data.get("poster_path")
    print(title, release_date, vote_average, poster_path)