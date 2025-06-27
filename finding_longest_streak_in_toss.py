# suppose two captains are flipping the coin and we want to see longest streak of heads of tails

import random
def counting_streak(n):
    toss = []
    for i in range(n):
        if random.randint(0,1) == 0:
            toss.append("T")

        else:
            toss.append("H")

    print(toss)

    
    streak_count_tail = -1
    streak_list_tail = [0]
    for i in toss:
 
        if i == "T":
            streak_count_tail +=1
        else:
            if streak_count_tail > streak_list_tail[0]:
                streak_list_tail = [streak_count_tail]
                streak_count_tail = 0


    streak_count_head = -1
    streak_list_head = [0]
    for i in toss:
 
        if i == "H":
            streak_count_head +=1
        else:
            if streak_count_head > streak_list_head[0]:
                streak_list_head = [streak_count_head]
                streak_count_head = 0

    return f" tails streak is {streak_list_tail} and heads streak is {streak_list_head}"


print(counting_streak(10))

