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

# Searches for exact card, then prints
card_pulled = sf.search_exact_card("The One Ring")
print(card_pulled)

# Gets information on all printings of one card
all_printings = sf.get_all_printings("voja jaws of the conclave")
print(all_printings)

# Searches for cards with One Ring in card text
card_list = sf.search_cards("Ghalta")
card_count = sf.card_search_count(card_list)
print(card_list)
print(f"\n", card_count)

# Using card_list, shows card name and card colors/identity
card_list_colors = sf.list_color_identity(card_list)
print(card_list_colors, "\n")

# gets card prices and displays them for each card in list
card_pricing = sf.print_card_prices(card_list, price_type='price_usd')
print(card_pricing, "\n")