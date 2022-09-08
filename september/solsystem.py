planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune", "Pluto"]
planets_gravity = [3.7, 8.7, 9.807, 3.721, 24.79, 19.44, 8.87, 11.15, 0.62]

your_weight = float(input("What is your weight in kg on Earth? "))

if your_weight <= 0:
    print("The weight must be a positive number")
    exit()

print("\n====PLANETS====")
print(f"1 - {planets[0]}")
print(f"2 - {planets[1]}")
print(f"3 - {planets[2]}")
print(f"4 - {planets[3]}")
print(f"5 - {planets[4]}")
print(f"6 - {planets[5]}")
print(f"7 - {planets[6]}")
print(f"8 - {planets[7]}")
print(f"9 - {planets[8]}")

planet_number = int(input("\nPick a planet by typing a number (int):"))

if 1 > planet_number > 9:
    print("There are no such planets")
    exit()

planets_index = planet_number-1
#jordvekt / jordtyngdekraft * planettyngdekraft
planet_weight = your_weight/planets_gravity[2]*planets_gravity[planets_index]
print(f"Your weight is {planet_weight} kg on {planets[planet_number-1]}")