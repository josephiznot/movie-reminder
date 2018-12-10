import movies

from add_event import add_event
from datetime import datetime

if __name__ == '__main__':
  count = 0
  for movie in movies.scrape_movies():
    if datetime.now().strftime('%b') in movie.release_date:
      count = count + 1
      add_event(movie.title,
                datetime.strptime('%s %d'%(movie.release_date, datetime.now().year), '%b %d %Y'),
                movie.__dict__.get('rating'))
      print('Addeded %s' % movie.title)
  print('Succesfully added %d movies!'%count)
