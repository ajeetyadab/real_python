strings = "madam"



def is_palindrome(strings):
    reversed_string = reversed(strings)
    reversed_string = "".join(reversed_string)

    if strings.lower() == reversed_string.lower():
        print("its a palindrome")

    else:
        print("its not a palindrome")

is_palindrome("Modam")




