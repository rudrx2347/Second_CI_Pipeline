def rotate_string(text, k):
    if not text:
        return text

    k = k % len(text)
    return text[-k:] + text[:-k] if k else text
