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

        ft_made = sum(1 for _ in range(2) if random.random() < opponent_free_throw_percent)

        if ft_made == 0:
            # Opponent misses both chances to score

            if random.random() < three_point_percentage:
                wins_foul += 1
                points_foul += 3
            else:
                if random.random() < offensive_rebound_prob:
                    if random.random() < two_point_percentage:
                        if random.random() < overtime_win_prob:
                            wins_foul += 1 
                        points_foul += 2
                    else: 
                        points_foul += 0
                else:
                    points_foul += 0   
        elif ft_made == 1:
            if random.random() < three_point_percentage:
                if random.random() < overtime_win_prob:
                    wins_foul += 1
                else:
                    points_foul += 3
            else:
                points_foul += 0
        else:
            # opp makes both- need 3 to tie
            if random.random() < three_point_percentage:
                wins_foul += 3
            else:
                points_foul += 0   

    #results
    results_text = (
        "== Simulation Results==\n"
        f"Trials: {trials}\n\n"
        "Strategy A: Take 3-pointer\n"
        f"Win % {wins_three / trials * 100:.2f}%\n"
        f"Avg Points: {points_three / trials:.2f}\n\n"
        "Strategy B: Foul Opponent \n"
        f"win %: {wins_foul / trials * 100:.2f}%\n"
        f"Avg points: {points_foul / trials:.2f}\n" 
    )
    #write results in text file
    f = open("BasketBall_Information.txt", "w")
    f.write(results_text)
    f.close()

    print(results_text) 
simulate_endgame()                                   




