def find_max_even(data):
    """
    Given the list of numbers, Find the maximum even number in the list
    args:
        data: list of numbers
    returns: maximum even number in the list
    """
    return max(data,key=lambda x:x if x%2==0 else 0)
print(find_max_even([1,2,3,4,5,6,7]))