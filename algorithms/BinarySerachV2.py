def binarySerch(array, number):
    min = 0
    if len(array) == 0:
        return 0

    max = len(array) - 1
    mid = round((min + max) / 2)
    guess = array[mid]
    if guess > number:
        return min + binarySerch(array[:(mid - 1)], number)
    elif guess < number:
        return mid + 1 + binarySerch(array[(mid + 1):], number)
    else:
        return mid


array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


print("Dla liczby 1 index : ", binarySerch(array, 1))
print("Dla liczby 2 index : ", binarySerch(array, 2))
print("Dla liczby 3 index : ", binarySerch(array, 3))
print("Dla liczby 4 index : ", binarySerch(array, 4))
print("Dla liczby 5 index : ", binarySerch(array, 5))
print("Dla liczby 6 index : ", binarySerch(array, 6))
print("Dla liczby 7 index : ", binarySerch(array, 7))
print("Dla liczby 8 index : ", binarySerch(array, 8))
print("Dla liczby 9 index : ", binarySerch(array, 9))
print("Dla liczby 10 index : ", binarySerch(array, 10))

