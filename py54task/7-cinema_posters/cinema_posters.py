class MovieRegistry:
    _titles = set()
    
    @classmethod
    def add_title(cls, title: str):
        if title in cls._titles:
            return False
        cls._titles.add(title)
        return True
    
    @classmethod
    def remove_title(cls, title: str):
        cls._titles.discard(title)
    

class Movie:
    def __init__(self, title: str):
        if not MovieRegistry.add_title(title):
            raise ValueError(f"Movie with title {title} already exists")
        self.title = title

        
class Cinema:
    def __init__(self):
        self.poster: list[Movie] = []
    
    def add_movie(self, movie: Movie):
        self.poster.append(movie)
    
    def remove_movie(self, title: str):
        for movie in self.poster:
            if movie.title == title:
                self.poster.remove(movie)


def test():
    # movies 
    movie1 = Movie("Interstellar")
    movie2 = Movie("Fight Club")
    movie3 = Movie("Forrest Gump")
    movie4 = Movie("Leon")
    
    try:
        movie5 = Movie("Fight Club")
    except ValueError:
        ... # duplicate
    else:
        raise AssertionError("duplicate created")
    
    
    # Cinema theatres
    zamok_cinema = Cinema()
    silverscr_cinema = Cinema()
    
    # Add Posters
    zamok_cinema.add_movie(movie1)
    zamok_cinema.add_movie(movie2)
    zamok_cinema.add_movie(movie3)
    silverscr_cinema.add_movie(movie2)
    silverscr_cinema.add_movie(movie3)
    silverscr_cinema.add_movie(movie4)
    
    # Remove posters
    silverscr_cinema.remove_movie(movie4.title)
    zamok_cinema.remove_movie(movie1.title)
    
    # prints
    # print(MovieRegistry._titles)
    # print(zamok_cinema.poster)
    # print(silverscr_cinema.poster)

    
if __name__ == "__main__":
    test()
