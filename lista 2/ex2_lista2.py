# obs: fiz duas funções pois a media definida no exemplo do enunciado estava estranha
# Ela não seguia a definição de média aritmetica
# Sendo assim, por medo de haver um erro no enunciado, fiz uma função com a media aritmetica "tupla_media1"
# E outra função com a media definida no exemplo do enunciado (soma/2) "tupla_media2"

# Essa primeira função retorna a média aritmetica de cada tupla
def tupla_media1(lista):
    tupla_media = ()
    for tupla in lista:
        s = 0
        for n in tupla:
            s = s + n
        m = s/len(tupla)
        tupla_media = tupla_media + (m,)

    return tupla_media

# Essa segunda função retorna a "media" usada no exemplo dado no exercicio (soma dos numeros da tupla dividido po 2)
# Achei essa definição estranha, por isso fiz a primeira função também, não sei se houve erro no ex do enunciao


def tupla_media2(lista):
    tupla_media = ()
    for tupla in lista:
        s = 0
        for n in tupla:
            s = s + n
        m = s/2
        tupla_media = tupla_media + (m,)

    return tupla_media


# teste:

# tupla = ((2, 3, 4), (3, 4, 5, 6), (2, 4), (4, 8, 9))
# print(tupla_media1(tupla))
# print(tupla_media2(tupla))
