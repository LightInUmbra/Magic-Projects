import requests
import pandas as pd
import Functions.ScryFunctions as sf
import classes.card as cc
import time

# Base URL from where the API is called from
BASE_URL = f'https://api.scryfall.com'

# Headers as required per API documentation
HEADERS = {
    
    'User-Agent': 'GathererOfDataTestApp/1.0',
    'Accept': 'application/json'
    
}

# Searches for exact card, then prints name, set code, and rarity
printings = sf.get_all_printings("Wilhelt, the Rotcleaver")

