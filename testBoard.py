from BoardClass import Board
from PlayerClass import Player
import random

a=Board(3,3)
a.create_Board()
'''
a.set_Move(0,0,'X')
a.set_Move(0,1,'X')
a.set_Move(0,2,'X')

a.set_Move(1,0,'d')
a.set_Move(1,1,'e')
a.set_Move(1,2,'f')

a.set_Move(2,0,'g')
a.set_Move(2,1,'h')
a.set_Move(2,2,'i')
'''
print(a.rows())
print(a.cols())
print(a.diags())

def check_win(board,player):
    in_a_row = [player]*board.width
    rows = board.rows()
    cols = board.cols()
    diags = board.diags()
    for i in range(board.width):
        if in_a_row == rows[i] or in_a_row == cols[i]:
            return True
        elif in_a_row == diags[0] or in_a_row == diags[1]:
            return True
    return False

def first():
    global turn
    val = random.random()
    turn = 'X' if val <= 0.5 else 'O'

def setup():
    global turn,board
    board = Board(3,3)
    board.create_Board
    players = [Player('X'),Player('O')]
    first()
    
    if num_players():        
        print("You are 'X'")

def num_players():
    num = int(input("How many players?\n Default is 1"))
    return True if num == 2 else False

print(check_win(a,'X'))
