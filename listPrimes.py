def main():
    N = int(input())

    primes = allPrimes(N)
    print(primes)

def allPrimes(N):
    primes = []

    if N >= 2:
        primes.append(2)
    
    for i in range(3, N + 1, 2):
        isPrime = True
        for p in primes:
            if i % p == 0:
                isPrime = False
                break
        if isPrime:
            primes.append(i)

    return primes


if __name__ == '__main__':
    main()