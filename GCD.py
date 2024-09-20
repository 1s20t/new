def gcd(a, b): # greatest common Divisor Algorithm
    while b:
        a, b = b, a % b
    return a

print(gcd(91, 35))
