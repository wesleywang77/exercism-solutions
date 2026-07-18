def reverse(text):
    length = len(text)
    result = ''
    for i in range(length-1, -1, -1):
        result += text[i]
    return result
