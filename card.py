class Card(object):
	"""docstring for Card"""
	RANKS = ["A","2","3","4","5","6","7","8","9","10","J","Q","K"]   #牌面数字
	SUITS = ["梅","方","红","黑"]										 #牌面类型
	def __init__(self,rank,suit,face_up = True):
		super(Card, self).__init__()
		self.rank = rank
		self.suit = suit
		self.is_face_up = face_up

	def __str__(self):
		if self.is_face_up:
			rep = self.suit + self.rank
		else:
			rep = "XX"
		return rep

	def pic_order(self):        #牌的序号
		if self.rank == "A":
			FaceNum == "1"
		elif self.rank == "J":
			FaceNum == "11"
		elif self.rank == "Q":
			FaceNum == "12"
		elif self.rank == "K":
			FaceNum == "13"
		else:
			FaceNum = int(self.rank)
		if self.suit == "梅":
			Suit == "1"
		elif self.rank == "方":
			Suit == "2"
		elif self.rank == "黑":
			Suit == "3"
		else:
			Suit == "4"
		return(suit-1)*13+FaceNum

	def filp(self):            #翻牌方法
		self.is_face_up = not self.is_face_up



class Hand():
	"""docstring for Hard"""
	def __init__(self):
		self.cards = []
	def __str__(self):
		pass
		if self.cards:
			rep = ""
			for card in self.cards:
				rep+=str(card)+"\t"
		else:	
			rep = "无"
		return rep
	def clear(self):
		pass
		self.cards = []
	def add(self,card):
		pass
		self.cards.append(card)
	def give(self,card,other_hand):
		self.cards.remove(card)
		other_hand.add(card)

class Poke(Hand):
	"""docstring for Poke"""
	def populate(self):
		pass
		for suit in Card.SUITS:
			for rank in Card.RANKS:
				pass
				self.add(Card(rank,suit))


	def shuffle(self):
		pass
		import random
		random.shuffle(self.cards)
	def deal(self,hands,per_hand = 13):
		pass
		for rounds in range(per_hand):
			for hand in hands:
				if self.cards:
					top_card = self.cards[0]
					self.cards.remove(top_card)
					hand.add(top_card)
					#self.give(top_card,hand)
				else:
					print("牌已发完")

if __name__ == '__main__':
	players = [Hand(),Hand(),Hand(),Hand()]
	pokel=Poke()
	pokel.populate()
	pokel.shuffle()
	pokel.deal(players,13)

	n=1

	for hand in players:
		print("牌手", n ,end=':')
		print(hand)
		n=n+1
	input("\n Press the enter key to exit.")
		