# This program deals 5 cards at random & analyses the results

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

# Analyse Hand
values = [card["value"] for card in cards]
suits = [card["suit"] for card in cards]

# Pair / Triple
value_counts = {}
for value in values:
    value_counts[value] = value_counts.get(value, 0) + 1

if 3 in value_counts.values():
    print("\nCongratulations! You drew a triple")
elif 2 in value_counts.values():
    print("\nCongratulations! You drew a pair")

# Flush (all same suit)
if len(set(suits)) == 1:
    print("Congratulations! You drew a flush")

# Straight
try:
    nums = sorted(card_value_num(v) for v in values)
    is_straight = all(nums[i] + 1 == nums[i + 1] for i in range (4))

    # Ace-high straight check
    if sorted(nums) == [1, 10, 11, 12, 13]:
        is_straight = True

    if is_straight:
        print("Congratulations! You drew a straight")
except Exception: 
    pass