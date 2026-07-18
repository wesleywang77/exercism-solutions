import string

letters = set(string.ascii_lowercase)
vowels = set("aeiou")
consonants = letters - vowels
    


def translate(text):
    if ' ' in text:
        return ' '.join(translate(word) for word in text.split())

    if text.startswith(tuple(vowels) + ('xr', 'yt')):
        return text + 'ay'
        
    index = 0
    while (index < len(text) and text[index] in consonants
           and (index == 0 or text[index] != 'y')):
        index += 1
        
    if index > 0 and text[index-1] == 'q' and text[index] == 'u':
        return text[index+1:] + text[:index+1] + 'ay'
    
    elif text[index] == 'y':
        return text[index:] + text[:index] + 'ay'
    
    else: 
        return text[index:] + text[:index] + 'ay'
        
    
