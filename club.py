from player import PlayerStats


# class to store basic data about the club

class TeamStats:
    def __init__(self, name, manager=None, players=None,
                 team_record="0-0-0", points=0, points_per_game=0.0,
                 position=None, home_record=None, home_points=0,
                 away_record=None, away_points=0,
                 xG=0.0, xGA=0.0):
        self.name = name
        self.manager = manager
        self.players = players if players is not None else []
        self.points = points
        self.points_per_game = points_per_game
        self.position = position
        self.home_record = home_record
        self.home_points = home_points
        self.away_record = away_record
        self.away_points = away_points
        self.xG = xG
        self.xGA = xGA
        self.xG_difference = xG - xGA

    def add_player(self, player: PlayerStats):
        self.players.append(player)

    def __repr__(self):
        return (f"Team(name='{self.name}', Manager='{self.manager}', "
                f"Player count={len(self.players)} players, Record='{self.team_record}', "
                f"Points={self.points}, Points_per_game={self.points_per_game}, "
                f"League position={self.position}, Home record={self.home_record}, Home points={self.home_points}, "
                f"Away record={self.away_record}, Away points={self.away_points}, "
                f"xG={self.xG}, xGA={self.xGA}, xG_difference={self.xG_difference})")
