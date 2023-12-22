import multiprocessing
from main import prime_factors


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