# Write your solution here
def find_movies(database: list, search_term: str):
    search_term_lower = search_term.lower()
    matching_movies = []
    
    for movie in database:
        movie_name_lower = movie["name"].lower()
        if search_term_lower in movie_name_lower:
            matching_movies.append(movie)
  
    return matching_movies