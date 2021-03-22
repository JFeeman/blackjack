import random


#initiate the values for the deck of cards here
deckVals = []
counter = 2
for x in range(9):
    for y in range(4):
        deckVals.append(counter) 
    counter += 1
for x in range(12):
    deckVals.append(10)
for x in range(4):
    deckVals.append(11)

#initiate the strings that will represent the card faces here
deckFaces = ["Two of Hearts", "Two of Diamonds", "Two of Clubs", "Two of Spades", "Three of Hearts", "Three of Diamonds", "Three of Clubs", "Three of Spades", "Four of Hearts", "Four of Diamonds", "Four of Clubs", "Four of Spades", "Five of Hearts", "Five of Diamonds", "Five of Clubs", "Five of Spades", "Six of Hearts", "Six of Diamonds", "Six of Clubs", "Six of Spades", "Seven of Hearts", "Seven of Diamonds", "Seven of Clubs", "Seven of Spades", "Eight of Hearts", "Eight of Diamonds", "Eight of Clubs", "Eight of Spades", "Nine of Hearts", "Nine of Diamonds", "Nine of Clubs", "Nine of Spades", "Ten of Hearts", "Ten of Diamonds", "Ten of Clubs", "Ten of Spades", "Jack of Hearts", "Jack of Diamonds", "Jack of Clubs", "Jack of Spades", "Queen of Hearts", "Queen of Diamonds", "Queen of Clubs", "Queen of Spades", "King of Hearts", "King of Diamonds", "King of Clubs", "King of Spades", "Ace of Hearts", "Ace of Diamonds", "Ace of Clubs", "Ace of Spades"]

#put the values with the faces so i can reference the values based off the shuffled list of faces
fullDeck = dict(zip(deckFaces, deckVals))

random.shuffle(deckFaces)


deckCounter = 0

#all player variables here
playerScore = 0
playerHand = []
playerCounter = 0

#all dealer variables here
dealerScore = 0
dealerHand = []
dealerCounter = 0
dealerLimit = random.randint(14,20)

def deal_card_player():
    global playerScore
    global deckCounter
    global playerCounter
    playerHand.append(deckFaces[deckCounter])
    playerScore = playerScore + fullDeck[deckFaces[deckCounter]]
    print(playerHand[playerCounter])
    deckCounter += 1
    playerCounter += 1

def deal_card_dealer():
    global dealerScore
    global deckCounter
    global dealerCounter
    dealerHand.append(deckFaces[deckCounter])
    dealerScore = dealerScore + fullDeck[deckFaces[deckCounter]]
    deckCounter += 1
    dealerCounter += 1



getStarted = input("Are You Ready to Play Blackjack? Y or N   ")
if getStarted == "Y":
    print("Dealing the cards")
    print("Your First Card is:")
    deal_card_player()
    deal_card_dealer()
    print("Your Second Card is:")
    deal_card_player()
    deal_card_dealer()
    print("Your current score is: " + str(playerScore))
    print("The dealer is showing a " + dealerHand[0])

takeHit = input("Would you like another card?   ")
while takeHit =="Y":
    deal_card_player()
    print("Your current score is: " + str(playerScore))
    if playerScore > 21:
        print("You Busted!")
        break
    takeHit = input("Would you like another card?  ")
    
        

