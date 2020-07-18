class Player:
    def __init__(self, symbol, score):
        self.symbol = symbol
        self.score = score

    def win(self):
        self.score += 1

    def tie(self):
        self.score += 0

    def lose(self):
        self.score -= 1

    def show_score(self):
        print('Player {}: {} points'.format(self.symbol, self.score))