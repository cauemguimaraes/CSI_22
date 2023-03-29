# A função irá checar se os caracteres do string1 estão presentes no string2
def string_checker(string1, string2):
    for c in string1:
        have = 0
        for d in string2:
            if (c == d):
                have = 1
        if (have == 0):
            return False
    return True

# teste
# a = 'abcdef1060'
# b = 'abcdef10!'
# c = 'abcdefab'
# d = '10'
# print(string_checker(b,a))
# print(string_checker(c,a))
# print(string_checker(d,a))
