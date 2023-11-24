import math
import multiprocessing


def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


def prime_factors(n):
    factors = []
    for i in range(2, n + 1):
        if is_prime(i):
            while n % i == 0:
                factors.append(i)
                n //= i
    return factors


def main():
    pool = multiprocessing.Pool()
    results = pool.map(prime_factors, range(1, 101))
    print(results)


if __name__ == '__main__':
    main()
