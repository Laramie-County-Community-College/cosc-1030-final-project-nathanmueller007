   # Here is all of the code for the final project

import random

# my teams shooting percentages
three_point_percentage = 0.35

two_point_percentage = 0.50

    # Opponents free throw percentage

opponent_free_throw_percent = 0.60

# time remaining
time_remaining = 30

offensive_rebound_prob = 0.25

overtime_win_prob = 0.50

num_trials = 1000

def simulate_endgame(trials=num_trials):
    wins_three, points_three = 0, 0
    wins_foul, points_foul = 0, 0

    for _ in range(trials):

        # Strategy A: Take 3- pointer
        if random.random() < three_point_percentage:
            wins_three += 1
            points_three += 3
        else: 
            # Missed shot chance for offensive rebound
            if random.random() < offensive_rebound_prob:
                if random.random() < two_point_percentage:
                    #Tie game - goes into overtime

                    if random.random() < overtime_win_prob:
                        wins_three += 1
                    points_three += 2
                else:
                    points_three += 0
            else: 
                points_three += 0




