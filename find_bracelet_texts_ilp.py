"""
Contains ILP-based implementation of the find_best_texts function.
Is clearly faster than the recursive implementation for large inputs.
"""

import pulp


def create_text_letter_counts_matrix(texts: list[str]) -> list[list[int]]:
    """
    Creates a matrix where each row represents a text and each column represents a letter.
    The matrix contains the number of times each letter appears in each text.
    Assumes that the texts are in upper case and contain only A-Z characters.

    Args:
        texts (list[str]): A list of texts.

    Returns:
        list[list[int]]: A matrix of letter counts. First index is the text index,
            second index is the letter index (0-25 for A-Z).
    """
    matrix = [[0] * 26 for _ in range(len(texts))]
    for i, text in enumerate(texts):
        for letter in text:
            letter_idx = ord(letter) - ord("A")
            matrix[i][letter_idx] += 1

    return matrix


def find_best_texts_ilp(
    letter_counts: dict[str, int], texts: list[str]
) -> tuple[int, list[str]]:
    """
    Finds the best texts to form with the given letter counts
    using integer linear programming.
    The best texts are the ones that maximize the used letter count
    (and thus minimize the remaining letter count).

    Args:
        letter_counts (dict[str, int]): A dictionary of letter counts.
            The keys are the letters and the values are the counts.
        texts (list[str]): A list of texts to choose from. The texts must be in upper case
            and contain only A-Z characters.

    Returns:
        tuple[int, list[str], int]: A tuple of the lowest letter count possible and the
        list of texts chosen.
    """

    for text in texts:
        if not all(letter in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" for letter in text):
            raise ValueError("Texts must contain only A-Z characters.")

    # Create a matrix of letter counts for each text
    text_letter_counts: list[list[int]] = create_text_letter_counts_matrix(texts)

    # Create the ILP problem
    prob = pulp.LpProblem("bracelet_texts", pulp.LpMaximize)

    # Create a binary decision variable for each text: 1 if the text is chosen, 0 otherwise
    decision_vars: dict[str, pulp.LpVariable] = pulp.LpVariable.dicts(
        "texts", texts, cat="Binary"
    )

    # Objective function: maximize the total letter usage.
    prob += pulp.lpSum([len(text) * decision_vars[text] for text in texts])

    # Constraint: the used letters must not exceed the letter counts

    for letter, count in letter_counts.items():
        # Get the index of the letter in the text letter counts matrix.
        letter_idx = ord(letter) - ord("A")
        # Add the constraint for this letter
        prob += (
            # The sum of the counts of this letter in each chosen text...
            pulp.lpSum(
                [
                    text_letter_counts[text_idx][letter_idx] * decision_vars[text]
                    for text_idx, text in enumerate(texts)
                ]
            )
            # ...must be less than or equal to the available count of this letter
            <= count
        )

    # Solve the ILP problem. Produces prints.
    prob.solve()

    # Extract return values.
    chosen_texts = [text for text in texts if pulp.value(decision_vars[text]) == 1]
    letters_used = sum(len(text) for text in chosen_texts)
    lowest_letter_count = sum(letter_counts.values()) - letters_used

    return lowest_letter_count, chosen_texts
