from datetime import datetime
from dateutil.relativedelta import relativedelta
from googleapiclient.discovery import build
from httplib2 import Http
from oauth2client import file, client, tools

# If modifying these scopes, delete the file token.json.
SCOPES = 'https://www.googleapis.com/auth/calendar'

def add_event(title, release_date, rating = None):
    """Add event to Google Calendar."""
    store = file.Storage('token.json')
    creds = store.get()
    if not creds or creds.invalid:
        flow = client.flow_from_clientsecrets('credentials.json', SCOPES)
        creds = tools.run_flow(flow, store)
    service = build('calendar', 'v3', http=creds.authorize(Http()))
    # Call the Calendar API
    event = service.events().insert(calendarId='primary', body={
    'summary': '%s Movie' % title,
    'description': rating,
    'backgroundColor': 'Tomato',
    'foregroundColor': 'Tomato',
    'colorId': 11,
    'start': {
      'dateTime': (release_date + relativedelta(hours=16)).isoformat() + 'Z',
      'timeZone': 'America/Chicago',
    },
    'end': {
      'dateTime': (release_date + relativedelta(hours=17)).isoformat() + 'Z',
      'timeZone': 'America/Chicago',
    },
    'recurrence': [
      'RRULE:FREQ=DAILY;COUNT=1'
    ],
    'reminders': {
      'useDefault': 'useDefault',
      'overrides': [
        {'method': 'email', 'minutes': 24 * 60},
        {'method': 'popup', 'minutes': 10}
      ],
    },
    }).execute()