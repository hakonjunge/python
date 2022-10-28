class Filmer:
    def __init__(self, tittel, utgivelsesår, score):
        self.tittel = tittel
        self.utgivelsesår = utgivelsesår
        self.score = score

Filmer_1 = Filmer("Inception", "2010", 8.8)
print(f"{Filmer_1.tittel} was released in {Filmer_1.utgivelsesår} and currently has a score of {Filmer_1.score}")


Filmer_2 = Filmer("The Martian", "2015", 8.0)
print(f"{Filmer_2.tittel} was released in {Filmer_2.utgivelsesår} and currently has a score of {Filmer_2.score}")


Filmer_3 = Filmer("Joker", "2019", 8.4)
print(f"{Filmer_3.tittel} was released in {Filmer_3.utgivelsesår} and currently has a score of {Filmer_3.score}")


class Filmer:
    def __init__(self, tittel, utgivelsesår, score):
        self.tittel = tittel
        self.utgivelsesår = utgivelsesår
        self.score = score

    def info(self):
        return f"{self.tittel} was released in {self.utgivelsesår} and currently has a score of {self.score}"

Film_1 = Filmer("Inception", "2010", 8.0)
print(Film_1.info())

Film_2 = Filmer("The Martian", "2015", 8.0)
print(Film_2.info())

Film_3 = Filmer("Joker", "2019", 8.4)
print(Film_3.info())