import unittest
from statistics_service import StatisticsService
from player import Player
from enum import Enum

class SortByStub(Enum):
    POINTS = 1
    GOALS = 2
    ASSISTS = 3
    TEST = 4

class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),
            Player("Lemieux", "PIT", 45, 54),
            Player("Kurri",   "EDM", 37, 53),
            Player("Yzerman", "DET", 42, 56),
            Player("Gretzky", "EDM", 35, 89)
        ]

class TestStatisticsService(unittest.TestCase):
    def setUp(self):
        # annetaan StatisticsService-luokan oliolle "stub"-luokan olio
        self.stats = StatisticsService(
            PlayerReaderStub()
        )

    def test_search_name_in_player_list(self):
        players = PlayerReaderStub().get_players()

        self.assertEqual(players[0].name, self.stats.search('Semenko').name)

    def test_search_name_not_in_player_list(self):
        self.assertEqual(None, self.stats.search('Testi'))

    def test_search_team_on_list(self):
        players = PlayerReaderStub().get_players()

        self.assertEqual(players[1].name, self.stats.team('PIT')[0].name)

    def test_sorting_players_by_points(self):
        self.assertEqual(['Gretzky', 'Lemieux', 'Yzerman', 'Kurri', 'Semenko'], 
                  [i.name for i in self.stats.top(4, SortByStub.POINTS)]                  
        )

    def test_sorting_players_by_goals(self):
        self.assertEqual(['Lemieux', 'Yzerman', 'Kurri', 'Gretzky', 'Semenko'], 
                  [i.name for i in self.stats.top(4, SortByStub.GOALS)]                  
        )

    def test_sorting_players_by_assists(self):
        self.assertEqual(['Gretzky', 'Yzerman', 'Lemieux', 'Kurri', 'Semenko'], 
                  [i.name for i in self.stats.top(4, SortByStub.ASSISTS)]                  
        )

    def test_sorting_players_by_nonexisting_value(self):
        self.assertEqual(None, self.stats.top(4, SortByStub.TEST))