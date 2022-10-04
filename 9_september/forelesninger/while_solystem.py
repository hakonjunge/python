import random
i=1
guess = random.randrange(1, 101)
secret_number = random.randrange(1, 10)

while guess != 69:
    print(f"The guess was {guess}")
    guess = random.randrange(1, 101)
    i+=1

print(f"\nAfter {i} tries you finally guessed the right number that was {guess}")
