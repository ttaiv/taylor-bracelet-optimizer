"""
Contains helper functions and main the recursive function for searching the best texts. 
"""
def can_form_string(input_string: str, letter_counts: dict[str, int]):
    """
    Checks if the input string can be formed with the given letter counts.

    Args:
        input_string (str): The string to check.
        letter_counts (dict[str, int]): A dictionary of letter counts.
            The keys are the letters and the values are the counts.

    Returns:
        bool: True if the string can be formed with the given letter counts,
            False otherwise.
    """
    # Calculate letter counts in input string.
    input_letter_counts: dict[str, int] = {}
    for letter in input_string:
        if letter in input_letter_counts:
            input_letter_counts[letter] += 1
        else:
            input_letter_counts[letter] = 1
    # Check if we have enough letters.
    for letter, count in input_letter_counts.items():
        if letter not in letter_counts or count > letter_counts[letter]:
            return False
    return True

def update_remaining_letters(chosen_string: str, letter_counts: dict[str, int]):
    """
    Forms chosen string using the given letter pool and returns the updated letter pool.
    Assumes that the chosen string can be formed with the given letter counts.
    Does not modify the original letter counts dictionary.

    Args:
        chosen_string (str): The string to form.
        letter_counts (dict[str, int]): A dictionary of letter counts.
            The keys are the letters and the values are the counts.
    
    Returns:
        dict[str, int]: The updated letter counts after forming the chosen string.
    """
    updated_letter_counts: dict[str, int] = letter_counts.copy()
    for letter in chosen_string:
        # If the letter is in the dictionary, decrement its count
        if letter in updated_letter_counts:
            updated_letter_counts[letter] -= 1
        # If the letter is not in the dictionary, this is an error state
        else:
            raise ValueError(f"Letter '{letter}' not found in letter_counts")

    return updated_letter_counts

def find_best_texts(letter_counts: dict[str, int], texts: list[str]) -> tuple[int, list[str]]:
    """
    Finds the best texts to form with the given letter counts.
    The best texts are the ones that minimize the total letter count.

    Args:
        letter_counts (dict[str, int]): A dictionary of letter counts.
            The keys are the letters and the values are the counts.
        texts (list[str]): A list of texts to choose from.

    Returns:
        tuple[int, list[str]]: A tuple of the lowest letter count possible and the 
        list of texts chosen
    """
    # Inner recursive function
    def choose_text(current_text_idx: int, letters_left_total: int,
                    letters_left_dict: dict[str, int]) -> tuple[int, list[str]]:
        """
        Recursive function to choose the best texts to form with the given letter counts.
        Tries all possible combinations of texts by including or excluding each text.
        Is slow as heck for large inputs.
        """
        if current_text_idx <  0:
            # out of texts to try
            return letters_left_total, []

        # Try this text.
        current_text: str = texts[current_text_idx]

        if not can_form_string(current_text, letters_left_dict):
            # exclude this text
            return choose_text(current_text_idx - 1, letters_left_total, letters_left_dict)

        # Can form current text.
        # Search for the best texts to form with the remaining letters.
        new_letters_left = update_remaining_letters(current_text, letters_left_dict)
        sub_letters_left, sub_solution = choose_text(
            current_text_idx - 1, letters_left_total - len(current_text), new_letters_left)

        # Compare the cases where this text is included or excluded.
        included = (sub_letters_left, sub_solution + [current_text])
        excluded = choose_text(current_text_idx - 1, letters_left_total, letters_left_dict)
        if included[0] < excluded[0]: # choose the one with the lowest letter count
            return included
        return excluded
    # Inner function ends

    return choose_text(len(texts) - 1, sum(letter_counts.values()), letter_counts)
