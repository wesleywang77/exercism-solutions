def is_armstrong_number(number):
    total_digits = len(list(str(number)))
    sum = 0
    for digit in list(str(number)):
        sum += int(digit) ** total_digits
    return number == sum
