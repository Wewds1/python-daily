"""
Nth Prime
A prime number is a positive integer greater than 1 that is divisible only by 1 and itself.
The first five prime numbers are 2, 3, 5, 7, and 11.

Given a positive integer n, return the nth prime number. 
For example, given 5 return the 5th prime number: 11.
"""


def nth_prime(n):
    prime_count = 0
    num = 2
    while prime_count != n:
        if is_prime(num):
            prime_count += 1
        num+=1


    return num -1


def is_prime(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    else:
        return True

print(nth_prime(5))

