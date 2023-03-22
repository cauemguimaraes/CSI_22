import turtle


def draw_poly(c, n, sz):

    for i in range(n):
        c.forward(sz)
        c.left(360/n)
