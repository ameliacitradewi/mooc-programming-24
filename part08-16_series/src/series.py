# Write your solution here:
class Series:
    def __init__(self, title: str, seasons: int, genres: list):
        self.title = title
        self.seasons = seasons
        self.genres = genres
        self.ratings = []

    def rate(self, rating: int):
        if 0 <= rating <= 5:
            self.ratings.append(rating)
    
    def __str__(self):
        genre_string = ", ".join(self.genres)
        if self.ratings:
            average_rating = sum(self.ratings) / len(self.ratings)
            return (f"{self.title} ({self.seasons} seasons)\n"
                  f"genres: {genre_string}\n"
                  f"{len(self.ratings)} ratings, average {average_rating:.1f} points")
        else:
            return (f"{self.title} ({self.seasons} seasons)\n"
                  f"genres: {genre_string}\n"
                  "no ratings")
    
#Example Usage
dexter = Series("Dexter", 8, ["Crime", "Drama", "Mystery", "Thriller"])
dexter.rate(4)
dexter.rate(5)
dexter.rate(5)
dexter.rate(3)
dexter.rate(0)
print(dexter)