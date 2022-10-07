class Animal:
    def __init__(self, name, species, age):
        self.name = name
        self.species = species
        self.age = age

    def getDescription(self):
        return f"{self.name} is a {self.species}"


dog = Animal("Balder", "Dog", 3)
print(dog.getDescription())
