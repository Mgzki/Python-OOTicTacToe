from BoardClass import Board
from PlayerClass import Player
import random

#checks if the current player met a win condition
def check_win(board,player):
    in_a_row = [player]*board.width
    rows,cols,diags = board.rows(),board.cols(),board.diags()
    for i in range(board.width):
        if in_a_row == rows[i] or in_a_row == cols[i]:
            return True
        elif in_a_row == diags[0] or in_a_row == diags[1]:
            return True
    return False

#checks for empty moves, if one exists it's not a tie
#used with check_win(board,player) such that if no win condition is met
#and there are no free moves, it's a tie
def check_tie(board):
    return board.full_Board()

#determines who goes first
def first():
    val = random.random()
    turn = 'X' if val <= 0.5 else 'O'
    print(turn + " Goes first")
    return turn

#initializes an empty 3x3 board, and 2 players('X','O')
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
    #Human vs AI move handling
    else:
        #Human move handling
        if turn == 'X':
            x,y = convert_move(int(input(turn + " Enter your move (1-9):\n")))
            if board.set_Move(x,y,turn):
                print(board)
            else:
                print("Invalid move")
                move(mode,board,turn)
        #AI move handling
        else:
            print(turn + " is deciding")
            bot_move(board,turn)
            print(board)

#Determines best possible move for the AI
#The worst outcome it will allow for is a tie
def bot_move(board,turn):
    bestScore = float("-inf")
    for i in range(9):
        x,y = convert_move(i+1)
        #Attempts the move and passes in the next turn as the human player
        if board.set_Move(x,y,turn):
            score = minimax(board, 0, 'X')
            board.play_field[x][y] = i+1
            if score > bestScore:
                bestScore = score
                bot_x, bot_y = (x,y)
    board.set_Move(bot_x, bot_y, turn)
        
#AI ('O') is maximizing player | human ('X') is minimizing player
#Minimax tries every possible final state of the board to determine its best move
#assumes the human is trying to maximize it's score
def minimax(board, depth, turn):
    p_inf = float("inf")
    n_inf = float("-inf")
    if check_win(board,'O'): return 1
    if check_win(board,'X'): return -1
    if check_tie(board): return 0
    #Maximizing turn
    if turn == 'O':
        bestScore = n_inf
        for i in range(9):
            x,y = convert_move(i+1)
            if board.set_Move(x,y,'O'):
                score = minimax(board, depth+1, 'X')
                board.play_field[x][y] = i+1
                if score > bestScore:
                    bestScore = score
        return bestScore
    #Minimizing turn
    else:
        bestScore = p_inf
        for i in range(9):
            x,y = convert_move(i+1)
            if board.set_Move(x,y,'X'):
                score = minimax(board, depth+1, 'O')
                board.play_field[x][y] = i+1
                if score < bestScore:
                    bestScore = score
        return bestScore

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
