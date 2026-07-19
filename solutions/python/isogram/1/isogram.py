import string
def is_isogram(phrase):
    
    phrase = phrase.lower()
    phrase = "".join(ch for ch in phrase if ch in string.ascii_lowercase)
    return len(phrase) == len(set(phrase))
    
