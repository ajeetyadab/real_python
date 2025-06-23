

string = "hello world what a sunny day today"

# TODO
# longest substring - first split the string into substring
# now finding duplicate charecters in the word



string = "longest substring  first split the string into substring "

splitted_string = string.split()
print(splitted_string)

count_dict = {}

s = set()
l = []
temp_list = []
for word in splitted_string:
    for char in word:
        if char not in s:
            s.add(char)
            temp_list.append(char)

        else:
            s = set()
            temp_list = []
            break
    if temp_list != []  and temp_list != [","] and temp_list != [" "]:
        l.append("".join(temp_list))
        s = set()
        temp_list = []
print(l)