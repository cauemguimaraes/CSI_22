def filtro_pares(lista):
    result = list(filter(lambda x: (x % 2 == 0), lista))
    return result


# teste
# lista = [0, 8, 7, 5, 3, 4, 32]
# print(filtro_pares(lista))
