import random


class Card:
    def __init__(self, rank, suit, value, id):
        CARDRANK = [str(x) for x in (range(7,10))] + [y for y in str('TJQKA')]
        CARDSUIT = ['h','d','s','c']

        self.rank = rank
        self.suit = suit
        if value > 10:
            self.value = 10
        else:
            self.value = value
        self.id = id
        self.name = f'{CARDRANK[rank]}{CARDSUIT[suit]}'

    def __repr__(self):
        return self.name

    def __iter__(self):
        return self

    def __lt__(self, other):
        if isinstance(other, Card):
           return self.rank < other.rank
        else:
            return False

    def __add__(self, other):
        if isinstance(other, Card):
            return self.rank + other.rank

    def __radd__(self, other):
       if other == 0:
           return self
       else:
           return self.__add__(other)
    
    def __eq__(self, other):
       if isinstance(other, Card):
           return self.rank == other.rank         
       else:
           return False


class Deck:
    def __init__(self):
        self.deck = []
        num = 0
        for suit in range(4):
            val = 1
            for rank in range(8):
                card = Card(rank,suit,val,num)
                self.deck.append(card)
                val += 1
                num += 1
                rank += 1

    def __getitem__(self,s):
        return self.deck[s]

    def __iter__(self):
        return self


class Board:
    def __init__(self):
        self.hand = []
        deck = Deck()
        self.playdeck = deck.deck[:]
        random.shuffle(self.playdeck)
        self.hand = self.playdeck[1:6]