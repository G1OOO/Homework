def isTeenager(age, hasPermission):
    if age < 18 and not hasPermission:
        return False
    elif age == 18 and hasPermission:
        return True
    else:
        return False

print(isTeenager(17, False))
print(isTeenager(18, True))