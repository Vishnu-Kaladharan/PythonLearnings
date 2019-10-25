def largest(numbers):
    large = numbers[0]
    for number in numbers:
        if number > large:
            large = number

    return large


def smallest(numbers):
    small = numbers[0]
    for number in numbers:
        if number < small:
            small = number

    return small

