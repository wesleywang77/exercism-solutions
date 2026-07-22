import string
lowerletters = tuple(string.ascii_lowercase)
upperletters = tuple(string.ascii_uppercase)

def rotate(text, key):
    output = ""
    for char in text:
        
        if char in lowerletters:
            new_index = (lowerletters.index(char) + key) % 26
            output += lowerletters[new_index]
        elif char in upperletters:
            new_index = (upperletters.index(char) + key) % 26
            output += upperletters[new_index]
        else:
            output += char

    return output