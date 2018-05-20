def sum(array):
    if len(array) == 0:
        return 0
    else:
        return array[0] + sum(array[1:])

    array = [6, 4, 2, 8]
    print("Sum of array elements is: ", sum(array))
