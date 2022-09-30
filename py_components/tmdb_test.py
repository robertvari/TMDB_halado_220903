import tmdbsimple as tmdb
from datetime import datetime
# import locale
# locale.setlocale(locale.LC_TIME, "hu_HU")

tmdb.API_KEY = '83cbec0139273280b9a3f8ebc9e35ca9'
tmdb.REQUESTS_TIMEOUT = 5

movies = tmdb.Movies()
popular_movies = movies.popular(page=1)["results"]
for movie_data in popular_movies:
    title = movie_data.get("title")
    datetime_obj = datetime.strptime(movie_data.get("release_date"), "%Y-%m-%d")
    release_date = datetime_obj.strftime("%Y %b %d")

    vote_average = int(movie_data.get("vote_average") * 10)
    poster_path = "https://image.tmdb.org/t/p/w300" + movie_data.get("poster_path")
    print(title, release_date)