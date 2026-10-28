def first_non_repeating(text):
    for char in text:
        if text.count(char) == 1:
            return char
    return None
