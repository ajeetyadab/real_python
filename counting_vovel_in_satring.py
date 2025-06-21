strings = "A \"string\" can refer to several things, but most commonly it means a sequence of characters used to represent text in\
computer programming. It can also refer to a thin, flexible length of \
material used for tying or fastening, or to a series of related things or \
events. Additionally, in physics, a string is a theoretical one-dimensional entity."


def count_vovels(string):
    a = 0
    e = 0
    I = 0
    o = 0
    u = 0
    for i in strings:
        if i == "a".lower():
            a +=1
        if i == "e".lower():
            e +=1
        if i == "i".lower():
            I +=1
        if i == "o".lower():
            o+=1
        if i == "u".lower():
            u+=1
    print(f" a = {a}, e = {e} ,i = {I} , o = {o} , u = {u} ")

count_vovels(strings)
        




