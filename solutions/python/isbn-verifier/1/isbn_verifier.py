def is_valid(isbn):
    isbn = isbn.replace("-", "")

    if len(isbn) != 10:
        return False

    if not isbn[:9].isdigit():
        return False

    if not (isbn[9].isdigit() or isbn[9] == "X"):
        return False

    total = 0

    for index, ch in enumerate(isbn):
        value = 10 if ch == "X" else int(ch)
        total += value * (10 - index)

    return total % 11 == 0