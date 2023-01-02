def reverse_string(phrase):
    """Reverse string,

        >>> reverse_string('awesome')
        'emosewa'

        >>> reverse_string('sauce')
        'ecuas'
    """
    list = []
    for ltr in phrase :
        list.insert(0,ltr)

    return ''.join(list)