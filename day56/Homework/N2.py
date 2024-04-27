def blank_pages_needed(n, m):
    if n < 0 or m < 0:
        return 0
    return n * m
n1, m1 = 5, 5
n2, m2 = -5, 5

print(blank_pages_needed(n1, m1)) 
print(blank_pages_needed(n2, m2))
