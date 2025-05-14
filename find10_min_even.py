def find_min_even(data):
    """
    Given the list of numbers, Find the minimum even number in the list
    args:
        data: list of numbers
    returns: minimum even number in the list
    """
    return min(data, key=lambda x: x if x%2==0 else float('inf'))
print(find_min_even([1,2,3,4,5,6]))
