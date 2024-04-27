def remove_smallest(arr):
    if not arr:
        return []
    min_val = min(arr)
    return [x for x in arr if x != min_val]

print(remove_smallest([1, 2, 3, 4, 5]))
print(remove_smallest([5, 3, 2, 1, 4]))
print(remove_smallest([2, 2, 1, 2, 1]))
