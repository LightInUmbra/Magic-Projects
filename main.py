import sys
import Functions.ScryFunctions as sf

def show_menu():
    print(f""
          "\n===== Magic: The Gathering Toolkit ====="
          "\n\n1. Search cards"
          "\n2. Search exact card"
          "\n3. Search cards by set"
          "\n4. Print all printings"
          "\n5. Get most expensive printing"
          "\n6. Get cheapest printing"
          "\n7. Get a random card"
          "\n8. Quit"
          "")
    
def main():
    while True:
        show_menu()
        choice = int(input("Choose an option from above: "))
        
        if choice == 1:
            query = input("\nWhat are you searching for? ")
            results = sf.search_cards(query)
            
            if results is None:
                print(f"Sorry, but your search for {query} yielded no results or the API is having some issues. Please try again later.")
            else:
                for result in results:
                    print(f"\nCard name: {result.name}"
                          f"\nRarity: {result.rarity}"
                          f"\nCard set: {result.set_name}"
                          f"\nCard set code: {result.set}")
                print(f"\n\nCards found: {sf.card_search_count(results)}")
        elif choice == 2:
            query = input("\nWhat card are you searching for specifically? ")
            result = sf.search_exact_card(query)
            
            if result is None:
                print(f"Sorry, but your search for {query} yielded no results or the API is having some issues. Please try again later.")
            else:
                print(f"\nCard name: {result.name}"
                    f"\nRarity: {result.rarity}"
                    f"\nCard set: {result.set_name}"
                    f"\nCard set code: {result.set}")
        elif choice == 3:
            set_query = input("\nWhat set are you searching from? ")
            rarity_query = input("\nSpecific rarity? Common (C), Uncommon (U), Rare (R), Mythic (M))/leave blank to skip: ")
            color_query = input("\nSpecific color(s)? If so, type them in without spacing (wubrg). Leave blank to skip: ").lower()
            card_type_query = input("\nSpecific card type? (i.e: creature, instant, 'artifact creature')? Leave blank to skip: ")
            
            if " " in card_type_query:
                card_type_query = f'"{card_type_query}"'
            
            results = sf.search_cards_by_set(set_query, rarity_query, color_query, card_type_query)
            
            if results is None:
                print(f"Sorry, but your search for {set_query} yielded no results or the API is having some issues. Please try again later.")
            else:
                for result in results:
                    color_display = ', '.join(result.colors) if result.colors else 'Colorless'
                    print(f"\nCard name: {result.name}"
                            f"\nRarity: {result.rarity}"
                            f"\nColor Identity: {color_display}"
                            f"\nCard set: {result.set_name}"
                            f"\nCard set code: {result.set}")
                print(f"\n\nCards found: {sf.card_search_count(results)}")
        elif choice == 4:
            query = input("\nWhich card do you need all printings for? ")
            cards = sf.get_all_printings(query)
            
            if cards is None:
                print(f"Sorry, but your search for {query} yielded no results or the API is having some issues. Please try again later.")
            else:
                sf.print_all_printings(cards)
        elif choice == 5:
            query = input("\nWhich card do you need the most expensive printing for? ")
            cards = sf.get_all_printings(query)
            
            if cards is None:
                print(f"Sorry, but your search for {query} yielded no results or the API is having some issues. Please try again later.")
            else:
                card_needed = sf.get_most_expensive_printing(cards)
                sf.print_most_expensive_printing(card_needed)
        elif choice == 6:
            query = input("\nWhich card do you need the cheapest printing for? ")
            cards = sf.get_all_printings(query)
            
            if cards is None:
                print(f"Sorry, but your search for {query} yielded no results or the API is having some issues. Please try again later.")
            else:
                card_needed = sf.get_cheapest_printing(cards)
                sf.print_cheapest_printing(card_needed)
        elif choice == 7:
            card = sf.get_random_card()
            sf.print_random_card(card)
        elif choice == 8:
            sys.exit()
      
if __name__ == "__main__":
    main()