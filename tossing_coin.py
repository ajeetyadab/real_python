import random

def flipping_fair_coin(n):
    heads = 0
    tails = 0

    for i in range(n):
        if random.randint(0,1) == 0:
            tails +=1

        else:
            heads +=1

    ratio = round(heads/tails,2)

    return ratio

print(flipping_fair_coin(1000))




def flipping_unfair_coin(n):
    heads = 0
    tails = 0
    for i in range(n):
        if random.random()<=.85:
            tails +=1

        else:
            heads +=1

    ratio = round(heads/tails,2)

    return ratio


print(flipping_unfair_coin(1000))


