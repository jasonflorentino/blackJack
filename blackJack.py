#! python3
# Black Jack game, You vs. the dealer
# python3 blackJack.py

from time import sleep

from deckOfCards import Deck
from deckOfCards import Player

"""
FUNCTIONS

"""

# Prints the name of the game one char at a time
def printTitle(text):
	print('')
	for a in text:
		print(a, end='', flush=True)
		sleep(.05)
	sleep(1)
	print('\n')

# Shuffles the deck, deals out the hands to each player
def deal(deck, user, dealer):
	deck.shuffle()
	user.draw(deck)
	dealer.drawHidden(deck)
	user.draw(deck)
	dealer.draw(deck)

# Prints the hand of a given player.
def playerState(player):
	sleep(.05)
	print(player.name + ' hand:')
	for card in player.hidden:
		sleep(.05)
		print('?? of ??')
	sleep(.05)
	player.showHand()
	sleep(.05)
	print('')

# Counts the score of a player's hand, prints it, and returns it.
def tallyScore(player):
	score = 0
	for card in player.hand:
		if card.value in (11, 12, 13):
			score = score + 10
		elif card.value == 1 and score < 11:
			score = score + 11
		elif card.value == 1 and score > 10:
			score = score + 1
		else:
			score = score + card.value
	sleep(1)
	print('%s hand value: %s\n' % (player.name, str(score)))
	return score

# Checks if someone hits 21 or busts
def checkScore(score):
	global winner
	if score == 21:
		winner = True
		return True
	elif score > 21:
		sleep(1)
		print('Bust!\n')
		winner = True
		return True
	else:
		return False

# Run through dealer's turn
def dealerTurn(deck, dealer):
	sleep(1)
	print('Dealer\'s turn...\n')
	sleep(2)
	dealer.moveToHand(dealer.hidden)
	playerState(dealer)
	dealer.score = tallyScore(dealer)
	if dealer.score >= 17:
		sleep(2)
		print('Dealer stays.\n')
	while dealer.score < 17:
		sleep(2)
		print('Dealer hits.\n')
		dealer.draw(deck)
		sleep(1)
		playerState(dealer)
		dealer.score = tallyScore(dealer)
		checkScore(dealer.score)
	return

# Run through user's turn
def userTurn(deck, user):
	move = 'h'
	while move == 'h':
		move = input('Hit or Stay? (h/s)\n> ')
		if move == 'h':
			print('\nYou hit.\n')
			sleep(.5)
			user.draw(deck)
			playerState(user)
			sleep(.5)
			user.score = tallyScore(user)
		else:
			print('\nYou stay.\n')
			sleep(.5)
			user.score = tallyScore(user)
		if checkScore(user.score):
			break

# Prints result of the game
def gameResult(user, comp):
	if user.score == comp.score:	# Tie game
		sleep(.5)
		return print('Push!\n')		
	elif user.score > 21:			# Player busts
		sleep(.5)
		return print('You Lose!\n')
	elif comp.score > 21:			# Dealer busts
		sleep(.5)
		return print('You Win!\n')
	elif user.score > comp.score:	# Player beats dealer
		sleep(.5)
		return print('You Win!\n')
	elif user.score < comp.score:	# Dealer beats player
		sleep(.5)
		return print('You Lose!\n')
	else:
		sleep(.5)
		return

# Creates deck and player objects, calls game functions
def main():
	global winner 
	deck = Deck()
	user = Player('Your')
	dealer = Player('Dealer')
	title = 'LET\'S PLAY BLACKJACK!'

	# Main game structure
	printTitle(title)
	deal(deck, user, dealer)
	playerState(dealer)
	playerState(user)
	userTurn(deck, user)
	# Skip dealer turn if player hits blackjack or busts
	if winner == False:
		dealerTurn(deck, dealer)
	gameResult(user, dealer)
	# Reset global winner var
	winner = False

"""
MAIN PROGRAM

"""

winner = False

if __name__ == '__main__':
	main()
	sleep(.5)
	while input('Play again? (y/n)\n> ') == 'y':
		main()
		sleep(.5)
	printTitle('Hit the road, Jack!')
