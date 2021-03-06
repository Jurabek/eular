def primes():
    yield 2
    ps = [2]
    n = 3
    while True:
        for p in ps:
            if n % p == 0:
                break
            if p**2 >= n:
                ps.append(n)
                yield n
                break
        n += 2

def main():
    s = 0
    for p in primes():
        if p >= 2000000:
            break
        s += p
    print(s)

main()
