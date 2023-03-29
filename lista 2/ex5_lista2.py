def mult_matriz(a, b):
    n_l_a = len(a)
    n_l_b = len(b)
    n_c_a = len(a[0])
    n_c_b = len(b[0])

    result = [[0 for j in range(n_c_b)] for i in range(n_l_a)]
    for i in range(n_l_a):
        for j in range(n_c_b):
            for k in range(n_c_a):
                result[i][j] = result[i][j] + a[i][k]*b[k][j]

    return result


# teste
# A = [[1, 2, 3], [4, 5, 6]]
# B = [[7, 8], [9, 10], [11, 12]]

# print(mult_matriz(A, B))
