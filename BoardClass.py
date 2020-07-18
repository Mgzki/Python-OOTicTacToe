class Board:

    def __init__(self, n, m):
        self.width = n
        self.length = m
        self.play_field = []
    #creates an NxM sized board
    def create_Board(self):
        for i in range(self.width):
            self.play_field.insert(i,[])
            for j in range(self.length):
                self.play_field[i].insert(j,None)

    #Updates board state with player move if available
    def set_Move(self, n, m, player):
        if self.play_field[n][m] is not None:
            return False
        self.play_field[n][m] = player
        return True
    #Returns if there are any moves available
    def full_Board(self):
        for row in self.play_field:
            for col in row:
                if col is None:
                    return False
        return True

    #Returns current board state by rows
    def rows(self):
        return self.play_field
    #Returns current board state by columns
    def cols(self):
        columns = []
        for i in range(self.width):
            columns.insert(i,[])
            for j in range(self.length):
                columns[i].insert(j,self.play_field[j][i])
        return columns
    #Returns current board state's diagonals, for use in square shaped boards
    def diags(self):
        #only two diagonals possible
        diags = [[],[]]
        #top-left to bottom-right
        for i in range(self.width):
            j = i
            diags[0].insert(i,self.play_field[i][j])
        #top-right to bottom-left
        j = self.length - 1
        for i in range(self.width):
            diags[1].insert(i,self.play_field[i][j])
            j -=1
        return diags

