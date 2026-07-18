import string

letters = set(string.ascii_lowercase)
vowels = set("aeiou")
consonants = letters - vowels
    


def translate(text):
    if ' ' in text:
        return ' '.join(translate(word) for word in text.split())

    if text.startswith(tuple(vowels) + ('xr', 'yt')):
        return text + 'ay'
        
    i = 0
    while (i < len(text) and text[i] in consonants
           and (i == 0 or text[i] != 'y')):
        i += 1
        
    if i > 0 and text[i-1] == 'q' and text[i] == 'u':
        return text[i+1:] + text[:i+1] + 'ay'
    
    elif text[i] == 'y':
        return text[i:] + text[:i] + 'ay'
    
    else: 
        return text[i:] + text[:i] + 'ay'
        
    
