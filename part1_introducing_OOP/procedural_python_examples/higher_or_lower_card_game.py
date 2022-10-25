'''

Non-OOP

HigherOrLower

This is a card game called Higher or Lower, built using procedural paradigm.
In this game, eight cards are randomly chosen from a deck. The first card is
shown face up. The game asks the player to predict whether the next card in
the selection will have a higher or lower value than the currently
showing card. For example, say the card that's shown is a 3. The player
chooses “higher,” and the next card is shown. If that card has a higher
value, the player is correct. In this example, if the player had chosen
“lower,” they would have been incorrect. If the player guesses correctly,
they get 20 points. If they choose incorrectly, they lose 15 points. If
the next card to be turned over has the same value as the previous card,
the player is incorrect.

Data Representation:
    The program needs to represent a deck of 52 cards, which I'll build as a
    list. Each of the 52 elements in the list will be a dictionary (a set of
    key/value pairs). To represent any card, each dictionary will contain three
    key/value pairs: 'rank', 'suit', and 'value'. The rank is the name of the
    card (Ace, 2, 3, … 10, Jack, Queen, King), but the value is an integer used
    for comparing cards (1, 2, 3, … 10, 11, 12, 13). For example, the Jack of
    Clubs would be represented as the following dictionary:

                {'rank': 'Jack', 'suit': 'Clubs', 'value': 11}

    Before the player plays a round, the list representing the deck is created
    and shuffled to randomize the order of the cards.
    each time the user chooses “higher” or “lower,”
    the program gets a card dictionary from the deck and prints the rank and
    the suit for the user. The program then compares the value of the new card
    to that of the previous card and gives feedback based on the correctness of
    the user's answer.

'''

import random

# Card constants
SUIT_TUPLE = ('Spades', 'Hearts', 'Clubs', 'Diamonds')
RANK_TUPLE = ('Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack',
              'Queen', 'King')

# Number of chosen cards
NCARDS = 8


# Pass in a deck and this function returns a random card from the deck
def getCard(deckListIn):
    thisCard = deckListIn.pop()  # pop one off the top the deck and return
    return thisCard


# Pass in a deck and this function returns a shuffled copy of the deck
def shuffle(deckListIn):
    deckListOut = deckListIn.copy()  # make a copy of the starting deck
    random.shuffle(deckListOut)
    return deckListOut


# Main code
print('Welcome to Higher or Lower.')
print('You have to choose whether the next card to be shown will be higher\
       or lower than the current card.')
print('Getting it right adds 20 points; get it wrong and you lose 15 points.')
print('You have 50 points to start.')
print()

startingDeckList = []
for suit in SUIT_TUPLE:
    for thisValue, rank in enumerate(RANK_TUPLE):
        cardDict = {'rank': rank, 'suit': suit, 'value': thisValue + 1}
        startingDeckList.append(cardDict)

score = 50

while True:  # play multiple games
    print()
    gameDeckList = shuffle(startingDeckList)
    currentCardDict = getCard(gameDeckList)
    currentCardRank = currentCardDict['rank']
    currentCardValue = currentCardDict['value']
    currentCardSuit = currentCardDict['suit']
    print('Starting card is:', currentCardRank + ' of ' + currentCardSuit)
    print()

    for cardNumber in range(0, NCARDS):  # play one game of this many cards
        answer = input('Will the next card be higher or lower than the ' +
                       currentCardRank + ' of ' +
                       currentCardSuit + '? (enter h or l): ')

        answer = answer.casefold()  # force lower case
        nextCardDict = getCard(gameDeckList)
        nextCardRank = nextCardDict['rank']
        nextCardSuit = nextCardDict['suit']
        nextCardValue = nextCardDict['value']
        print('Next card is:', nextCardRank + ' of ' + nextCardSuit)

        if answer == 'h':
            if nextCardValue > currentCardValue:
                print('You got it right, it was higher')
                score = score + 20
            else:
                print('Sorry, it was not higher')
                score = score - 15

        elif answer == 'l':
            if nextCardValue < currentCardValue:
                score = score + 20
                print('You got it right, it was lower')

            else:
                score = score - 15
                print('Sorry, it was not lower')

        print('Your score is:', score)
        print()
        currentCardRank = nextCardRank
        currentCardValue = nextCardValue
        currentCardSuit = nextCardSuit

    goAgain = input('To play again, press ENTER, or "q" to quit: ')
    if goAgain == 'q':
        break

print('OK bye')


'''
Reusability:
    Since this is a playing card-based game, the code obviously creates and
    manipulates a simulated deck of cards. If we wanted to write another
    cardbased game, it would be great to be able to reuse the code for the
    deck and cards.
    In a procedural program, it can often be difficult to identify all the
    pieces of code associated with one portion of the program, such as the deck
    and cards in this example. In Listing 1-1, the code for the deck consists
    of two tuple constants, two functions, some main code to build a global
    list that represents the starting deck of 52 cards, and another global list
    that represents the deck that is used while the game is being played.
    Further, notice that even in a small program like this, the data and the
    code that manipulates the data might not be closely grouped together.
    Therefore, reusing the deck and card code in another program is not
    that easy or straightforward.

'''
