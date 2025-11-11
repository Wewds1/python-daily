"""
Counting Cards
A standard deck of playing cards has 13 unique cards in each suit. Given an integer representing the number of cards to pick from the deck, return the number of unique combinations of cards you can pick.

Order does not matter. Picking card A then card B is the same as picking card B then card A.
For example, given 52, return 1. There's only one combination of 52 cards to pick from a 52 card deck. And given 2, return 1326, There's 1326 card combinations you can end up with when picking 2 cards from the deck.


"""

def combinations(cards):
    deck = 52
    deck_fact = factorial(deck)
    cards_fact = factorial(cards)
    total_fact = factorial(deck - cards)
    
    return deck_fact // (cards_fact * total_fact)
    


def factorial(n):
    if n ==0 or n==1:
        return 1
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result




print(combinations())