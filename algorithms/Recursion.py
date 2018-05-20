def pow(x):
    if x < 1:
        return 1
    else:
        return x * pow(x-1)



print(pow(3))

