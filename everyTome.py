import tweepy
import time
import random
from secret import CONSUMER_TOKEN, CONSUMER_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET
from endings import endings


auth = tweepy.OAuthHandler(CONSUMER_TOKEN, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

api = tweepy.API(auth)
wordlist = 'filename.txt'

with open(wordlist, 'r') as words:
    lines = words.readlines()
    words.close()

for line in lines:

    baseWord = line
    line = line.capitalize()
    line = line.strip()
    ending = random.choice(endings)
    line = line + ending
    postString = "Allagan Tomestone of " + line
    api.update_status(postString)
    print baseWord
        
    time.sleep(900)
    