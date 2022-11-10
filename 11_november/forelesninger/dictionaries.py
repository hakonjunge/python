'''def printFilmInfo(filmer, film):
    printfilm = filmer[film]
    print(film)
    print(printfilm)

printFilmInfo(filmer, "The Dark Knight")
print()
for film in filmer:
    print(film)'''


def printFilmInfo(films_dict):
    lange_filmer = {}
    for name, info in films_dict.items():
        if info["lengde"] > 120:
            lange_filmer[name] = info
    return lange_filmer

filmer = {
    "The Lord of the Rings: The Fellowship of the Ring": {"utgivelsesår": 2001, "IMDB-rating": 8.8, "lengde": 178},
    "The Lord of the Rings: The Two Towers": {"utgivelsesår": 2002, "IMDB-rating": 8.8, "lengde": 179},
    "The Lord of the Rings: The Return of the King": {"utgivelsesår": 2003, "IMDB-rating": 9.0, "lengde": 201},
    "The Shawshank Redemption": {"utgivelsesår": 1994, "IMDB-rating": 9.3, "lengde": 144},
    "The Dark Knight": {"utgivelsesår": 2008, "IMDB-rating": 9.0, "lengde": 152}
}
printFilmInfo(filmer)