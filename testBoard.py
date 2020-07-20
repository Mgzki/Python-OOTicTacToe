from BoardClass import Board
from PlayerClass import Player
import random

#checks if the current player met a win condition
def check_win(board,player):
    in_a_row = [player]*board.width
    rows = board.rows()
    cols = board.cols()
    diags = board.diags()

    for i in range(board.width):
        if in_a_row == rows[i] or in_a_row == cols[i]:
            return True

    if in_a_row == diags[0] or in_a_row == diags[1]:
        return True

    return False

#checks for empty moves, if one exists it's not a tie
#used with check_win(board,player) such that if no win condition is met
#and there are no free moves, it's a tie
def check_tie(board):
    for i in board.rows():
        for col in i:
            if isinstance(col,int):
                return False
    return True

#determines who goes first
def first():
    val = random.random()
    turn = 'X' if val <= 0.5 else 'O'
    print(turn + " Goes first")
    return turn

#initializes an empty board, and 2 players
def setup():
    board = Board(3,3)
    board.create_Board()
    player1 = Player('X')
    player2 = Player('O')
    return board,player1,player2

#converts move from int value to the correct grid location
def convert_move(move):
    if move == 1: return (0,0)
    elif move == 2: return (0,1)
    elif move == 3: return (0,2)
    elif move == 4: return (1,0)
    elif move == 5: return (1,1)
    elif move == 6: return (1,2)
    elif move == 7: return (2,0)
    elif move == 8: return (2,1)
    elif move == 9: return (2,2)

#Determines single vs multiplayer game
def num_players():
    try:
        num_players = int(input("How many players?\nAny answer that isn't 2 will default to 1\n"))
    except ValueError:
        num_players = 1
    return True if num_players == 2 else False

#Changes whose turn it is
def change_turn(turn):
    turn = 'O' if turn == 'X' else 'X'
    return turn
#
def move(mode,board,turn):
    #Two human players move handling
    if mode:
        x,y = convert_move(int(input(turn + " Enter your move (1-9):\n")))
        if board.set_Move(x,y,turn):
            print(board)
        else:
            print("Invalid move")
            move(mode,board,turn)
    else:
        if turn == 'X':
            x,y = convert_move(int(input(turn + " Enter your move (1-9):\n")))
            if board.set_Move(x,y,turn):
                print(board)
            else:
                print("Invalid move")
                move(mode,board,turn)
        else:
            make_bot_selection(board)

def make_bot_selection(board):
    best_score = float("-inf")
    best_move = -1

    for row in range(len(board.play_field)):
        for column in range(row):
            if isinstance(board.play_field[row][column], int):
                old_value = board.play_field[row][column]
                board.play_field[row][column] = "O"
                score = minimax(board, 0, True)
                board.play_field[row][column] = old_value

                if score > best_score:
                    best_score = score
                    best_move = old_value

    # print("Best move " + str(best_move))
    x, y = convert_move(best_move)
    board.set_Move(x, y, "O")
    # board.play_field[x][y] = "O"
    print(board)

def minimax(board, depth, maximizing_player):
    if check_win(board, "O"):
        return 1

    if check_win(board, "X"):
        return -1

    if check_tie(board):
        return 0

    if maximizing_player:
        best_score = float("-inf")
        for row in range(len(board.play_field)):
            for column in range(row):
                if isinstance(board.play_field[row][column], int):
                    old_value = board.play_field[row][column]
                    board.play_field[row][column] = "O"
                    print("changed at position: " + str(old_value))
                    print(board)
                    score = minimax(board, depth + 1, False)
                    board.play_field[row][column] = old_value

                    if score > best_score:
                        best_score = score
        return best_score
    else:
        best_score = float("inf")
        for row in range(len(board.play_field)):
            for column in range(row):
                if isinstance(board.play_field[row][column], int):
                    old_value = board.play_field[row][column]
                    board.play_field[row][column] = "X"
                    score = minimax(board, depth + 1, True)
                    board.play_field[row][column] = old_value

                    if score < best_score:
                        best_score = score
        return best_score

if __name__ == "__main__":
    #initialize the game, players
    board,player1,player2 = setup()
    mode = num_players() #True for 2 players, False for 1 player vs AI
    #prints the initial/empty board
    print(board)
    turn = first()
    #while it's not a tie (or a win for either player) repeatedly ask for the next move
    while not check_tie(board):
        move(mode,board,turn)
        if check_win(board,turn):
            if turn == player1.symbol:
                player1.win()
                player2.lose()
            else:
                player2.win()
                player1.lose()
            print(turn + " won!")
            break
        elif check_tie(board):
            print('tie game')
        turn = change_turn(turn)
    player1.show_Score()
    player2.show_Score()