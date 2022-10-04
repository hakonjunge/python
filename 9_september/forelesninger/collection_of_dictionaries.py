'''"Uncharted 4", "Grand Turismo Sport", "Trackmania Nations Forever", "New Super Mario Bros DS",
         "Lego Star Wars the Complete Saga", "Wii Sports", "Cities Skylines"'''
games = {
    "Trackmania Nations Forever": {"genre": "Racing", "developer": "Nadeo", "platform": "PC"},
    "Spiderman": {"genre": "Action", "developer": "Sony", "platform": "Playstation & PC"}
}
print(games)
games["New Super Mario Bros DS"] = {"genre": "Adventure", "developer": "Multiplayer", "platform": "Nintendo DS"}
print()
print(games["Trackmania Nations Forever"]["platform"])
print()
for key, value in games.items():
    print(f"{key} - {value['genre']}")
