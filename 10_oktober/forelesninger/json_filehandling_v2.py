import json_module


game = {"name": "Trackmania Nations Forever", "genre": "Racing", "max players": 64}

filename = "text_files/game2.json"

json_module.write_json(game, filename)

dict_from_file = json_module.load_json(filename)
print(dict_from_file)
print(dict_from_file["name"] + " is a " + dict_from_file["genre"] + " game.")
