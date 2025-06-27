# generating fibonacci sequence 


def finding_fibonaci_number(n):
    a = 0
    b = 1
    count = 3

    while count <=n:
        c = a + b
        a,b = b,c

        count +=1
    return(c)
print(finding_fibonaci_number(6))

# using recursion 


def fibonaci_recursive_approach(n):
    if n<1:
        print("incorrect input")

    elif n == 0:
        return 0
    elif n ==1 or n == 2:
        return 1
    
    else:
        return fibonaci_recursive_approach(n-1) + fibonaci_recursive_approach(n-2)

print(fibonaci_recursive_approach(3))