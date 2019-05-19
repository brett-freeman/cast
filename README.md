# Bongcast.com - #420 @ irc.p2p-network.net
Source code for bongcast.com, the website of #420@irc.p2p-network.net.
Maintained by Brett.

Currently being re-written in python3.

## Install ##
Create a virtualenv and install dependencies found in requirements.txt

Within a python shell in the context of the app:
```
import db, create_app from app  
db.create_all(app=create_app())  
```
From root folder: 
```
flask run
```
