def square_root(number):
    x = number
    y = (x + number // x) // 2
    while y < x:
        x = y
        y = (x + number // x) // 2

    return x