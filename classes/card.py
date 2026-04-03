class Card:
    
    def __init__(self, data: dict):
        
        # ── Core Identity ──────────────────────────────
        self.id              = data.get('id')               # Scryfall UUID
        self.oracle_id       = data.get('oracle_id')        # Shared across all printings
        self.name            = data.get('name')
        self.layout          = data.get('layout')           # 'normal', 'transform', 'split', etc.
        self.lang            = data.get('lang')             # 'en', 'fr', 'jp', etc.

        # ── Gameplay ───────────────────────────────────
        self.mana_cost       = data.get('mana_cost')        # '{2}{R}{R}'
        self.cmc             = data.get('cmc')              # Float e.g. 4.0
        self.type_line       = data.get('type_line')        # 'Legendary Creature — Dragon'
        self.oracle_text     = data.get('oracle_text')      # Rules text
        self.colors          = data.get('colors', [])       # ['R', 'G']
        self.color_identity  = data.get('color_identity', [])
        self.keywords        = data.get('keywords', [])     # ['Flying', 'Haste']
        self.power           = data.get('power')            # String — can be '*'
        self.toughness       = data.get('toughness')        # String — can be '*'
        self.loyalty         = data.get('loyalty')          # Planeswalkers only
        self.defense         = data.get('defense')          # Battle cards only

        # ── Print / Edition Info ───────────────────────
        self.set             = str(data.get('set')).upper() # 'dmu'
        self.set_name        = data.get('set_name')         # 'Dominaria United'
        self.set_type        = data.get('set_type')         # 'expansion', 'core', etc.
        self.collector_number = data.get('collector_number')
        self.rarity          = data.get('rarity')           # 'common', 'uncommon', 'rare', 'mythic'
        self.artist          = data.get('artist')
        self.released_at     = data.get('released_at')      # 'YYYY-MM-DD'
        self.reprint         = data.get('reprint')          # Boolean
        self.digital         = data.get('digital')          # Boolean (Arena/MTGO only)
        self.booster         = data.get('booster')          # Boolean
        self.frame           = data.get('frame')            # '2015', 'future', etc.
        self.frame_effects   = data.get('frame_effects', []) # ['legendary', 'extendedart']
        self.finishes        = data.get('finishes', [])     # ['nonfoil', 'foil', 'etched']
        self.promo           = data.get('promo')            # Boolean
        self.variation       = data.get('variation')        # Boolean

        # ── Prices ─────────────────────────────────────
        prices               = data.get('prices', {})
        self.price_usd       = float(prices.get('usd') if prices.get('usd') is not None else 0.0)            # String or None
        self.price_usd_foil  = float(prices.get('usd_foil') if prices.get('usd_foil') is not None else 0.0)
        self.price_eur       = float(prices.get('eur') if prices.get('eur') is not None else 0.0)
        self.price_tix       = float(prices.get('tix') if prices.get('tix') is not None else 0.0)            # MTGO tickets

        # ── Legalities ─────────────────────────────────
        legalities           = data.get('legalities', {})
        self.legal_standard  = legalities.get('standard')   # 'legal', 'not_legal', 'banned', 'restricted'
        self.legal_pioneer   = legalities.get('pioneer')
        self.legal_modern    = legalities.get('modern')
        self.legal_legacy    = legalities.get('legacy')
        self.legal_vintage   = legalities.get('vintage')
        self.legal_commander = legalities.get('commander')
        self.legal_pauper    = legalities.get('pauper')

        # ── Images ─────────────────────────────────────
        image_uris           = data.get('image_uris', {})
        self.image_small     = image_uris.get('small')
        self.image_normal    = image_uris.get('normal')
        self.image_large     = image_uris.get('large')
        self.image_art_crop  = image_uris.get('art_crop')

        # ── Multi-face Cards ───────────────────────────
        self.card_faces      = data.get('card_faces', [])   # List of face dicts
        self.all_parts       = data.get('all_parts', [])    # Related cards (tokens, etc.)

    def __repr__(self):
        return f"Card('{self.name}', {self.set}, {self.rarity})"