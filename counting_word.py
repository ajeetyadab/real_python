def counting_word_in_string(string):
    list_of_string = string.split(" ")
    return len(list_of_string)


string = "hi how are you doing today"

print(f" words is a given string is : {counting_word_in_string(string)}")
