import threading


def prime_decomposition(start, step):
    for i in range(start, 100, step):
        if i <= 1:
            return
        for j in range(2, int(i**0.5) + 1):
            if i % j == 0:
                print(f"Found factor {j} for {i}")


def main():
    num_threads = 4  # Number of threads
    threads = []
    for i in range(num_threads):
        t = threading.Thread(target=prime_decomposition, args=(i + 1, num_threads))
        threads.append(t)
        t.start()
    for t in threads:
        t.join()


if __name__ == "__main__":
    main()
