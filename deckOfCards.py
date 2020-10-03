#! python3
# Built from Executed Binary's video "Python OOP - Deck of Cards" (https://www.youtube.com/watch?v=t8YkjDH86Y4)

import random

class Card(object):
	def __init__(self, suit, val):
		self.suit = suit
		self.value = val
		
	def show(self):
		if self.value == 1:
			val = "Ace"
		elif self.value == 11:
			val = "Jack"
		elif self.value == 12:
			val = "Queen"
		elif self.value == 13:
			val = "King"
		else:
			val = self.value
		return f"{val} of {self.suit}"

class Deck(object):
	def __init__(self):
		self.cards = []
		self.build()
	
	# Display all cards in deck
	def show(self):
		for card in self.cards:
			print(card.show())
	
	# Generate 52 cards
	def build(self):
		self.cards = []
		for suit in ['Spades', 'Clubs', 'Diamonds', 'Hearts']:
			for val in range(1,14):
				self.cards.append(Card(suit, val))
	
	# Shuffle the deck
	def shuffle(self):
		# fisher yates shuffle algorithm
		for i in range(len(self.cards)-1, 0, -1):
			randi = random.randint(0, i)
			self.cards[i], self.cards[randi] = self.cards[randi], self.cards[i]
	
	# Return top card
	def dealCard(self):
		return self.cards.pop()

class Player(object):
	def __init__(self, name):
		self.name = name
		self.score = 0
		self.hand = []
		self.hidden = []
	
	def draw(self, deck):
		self.hand.append(deck.dealCard())
		return self

	def drawHidden(self, deck):
		self.hidden.append(deck.dealCard())
		return self

	def moveToHand(self, cards):
		for card in cards:
			self.hand.append(cards.pop())

	def showHand(self):
		for card in self.hand:
			print(card.show())

	def discard(self):
		return self.hand.pop()
	