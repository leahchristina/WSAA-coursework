

import requests

SHUFFLE_URL = "https://deckofcardsapi.com/api/deck/new/shuffle/?deck_count=1"


def card_value_num(value):
    mapping = {
        "ACE": 1,
        "JACK": 11,
        "QUEEN": 12,
        "KING": 13,
    }
    return mapping.get(value, int(value))


# Shuffle a new deck
shuffle_response = requests.get(SHUFFLE_URL)
shuffle_data = shuffle_response.json()

deck_id = shuffle_data["deck_id"]

# Draw 5 cards
DRAW_URL = f"https://deckofcardsapi.com/api/deck/{deck_id}/draw/?count=5"
draw_response = requests.get(DRAW_URL)
draw_data = draw_response.json()

cards = draw_data["cards"]

print("Your 5 cards:\n")
for card in cards:
    print(f"{card['value']} of {card['suit']}")