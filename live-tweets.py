# Import the necessary package to process data in JSON format
try:
    import json
except ImportError:
    import simplejson as json

from twitter import Api
from datetime import datetime, timedelta

consumer_key = ''
consumer_secreet = ''
access_token = ''
access_token_screet = ''

api = Api(consumer_key, consumer_secreet, access_token, access_token_screet)

KEYWORD = ['MarsLanding']
word = input("Enter the keyword: ")
KEYWORD.append(word)
LANGUAGES = ['en']

#realtime data
def get_real_time_data():
    print("Hang on acquiring data from twitter...")
    for line in api.GetStreamFilter(track=KEYWORD, languages=LANGUAGES):
        if 'text' in line:
            print(line['user']['name'] + ':-' + line['text'])
            print('Time: ' + line['created_at'])
            print(' ')
            print(' ')
    #print(json.dumps(line))

#history data
def get_history_data():
    print("Hang on acquiring data from twitter...")
    for line in api.GetStreamSample():
        if 'text' in line:
            if word in line['text']:
                print(line)
                print(' ')
                print(line['user']['name'] + ':-' + line['text'])
                created_at = datetime.strptime(
                    line['created_at'], '%a %b %d %X %z %Y')
                print('created ' + created_at)
                last_five_minute = datetime.utcnow() - timedelta(minutes=5)
                print('last ' + last_five_minute)
                current_time = datetime.utcnow()
                print('now ' + current_time)

                if last_five_minute > created_at and created_at < current_time:

                    print(line['user']['name'] + ':-' + line['text'])
                    print('Time: ' + line['created_at'])
                    print(' ')
                    print(' ')


get_history_data()

