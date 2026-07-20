def rebase(input_base, digits, output_base):
    if input_base < 2:
        raise ValueError("input base must be >= 2")
    
    if not len(digits) or (set(digits) == {0}):
        return [0]


    if min(digits) < 0 or max(digits) >= input_base:
        raise ValueError("all digits must satisfy 0 <= d < input base")

    if output_base < 2:
        raise ValueError("output base must be >= 2")
    
    number_base_10 = 0
    result = []
    for digit in digits:
        number_base_10 = number_base_10 * input_base + digit

    while number_base_10 > 0:
        result.insert(0, number_base_10 % output_base)
        number_base_10 //= output_base

    return result