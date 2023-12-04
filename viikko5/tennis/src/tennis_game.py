from enum import Enum

class Points(Enum):
    Love = 0
    Fifteen = 1
    Thirty = 2
    Forty = 3

class Player():
    def __init__(self, name):
        self.name = name
        self.points = 0

class TennisGame:
    def __init__(self, player1_name, player2_name):
        self.player1 = Player(player1_name)
        self.player2 = Player(player2_name)
        self.ad_limit = 3


    def won_point(self, player_name):
        if player_name == self.player1.name:
            self.player1.points += 1
        else:
            self.player2.points += 1

    def even_points(self, points):
        if points < self.ad_limit:
            return f"{Points(points).name}-All"
        else:
            return "Deuce"
        
    def advantage_or_win(self, winning: Player, losing: Player):
        difference = winning.points - losing.points
        if difference == 1:
            return "Advantage"
        else:
            return "Win for"
        
    def compare_points(self):
        if self.player1.points > self.player2.points:
            return [self.player1, self.player2]
        else:
            return [self.player2, self.player1]
        
    def advantage(self):
        comparison = self.compare_points()
        winning = comparison[0]
        losing = comparison[1]

        return f"{self.advantage_or_win(winning, losing)} {winning.name}"

    def get_score(self):
        p1_points = self.player1.points
        p2_points = self.player2.points

        if p1_points == p2_points:
            score = self.even_points(p1_points)

        elif p1_points > self.ad_limit or p2_points > self.ad_limit:
            score = self.advantage()
            
        else:
            score = f"{Points(p1_points).name}-{Points(p2_points).name}"

        return score
