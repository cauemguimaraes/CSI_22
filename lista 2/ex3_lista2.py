# Do enunciado entendi que devia ser feita uma função que criasse uma nova lista
# que possua apenas as strings que continham somente caracteres alfabeticos e numericos

def string_filter(lista):
    lista_filtrada = []
    for string in lista:
        caractere_proibido = 0
        for c in string:
            if (c.isalpha() == 0) and (c.isdigit() == 0):
                caractere_proibido = 1
        if (caractere_proibido == 0):
            lista_filtrada.append(string)

    return lista_filtrada


# teste
# lista = ['hdadahJ','abc10', '*!k9', 'kahd568LB20','652244', '$#!', 'ajahgd!!', 'sjhdga82BN']
# print(string_filter(lista))
