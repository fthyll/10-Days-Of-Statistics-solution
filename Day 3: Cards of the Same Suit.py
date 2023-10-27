# Total number of cards in a deck
total_cards = 52

# Number of suits in a deck
suits = 4

# Number of cards of the same suit after drawing the first card
same_suit_cards_after_first_draw = total_cards // suits - 1

# Probability of drawing a card of the same suit on the second draw
probability_same_suit_second_draw = same_suit_cards_after_first_draw / (total_cards - 1)

print("The probability that both cards are of the same suit is:", probability_same_suit_second_draw)
