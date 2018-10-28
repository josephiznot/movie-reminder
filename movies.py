import os
import time
import re
import add_event
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--disable-extensions')   
rotten_tomatoes_url = 'https://www.rottentomatoes.com/browse/in-theaters?minTomato=60&maxTomato=100&minPopcorn=60&maxPopcorn=100&genres=1;2;4;5;6;8;9;10;11;13;18;14&sortBy=popularity'
driver = webdriver.Chrome(executable_path=os.path.abspath("chromedriver"),   options=chrome_options) 
movies = []
class Movie:
  def __init__(self, title, rating, release_date):
    self.title = title
    self.rotten_tomatoes = re.findall('\d{2}',rating)[0]
    self.audience = re.findall('\d{2}',rating)[1]
    self.release_date = ' '.join(release_date.split()[2:4])

def scrape_movies():
  driver.get(rotten_tomatoes_url)
  movies_list = driver.find_elements_by_class_name('movie_info')
  for movie in movies_list:
    title, rating, release_date = movie.text.split('\n')
    movies.append(Movie(title, rating, release_date))
  driver.close()
  return movies[0]