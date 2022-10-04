while True:
    try:
        number = int(input("Skriv eit tal "))
        number2 = int(input("Skriv eit tal te "))
        result = number/number2
        print(f"{number} / {number2} = {result}")
    except ValueError:
        print("Vennligst skriv eit tal ")
    except ZeroDivisionError:
        print("ikke del med null")
    except KeyboardInterrupt:
        print()
        continue
    else:
        print("everything is awesome")