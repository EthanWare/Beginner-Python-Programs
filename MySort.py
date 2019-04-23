# This method takes an array of integers and returns them sorted in ascending order
def mysort(arr):
    """
    >>> mysort([3,7,3,111,10,330])
    [3, 3, 7, 10, 111, 330]
    >>> mysort([3000,13791395,3,2947])
    [3, 2947, 3000, 13791395]
    """
    arr.sort(key=int)

    return arr

if __name__ == '__main__':

    # open file
    file = open("input.txt", "r")

    # read in numbers from file as an array
    input = file.read().split(',')

    # pass array into mysort, then print the sorted array
    mysort(input)
    print("The sorted list: " + str(input))

    import doctest
    doctest.testmod()