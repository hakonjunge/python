car_register = {
    "toyotaBZ4X": {
        "brand": "Toyota",
        "model": "Corolla",
        "price": 96_000,
        "year": 2012,
        "month": 8,
        "new": False,
        "km": 163_000
    },
    "pugeot408": {
        "brand": "Pugeot",
        "model": "408",
        "price": 330_000,
        "year": 2019,
        "month": 1,
        "new": False,
        "km": 40_000
    },
    "audiRS3": {
        "brand": "Audi",
        "model": "RS3",
        "price": 473_000,
        "year": 2022,
        "month": 2,
        "new": True,
        "km": 0
    },
}

# Oppgave 3.1
def print_car_information(car):
    if car['new'] == True:
        newold = "New"
    else:
        newold = "Used"

    print(f"Brand: {car['brand']}\nModel: {car['model']}\n"
          f"Price: {car['price']},-\nManufactured: {car['year']}-{car['month']}\nCondition: {newold}")
    return newold

print_car_information(car_register["pugeot408"])