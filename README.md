# Bongcast.com - #420 @ irc.p2p-network.net
Source code for bongcast.com, the website of #420@irc.p2p-network.net.
Maintained by Brett.

Currently being re-written in python3.

## Install ##
Create a virtualenv and install dependencies found in requirements.txt

## Database Initialization / Migration ##
```
flask db init #Initialize database
flask db migrate -m "Message" #Stage model changes
flask db upgrade #Apply model changes staged in migrate
```

## Run the app in development mode ##
```
flask run
```
