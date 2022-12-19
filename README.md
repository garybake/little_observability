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
