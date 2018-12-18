# Mini-project #6 - Blackjack

import simplegui
import random

# load card sprite - 936x384 - source: jfitz.com
CARD_SIZE = (72, 96)
CARD_CENTER = (36, 48)
card_images = simplegui.load_image("http://storage.googleapis.com/codeskulptor-assets/cards_jfitz.png")

CARD_BACK_SIZE = (72, 96)
CARD_BACK_CENTER = (36, 48)
card_back = simplegui.load_image("http://storage.googleapis.com/codeskulptor-assets/card_jfitz_back.png")

# initialize some useful global variables
in_play = False
outcome = ""
dealer_score = 0
player_score = 0

# define globals for cards
SUITS = ('C', 'S', 'H', 'D')
RANKS = ('A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K')
VALUES = ({'A': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8,
          '9': 9, 'T': 10, 'J': 10, 'Q': 10, 'K': 10})


# define card class
class Card:
    def __init__(self, suit, rank):
        if (suit in SUITS) and (rank in RANKS):
            self.suit = suit
            self.rank = rank
        else:
            self.suit = None
            self.rank = None
            print "Invalid card: ", suit, rank

    def __str__(self):
        return self.suit + self.rank

    def get_suit(self):
        return self.suit

    def get_rank(self):
        return self.rank

    def draw(self, canvas, pos):
        card_loc = (CARD_CENTER[0] + CARD_SIZE[0] * RANKS.index(self.rank),
                    CARD_CENTER[1] + CARD_SIZE[1] * SUITS.index(self.suit))
        canvas.draw_image(card_images, card_loc, CARD_SIZE,
                          [pos[0] + CARD_CENTER[0], pos[1] + CARD_CENTER[1]],
                          CARD_SIZE)


# define hand class
class Hand:
    def __init__(self):
        self.cards = []

    def __str__(self):
        s = "Hand contains "
        for card in self.cards:
            s += str(card) + " "
        return s

    def add_card(self, card):
        self.cards.append(card)

    def get_value(self):
        hand_value = 0
        for card in self.cards:
            hand_value += VALUES[card.get_rank()]
        # count "A" in str(self) after "Hand contains "
        if str(self).count('A', 15, len(str(self))) > 0 and hand_value + 10 <= 21:
            hand_value += 10
        return hand_value

    def draw(self, canvas, pos):
        for card in self.cards:
            card.draw(canvas, pos)
            pos[0] += CARD_SIZE[0]


# define deck class
class Deck:
    def __init__(self):
        self.deck_cards = []
        for suit in SUITS:
            for rank in RANKS:
                self.deck_cards.append(Card(suit, rank))

    def shuffle(self):
        random.shuffle(self.deck_cards)

    def deal_card(self):
        self.card = self.deck_cards[-1]
        self.deck_cards.pop()
        return self.card

    def __str__(self):
        s = "Deck contains "
        for card in self.deck_cards:
            s += str(card) + " "
        return s


# define event handlers for buttons
def deal():
    global outcome, in_play, player_hand, dealer_hand, new_deck, dealer_score
    if in_play is True:
        dealer_score += 1
        outcome = "You lose the round. Hit or stand?"
    else:
        outcome = "Hit or stand?"
        new_deck = Deck()
        new_deck.shuffle()
        player_hand = Hand()
        dealer_hand = Hand()
        for i in [0, 1]:
            player_hand.add_card(new_deck.deal_card())
            dealer_hand.add_card(new_deck.deal_card())
        in_play = True


def hit():
    global outcome, in_play, dealer_score
    if player_hand.get_value() <= 21:
        player_hand.add_card(new_deck.deal_card())
        if player_hand.get_value() > 21:
            outcome = "You have busted. New deal?"
            dealer_score += 1
            in_play = False


def stand():
    global outcome, in_play, dealer_score, player_score
    if in_play is False:
        pass
    elif player_hand.get_value() > 21:
        outcome = "You have busted. New deal?"
        dealer_score += 1
        in_play = False
    else:
        while dealer_hand.get_value() <= 17:
            dealer_hand.add_card(new_deck.deal_card())
        else:
            if dealer_hand.get_value() > 21:
                outcome = "Dealer has busted, you win. New deal?"
                player_score += 1
                in_play = False
            elif dealer_hand.get_value() >= player_hand.get_value():
                outcome = "Dealer wins. New deal?"
                dealer_score += 1
                in_play = False
            else:
                outcome = "You win. New deal?"
                player_score += 1
                in_play = False


# draw handler
def draw(canvas):
    # test to make sure that card.draw works, replace with your code below
    dealer_hand.draw(canvas, [50, 150])
    player_hand.draw(canvas, [50, 450])
    if in_play is True:
        canvas.draw_image(card_back, CARD_BACK_CENTER, CARD_BACK_SIZE,
                          [50 + CARD_BACK_CENTER[0], 150 + CARD_BACK_CENTER[1]],
                          CARD_SIZE)
    canvas.draw_text(outcome, [50, 350], 35, "Yellow")
    canvas.draw_text("Dealer wins: "+str(dealer_score), [50, 130], 30, "Black")
    canvas.draw_text("Player wins: "+str(player_score), [50, 430], 30, "Black")
    canvas.draw_text("BlackJack", [230, 60], 35, "Black")


# initialization frame
frame = simplegui.create_frame("Blackjack", 600, 600)
frame.set_canvas_background("Green")

# create buttons and canvas callback
frame.add_button("Deal", deal, 200)
frame.add_button("Hit",  hit, 200)
frame.add_button("Stand", stand, 200)
frame.set_draw_handler(draw)


# get things rolling
deal()
frame.start()

