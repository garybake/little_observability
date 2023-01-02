# Little Observability
Somewhere to ingest data and pipe out to a tiny screen

This is just for me to learn a few things so there won't be much quality.  
Uses poetry for package management.

Components
==========

## Hub
Ingests data from modules, stores data, output to modules.  
Backup db to NAS regulary  
Should run on rpi zero

## Input modules
 - Energy usage - from energy supplier feed
 - Share price - price of shares/bitcoin
 - Weather - current temperature, weather

## Output modules
 - Web server - something to share graphs and charts
 - Pandas server - serve data as pandas dataframes?
 - ESP8266 screen - I have some tiny screens and esp devices laying around.

Setup
=====

## .env
Fill in the entries in a .env file in the root folder

    # Hub settings
    HUB_VERSION='0.1'
    HUB_API_VERSION='v1'
    DB_PATH='logs.db'

    # Energy settings
    ELECTRICITY_BASE_URL=https://api.octopus.energy/v1/
    ELECTRICITY_API_KEY=***
    ELECTRICITY_MPAN=***
    ELECTRICITY_SERIAL=***
    ELECTRICITY_API_URL=http://localhost:8000/api/v1/energy/electricity_consumption



Links
=====
TODO: Tidy this up  

To run the hub app

    cd hub  
    uvicorn main:app --reload
test url  

    curl localhost:8000/version 

 http://127.0.0.1:8000/docs


Electricity Module
==================
Fill in the .env with the ELECTRICITY variables.
Variables can be found at https://octopus.energy/dashboard/developer/  

Docs for the api can be found at  
https://developer.octopus.energy/docs/api/

    usage: energy.py [-h] [-r ROWS]

    options:
    -h, --help            show this help message and exit
    -r ROWS, --rows ROWS  Number of rows to request

Shares Module
=============
Tracks share prices  
grab an api key at https://twelvedata.com/  

.env file

    SHARES_BASE_URL=https://api.twelvedata.com/time_series
    SHARES_TWELVEDATA_KEY=***
    SHARES_WATCH_LIST="APPL,BRK.B"
