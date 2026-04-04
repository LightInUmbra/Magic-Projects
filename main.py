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
card_pulled = sf.search_exact_card("The One Ring")

if card_pulled:
    print(f"Card pulled: {card_pulled.name} | {card_pulled.set} | {card_pulled.rarity}\n")
else:
    print("Card not found.\n")

"""
Gets information on all printings of one card
Output: Card Name: [card name]

Set: Set name
Pricing in each currency/availability
"""
sf.get_all_printings("voja jaws of the conclave")

"""
Searches for cards with Ghalta in card text AND counts how many cards it found
Output: Card name, set code, rarity
Output: Number of cards it found
"""
card_list = sf.search_cards("Ghalta")

if card_list:
    print(f"Cards found: {sf.card_search_count(card_list)}")
else:
    print("No cards found.")

"""
Using card_list, shows card name and card colors/identity
Output: Card Name: Color(s)
"""
print("\nColor Identities:")
sf.list_color_identity(card_list)

"""
gets card prices and displays them for each card in list
Output: Card Name: Price (USD Nonfoil assumed unless specified)
"""
print("\nCard Prices:")
sf.print_card_prices(card_list)