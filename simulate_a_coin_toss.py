import random 

def coin_toss(n):
   
    
    count_list = []
    for i in range(n):
        toss = []
        count = 0
        is_both_side_attained = False

        while not is_both_side_attained:
            n = random.randint(0,1)
            if n == 0 :
                toss.append("tails")

            if n == 1 :
                toss.append("heads")

            count = count+1

        

            if "heads" in toss and "tails" in toss:
            
                is_both_side_attained = True
                # print(toss)
                # print(count)
                count_list.append(count)

    return count_list
        


x= coin_toss(1000)
print(sum(x)/len(x))


        



