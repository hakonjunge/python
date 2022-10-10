# 5.1 A:
# Har opprettet en liste med tre dictionaries
movies = [
    {"name": "Inception", "year": 2010, "rating": 8.7},
    {"name": "Inside Out", "year": 2015, "rating": 8.1},
    {"name": "Con Air", "year": 1997, "rating": 6.9}
]


# 5.1 B
# Definerte en funksjon som tar fire parametre.
# Den ene parameteret har en default-verdi på 5.0 for senere deloppgave

def nyFilm(leksikon, name, year, rating=5.0):
    leksikon.append({"name": name, "year": year, "rating": rating})


# La til tre filmer for å teste om det fungerer
nyFilm(movies, "The Dark Knight", 2008, 9.0)
nyFilm(movies, "Pulp Fiction", 1994, 8.8)
nyFilm(movies, "The Shawshank Redemption", 1994, 9.3)

# 5.1 C
# La til en film uten rating for å se om default-ratingen fungerte
nyFilm(movies, "Interstellar", 2014)
print(movies)
print()


# 5.2 A
def filmSammendrag(movies):
    # lager en for-løkke for å skrive ut filmene nedover i en fin liste
    for leksikon in movies:
        print(f"{leksikon['name']} - {leksikon['year']}"
              f" has a rating of {leksikon['rating']}")


filmSammendrag(movies)
print()


# 5.2 B
def gjennomsnittRating(movies):
    if len(movies) == 0:
        return 0
    # Jeg har en if-statement for hvis len av movies er 0 siden å dele på null det er bare tull
    num = 0
    for leksikon in movies:
        num += leksikon['rating']
    return num / len(movies)
    # legger ratingene inn i en liste (num)
    # og deler totalsummen av listen på antall elementer i movies-lista vedhjelp av len


print(f"Gjennomsnittsratingen på alle filmene er {gjennomsnittRating(movies)}")
print()


# 5.2 C
def filmerFraGittÅrstall(movies, year):
    nyListe = []
    # oppretter en tom liste som skal ha filmene fra gitt årstall
    for leksikon in movies:
        # kjører en loop med en if statement som tester om filmen er fra gitt årstall eller ikke
        if leksikon['year'] >= year:
            nyListe.append(leksikon)
    return nyListe
    # returnerer listen


filmSammendrag(filmerFraGittÅrstall(movies, 2010))
# forteller hva årstall jeg vil bruke,
# og bruker sammendrag-funksjonen til å skrive ut listen på en estetisk pleasing måte


print("5.3")
print()
print("5.3 A")


# 5.3 A
def åpneFilogSkriv(movies, filename):
    with open(filename, 'w') as filename:
        # Oppretter en fil med navn movies.txt og bruker 'w' for å fortelle at jeg skal skrive i filen
        for leksikon in movies:
            # prøvde å bruke sammendrag-funksjonen i denne loopen men den hadde noen andre elementer
            # så jeg bare lagde en ny
            filename.write(f"{leksikon['name']} - {leksikon['year']} has a rating of {leksikon['rating']}\n")


åpneFilogSkriv(movies, "text_files/movies.txt")
# Her forteller jeg funksjonen hvilken fil vi skal bruke
print()
print("5.3 B")


# 5.3 B
def åpneFilogLesFil(movies, filename):
    with open(filename, 'r') as films:
        for description in films:
            print(description[:-1])



åpneFilogLesFil(movies, "text_files/movies.txt")
# Her forteller jeg funksjonen hvilken fil vi skal bruke
