import threading

def prime_decomposition(n):
    if n <= 1:
        return
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            print(f"Found factor {i} for {n}")

def main():
    num_threads = 4  # Number of threads
    for i in range(num_threads):
        t = threading.Thread(target=prime_decomposition, args=(i*num_threads + 1, num_threads))
        t.start()

if __name__ == "__main__":
    main()