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
        return classes[0]
    divisors = []
    for i in range(1, math.ceil(math.sqrt(number))):
        if number % i == 0:
            divisors.append(i)
            divisors.append(number // i)
            
    divisors.remove(number)
    s = sum(divisors)
    
    if s < number:
        return classes[0]
    elif s == number:
        return classes[1]
    else:
        return classes[2]

        
    