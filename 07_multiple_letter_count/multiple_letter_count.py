def multiple_letter_count(phrase):
    """Return dict of {ltr: frequency} from phrase.

        >>> multiple_letter_count('yay')
        {'y': 2, 'a': 1}

        >>> multiple_letter_count('Yay')
        {'Y': 1, 'a': 1, 'y': 1}
    """
    dic = {}
    for ltr in phrase :
        if ltr in dic.keys():
            dic[ltr] += 1
        else :
            dic[ltr] = 1
    
    return dic