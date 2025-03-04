import re
from collections import Counter


def is_prime(n: int) -> bool:
    if n < 2:
        return False
    i = 2
    while i*i <= n:
        if n % i == 0:
            return False
        i += 1
    return True


def prime_selector(numbers: list[int]) -> list[int]:
    return [x for x in numbers if is_prime(x)]


def round_numbers(numbers: list[int], threshold: int) -> list[int]:
    rounded_numbers = []
    for number in numbers:
        if number < threshold:
            rounded_number = (number // 10) * 10
        else:
            rounded_number = ((number + 9) // 10) * 10
        rounded_numbers.append(rounded_number)
    return rounded_numbers


def longest_increasing_subsequence(sequence: list[int]) -> list[int]:
    if not sequence:
        return 0

    max_length = 1
    current_length = 1

    for i in range(1, len(sequence)):
        if sequence[i] > sequence[i - 1]:
            current_length += 1
        else:
            max_length = max(max_length, current_length)
            current_length = 1

    return max(max_length, current_length)


def is_balanced(expression: str) -> bool:
    stack = []
    for c in expression:
        if c in ["(", "[", "{"]:
            stack.append(c)
        elif c in [")", "]", "}"]:
            try:
                stack.pop()
            except:
                return False

    return len(stack) == 0


def transposition_cipher(text: str, key: int) -> str:
    if key > len(text):
        return text

    text_list = list(text)
    for i in range(0, len(text), key):
        if i + key < len(text):
            text_list[i], text_list[i + key] = text_list[i + key], text_list[i]

    return ''.join(text_list)


def fibonacci_generator(n: int):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b


def most_frequent_elements(data: list[int]) -> int:
    freq = Counter(data)
    return max(freq, key=freq.get)


def count_syllables(word: str) -> int:
    word = word.lower()
    syllable_count = len(re.findall(r'[aeiouy]+', word))
    return syllable_count if syllable_count > 0 else 1


def readability_score(text: str) -> float:
    sentences = re.split(r'[.!?]', text)
    sentences = [s for s in sentences if s.strip()]
    words = re.findall(r'\b\w+\b', text)
    num_sentences = len(sentences)
    num_words = len(words)
    num_syllables = sum(count_syllables(word) for word in words)
    if num_sentences == 0 or num_words == 0:
        return 0.0

    avg_words_per_sentence = num_words / num_sentences
    avg_syllables_per_word = num_syllables / num_words
    return (avg_words_per_sentence + avg_syllables_per_word) / 2


def unique_permutations(elements: list) -> list[list]:
    if len(elements) == 0:
        return [[]]

    permutations = []
    for i, element in enumerate(elements):
        remaining_elements = elements[:i] + elements[i+1:]
        for perm in unique_permutations(remaining_elements):
            permutation = [element] + perm
            if permutation not in permutations:
                permutations.append(permutation)

    return permutations


def group_words_by_length(words: list[str]) -> dict[int, str]:
    word_groups = {}
    for word in words:
        word_length = len(word)
        if word_length not in word_groups:
            word_groups[word_length] = []
        word_groups[word_length].append(word)

    return word_groups


if __name__ == "__main__":
    print(prime_selector([1, 2, 3, 4, 5, 6, 7, 8]))
    print(round_numbers([123, 132, 142, 111], 130))
    print(longest_increasing_subsequence([1, 2, 3, 2, 5, 6, 7, 8, 1, 2]))
    print(is_balanced("([{}]){}[{}]"))
    print(transposition_cipher("Hello, world!", 3))
    for fib in fibonacci_generator(5):
        print(fib)
    print(most_frequent_elements([1, 2, 3, 2, 4, 1, 2, 3, 3, 2]))
    print(readability_score(
        "Oto przykładowy tekst. Zawiera on kilka zdań. Każde zdanie ma różną liczbę słów i sylab."))
    print(unique_permutations([1, 2, 3]))
    print(group_words_by_length(["asdf", "asdf", "fdsa", "asd", "dsa"]))
