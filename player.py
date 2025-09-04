class PlayerStats:
    def __init__(self, name, position):
        self.name = name
        self.position = position  # GK, DEF, MID, ATT
        self.stats = {}


        # GK stats
        
        if self.position == "GK":
            self.stats.update({
                "goals_allowed": 0,
                "goals_per_90": 0.0,
                "saves": 0,
                "save_percent": 0.0,
                "net_psxG": 0.0,
                "pass_percent_launched": 0.0,
                "passes": 0,
                "avg_pass_length": 0.0,
                "goal_kick_percent_launched": 0.0,
                "avg_goal_kick_length": 0.0,
                "def_actions_outside_box_per90": 0.0,
                "passes_completed": 0,
                "passes_attempted": 0,
                "pass_completion_percent": 0.0,
                "short_pass_completion_percent": 0.0,
                "long_pass_completion_percent": 0.0,
                "medium_pass_completion_percent": 0.0,
                "assists": 0,
                "interceptions": 0,
                "clearances": 0,
                "errors": 0,
                "miscontrols": 0,
                "dispossessed": 0,
                "total_minutes": 0,
                "games_starting": 0,
                "games_sub": 0,
                "unused_sub": 0,
                "yellow_cards": 0,
                "red_cards": 0,
                "fouls": 0,
                "fouled": 0,
                "ball_recoveries": 0,
                "aerials_won": 0,
                "aerials_lost": 0,
                "aerials_win_percent": 0.0
            })


        # stats for all outfielders

        else:
            general_stats = {
                "goals": 0,
                "shots": 0,
                "avg_shot_distance": 0.0,
                "xG": 0.0,
                "non_pen_xG_per_shot": 0.0,
                "passes_completed": 0,
                "passes_attempted": 0,
                "pass_completion_percent": 0.0,
                "short_pass_completion_percent": 0.0,
                "long_pass_completion_percent": 0.0,
                "medium_pass_completion_percent": 0.0,
                "assists": 0,
                "passes_into_final_3rd": 0,
                "pass_xA": 0.0,
                "assisted_shots": 0,
                "crosses": 0,
                "progressive_passes": 0,
                "sca_per_90": 0.0,
                "gca_per_90": 0.0,
                "challenge_tackles": 0,
                "challenges_lost": 0,
                "challenge_percent": 0.0,
                "interceptions": 0,
                "clearances": 0,
                "errors": 0,
                "touches_def_3rd": 0,
                "touches_mid_3rd": 0,
                "touches_att_3rd": 0,
                "progressive_carries": 0,
                "carries_into_final_3rd": 0,
                "miscontrols": 0,
                "dispossessed": 0,
                "total_minutes": 0,
                "minutes_per_game": 0,
                "games_starting": 0,
                "games_sub": 0,
                "unused_sub": 0,
                "on_xG_for": 0.0,
                "on_xG_against": 0.0,
                "xG_plus_minus_per_90": 0.0,
                "yellow_cards": 0,
                "red_cards": 0,
                "fouls": 0,
                "fouled": 0,
                "ball_recoveries": 0,
                "aerials_won": 0,
                "aerials_lost": 0,
                "aerials_win_percent": 0.0
            }
            self.stats.update(general_stats)

            # extra stats for defenders

            if self.position == "DEF":
                self.stats.update({
                    "blocks": 0,
                    "blocked_shots": 0,
                    "blocked_passes": 0,
                    "tackles_def_3rd": 0,
                    "tackles_mid_3rd": 0,
                    "tackles_att_3rd": 0,
                    "pens_conceded": 0
                })

            # extra stats for attackers

            elif self.position == "ATT":
                self.stats.update({
                    "shot_on_target_percent": 0.0,
                    "shots_per_90": 0,
                    "shots_on_target_per_90": 0.0,
                    "goals_per_shot": 0.0,
                    "goals_per_shot_on_target": 0.0,
                    "pens_made": 0,
                    "pens_attempted": 0,
                    "non_pen_xG": 0.0,
                    "net_xG": 0.0,
                    "tackles_att_3rd": 0,
                    "touches_pen_area": 0,
                    "take_ons": 0,
                    "take_on_win_percent": 0.0,
                    "take_on_tackled_percent": 0.0,
                    "carries_into_pen_area": 0,
                    "offsides": 0,
                    "pens_won": 0
                })

            # extra stats for midfielders, midfielders have all available stats

            else:
                self.stats.update({
                    "shot_on_target_percent": 0.0,
                    "shots_per_90": 0,
                    "shots_on_target_per_90": 0.0,
                    "goals_per_shot": 0.0,
                    "goals_per_shot_on_target": 0.0,
                    "pens_made": 0,
                    "pens_attempted": 0,
                    "non_pen_xG": 0.0,
                    "net_xG": 0.0,
                    "blocks": 0,
                    "blocked_shots": 0,
                    "blocked_passes": 0,
                    "tackles_def_3rd": 0,
                    "tackles_mid_3rd": 0,
                    "tackles_att_3rd": 0,
                    "touches_pen_area": 0,
                    "take_ons": 0,
                    "take_on_win_percent": 0.0,
                    "take_on_tackled_percent": 0.0,
                    "carries_into_pen_area": 0,
                    "offsides": 0,
                    "pens_won": 0,
                    "pens_conceded": 0
                })

    def __repr__(self):
        return f"PlayerStats(name='{self.name}', position='{self.position}', stats={self.stats})"