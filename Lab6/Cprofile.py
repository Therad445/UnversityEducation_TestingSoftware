import math
import multiprocessing
import cProfile


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


def profile(func):
    """Decorator for run function profile"""
    def wrapper(*args, **kwargs):
        profile_filename = func.__name__ + '.prof'
        profiler = cProfile.Profile()
        result = profiler.runcall(func, *args, **kwargs)
        profiler.dump_stats(profile_filename)
        return result
    return wrapper


@profile
def main():
    pool = multiprocessing.Pool()
    results = pool.map(prime_factors, range(1, 10001))
    for i in range(len(results)):
        str_out = ""
        for elem in results[i]:
            str_out = str_out + " " + str(elem)
        print(str(i) + " = " + str_out)


if __name__ == '__main__':
    main()