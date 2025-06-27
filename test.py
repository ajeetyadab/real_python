import random 
toss =[]
for i in range(1000000):
    if random.randint(0,1) == 0:
       toss.append(0)
    else:
       toss.append(1)
       
streak_count_tail = 0
streak_list_tail = [0]
for i in toss:
 
    if i == 1:
        streak_count_tail +=1
    else:
        if streak_count_tail > streak_list_tail[0]:
            streak_list_tail = [streak_count_tail]
        streak_count_tail = 0

    
   
print(streak_list_tail)


