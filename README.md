# everytomestone
A twitter bot that posts "Allagan Tomestone of [word + random ending]" for every word in some list. You can replace that text with any string you'd like to adapt the bot for.

Requires Python 2.x and the Tweepy library. Install Tweepy from: https://github.com/tweepy/tweepy

<h3>Deployment</h3>
Set up a Twitter app and obtain a consumer token, consumer secret, access token, and access token secret for that app. Enter these values in secret.py as the string values for the appropriate variables.
Change the value of "wordlist" to the filepath of the word list file you will use. Make sure that the file is read/write accessible. EveryTome will delete words from the file as it uses them, so be sure to back up your wordlist with a different filename.

Make sure that the shebang line at the top of everyTome.py matches the location of your python installation.

You can edit endings.py to add or remove any desired endings. One is chosen from the list at random and appended to the word it is chosen for without any modification. If the word already ends with any of the endings in endings.py, everyTome.py skips adding an ending.

Execute the script with the following command:
python everyTome.py

One execution of the script will post one word and remove it from the wordlist file.

You can use a crontab task to automatically run the script with the desired frequency.
