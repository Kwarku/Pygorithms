def quickSort(array):
    if len(array) < 2:
        return array
    else:
        pivot = array[0]
        low = [i for i in array[1:] if i <= pivot]
        greater = [i for i in array[1:] if i > pivot]
        return quickSort(low) + [pivot] + quickSort(greater)


print(quickSort([10, 2, 4, 1, 7, 5]))
