import random

words = ["word", "capybara", "dog", "macbook", "norway", "python"]

secret_word = words[random.randrange(0, len(words))]
secret_word_list = list(secret_word)
antall_liv = int(input("Hvor mange liv skal du ha: "))

hint = ["_"] * len(secret_word)
feil_bokstav = []

while "_" in hint:
    print(f"Hint: {''.join(hint)}")
    gjett = str.lower(input("Skriv inn en bokstav: "))

    if gjett in secret_word:
        for index in range(len(secret_word_list)):
            if gjett == secret_word_list[index]:
                hint[index] = gjett

    if gjett not in secret_word:
        feil_bokstav.append(gjett)
        antall_liv -= 1
        print(feil_bokstav)
        if antall_liv == 0:
            print("du tapte")
            break

    print(f"Du har {antall_liv} liv igjen")
    print()

print()
print(f"Gratulerer du klarte å gjette ordet {''.join(hint)}")