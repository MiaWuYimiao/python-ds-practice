def capitalize(phrase):
    """Capitalize first letter of first word of phrase.

        >>> capitalize('python')
        'Python'

        >>> capitalize('only first word')
        'Only first word'
    """
    res = ''
    
    for i in range( len(phrase) ):
        if phrase[i].isalpha() :
            res = phrase[:i+1].upper() + phrase[i+1:]
            break
    
    return res