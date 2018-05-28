def binary_search(list, num):
    low = 0
    high = len(list) - 1

    while low <= high:
        mid = round((low + high) / 2)
        guess = list[mid]

        if guess == num:
            return mid
        elif guess < num:
            low = mid + 1
        else:
            high = mid - 1
    return None


num_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(binary_search(num_list, 9))
