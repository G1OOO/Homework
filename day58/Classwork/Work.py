def remove_largest_with_remove(lst, value):
    if not lst:
        return None

    max_value = max(lst)
    lst.remove(max_value)
    return lst

def remove_largest_custom(lst, value):
    if not lst:
        return None

    max_value = float('-inf')
    max_index = None

    for i in range(len(lst)):
        if lst[i] > max_value:
            max_value = lst[i]
            max_index = i

    lst.pop(max_index)
    return lst
