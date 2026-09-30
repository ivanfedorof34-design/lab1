"""Заготовки задач на базовый Python."""

from grader_contracts.python_basics import PositiveIntegerInput, TextInput, VectorPairInput


def count_vowels(s: str) -> int:
    vowels = str("aeiouAEIOU")
    return sum(1 for ch in s if ch in vowels)


def has_unique_characters(s: str) -> bool:
    return len(s) == len(set(s))


def count_one_bits(number: int) -> int:
    return bin(number).count("1")


def multiplicative_persistence(number: int) -> int:
    count = 0
    while number >= 10:
        result = 1
        while number > 0:
            digit = number % 10
            result = result * digit
            number = number // 10
        number = result
        count = count + 1
    return count

    raise NotImplementedError  # TODO


def mse(data: float) -> float:
    predicted = data.predicted
    expected = data.expected
    total = 0
    for i in range(len(predicted)):
        difference = predicted[i] - expected[i]
        total = total + difference * difference
    return total / len(predicted)
    raise NotImplementedError  # TODO


def prime_factorization(data: PositiveIntegerInput) -> str:
    number = data.value
    result = ""
    delitel = 2
    while number > 1:
        power = 0
        while number % delitel == 0:
            number = number // delitel
            power = power + 1
        if power > 0:
            if power == 1:
                result = result + "(" + str(delitel) + ")"
            else:
                result = result + "(" + str(delitel) + "**" + str(power) + ")"
        delitel = delitel + 1
    return result
    raise NotImplementedError  # TODO


def pyramid(data: PositiveIntegerInput) -> int | str:
    cube_count = data.value
    total = 0
    k = 1
    while total < cube_count:
        total = total + k * k
        if total == cube_count:
            return k
        k = k + 1
    return "It is impossible"
    raise NotImplementedError  # TODO


def is_balanced_number(data: PositiveIntegerInput) -> bool:
    number = str(data.value)
    middle = len(number) // 2
    left_sum = 0
    right_sum = 0
    for i in range(middle):
        left_sum = left_sum + int(number[i])
    start = middle
    if len(number) % 2 == 1:
        start = start + 1
    for i in range(start, len(number)):
        right_sum = right_sum + int(number[i])
    return left_sum == right_sum
    raise NotImplementedError  # TODO
