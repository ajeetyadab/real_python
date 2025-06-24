string = "hello world how are you"



    
def capitalised_string(string):
    capitalised_strig = ""

    splitted_string = string.split(" ")

    capitalised_string = ""

    for i in splitted_string:
        random_var = i.capitalize()
        capitalised_strig = capitalised_strig +" "+ random_var

    return capitalised_strig

print(capitalised_string(string))