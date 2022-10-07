movies = [
    {"name": "Inception", "year": 2010, "rating": 8.7},
    {"name": "Inside Out", "year": 2015, "rating": 8.1},
    {"name": "Con Air", "year": 1997, "rating": 6.9}
]
for titles in movies:
    print(f"Tittel: {titles['name']} -Utgivelseår: {titles['year']} - IMDB-rating: {titles['rating']}")

while True:
    ny_film = str(input("\nNy film? "))
    if ny_film == "ja":
        try:
            name = str(input("Hva er tittelen på filmen? "))
            year = int(input("Hvilket år kom filmen ut? "))
            rating = float(input("Hva er ratingen på IMDB? "))
            movies.append({"name": name, "year": year, "rating": rating})
        except ValueError:
            rating = 5.0
            movies.append({"rating": rating})
    else:
        break

print()
for titles in movies:
    print(f"{titles['name']} - {titles['year']} has a rating of {titles['rating']}")

