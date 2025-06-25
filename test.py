from collections import Counter

def prime_factors(n):
    i = 2
    factors = []
    while i * i <= n:
        while n % i == 0:
            factors.append(i)
            n //= i
        i += 1
    if n > 1:
        factors.append(n)
    return Counter(factors)  # Dictionary of prime: count

# def lcm_by_prime_factorization(a, b):
#     factors_a = prime_factors(a)
#     factors_b = prime_factors(b)

#     lcm_factors = factors_a.copy()
#     for prime in factors_b:
#         lcm_factors[prime] = max(lcm_factors.get(prime, 0), factors_b[prime])

#     # Multiply primes raised to their max powers
#     lcm = 1
#     for prime in lcm_factors:
#         lcm *= prime ** lcm_factors[prime]

#     return lcm

# # Example
# print("LCM (24, 90):", lcm_by_prime_factorization(24, 90))
prime_factors(27)