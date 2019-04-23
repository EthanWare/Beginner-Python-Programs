# This method takes an array and a number, and returns the index of the number in the array (-1 if not in array)
def mysearch(arr, value):
    """
    >>> mysearch([3,7,3,111,10,330], 111)
    3
    >>> mysearch([3000,13791395,3,2947], 99)
    -1
    """

    index = 0
    for num in arr:
        if num == value:
            return index
        index += 1
    return -1

if __name__ == '__main__':
    # open file
    file  = open("input.txt", "r")

    # read in numbers from file as an array
    userInput = file.read().split(',')

    # get a value to search for
    value = input("Enter a value to search for: ")

    # search for the value in the array and print out the result
    searchOutput = mysearch(userInput, value)
    if searchOutput == -1:
        print("The value is not in the array")
    else:
        print("The value is in the array. The index is: ", searchOutput)

    import doctest
    doctest.testmod()