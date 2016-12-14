import tweepy
import time
import random
import os
from secret import CONSUMER_TOKEN, CONSUMER_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET
from endings import endings

def generateName(baseWord):

    name = baseWord.capitalize()
    name = baseWord.strip()
    
    matched = 0
    for choice in endings:
        endingLength = len(choice)
        endingLength = endingLength * -1
        strending = name[endingLength:]
        if choice == strending:
            matched = 1
        
    if matched == 0:
        ending = random.choice(endings)
        name = name + ending

    print baseWord
    return name

def postTomestone(word):

    postString = "Allagan Tomestone of " + word
    api.update_status(postString)
    print word
    
auth = tweepy.OAuthHandler(CONSUMER_TOKEN, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

api = tweepy.API(auth)

wordlist = "/home/ec2-user/everyTome/mergedProgressOneWord.txt"
with open(wordlist, 'r') as words:
    contents = words.readlines()
    baseWord = contents[0]

newWord = ""


try:
    name = generateName(baseWord)
    postTomestone(name)
    
except:
    newWord = contents[1]
    postTomestone(generateName(newWord))
    
with open(wordlist, 'w') as words:
    for thing in contents:
        if thing != baseWord and thing != newWord:
            words.write(thing)
