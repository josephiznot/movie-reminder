# movie-reminder
Movie Reminder is a Python script that adds all upcoming movies from Rotten Tomatoes to your Google Calendar. It is meant to be an automation script that is ran monthly at the beginning of the month and populate your Google Calendar with movie events for that month.

### Getting Started
* Install Latest Version of Python. If you do not have Python on your machine, install the latest [version](https://www.python.org/downloads/).
* Enable Google Calendar's API. To get started with connecting to Google Calendar's API, follow Google Calendar's [quickstart-guide](https://developers.google.com/calendar/quickstart/python).

### Install Dependencies Using a Virtual Environment
Afterwards, install all required packages. Its recommended to use a virtual environment when installing Python packages. A virtual environment is an isolated environment for Python projects. Each Python project would have its own dependencies regardless of the dependencies other Projects will have. I use [Pipenv](https://pipenv.readthedocs.io/en/latest/.

### Customize Calendar Colors
You can customize the color of your Calendar events as well. All you need to do is to add a 'colorId' key to the body of the the request and assign the event any color ID between 1 - 11. 

1. colorId: 1
  Background: #a4bdfc
  Foreground: #1d1d1d
2. colorId: 2
  Background: #7ae7bf
  Foreground: #1d1d1d
3. colorId: 3
  Background: #dbadff
  Foreground: #1d1d1d
4. colorId: 4
  Background: #ff887c
  Foreground: #1d1d1d
5. colorId: 5
  Background: #fbd75b
  Foreground: #1d1d1d
6. colorId: 6
  Background: #ffb878
  Foreground: #1d1d1d
7. colorId: 7
  Background: #46d6db
  Foreground: #1d1d1d
8. colorId: 8
  Background: #e1e1e1
  Foreground: #1d1d1d
9. colorId: 9
  Background: #5484ed
  Foreground: #1d1d1d
10. colorId: 10
  Background: #51b749
  Foreground: #1d1d1d
11. colorId: 11
  Background: #dc2127
  Foreground: #1d1d1d

Reference to event [colors](https://developers.google.com/calendar/v3/reference/colors/get).
