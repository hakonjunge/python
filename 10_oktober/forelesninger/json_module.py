import json


def write_json(dictionary, filename):
    try:
        with open(filename, "w") as file:
            json.dump(dictionary, file, indent=4, )
    except FileNotFoundError:
        print("wasted")


def load_json(filename):
    try:
        with open(filename) as file:
            dict_from_file = json.load(file)
    except FileNotFoundError:
        print("File not found")

    except json.decoder.JSONDecodeError:
        print("FEIL")

    else:
        return dict_from_file
