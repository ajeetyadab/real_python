number = int(input("Please enter the number"))

def finding_factor(number):
    for i in range(1,number+1):
        if number % i ==0:
            print(f"{i} is factor of {number}")

finding_factor(number)