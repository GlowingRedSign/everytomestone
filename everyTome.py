#!/usr/bin/python

import tweepy
import random
from secret import CONSUMER_TOKEN, CONSUMER_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET
from endings import endings

'''Given a single-word string, generateName will
check to see whether it ends with any of the
strings in endings.py. If there is a match,
it will not modify the string. If the string ends
in 's' which is a common plural form, there will
be no modification. Otherwise, it chooses an ending
from endings.py and appends it to the string.'''

def generateName(baseWord):

    name = baseWord.capitalize()
    name = baseWord.strip()

    #Flag for match found
    matched = 0
    '''Each entry in endings.py
    has length n. Check the last n characters
    of the base word to see if they match
    the ending. If they do, set the matched flag.'''
    for choice in endings:
        endingLength = len(choice)
        endingLength = endingLength * -1
        strending = name[endingLength:]
        if choice == strending:
            matched = 1
            
    '''Adding 's' as an ending tended to
    cause duplicate posts, so just use the post
    as-is if it ends with 's'.'''
    if name.endswith("s"):
            matched = 1
            
    '''If there were no matches, choose
    an ending at random and append it.'''
    if matched == 0:
        ending = random.choice(endings)
        name = name + ending

    #Shows the wordlist progress in the console
    print baseWord
    
    return name

'''Given a single-word string that has been passed
through generateName(), postTomestone will concatenate
the post text and call the tweepy update_status function
to actually post the Twitter status update.

It will take the form of "Allagan Tomestone of " + string.'''

def postTomestone(word):

    postString = "Allagan Tomestone of " + word
    api.update_status(postString)
    print word

# Twitter authentication    
auth = tweepy.OAuthHandler(CONSUMER_TOKEN, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

api = tweepy.API(auth)


'''Change the value of wordlist to the filename of the wordlist
you want to use'''
wordlist = "XXXX"

'''Open the wordlist and read its
contents as a list of strings, with
each string as one line.'''
with open(wordlist, 'r') as words:
    contents = words.readlines()
    baseWord = contents[0]
    
'''Will be assigned the next word in the list if
posting the first word fails. Declaring it here
ensures it has scope beyond the except
block.'''
newWord = ""

'''Attempt to post the full string text to Twitter.
If the post fails, likely due to a duplicate post
error, repeat the process with the next word in the
wordlist.'''


try:
    name = generateName(baseWord)
    postTomestone(name)
    
except:
    '''Attempt to post the next word
    from the wordlist so the execution can
    end with a successful post.'''
    
    newWord = contents[1]
    postTomestone(generateName(newWord))


''' Update the wordlist by re-writing all of the read
words to the wordlist file, except the first word and
possibly the the second word (if the attempt to post
the first word resulted in an error and the except
block posted the second word.)'''

with open(wordlist, 'w') as words:
    for thing in contents:
        if thing != baseWord and thing != newWord:
            words.write(thing)
