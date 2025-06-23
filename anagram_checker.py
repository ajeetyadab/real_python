string1 = "Astronomer"
string2 = "Moon starer"

# string1 = string1.replace(" ","")
# string2 = string2.replace(" ","")

# string1 = string1.lower()
# string2 = string2.lower()

# # lenth must be equal
# # charecter count must be equal


# string1_count_dict = {}
# string2_count_dict = {}

# count = 1 

# for i in string1:
#     string1_count_dict[i] = count

# for i in string2:
#     string2_count_dict[i] = string2.count(i)

# print(string1_count_dict)
# print(string2_count_dict)


# if (string1_count_dict == string2_count_dict) and (len(string1)== len(string2)):
#     print("they are anagram ")




## improved version 
# earlier i had used count method in the loop which is making it inefficient


def palingram_checker(string1,string2):
    string1 = string1.replace(" ","")
    string2 = string2.replace(" ","")

    string1 = string1.lower()
    string2 = string2.lower()

    string1_count_dict = {}
    string2_count_dict = {}

    for char in string1:
        if char in string1_count_dict:
            string1_count_dict[char] =+1
        else:
            string1_count_dict[char] = 1

    for char in string2:
        if char in string2_count_dict:
            string2_count_dict[char] =+1
        else:
            string2_count_dict[char] = 1

    if string1_count_dict == string2_count_dict:
        print("Its a palingram")

    else:
        print("Its not a palingram")

palingram_checker(string1,string2)

