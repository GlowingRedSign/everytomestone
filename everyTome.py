import tweepy
import time
import random
from secret import CONSUMER_TOKEN, CONSUMER_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET
from endings import endings


auth = tweepy.OAuthHandler(CONSUMER_TOKEN, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

api = tweepy.API(auth)

wordlist = "corncobProgress.txt"

with open(wordlist, 'r') as words:
    lines = words.readlines()
    words.close()

for line in lines:

    line = line.capitalize()
    line = line.strip()
    baseWord = line
    
    
    matched = 0
    for choice in endings:
        endingLength = len(choice)
        endingLength = endingLength * -1
        strending = line[endingLength:]
        if choice == strending:
            matched = 1
    if matched == 0:
        ending = random.choice(endings)
        line = line + ending
    
    postString = "Allagan Tomestone of " + line
    api.update_status(postString)
    print baseWord
    time.sleep(900)
    
