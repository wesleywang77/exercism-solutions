def response(hey_bob):
    choice = [
        'Sure.',
        'Whoa, chill out!',
        'Calm down, I know what I\'m doing!',
        'Fine. Be that way!',
        'Whatever.'
    ]

    hey_bob = hey_bob.strip()
    
    if hey_bob.endswith('?'):
        if hey_bob.isupper():
            return choice[2]
        else:
            return choice[0]
    elif hey_bob.isupper():
        return choice[1]
    elif hey_bob.isspace() or hey_bob == '':
        return choice[3]
    else:
        return choice[4]
