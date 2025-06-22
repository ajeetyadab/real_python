strings = "hello"




def remove_duplicates_from_strings(strings):
    s = set()
    my_list = []
    for char in strings:
        if char not in s:
            s.add(char)
            my_list.append(char)
    return "".join(my_list)


print(remove_duplicates_from_strings(strings))