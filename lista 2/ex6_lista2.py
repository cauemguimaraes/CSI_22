def generator(lista):
    n = len(lista)
    for i in range(n):
        yield lista[n-1-i]


# teste
# lista = [1,4,8]
# gen = generator(lista)
# print(next(gen))
# print(next(gen))
# print(next(gen))
