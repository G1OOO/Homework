def replace_digits(string):
    result = ''
    for digit in string:
        if int(digit) < 5:
            result += '0'
        else:
            result += '1'
    return result
string = "123456789"
print(replace_digits(string))