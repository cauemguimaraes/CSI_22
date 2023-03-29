def primo_generator():
    primos = []
    n = 2
    while True:
        n_primo = 1
        for p in primos:
            if (n % p == 0):
                n_primo = 0
        if (n_primo == 1):
            primos.append(n)
            yield n
        n = n + 1


# gerando os primos
gen = primo_generator()
for primo in gen:
    print(primo)
