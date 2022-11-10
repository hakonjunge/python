from datetime import datetime
from datetime import date

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

NEW_CAR_REGISTRATION_FEE = 8745
RENT_CAR_PERCENTAGE = 0.4
RENT_NEW_CAR__FEE = 1000


# Oppgave 3.1
def print_car_information(car):
    if car['new'] == True:
        newold = "New"
    else:
        newold = "Used"

    print(f"Brand: {car['brand']}\nModel: {car['model']}\n"
          f"Price: {car['price']},-\nManufactured: {car['year']}-{car['month']}\nCondition: {newold}")
    return newold


# Oppgave 3.2
def create_car(car_register, name, brand, model, price, year, month, new, km):
    car = {}
    car.update({name : {"brand": brand, "model": model, "price": price, "year": year, "month": month, "new": new,"km": km}})
    print(car)
    car_register.update(car)


# Oppgave 3.3
def get_car_age(car):
    today = date.today()
    year = today.year
    car_year = year-car['year']
    return car_year

# Oppgave 3.4
def rent_car_monthly_price(car):
    monthly_base_price = (car['price']*0.4)/12
    monthly_price = round(monthly_base_price, 2)
    if car['new'] == True:
        monthly_price += 1000
    return monthly_price

# Oppgave 3.5
def next_eu_control(car):
    return datetime((lambda y:(y+1)
    if(y%2!=car["year"]%2)
    else((y)
         if(date.today().month<car["month"])
         else(y+2)))(date.today().year),car["month"],1)



# Oppgave 3.6
def calculate_total_price(car):
    car_price = 0
    if car['new'] == True:
        car_price += car['price'] + 10783
    elif 0 <= get_car_age(car) <= 3:
        car_price += car['price'] + 6681
    elif 4 <= get_car_age(car) <= 11:
        car_price += car['price'] + 4034
    elif 12 <= get_car_age(car) <= 29:
        car_price += car['price'] + 1729
    else:
        car_price += car['price'] + 0
    return car_price

class Car:
    def __init__(self, name, brand, model, price, year, month, new, km):
        self.name = name
        self.brand = brand
        self.model = model
        self.price = price
        self.year = year
        self.month = month
        self.new = new
        self.km = km

    def print_car_information(self):
        pass

    def get_car_age(self):
        pass

    def rent_car_monthly_price(self):
        pass

    def next_eu_control(self):
        pass

    def calculate_total_price(self):
        pass

car = Car("porsche911", "Porsche","911 Carrera", 450_000, 1984, 5, False, 298_000)
car.print_car_information()
