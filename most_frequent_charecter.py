charecter = "hello world"
splillted_strig = list(charecter)

my_dict = {}

for i in charecter:
    my_dict[i] = charecter.count(i)


count_item = {}
count = 0
for key,val in my_dict.items():
    if val>count:
        count = val
        count_item = {key:val}

print(count_item)


# Bonus
# deleting first item from a dictionary 

my_dict = {"a":1,"b":2,"c":3}

iterator = iter(my_dict)
key = next(iterator)

my_dict.pop(key)
print(my_dict)
    

    