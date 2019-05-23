# Bongcast.com - #420 @ irc.p2p-network.net
Source code for bongcast.com, the website of #420@irc.p2p-network.net.
Maintained by Brett.

Currently being re-written in python3. Sometimes there is a live version at https://dev.bongcast.com/ to play with.

## Install ##
Create a virtualenv and install dependencies found in requirements.txt

## Database Initialization / Migration ##
```
# Initialize the database for the first time
flask db init 

# Stage changes to models
flask db migrate -m "Message"

# Apply staged changes to models
flask db upgrade 
```

## Run the app in development mode ##
```
flask run
```
