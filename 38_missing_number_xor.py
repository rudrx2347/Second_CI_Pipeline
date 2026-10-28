def missing_number(numbers):
    result = len(numbers)

    for i, num in enumerate(numbers):
        result ^= i ^ num

    return result
