def find_max_count(data):
    """
    Given the list of numbers, Find count of maximum numbers in the list
    args:
        data: list of numbers
    returns: count of maximum numbers in the list
    """
    a=max(data)
    c=data.count(a)
    return c
print(find_max_count([1,3,4,3,4,2,4]))
