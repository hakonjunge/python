if True:
    print("Look, the if-statement is True.")
    print("We can add more than one line.")

statement = 2 == 2
if statement:
    print(f"The if-statement rounds because the statement is {statement}.")

if "text" == "TEXT":
    print("The texts are the same.")

print()
i = 1
while True:

    print()
    number = int(input("Skriv et tall da mann"))
    if 0 < number < 65:
        print(f"{number} er større enn 0")
    elif number > 65:
        print(f"{number} er større enn 65")
    else:
        print(f"{number} er ikke innafor ass")
    print(f"forsøk {i}")
    i += 1