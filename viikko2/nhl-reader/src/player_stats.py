from player_reader import PlayerReader

class PlayerStats():
    def __init__(self, reader):
        self.reader = reader

    def top_scorers_by_nationality(self, nationality):
        all_players = self.reader.get_players()
        players = list(filter(lambda x: x.nationality == nationality, all_players))
        players.sort(key=lambda x: x.points, reverse=True)

        return players