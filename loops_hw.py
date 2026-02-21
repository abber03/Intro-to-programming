# Problem 1: The diamond of stars.

def diamond_of_stars(n: int) -> None:
    if n == 0:
        return

    # top half (including middle)
    for i in range(1, n + 1):
        spaces = n - i
        stars = "* " * i
        print(" " * spaces + stars.rstrip())

    # bottom half
    for i in range(n - 1, 0, -1):
        spaces = n - i
        stars = "* " * i
        print(" " * spaces + stars.rstrip())


# Problem 2: The weird sequence of numbers.

def weird_sequence(n: int) -> list[int]:
    result = []

    for power in range(n):
        base = 10 ** power
        for i in range(1, 10):
            result.append(i * base)

    return result


# Problem 3: Count the number of repeated occurrences of letters.

def count_double_letters(input_string: str) -> int:
    count = 0

    for i in range(len(input_string) - 1):
        if input_string[i] == input_string[i + 1]:
            count += 1

    return count

  
