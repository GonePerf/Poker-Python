#  Autor: Konrad Gumienny
#  Nr albumu: 109146
#  Informatyka II rok

import random

class Card:
    unicode_dict = {'s': '\u2660', 'h': '\u2665', 'd': '\u2666', 'c': '\u2663'}
    rangs = {0: '2', 1: '3', 2: '4', 3: '5', 4: '6', 5: '7', 6: '8', 7: '9', 8: '10', 9: 'J', 10: 'Q', 11: 'K', 12: 'A'}
    def __init__(self, value, color):
        self.value = value
        self.color = color
    def getValue(self):
        return (self.value,self.color)
    def __str__(self):
        return rangs[self.value] + self.unicode_dict[self.color] + ' '

class Deck:
    def __init__(self, cards):
        self.cards = cards
    def shuffle(self):
        self.cards = random.sample(self.cards, len(self.cards))
    def deal(self, players):
        cardsList = list((self.cards[i].value, self.cards[i].color) for i in range(0, 5 * len(players)))
        i = -1
        for j in range(0, len(players)):
            for i in range(i + 1, i + 6):
                players[j].take_card(cardsList[i])
        return players
    def __str__(self):
        value = ' '
        for i in self.cards:
            value += str(i)
        return value


class Player:
    def __init__(self, money, name=""):
        self.__stack_ = money
        self.__name_ = name
        self.__hand_ = []
    def take_card(self, card):
        self.__hand_.append(card)

    def get_stack_amount(self):
        return self.__stack_

    def get_player_hand_immutable(self):
        return tuple(self.__hand_)

    def cards_to_str(self):
        value = ''
        for i in self.__hand_:
            value += str(i)
        return value

def histogram(list):
    my_dict = {i: list.count(i) for i in list}
    return my_dict

def get_player_hand_rank(hand):
    hand_rank_list = [i[0] for i in hand]
    hand_color_list = [i[1] for i in hand]

    def is_rank_sequence(hand):
        hand_rank_list = [i[0] for i in hand]
        hand_rank_list.sort()
        seq_hand = [i for i in range(hand_rank_list[0], hand_rank_list[0] + 5)]
        if seq_hand == hand_rank_list:
            return True
        else:
            return False
    # histogramy rang kart graczy  okresla ile razy wystapila karta o tej samej randze,
    # potrzebne do ustalenia ukladu kart
    hand_rank_histogram = histogram(hand_rank_list)
    # histogramy kolorow kart graczy, jesli 5 in hand_color_histogram.values() == True
    # to wszystkie karty sa jednego koloru
    hand_color_histogram = histogram(hand_color_list)
    # czy karty sa "po kolei" (konieczne w: poker krolewski, pokerze, strit)
    is_hand_rank_sequence = is_rank_sequence(hand)

    hand_strength = 0 # zwracana zmienna, ja trzeba ustawic
    # ------ sprawdzamy uklad gracza 1:
    # --- sprawdzamy poker krolewski: 5 kart w tym samym kolorze, po kolei, najwyzsza to as
    if( (5 in hand_color_histogram.values()) and ( 12 in hand_rank_list ) and is_hand_rank_sequence):
        hand_strength = 10
    # --- sprawdzamy poker: 5 kart w tym samym kolorze, po kolei
    elif( ( 5 in hand_color_histogram.values()) and is_hand_rank_sequence):
        hand_strength =  9
    elif( ( 4 in hand_rank_histogram.values())):
        hand_strength = 8
    elif( ( 3 in hand_rank_histogram.values()) and ( 2 in hand_rank_histogram.values())):
        hand_strength = 7
    elif((5 in hand_color_histogram.values())):
        hand_strength = 6
    elif(is_hand_rank_sequence):
        hand_strength = 5
    elif(( 3 in hand_rank_histogram.values())):
        hand_strength = 4
    elif(( 2 in hand_rank_histogram.values()) and len(hand_rank_histogram) == 3):
        hand_strength = 3
    elif ((2 in hand_rank_histogram.values())):
        hand_strength = 2
    elif (sorted(hand_rank_list)[4] > 8):
        hand_strength = 1
    return hand_strength


colors = ['c','d','h', 's']
rangs = {0:'2',1:'3',2:'4',3:'5',4:'6',5:'7',6:'8',7:'9',8:'10',9:'J',10:'Q',11:'K',12:'A'}

deck = list(Card(value, color) for value in rangs for color in colors)
print(len(deck))
def shuffle_deck(deck):
    lr = random.sample(deck, len(deck))
    return lr

def deal(deck, n):
    cardsList = list((deck[i].value, deck[i].color) for i in range(0,5*n))
    i = -1
    lista = []
    for j in range(0, n):
        for i in range(i+1,i+6):
            lista.append(cardsList[i])

    return  lista;


num_players = 2
players = []

for i in range(0, num_players):
    players.append(Player(1000))

print("Nowa talia:")
deck = Deck(deck)
print(deck)

print("Talia potasowana:")
deck.shuffle()
print(deck)

print("Rozdane karty 2 graczom:")

hands = deck.deal(players)
for player in players:
    print(player.cards_to_str() + " : " + str(get_player_hand_rank(player.get_player_hand_immutable())))

