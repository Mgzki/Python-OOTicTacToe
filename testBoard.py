from BoardClass import Board
from TicTacToeClass import TicTacToe
from PlayerClass import Player

test = Board(3,3)
test.create_Board()
test.show_Board()
print(test.full_Board())
test.set_Move(0,0,'a')
test.set_Move(0,1,'b')
test.set_Move(0,2,'c')

test.set_Move(1,0,'d')
test.set_Move(1,1,'e')
test.set_Move(1,2,'f')

test.set_Move(2,0,'g')
test.set_Move(2,1,'h')
test.set_Move(2,2,'i')

a=TicTacToe(3,3)
a.create_Board()

a.set_Move(0,0,'X')
a.set_Move(0,1,'X')
a.set_Move(0,2,'X')

a.set_Move(1,0,'d')
a.set_Move(1,1,'e')
a.set_Move(1,2,'f')

a.set_Move(2,0,'g')
a.set_Move(2,1,'h')
a.set_Move(2,2,'i')

print(a.rows())
print(a.cols())
print(a.diags())
print(a.check_win('X'))

