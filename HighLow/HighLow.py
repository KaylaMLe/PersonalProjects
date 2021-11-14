# Validates entered suit value and re-prompts the user if necessary
def SuitValue(suit: str) -> str:
    if suit.lower() == "diamonds" or suit.lower() == "hearts" or suit.lower() == "clubs" \
            or suit.lower() == "spades" or suit.lower() == "new":
        return suit.lower()
    else:
        SuitValue(input("Please reenter the suit.: "))


# Marks the card as seen in the list of the card's suit
# 2 -> index 0 since it is the lowest possible value
# 3 -> index 1, 10 -> index 8, jacks -> index 9, aces -> index 14
def UpdateCardsSeen(this_card: list, this_deck: list):
    if this_card[0] == "diamonds":
        this_deck[0][this_card[1] - 2] = 1
    elif this_card[0] == "hearts":
        this_deck[1][this_card[1] - 2] = 1
    elif this_card[0] == "clubs":
        this_deck[2][this_card[1] - 2] = 1
    elif this_card[0] == "spades":
        this_deck[3][this_card[1] - 2] = 1
    return


# returns the number of cards below and including this card's value that haven't been seen
def LowerCards(this_card: list, this_deck: list) -> float:
    # adds all cards below this card's value that have been seen
    tot = sum(this_deck[0][:this_card[1] - 1]) + sum(this_deck[1][:this_card[1] - 1]) \
          + sum(this_deck[2][:this_card[1] - 1]) + sum(this_deck[3][:this_card[1] - 1])
    # subtracts the number of lower cards seen from the highest possible number of lower cards
    tot = (4.0 * (this_card[1] - 1.0)) - tot
    return tot


# returns the number of cards above and including this cards value that haven't been seen
def HigherCards(this_card: list, this_deck: list) -> float:
    # adds all cards above this card's value that have been seen
    tot = sum(this_deck[0][this_card[1] - 2:]) + sum(this_deck[1][this_card[1] - 2:]) \
          + sum(this_deck[2][this_card[1] - 2:]) + sum(this_deck[3][this_card[1] - 2:])
    # subtracts the number of higher cards seen from the highest possible number of higher cards
    tot = ((13.0 - (this_card[1] - 2.0)) * 4.0) - tot
    return tot


# adds up all cards seen and subtracts from the total number of cards in the deck
def TotalCardsLeft(this_deck) -> float:
    tot = sum(this_deck[0]) + sum(this_deck[1]) + sum(this_deck[2]) + sum(this_deck[3])
    tot = 52.0 - tot
    # a float is returned for later calculations
    return tot


# Calculates the proportion of higher and lower cards and prints what choice to make
def HighLow(high: float, low: float, tot: float) -> str:
    # calculates chance of the next card being higher or lower
    percentHigh = high / tot
    percentLow = low / tot

    if percentHigh > percentLow:
        return "High"
    elif percentLow > percentHigh:
        return "Low"
    else:
        return "Either"


# Initializes lists of cards that have been seen
# suit[i] is 0 when the card has not been seen or 1 when the card has been seen
deck = 4 * [13 * [0]]

while True:
    # Using a list and not a tuple to store the input card suit and value to allow validation
    currentCard = list()
    currentCard.append(SuitValue(input("First card's suit: ")))
    currentCard.append(0)

    # Re-prompt if the card's given value is less than 2 or more than ace
    while currentCard[1] < 2 or currentCard[1] > 14:
        currentCard[1] = int(input("First card's value: "))

    # Mark the entered and validated card as seen
    UpdateCardsSeen(currentCard, deck)
    # Calculates the number of cards that haven't been seen and are lower or higher
    lower = LowerCards(currentCard, deck)
    higher = HigherCards(currentCard, deck)
    total = TotalCardsLeft(deck)

    print(HighLow(higher, lower, total))
    # re-prompts and recalculates the most likely outcome of the next card
    while total < 52:
        currentCard[0] = SuitValue(input("Next card's suit ('new' for new game): "))
        if currentCard[0] == "new":
            break
        currentCard[1] = int(input("Next card's value: "))

        while currentCard[1] < 2 or currentCard[1] > 14:
            currentCard[1] = int(input("Next card's value: "))

        UpdateCardsSeen(currentCard, deck)
        lower = LowerCards(currentCard, deck)
        higher = HigherCards(currentCard, deck)
        total = TotalCardsLeft(deck)

        print(HighLow(higher, lower, total))