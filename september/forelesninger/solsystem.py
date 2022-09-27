planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune", "Pluto"]
planets_gravity = [3.7, 8.7, 9.807, 3.721, 24.79, 19.44, 8.87, 11.15, 0.62]


def get_user_weight():
    user_weight = float(input("What is your weight in kg on Earth? "))

    if user_weight <= 0:
        print("The weight must be a positive number")
        exit()

    return user_weight


def print_planet_choises(planet_list):
    print("\n====PLANETS====")
    for index in range(len(planet_list)):
        print(f"{index + 1} - {planet_list[index]}")


def get_planet_choise_index():
    planet_number = int(input("\nPick a planet by typing a number: "))

    if planet_number < 1 or planet_number > number_of_planets:
        print("The number of planets is out of the accepted range")
        exit()
    return planet_number - 1

def calculate_and_display_planet_weight(user_weight, gravity_list, planet_list, index):
    planet_weight = user_weight / gravity_list[2] * gravity_list[index]

    print(f"\nYour weight is {round(planet_weight)} kg on {planets[index - 1]}")

while True:
    your_weight = get_user_weight()

    print_planet_choises(planets)

    get_planet_choise_index(len(planets))

    calculate_and_display_planet_weight(your_weight, planets_gravity, planets, planets_index)

    avslutt = str(input("Do you wish to quit? "))
    if avslutt == "yes":
        break
    else:
        continue
