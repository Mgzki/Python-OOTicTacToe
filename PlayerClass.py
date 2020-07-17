class Player:
    def __init__(self, name, symbol, score):
        self.name = name
        self.symbol = symbol
        self.score = score

    def win(self):
        self.score += 1

    def tie(self):
        self.score += 0

    def lose(self):
        self.score -= 1

    def show_score(self):
        print('Player {}({}): {} points'.format(self.name, self.symbol, self.score))