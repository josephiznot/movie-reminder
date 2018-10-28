from __future__ import print_function
import datetime
from googleapiclient.discovery import build
from httplib2 import Http
from oauth2client import file, client, tools

# If modifying these scopes, delete the file token.json.
SCOPES = 'https://www.googleapis.com/auth/calendar'

def add_event(movie):
    """Add event to Google Calendar."""
    store = file.Storage('token.json')
    creds = store.get()
    if not creds or creds.invalid:
        flow = client.flow_from_clientsecrets('credentials.json', SCOPES)
        creds = tools.run_flow(flow, store)
    service = build('calendar', 'v3', http=creds.authorize(Http()))

    # Call the Calendar API
    now = datetime.datetime.utcnow().isoformat() + 'Z' # 'Z' indicates UTC time
    event = service.events().insert(calendarId='primary', body={
  'summary': '%s Movie' % movie.title,
  'description': 'Tomatometer: %s, Audience: %s' % (movie.rotten_tomatoes, movie.audience),
  'start': {
    'dateTime': now,
    'timeZone': 'America/Chicago',
  },
  'end': {
    'dateTime': '2018-10-25T17:00:00-07:00',
    'timeZone': 'America/Chicago',
  },
  'recurrence': [
    'RRULE:FREQ=DAILY;COUNT=2'
  ],
  'reminders': {
    'useDefault': False,
    'overrides': [
      {'method': 'email', 'minutes': 24 * 60},
      {'method': 'popup', 'minutes': 10},
    ],
  },
}).execute()