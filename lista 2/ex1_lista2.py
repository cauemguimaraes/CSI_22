def remove_empty_tuple(a):
    for tupla in a:
        if len(tupla) == 0:
            a.remove(tupla)
