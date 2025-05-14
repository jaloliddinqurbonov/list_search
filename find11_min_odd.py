def find_min_odd(data):
    """
    Given the list of numbers, Find the minimum odd number in the list
    args:
        data: list of numbers
    returns: minimum odd number in the list
    """
    return min(data, key=lambda x: x if x%2==1 else float('inf'))
print(find_min_odd([1,2,3,4,5,6]))

