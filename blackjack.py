import random,sys

HEARTS=chr(9829)
DIAMONDS=chr(9830)
SPADES=chr(9824)
CLUBS=chr(9827)
BACKSIDE='backside'
print(HEARTS,DIAMONDS,SPADES,CLUBS)

def main():
    print('BLACKJACK')
    money=5000

    while True:
        if money<=0:
            print("You're broke")
            sys.exit()
        
        print('Money: ',money)
        bet=getBet(money)

        deck=getDeck()
        dealerHand=[deck.pop(),deck.pop()]
        playerHand=[deck.pop(),deck.pop()]

        print("Bet: ",bet)

        while True:
            displayHands(playerHand,dealerHand,False)
            print()

            if getHandValue(playerHand)>21:
                break

            move=getMove(playerHand,money-bet)

            if move=='D':
                additionalBet=getBet(min(bet,(money-bet)))
                bet+=additionalBet
                print('Bet increase to:{}'.format(bet))
                print('Bet:',bet)

            if move in ('H','D'):
                newcard=deck.pop()
                rank,suit=newcard
                print('You drew a {} of {}'.format(rank,suit))
                playerHand.append(newcard)

                if getHandValue(playerHand)>21:
                    continue
            
            if move in ('S','D'):
                break
        if getHandValue(playerHand)<=21:
            while getHandValue(dealerHand)<17:
                print('Dealer hits...')
                dealerHand.append(deck.pop())
                displayHands(playerHand,dealerHand,False)

                if getHandValue(dealerHand)>21:
                    break
                input('Prees Enter to continue...')
                print('\n\n')

        displayHands(playerHand,dealerHand,True) 

        playerValue=getHandValue(playerHand)
        dealerValue=getHandValue(dealerHand)
             