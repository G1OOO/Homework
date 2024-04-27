def to_jaden_case(string):
    words = string.split()
    jaden_cased_words = [word.capitalize() for word in words]
    return ' '.join(jaden_cased_words)

quote = "How can mirrors be real if our eyes aren't real"
print(to_jaden_case(quote))
