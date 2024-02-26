#from game import communityCards, playerCards, computerCards

def check(communityCards, playerCards, computerCards):
    checkPair(communityCards, playerCards, computerCards)
    checkFlush(communityCards, playerCards, computerCards)
    checkRoyalFlush(communityCards, playerCards, computerCards)

def checkPair(communityCards, playerCards, computerCards):
    playerPairCount = 0
    computerPairCount = 0
    for CCcard in communityCards:
        if any(playercard.number == CCcard.number for playercard in playerCards):
            playerPairCount += 1
        if any(computercard.number == CCcard.number for computercard in computerCards):
            computerPairCount += 1
    print("Player Pair" + str(playerPairCount))
    print("Computer Pair" + str(computerPairCount))
    
def checkFlush(communityCards, playerCards, computerCards):
    playerSuitCount = 0
    computerSuitCount = 0
    for CCcard in communityCards:
        if any(playercard.suit == CCcard.suit for playercard in playerCards):
            playerSuitCount += 1
        if any(computercard.suit == CCcard.suit for computercard in computerCards):
            computerSuitCount += 1
    print("Player Suit Count" + str(playerSuitCount))
    print("Computer Suit Count" + str(computerSuitCount))

def checkRoyalFlush(communityCards, playerCards, computerCards):
    return