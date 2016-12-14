# everytomestone
A twitter bot that posts "Allagan Tomestone of [word]" for every word in some list.

Requires Python 2.x.

<h3>Deployment</h3>
Set up a Twitter app and obtain a consumer token, consumer secret, access token, and access token secret for that app. Enter these values in secret.py as the string values for the appropriate variables.
Change the value of "wordlist" to the filename of the word list file you will use. Make sure that the file is read/write accessible.

You can edit endings.py to add or remove any desired endings. One is chosen from the list at random and appended to the word it is chosen for without any modification.

Execute the script with the following command:
python everyTome.py

One execution of the script will post one word and remove it from the wordlist file.

You can use a crontab task to automatically run the script with the desired frequency.
