from collections import Counter


def most_frequent(numbers):
    if not numbers:
        return None
    counts = Counter(numbers)
    return max(counts, key=counts.get)
