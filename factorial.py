# Write a program to find the factorial of a number
def factorial_solution(n):

    solution = 1

    while n > 1:
        solution *=n 
        n -=1


    return solution

print(factorial_solution(7))
print(7*6*5*4*3*2)
        
