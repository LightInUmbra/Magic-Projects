import requests
import pandas as pd
import time as t
import classes.card as cc

# Base URL from where the API is called from
BASE_URL = f'https://api.scryfall.com'

# Headers as required per API documentation
HEADERS = {
    
    'User-Agent': 'GathererOfDataTestApp/1.0',
    'Accept': 'application/json'
    
}


# Searches for cards in scryfall database by name
# Requires query input
def search_cards(query):
    url = f'https://api.scryfall.com/cards/search'
    params = {
        
        "q": query
        
    }
    all_cards = []
    
    while url:
        response = requests.get(url, params=params, headers=HEADERS)
        params = {}
    
        if response.status_code == 200:
            data = response.json()
            all_cards.extend([cc.Card(c) for c in data['data']])
            url = data.get('next_page') if data.get('has_more') else None
        else:
            print(f"Error: {response.status_code} - {response.json().get('details')}")     
            return None
        
        t.sleep(0.1)
        
    return all_cards

# Searches for exact card in database
# Requires exact input
def search_exact_card(card):
    url = f'https://api.scryfall.com/cards/named'
    params = {
        
        "exact": card
        
    }
    response = requests.get(url, params=params, headers=HEADERS)
    
    if response.status_code == 200:
        data = response.json()
        card_pulled = cc.Card(data)
        t.sleep(0.1)
        return card_pulled        
    else:
        t.sleep(0.1)
        print(f"Error: {response.status_code} - {response.json().get('details')}")     
        return None
        
# Grabs how many cards (in numerical form) search_cards found
# Requires list of cards from search_cards
def card_search_count(all_cards):
    return len(all_cards)

# Finds and lists all cards from search_cards with their color identities
# Requires list of cards from search_cards
def list_color_identity(all_cards):
    COLOR_MAP = {
        'W': 'White',
        'U': 'Blue',
        'B': 'Black',
        'R': 'Red',
        'G': 'Green'
        }
    
    for card in all_cards:
        color_names = [COLOR_MAP[color] for color in card.color_identity] if card.color_identity else ['Colorless']
        print(f"{card.name}: {','.join(color_names)}")
    
# Gets prices for all cards in list
# Requires list of cards from search_cards        
def print_card_prices(all_cards, price_type='price_usd'):
    for card in all_cards:
        price = getattr(card, price_type)
        price_display = f"${price:.2f}" if price > 0.0 else "N/A"
        print(f"{card.name}: {price_display}")

# Gets all printings of a single card
# Requires card from search_exact_card
def get_all_printings(card):
    url = f'https://api.scryfall.com/cards/search'
    params = {
        
        "q": f'!"{card}" -is:digital',
        "unique": 'prints',
        "order" : 'usd',
        "dir" : 'asc'
        
    }
    response = requests.get(url, params=params, headers=HEADERS)
    
    if response.status_code == 200:
        data = response.json()
        list_of_prints = []
        
        for chunk in data['data']:
            
            card_pulled = cc.Card(chunk)
            
            price_list = {
                
                'price_nonfoil' : card_pulled.price_usd,
                'price_foil' : card_pulled.price_usd_foil,
                'price_eur' : card_pulled.price_eur,
                'price_tix' : card_pulled.price_tix
                
            }
            
            list_of_prints.append({
                
                'name' : card_pulled.name,
                'set' : card_pulled.set_name,
                'pricing' : price_list
                
            })
    
        print(f"Card Name: {card_pulled.name}\n")
        for printing in list_of_prints:
            price_nonfoil = printing['pricing']['price_nonfoil']
            price_foil    = printing['pricing']['price_foil']
            price_eur     = printing['pricing']['price_eur']
            price_tix     = printing['pricing']['price_tix']
            
            print(f"Set: {printing['set']}")
            print(f"  USD Nonfoil : {'N/A' if price_nonfoil == 0.0 else f'${price_nonfoil:.2f}'}")
            print(f"  USD Foil    : {'N/A' if price_foil == 0.0 else f'${price_foil:.2f}'}")
            print(f"  EUR         : {'N/A' if price_eur == 0.0 else f'${price_eur:.2f}'}")
            print(f"  TIX         : {'N/A' if price_tix == 0.0 else f'{price_tix:.2f}'}")
            print(f"{'─' * 35}")  # separator between printings
        t.sleep(0.1)    

    else:
        t.sleep(0.1)
        print(f"Error: {response.status_code} - {response.json().get('details')}")     
        return None

"""
FIX THIS BEFORE MOVING ON
"""
# Grabs the most expensive printing of cards found in search_cards dictionary
# Requires list of cards from print_card_prices
def most_expensive_printing(all_cards, price_type='price_usd'):
    max_card_price = max(all_cards, key=lambda card: getattr(card, price_type))
    print(f"{max_card_price.name}: ${getattr(max_card_price, price_type)}")