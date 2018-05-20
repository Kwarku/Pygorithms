def smallest_number(arr):
    smallest = arr[0]
    smallest_index = 0

    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i

    return smallest_index


def select_sort(arr):
    new_array = []
    for i in range(len(arr)):
        smallest_number_index = smallest_number(arr)
        new_array.append(arr.pop(smallest_number_index))

    return new_array


print(select_sort([2, 5, 7, 2, 9, 1, 10]))
