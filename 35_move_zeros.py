def move_zeros(numbers):
    non_zeros = [num for num in numbers if num != 0]
    zeros = [num for num in numbers if num == 0]
    return non_zeros + zeros
