from math import log

def woof_woof_bark():
    print("Woof Woof Bark")


def dog_to_human_age(dog_age):
    human_equivalent_age = 16 * log(dog_age) + 31
    woof_woof_bark()
    return round(human_equivalent_age)

print(dog_to_human_age(20))
print(dog_to_human_age(8))
print(dog_to_human_age.__doc__)
print(log.__doc__)
