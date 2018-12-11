# implementation of card game - Memory

import simplegui
import random


# helper function to initialize globals
def new_game():
    global state, counter, cards, exposed
    state = 0
    counter = 0
    cards = range(8)
    cards.extend(range(8))
    random.shuffle(cards)
    exposed = [False]*len(cards)


# define event handlers
def mouseclick(pos):
    global state, card1, card2, card1_index, card2_index, counter
    card_index = pos[0] // 50
    if exposed[card_index] is True:
        pass
    elif state == 0:
        exposed[card_index] = True
        card1 = cards[card_index]
        card1_index = card_index
        state = 1
    elif state == 1:
        exposed[card_index] = True
        card2 = cards[card_index]
        card2_index = card_index
        state = 2
    elif state == 2:
        counter += 1
        if card1 != card2:
            exposed[card1_index] = False
            exposed[card2_index] = False
        exposed[card_index] = True
        card1 = cards[card_index]
        card1_index = card_index
        state = 1


# cards are logically 50x100 pixels in size
def draw(canvas):
    for card in range(len(cards)):
        card_pos = card*50
        if exposed[card] is False:
            canvas.draw_polygon([(card_pos, 0), (50*(card+1), 0),
                                (50*(card+1), 100), (50*card, 100)],
                                3, "Red", "Green")
        elif exposed[card] is True:
            canvas.draw_text(str(cards[card]),
                                (card_pos + 12, 60), 45, 'White')
    label.set_text("Turns = " + str(counter))


# create frame and add a button and labels
frame = simplegui.create_frame("Memory", 800, 100)
frame.add_button("Reset", new_game)
label = frame.add_label("Turns =  ")


# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

# get things rolling
new_game()
frame.start()


# Always remember to review the grading rubric

