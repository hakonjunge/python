'''"Uncharted 4", "Grand Turismo Sport", "Trackmania Nations Forever", "New Super Mario Bros DS",
         "Lego Star Wars the Complete Saga", "Wii Sports", "Cities Skylines"'''
games = {
    "name": "Trackmania Nations Forever",
     "genre": "Racing", 
     "developer": "Nadeo", 
     "platform": "PC"
}

print(games)


print(games['name'])
games['players'] = 'Multiplayer'
print()
print(f"{games.get('name')} is a {games.get('players')}-{games.get('genre')}-game and is developed by"
      f" {games.get('developer')} for "
      f"{games.get('platform')} ")
for key, value in games.items():
    print(f"{key} - {value}")
