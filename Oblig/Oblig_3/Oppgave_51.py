movies = [
    {"name": "Inception", "year": 2010, "rating": 8.7},
    {"name": "Inside Out", "year": 2015, "rating": 8.1},
    {"name": "Con Air", "year": 1997, "rating": 6.9}
]


def nyFilm(leksikon, name, year, rating=5.0):
    leksikon.append({"name": name, "year": year, "rating": rating})


nyFilm(movies, "The Dark Knight", 2008, 9.0)
nyFilm(movies, "Pulp Fiction", 1994, 8.8)
nyFilm(movies, "The Shawshank Redemption", 1994, 9.3)

nyFilm(movies, "Interstellar", 2014)
print(movies)
