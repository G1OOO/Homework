def multiply_values(array):
    result = 1
    for num in array:
        result *= num
    return result

arr = [1, 2, 3, 4]
print(multiply_values(arr))