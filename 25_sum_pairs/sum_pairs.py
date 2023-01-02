def sum_pairs(nums, goal):
    """Return tuple of first pair of nums that sum to goal.

    For example:

        >>> sum_pairs([1, 2, 2, 10], 4)
        (2, 2)

    (4, 2) sum to 6, and come before (5, 1):

        >>> sum_pairs([4, 2, 10, 5, 1], 6) # (4, 2)
        (4, 2)

    (4, 3) sum to 7, and finish before (5, 2):

        >>> sum_pairs([5, 1, 4, 8, 3, 2], 7)
        (4, 3)

    No pairs sum to 100, so return empty tuple:

        >>> sum_pairs([11, 20, 4, 2, 1, 5], 100)
        ()
    """

    ### this method cannot get (4, 3) for sum_pairs([5, 1, 4, 8, 3, 2], 7)
    ### it will generate (5, 2)
    # for i, num in enumerate(nums) :
    #     if nums[i+1:].count( goal - num ) :
    #         return (num, goal-num)

    # return ()

    visited = set()

    for num in nums :
        diff = goal - num
        if diff in visited :
            return (diff, num)
        visited.add(num)
    
    return ()