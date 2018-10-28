from add_event import add_event
import movies

if __name__ == '__main__':
  movie = movies.scrape_movies()
  add_event(movie)
