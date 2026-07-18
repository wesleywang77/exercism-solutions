import math

def classify(number):
    """ A perfect number equals the sum of its positive divisors.

    :param number: int a positive integer
    :return: str the classification of the input integer
    """
    
    classes = [
        "deficient",
        "perfect",
        "abundant"
    ]

    if number < 1:
        raise ValueError("Classification is only possible for positive integers.")
    if number == 1:
        return "deficient"
    
    divisors = []
    limit = math.isqrt(number)+1
    
    for i in range(1, limit):
        if number % i == 0:
            divisors.append(i)
            paired_divisor = number // i
            if paired_divisor != i:
                divisors.append(paired_divisor)
    
    divisors.sort()
    # print(divisors)
            
    divisors.remove(number)
    
    s = sum(divisors)
    
    if s < number:
        return classes[0]
    elif s == number:
        return classes[1]
    else:
        return classes[2]

        
    