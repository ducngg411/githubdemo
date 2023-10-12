import math

def is_prime(n):
    if n <= 1:
        return False

    return all(n % i != 0 for i in range(2, int(math.sqrt(n)) + 1))

def print_primes(n):
    primes = []
    for num in range(2, n + 1):
        if is_prime(num):
            primes.append(num)

    for prime in primes:
        print(prime)

print_primes(20)
