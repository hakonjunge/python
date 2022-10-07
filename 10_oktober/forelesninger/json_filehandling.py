import json

game = {"name": "New Super Mario Bros DS", "genre": "Adventure", "max players": 2}

try:
    with open("text_files/game.json", "w") as file:
        json.dump(game, file, indent=4, )
except FileNotFoundError:
    print("wasted")

try:
    with open("text_files/game.json") as file:
        dict_from_file = json.load(file)
except FileNotFoundError:
    print("File not found")

except json.decoder.JSONDecodeError:
    print("FEIL")

else:
    for key, value in dict_from_file.items():
        print(f"{key} - {value}")
