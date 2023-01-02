def vowel_count(phrase):
    """Return frequency map of vowels, case-insensitive.

        >>> vowel_count('rithm school')
        {'i': 1, 'o': 2}
        
        >>> vowel_count('HOW ARE YOU? i am great!') 
        {'o': 2, 'a': 3, 'e': 2, 'u': 1, 'i': 1}
    """
    dic = {}
    for ltr in phrase :
        lo_ltr = ltr.lower()
        if ltr.lower() in 'aeiou' :
            dic[lo_ltr] = dic.get(lo_ltr, 0) + 1

    return dic