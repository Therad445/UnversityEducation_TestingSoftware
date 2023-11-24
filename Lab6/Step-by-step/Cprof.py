import profile
import threading
import cProfile

def factorize(n):
    # Calculate the factorization of n
    factors = []
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            factors.append(i)
            n = n // i
            if n == 1:
                break
    return factors

def main():
    # Set the number of threads
    n = 10

    # Create a list of threads
    threads = []
    for i in range(n):
        t = threading.Thread(target=factorize, args=(i,))
        threads.append(t)
        t.start()

    # Wait for all threads to finish
    for t in threads:
        t.join()

if __name__ == '__main__':
    main()

# Run the program with profiling
cProfile.run('main()')

# Print the profiling results
print(cProfile.get_stats())