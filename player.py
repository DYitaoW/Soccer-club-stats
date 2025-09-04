class PlayerStats:
    def __init__(self, name, position):
        self.name = name
        self.position = position  # GK, DEF, MID, ATT

        # Initialize all possible stats with default values -1 or -1.0
        self.stats = {
            "goals_allowed": -1,
            "goals_per_90": -1.0,
            "saves": -1,
            "save_percent": -1.0,
            "clean_sheets": -1,
            "pk_saved": -1,
            "net_psxG": -1.0,
            "pass_percent_launched": -1.0,
            "passes": -1,
            "avg_pass_length": -1.0,
            "goal_kick_percent_launched": -1.0,
            "avg_goal_kick_length": -1.0,
            "def_actions_outside_box_per90": -1.0,
            "passes_completed": -1,
            "passes_attempted": -1,
            "pass_completion_percent": -1.0,
            "short_pass_completion_percent": -1.0,
            "long_pass_completion_percent": -1.0,
            "medium_pass_completion_percent": -1.0,
            "assists": -1,
            "interceptions": -1,
            "clearances": -1,
            "errors": -1,
            "miscontrols": -1,
            "dispossessed": -1,
            "total_minutes": -1,
            "games_starting": -1,
            "games_sub": -1,
            "unused_sub": -1,
            "yellow_cards": -1,
            "red_cards": -1,
            "fouls": -1,
            "fouled": -1,
            "ball_recoveries": -1,
            "aerials_won": -1,
            "aerials_lost": -1,
            "aerials_win_percent": -1.0,
            "goals": -1,
            "shots": -1,
            "avg_shot_distance": -1.0,
            "xG": -1.0,
            "non_pen_xG_per_shot": -1.0,
            "passes_into_final_3rd": -1,
            "pass_xA": -1.0,
            "assisted_shots": -1,
            "crosses": -1,
            "progressive_passes": -1,
            "sca_per_90": -1.0,
            "gca_per_90": -1.0,
            "challenge_tackles": -1,
            "challenges_lost": -1,
            "challenge_percent": -1.0,
            "touches_def_3rd": -1,
            "touches_mid_3rd": -1,
            "touches_att_3rd": -1,
            "progressive_carries": -1,
            "carries_into_final_3rd": -1,
            "minutes_per_game": -1,
            "on_xG_for": -1.0,
            "on_xG_against": -1.0,
            "xG_plus_minus_per_90": -1.0,
            "blocks": -1,
            "blocked_shots": -1,
            "blocked_passes": -1,
            "tackles_def_3rd": -1,
            "tackles_mid_3rd": -1,
            "tackles_att_3rd": -1,
            "touches_pen_area": -1,
            "take_ons": -1,
            "take_on_win_percent": -1.0,
            "take_on_tackled_percent": -1.0,
            "carries_into_pen_area": -1,
            "offsides": -1,
            "pens_won": -1,
            "pens_conceded": -1,
            "shot_on_target_percent": -1.0,
            "shots_per_90": -1,
            "shots_on_target_per_90": -1.0,
            "goals_per_shot": -1.0,
            "goals_per_shot_on_target": -1.0,
            "pens_made": -1,
            "pens_attempted": -1,
            "non_pen_xG": -1.0,
            "net_xG": -1.0
        }

    def __repr__(self):
        if self.position == "GK":
            return (f"PlayerStats(name='{self.name}', position='{self.position}', "
                    f"goals_allowed={self.stats.get('goals_allowed')}, "
                    f"goals_per_90={self.stats.get('goals_per_90')}, "
                    f"saves={self.stats.get('saves')}, "
                    f"save_percent={self.stats.get('save_percent')}, "
                    f"clean_sheets={self.stats.get('clean_sheets')}, "
                    f"pk_saved={self.stats.get('pk_saved')})")
        elif self.position == "DEF":
            return (f"PlayerStats(name='{self.name}', position='{self.position}', "
                    f"tackles_def_3rd={self.stats.get('tackles_def_3rd')}, "
                    f"blocks={self.stats.get('blocks')}, "
                    f"clearances={self.stats.get('clearances')}, "
                    f"errors={self.stats.get('errors')})")
        elif self.position == "ATT":
            return (f"PlayerStats(name='{self.name}', position='{self.position}', "
                    f"goals={self.stats.get('goals')}, "
                    f"assists={self.stats.get('assists')}, "
                    f"shots={self.stats.get('shots')}, "
                    f"xG={self.stats.get('xG')})")
        else:  # MID or unknown
            return (f"PlayerStats(name='{self.name}', position='{self.position}', "
                    f"goals={self.stats.get('goals')}, "
                    f"assists={self.stats.get('assists')}, "
                    f"passes_completed={self.stats.get('passes_completed')}, "
                    f"xG={self.stats.get('xG')})")
