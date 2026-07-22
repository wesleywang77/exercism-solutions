import string
alphabet = tuple(string.ascii_lowercase)


def is_pangram(sentence):
    count_list = [0] * 26
        
    sentence = sentence.lower()
    for index, ch in enumerate(alphabet):
        if ch in sentence:
            count_list[index] = 1

    return 0 not in count_list