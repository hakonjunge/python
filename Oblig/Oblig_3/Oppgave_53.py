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
print()


def filmSammendrag(movies):
    for leksikon in movies:
        print(f"{leksikon['name']} - {leksikon['year']}"
              f" has a rating of {leksikon['rating']}")


filmSammendrag(movies)
print()


def gjennomsnittRating(movies):
    if len(movies) == 0:
        return 0
    num = 0
    for leksikon in movies:
        num += leksikon['rating']
    return num / len(movies)


print(f"Gjennomsnittsratingen på alle filmene er {gjennomsnittRating(movies)}")
print()


def filmerFraGittÅrstall(movies, year):
    nyListe = []
    for leksikon in movies:
        if leksikon['year'] >= year:
            nyListe.append(leksikon)
    return nyListe


filmSammendrag(filmerFraGittÅrstall(movies, 2010))

print("5.3")
print()
print("5.3 A")


def åpneFilogSkriv(movies, filename):
    with open('text_files/movies.txt', 'w') as filename:
        for leksikon in movies:
            filename.write(f"{leksikon['name']} - {leksikon['year']} has a rating of {leksikon['rating']}\n")


åpneFilogSkriv(movies, "text_files/movies.txt")
print()
print("5.3 B")


def åpneFilogLesFil(movies, filename):
    terminal_lista = []
    with open('text_files/movies.txt', 'r') as filename:
        for leksikon in filename:
            # Remove linebreak which is the last character of the string
            aktuell_film = leksikon[:-1]
            # Add item to the list
            terminal_lista.append(aktuell_film)
    for titler in terminal_lista:
        print(titler)


åpneFilogLesFil(movies, "text_files/movies.txt")
