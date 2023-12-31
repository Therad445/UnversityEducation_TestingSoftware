import math

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
    for i in range(1, 2001):
        factors = prime_factors(i)
        str_out = ""
        for elem in factors:
            str_out = str_out + " " + str(elem)
        # print(str(i) + " = " + str_out)


if __name__ == '__main__':
    main()