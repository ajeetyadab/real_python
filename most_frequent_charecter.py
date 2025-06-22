charecter = "hello worlds"



def count_max_charecter(string):
    my_dict = {}
    count_item = {}
    count = 0

    for i in string:
        my_dict[i] = charecter.count(i)



    for key,val in my_dict.items():
        if val>count:
            count = val
            count_item = {key:val}

    return count_item



# Bonus
# deleting first item from a dictionary 

my_dict = {"a":1,"b":2,"c":3}

iterator = iter(my_dict)
key = next(iterator)

my_dict.pop(key)
print(my_dict) 
    

    