from BoardClass import Board

class TicTacToe(Board):
        def check_win(self,player):
        in_a_row = [player]*self.width
        rows = self.rows()
        cols = self.cols()
        diags = self.diags()
        for i in range(self.width):
            if in_a_row == rows[i] or in_a_row == cols[i]:
                return True
            elif in_a_row == diags[0] or in_a_row == diags[1]:
                return True
        return False
