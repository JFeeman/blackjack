import random
from time import sleep

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
#fullDeck = dict(zip(deckFaces, deckVals))
fullDeck = {face:value for face,value in zip(deckFaces, deckVals)}
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
    global deckCounter
    global playerScore
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


#This function initiates the game and deals out the first two cards to the player and the dealer
def startGame():
    getStart = input("Are you ready to play blackjack? Y or N    ")
    if getStart == "Y":
        print("Dealing the cards")
        print("Your First Card is:")
        deal_card_player()
        deal_card_dealer()
        sleep(1)
        print("Your Second Card is:")
        deal_card_player()
        deal_card_dealer()
        sleep(1)
        print("Your current score is: " + str(playerScore))
        sleep(1)
        print("The dealer is showing a " + dealerHand[0])


startGame()

#This is the players function. The player takes hits as he/she tries to maximize score while remaining under 21. In this section the player will either hold or bust
def player_round():
    takeHit = input("Would you like another card?   ")
    while takeHit =="Y":
        deal_card_player()
        print("Your current score is: " + str(playerScore))
        if playerScore > 21:
            #print("You Busted!")
            break
        takeHit = input("Would you like another card?  ")


player_round()
#This is the dealers function. The dealer will continue taking hits as long as the total score is under the dealer's limit. In this section the dealer will either hold or bust
def dealer_round():
    if dealerScore >= dealerLimit:
        print("The dealer stays on " + str(dealerScore))
    while dealerScore < dealerLimit:
        deal_card_dealer()
        print("The dealer takes a hit!")
        sleep(1)
        if dealerScore > 21:
            print("Dealer busts!")
            break
        elif dealerScore >= dealerLimit and dealerScore <= 21:
            print("The dealer stays on " + str(dealerScore))


if playerScore <= 21:
    dealer_round()

#This is the game evaluation function. Either the player wins or the dealer wins
def eval_scores():
    if playerScore > dealerScore and playerScore <= 21:
        print("Congratulations! You Won")
    elif playerScore > 21:
        print("You Lost")
    elif dealerScore>= playerScore and dealerScore<= 21:
        print("Dealer Won")
    else:
        print("You won!")


eval_scores()



    
        

