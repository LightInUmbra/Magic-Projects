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
    url = 'https://api.scryfall.com/cards/search'
    
    # TO DO: add order and dir as optional params with sensible defaults. Also include in
    # params dict
    
    params = {
        'q': f'!"{card}" -is:digital',
        'unique': 'prints',
        'order': 'usd',
        'dir': 'asc'
    }
    response = requests.get(url, params=params, headers=HEADERS)
    
    if response.status_code == 200:
        data = response.json()
        list_of_prints = []
        
        for chunk in data['data']:
            card_pulled = cc.Card(chunk)
            list_of_prints.append(card_pulled)
        
        t.sleep(0.1)
        return list_of_prints

    else:
        t.sleep(0.1)
        print(f"Error: {response.status_code} - {response.json().get('details')}")
        return None
    
# Prints all printings of card found from get_all_printings
def print_all_printings(all_cards):
    if all_cards:
        print(f"Card Name: {all_cards[0].name}\n")
        for card in all_cards:
            print(f"Set: {card.set_name}")
            print(f"  Collector #     : {card.collector_number}")
            print(f"  USD Nonfoil     : {'N/A' if card.price_usd == 0.0 else f'${card.price_usd:.2f}'}")
            print(f"  USD Foil        : {'N/A' if card.price_usd_foil == 0.0 else f'${card.price_usd_foil:.2f}'}")
            print(f"  EUR             : {'N/A' if card.price_eur == 0.0 else f'${card.price_eur:.2f}'}")
            print(f"  TIX             : {'N/A' if card.price_tix == 0.0 else f'{card.price_tix:.2f}'}")
            print(f"{'─' * 35}")

# Grabs the most expensive printing of a specific card found in get_all_printings dictionary
# Requires list of cards from get_all_printings
def most_expensive_printing(all_printings, price_type='price_usd'):
    max_card = max(all_printings, key=lambda card: getattr(card, price_type))
    
    print(f"Most Expensive Printing of {max_card.name}")
    print(f"{'─' * 35}")
    print(f"  Set             : {max_card.set_name}")
    print(f"  Collector #     : {max_card.collector_number}")
    print(f"  Artist          : {max_card.artist}")
    print(f"  Rarity          : {max_card.rarity.capitalize()}")
    print(f"  Released        : {max_card.released_at}")
    print(f"  Finishes        : {', '.join(max_card.finishes)}")
    print(f"{'─' * 35}")
    print(f"  USD Nonfoil     : {'N/A' if max_card.price_usd == 0.0 else f'${max_card.price_usd:.2f}'}")
    print(f"  USD Foil        : {'N/A' if max_card.price_usd_foil == 0.0 else f'${max_card.price_usd_foil:.2f}'}")
    print(f"  EUR             : {'N/A' if max_card.price_eur == 0.0 else f'${max_card.price_eur:.2f}'}")
    print(f"  TIX             : {'N/A' if max_card.price_tix == 0.0 else f'{max_card.price_tix:.2f}'}")
    print(f"{'─' * 35}")

# Grabs the cheapest printing of a specific card found in get_all_printings dictionary
# Requires list of cards from get_all_printings
def cheapest_printing(all_printings, price_type='price_usd'):
    min_card = min(all_printings, key=lambda card: getattr(card, price_type))
    
    print(f"Cheapest Printing of {min_card.name}")
    print(f"{'─' * 35}")
    print(f"  Set             : {min_card.set_name}")
    print(f"  Collector #     : {min_card.collector_number}")
    print(f"  Artist          : {min_card.artist}")
    print(f"  Rarity          : {min_card.rarity.capitalize()}")
    print(f"  Released        : {min_card.released_at}")
    print(f"  Finishes        : {', '.join(min_card.finishes)}")
    print(f"{'─' * 35}")
    print(f"  USD Nonfoil     : {'N/A' if min_card.price_usd == 0.0 else f'${min_card.price_usd:.2f}'}")
    print(f"  USD Foil        : {'N/A' if min_card.price_usd_foil == 0.0 else f'${min_card.price_usd_foil:.2f}'}")
    print(f"  EUR             : {'N/A' if min_card.price_eur == 0.0 else f'${min_card.price_eur:.2f}'}")
    print(f"  TIX             : {'N/A' if min_card.price_tix == 0.0 else f'{min_card.price_tix:.2f}'}")
    print(f"{'─' * 35}")
    
# Sorts printings of a specific card found in get_all_printings by price
# Requires list of cards from get_all_printings
def printings_by_price(all_cards, price_type='price_usd'):
    
    # Filter out cards with no price for the chosen type
    available = [card for card in all_cards if getattr(card, price_type) > 0.0]
    
    # Sorting the filtered list
    sorting_cards = sorted(available, key=lambda card: getattr(card, price_type))
    
    return sorting_cards

# Searches for a random card in database
# Requires exact input
def get_random_card(query=None):
    url = f'https://api.scryfall.com/cards/random'
    params = {'q': query} if query else {}
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
    
# Searches for cards in scryfall database by name
# Requires query input
def search_cards_by_set(set_code, rarity=None, color=None, card_type=None):
    
    # Ensures set_code is lowercase
    set_code = set_code.lower()
    
    # Builds query, starting with the set
    query = f"e:{set_code}"
    
    # For optional filters
    if rarity:
        query += f" r:{rarity.lower()}"
    if color:
        query += f" c:{color.lower()}"
    if card_type:
        query += f" t:{card_type.lower()}"
    
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