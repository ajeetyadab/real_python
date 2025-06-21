strings = "hello world"




def reversing_string_without_slice(strings):
    """ reversing a string without using slice"""

    j = ""
    for i in range(0,len(strings)):
        j = j+strings[len(strings)-i-1]

    return j 


print(reversing_string_without_slice(strings))