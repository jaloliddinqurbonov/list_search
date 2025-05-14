def find_max_odd(data):
    """
    Given the list of numbers, Find the maximum odd number in the list
    args:
        data: list of numbers
    returns: maximum odd number in the list
    """
    return max(data,key=lambda x:x if x%2==1 else 0)
print(find_max_odd([1,2,3,4,5,6,7]))