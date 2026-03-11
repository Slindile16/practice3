# --------------------------------
# SECTION 1 — BASIC LOOPS
# --------------------------------

def sum_to_n(n):
    """
    Return the sum of numbers from 1 to n.

    Example:
    sum_to_n(5) -> 15
    """
    total = 0
    for i in range(n+1):
        total += i
    return total
# print(sum_to_n(5))


def count_even(numbers):
    """
    Given a list of numbers, return how many
    even numbers exist in the list.
    """
    num = 0
    for i in numbers:
        if i % 2 == 0:
            num += 1
    return num
# print(count_even([1,2,3,4,6]))


def print_numbers(n):
    """
    Return a list containing numbers from
    1 up to n.

    Example:
    print_numbers(4) -> [1,2,3,4]
    """

    numbers = []

    for i in range(1, n + 1):
        numbers.append(i)

    return numbers
# print(print_numbers(4))

# --------------------------------
# SECTION 2 — ADVANCED LOOPS
# --------------------------------

def multiplication_table(n):
    """
    Return a list containing the first n
    multiples of n.

    Example:
    multiplication_table(3)
    -> [3,6,9]
    """
    
    # return [n * i for i in range(1, n + 1)]
    result = []

    for i in range(1, n + 1):
        result.append(n * i)

    return result

# print(multiplication_table(3))


def nested_count(n):
    """
    Use nested loops to count how many
    total iterations occur in an n x n loop.

    Example:
    nested_count(3) -> 9
    """
    count = 0

    for i in range(n):
        for j in range(n):
            count += 1

    return count
# print(nested_count(3))


def pyramid_levels(n):
    """
    Return a list representing pyramid levels.

    Example:
    pyramid_levels(3)
    -> ["*", "**", "***"]
    """
    pyramid = []

    for i in range(1, n + 1):
        stars = "*" * i
        pyramid.append(stars)

    return pyramid
# print(pyramid_levels(3))


# --------------------------------
# SECTION 3 — SIMPLE ALGORITHMS
# --------------------------------

def find_max(numbers):
    """
    Return the largest number in a list.
    """
    return max(numbers)
# print(find_max([13,8,4]))


def find_min(numbers):
    """
    Return the smallest number in a list.
    """
    return min(numbers)
# print(find_min([9,4,2,7]))


def average(numbers):
    """
    Return the average value of numbers in a list.
    """
    total = 0

    for num in numbers:
        total += num

    return total / len(numbers)


# print(average([1,3,4,6,7,5]))