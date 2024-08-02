"""
Contains helper functions and main the recursive function for searching the best texts. 
"""

from collections import Counter


def letter_dict_to_tuple(letter_counts: dict[str, int]) -> tuple[int, ...]:
    """
    Converts a dictionary of letter counts to an array of letters.

    Args:
        letter_counts (dict[str, int]): A dictionary of letter counts.
            The keys are the letters and the values are the counts.

    Returns:
        tuple[int, ...]: An array of letter counts. The index of the array
            corresponds to the letter's position in the alphabet, starting from 'A' at index 0.
    """
    letters: list[int] = [0] * 26
    for letter, count in letter_counts.items():
        if not "A" <= letter <= "Z":
            print(f"Invalid letter '{letter}' found in letter_counts, skipping.")
            continue
        idx: int = ord(letter) - ord("A")
        letters[idx] = count

    return tuple(letters)


def can_form_string(input_string: str, letter_counts: tuple[int, ...]) -> bool:
    """
    Checks if the input string can be formed with the given letter counts.

    Args:
        input_string (str): The string to check.
        letter_counts (tuple[int, ...]): A tuple of letter counts. The index of the tuple
            corresponds to the letter's position in the alphabet, starting from 'A' at index 0.

    Returns:
        bool: True if the string can be formed with the given letter counts,
            False otherwise.
    """
    # Calculate letter counts in input string.
    input_letter_counts: dict[str, int] = Counter(input_string)
    # Check if we have enough letters.
    for letter, count in input_letter_counts.items():
        if not "A" <= letter <= "Z" or count > letter_counts[ord(letter) - ord("A")]:
            return False

    return True


def update_remaining_letters(
    chosen_string: str, letter_counts: tuple[int, ...]
) -> tuple[int, ...]:
    """
    Forms chosen string using the given letter pool and returns the updated letter pool.
    Assumes that the chosen string can be formed with the given letter counts.

    Args:
        chosen_string (str): The string to form.
        letter_counts (tuple[int, ...]): A tuple of letter counts. The index of the tuple
            corresponds to the letter's position in the alphabet, starting from 'A' at index 0.

    Returns:
        tuple[int, ...]: The updated letter counts after forming the chosen string.
    """
    # Calculate letter counts in input string.
    input_letter_counts: dict[str, int] = Counter(chosen_string)
    # Update letter counts.
    new_letter_counts: list[int] = list(letter_counts)
    for letter, count in input_letter_counts.items():
        new_letter_counts[ord(letter) - ord("A")] -= count

    return tuple(new_letter_counts)


def find_best_texts_recursive(
    letter_counts: dict[str, int], texts: list[str]
) -> tuple[int, list[str], int]:
    """
    Finds the best texts to form with the given letter counts.
    The best texts are the ones that minimize the total letter count.

    Args:
        letter_counts (dict[str, int]): A dictionary of letter counts.
            The keys are the letters and the values are the counts.
        texts (list[str]): A list of texts to choose from.

    Returns:
        tuple[int, list[str], int]: A tuple of the lowest letter count possible, the
        list of texts chosen and the number of made recursive calls.
    """

    letter_counts_tuple = letter_dict_to_tuple(letter_counts)

    # Inner recursive function
    def choose_text(
        current_text_idx: int,
        letters_left_total: int,
        letters_left: tuple[int, ...],
        recursive_calls: int,
    ) -> tuple[int, list[str], int]:
        """
        Recursive function to choose the best texts to form with the given letter counts.
        Tries all possible combinations of texts by including or excluding each text.
        Is slow as heck for large inputs.
        """
        if current_text_idx < 0:
            # out of texts to try
            return (letters_left_total, [], recursive_calls)

        # Try this text.
        current_text: str = texts[current_text_idx]

        if not can_form_string(current_text, letters_left):
            # exclude this text
            return choose_text(
                current_text_idx - 1,
                letters_left_total,
                letters_left,
                recursive_calls + 1,
            )

        # Can form current text.
        # Search for the best texts to form with the remaining letters.
        new_letters_left: tuple[int, ...] = update_remaining_letters(
            current_text, letters_left
        )
        inc_letters_left, incl_sub_sol, inc_sub_calls = choose_text(
            current_text_idx - 1,
            letters_left_total - len(current_text),
            new_letters_left,
            1,  # start a new counter for the recursive calls
        )

        # Compare the cases where this text is included or excluded.
        excl_letters_left, excl_sol, excl_sub_calls = choose_text(
            current_text_idx - 1, letters_left_total, letters_left, 1
        )
        new_calls = recursive_calls + inc_sub_calls + excl_sub_calls

        if inc_letters_left < excl_letters_left:
            return (inc_letters_left, incl_sub_sol + [current_text], new_calls)

        return (excl_letters_left, excl_sol, new_calls)

    # Inner function ends

    return choose_text(
        len(texts) - 1, sum(letter_counts.values()), letter_counts_tuple, 0
    )
