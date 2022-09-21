planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune", "Pluto"]
planets_gravity = [3.7, 8.7, 9.807, 3.721, 24.79, 19.44, 8.87, 11.15, 0.62]

while True:
    your_weight = float(input("What is your weight in kg on Earth? "))

    if your_weight <= 0:
        print("The weight must be a positive number")
        exit()

    print("\n====PLANETS====")
    for index in range(len(planets)):
        print(f"{index + 1} - {planets[index]}")

    planet_number = int(input("\nPick a planet by typing a number: "))

    if 1 > planet_number > 9:
        print("There are no such planets")
        exit()

    planets_index = planet_number - 1
    # jordvekt / jordtyngdekraft * planettyngdekraft
    planet_weight = your_weight / planets_gravity[2] * planets_gravity[planets_index]
    print(f"Your weight is {round(planet_weight)} kg on {planets[planet_number - 1]}")
    avslutt = str(input("Do you wish to quit? "))
    if avslutt == "yes":
        break
    else:
        continue
