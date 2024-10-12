def is_good_or_bad(P, K):
    sieve = [True] * K
    sieve[0] = sieve[1] = False
    primes = []
    for i in range(2, K):
        if sieve[i]:
            primes.append(i)
            for j in range(i * i, K, i):
                sieve[j] = False
    for prime in primes:
        if P % prime == 0:
            t = min(prime, P // prime)
            print(f"BAD {t}")
            return
    print("GOOD")
P, K = map(int,input().split())
is_good_or_bad(P, K)