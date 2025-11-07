import math

def unique_card_combinations(k_cards_to_pick):
    """
    Calculates the number of unique combinations when picking k cards 
    from a standard 52-card deck, where order does not matter.
    """
    # Total number of cards in the deck
    n = 52
    
    if k_cards_to_pick < 0 or k_cards_to_pick > n:
        return "Error: Number of cards to pick must be between 0 and 52."
    
    # Use the math.comb function to calculate C(52, k)
    # This is mathematically equivalent to (52!) / (k! * (52-k)!)
    combinations = math.comb(n, k_cards_to_pick)
    
    return combinations

# --- Examples ---
k1 = 52
k2 = 2

print(f"Number of combinations for picking {k1} cards: {unique_card_combinations(k1)}")

print(f"Number of combinations for picking {k2} cards: {unique_card_combinations(k2)}") 
# C(52, 2) = (52*51) / (2*1) = 2652 / 2 = 1326

print(f"Number of combinations for picking 5 cards (a poker hand): {unique_card_combinations(5)}")