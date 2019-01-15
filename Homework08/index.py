"""
Monte Carlo Tic-Tac-Toe Player
"""

import random
import poc_ttt_gui
import poc_ttt_provided as provided

# Constants for Monte Carlo simulator
# You may change the values of these constants as desired, but
#  do not change their names.
NTRIALS = 100        # Number of trials to run
SCORE_CURRENT = 1.0  # Score for squares played by the current player
SCORE_OTHER = 1.0    # Score for squares played by the other player


# Add your functions here.
def mc_trial(board, player):
    """
    The function plays a game starting with the given player
    by making random moves, alternating between players.
    """
    while board.check_win() is None:
        random_move = random.choice(board.get_empty_squares())
        board.move(random_move[0], random_move[1], player)
        player = provided.switch_player(player)


def mc_update_scores(scores, board, player):
    """
    The function scores the completed board and updates
    the scores grid.
    """
    board_dim = range(board.get_dim())
    winner = board.check_win()
    for row in board_dim:
        for col in board_dim:
            square = board.square(row, col)
            if player is winner:
                if square == player:
                    scores[row][col] += SCORE_CURRENT
                elif square == provided.switch_player(player):
                    scores[row][col] -= SCORE_OTHER

            elif provided.switch_player(player) is winner:
                if square == player:
                    scores[row][col] -= SCORE_CURRENT
                elif square == provided.switch_player(player):
                    scores[row][col] += SCORE_OTHER


def get_best_move(board, scores):
    """
    The function finds all of the empty squares with
    the maximum score and randomly returns one of them
    as a (row,column) tuple.
    """
    empty_squares = board.get_empty_squares()
    scores_value = []
    best_scores = []

    for square in empty_squares:
        scores_value.append(scores[square[0]][square[1]])

    for square in empty_squares:
        if scores[square[0]][square[1]] is max(scores_value):
            best_scores.append(square)

    for dummy_i in best_scores:
        return random.choice(best_scores)


def mc_move(board, player, trials):
    """
    The function uses functions described above to return
    a move for the machine player
    in the form of a (row,column) tuple.
    """

    dim = board.get_dim()
    scores = [[0 for dummy_row in range(dim)] for dummy_col in range(dim)]
    for dummy_index in range(trials):
        board_copy = board.clone()
        mc_trial(board_copy, player)
        mc_update_scores(scores, board_copy, player)
    return get_best_move(board, scores)

# Test game with the console or the GUI.  Uncomment whichever
# you prefer.  Both should be commented out when you submit
# for testing to save time.

# provided.play_game(mc_move, NTRIALS, False)
poc_ttt_gui.run_gui(3, provided.PLAYERX, mc_move, NTRIALS, False)

