def same_frequency(num1, num2):
    """Do these nums have same frequencies of digits?
    
        >>> same_frequency(551122, 221515)
        True
        
        >>> same_frequency(321142, 3212215)
        False
        
        >>> same_frequency(1212, 2211)
        True
    """
    lst_num1 = list(str(num1))
    lst_num2 = list(str(num2))
    if len(lst_num1) != len(lst_num2) :
        return False

    for num in lst_num1 :
        if lst_num1.count(num) != lst_num2.count(num) :
            return False

    return True