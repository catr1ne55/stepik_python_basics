import itertools


def primes():
    prime = 2
    while True:
        for i in range(2, prime - 1):
            if prime % i == 0:
                break
        else:
            yield prime
        prime += 1


print(list(itertools.takewhile(lambda x: x <= 4, primes())))
