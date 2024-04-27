def is_pangram(sentence):
    sentence = sentence.lower()
    letters_found = set()
    for char in sentence:
        if char.isalpha():
            letters_found.add(char)
    return len(letters_found) == 26

sentence = "The quick brown fox jumps over the lazy dog"
print(is_pangram(sentence))

sentence = "Pack my box with five dozen liquor jugs"
print(is_pangram(sentence))

sentence = "Hello world!"
print(is_pangram(sentence))
