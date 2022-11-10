class Movie:
    def __init__(self, title, year, rating):
        self.title = title
        self.year = year
        self.rating = rating

pulpfiction = Movie("Pulp Fiction", 1994, 8.8)
print(f"{pulpfiction.title} was released in {pulpfiction.year}")