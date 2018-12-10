import os
import time
import re
import add_event
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--disable-extensions')   
in_theaters = 'https://www.rottentomatoes.com/browse/in-theaters?minTomato=60&maxTomato=100&minPopcorn=60&maxPopcorn=100&genres=1;2;4;5;6;8;9;10;11;13;18;14&sortBy=popularity'
upcoming = 'https://www.rottentomatoes.com/browse/upcoming'
driver = webdriver.Chrome(executable_path=os.path.abspath("chromedriver"),   options=chrome_options) 
movies = []

class Movie:
  def __init__(self, title, release_date, rating = None):
    self.title = title
    self.release_date = ' '.join(release_date.split()[2:4])
    self.rating = rating

def scrape_movies():
  """Initiates web driver and retrieves movies from Rotten Tomatoes.
  
  Returns:
    A Tuple of movies with month and day in string format.
    Eg ('Jan 1', 'Feb 2', etc)
    """
  driver.get(upcoming)
  movies_list = driver.find_elements_by_class_name('movie_info')
  for movie in movies_list:
    try:
      title, rating, release_date = movie.text.split('\n')
      movies.append(Movie(title, release_date, rating))
    except ValueError:
      title, release_date = movie.text.split('\n')
      movies.append(Movie(title, release_date))
  driver.close()
  return movies