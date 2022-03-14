def binary_search(array, element):
    validity(array)
    array = sorted(array)
    left = 0
    right = len(array) - 1
    mid = 0

    while left <= right:
        print("Begin left = {} mid = {} right = {}".format(left, mid, right))
        print(array)
        mid = (left + right) // 2
        if array[mid] < element:
            left = mid+1
        elif array[mid] > element:
            right = mid-1
        elif array[mid] == element:
            print("Element {} found at index {}".format(element, mid))
            return 0
        print("End left = {} mid = {} right = {}".format(left, mid, right))
    if element != array[mid]:
        print("Element {} not in array".format(element))
        return 1

def validity(array):
    if type(array) != list:
        raise TypeError("Item passed to function must be an array")
    for i in range(len(array)):
        if type(array[0]) != type(array[i]):
                raise TypeError("Array Items must all be same type to compare")
    if None in array:
        raise TypeError("Array must not be null")
    if len(array) <= 0:
        raise Exception("Array must not be empty")