number1 = 8
number2 = 12

# #4 finding prime numbers

# def finding_factors(number):
#     factors = []
#     for i in range(1,number+1):
#         if number % i == 0:
#             factors.append(i)

#     return factors

# factors1 = finding_factors(number1)
# factors2 = finding_factors(number2)

# print(factors1)
# print(factors2)
        
# def finding_prime_factors(factors):
#     prime_factors = []
#     for i in factors:
#         is_prime = True
#         for j in range(1,i):
           
#             if  (j !=1):
#                 if i% j == 0:
#                     is_prime = False
#                     break

#         if is_prime and i !=1 :
#             prime_factors.append(i)
            
#     return prime_factors

# print(finding_prime_factors(factors1),finding_prime_factors(factors2))


def finding_gcd(number1,number2):
        while number2 :

            number1,number2 = number2, number1%number2

        return number1
      


print(finding_gcd(6,90))


def finding_lcm(n1,n2):
    gcd = finding_gcd(n1,n2)
    lcm = (n1*n2)//gcd

    return lcm

# print(finding_lcm(21,45))