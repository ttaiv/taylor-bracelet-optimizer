"""
Script to plot the available letter counts and the letter counts in the possible texts.
"""

import string
import pandas as pd
from matplotlib import pyplot as plt
from bracelet_texts import taylor_texts
from find_bracelet_texts_recursive import can_form_string

LETTER_COUNTS_FILENAME = "letter_counts_real.xlsx"

# Read letter counts from xlsx file.
letter_counts_df = pd.read_excel(LETTER_COUNTS_FILENAME, header=None)
letter_counts_dict = dict(zip(letter_counts_df[0], letter_counts_df[1]))

# Make texts upper case and remove spaces.
texts = [text.upper().replace(" ", "") for text in taylor_texts]

# Plot bar chart of available letter counts.
plt.figure(1)
plt.bar(letter_counts_dict.keys(), letter_counts_dict.values())
plt.xlabel("Letter")
plt.ylabel("Count")
plt.title("Available letters")


def remove_impossible_texts(
    letter_counts: dict[str, int], texts_list: list[str]
) -> list[str]:
    """
    Removes texts that cannot be formed from the available letters.

    Args:
        letter_counts_dict (dict[str, int]): A dictionary of letter counts.
            The keys are the letters and the values are the counts.
        texts_list (list[str]): A list of texts to choose from.

    Returns:
        list[str]: A list of texts that can be formed from the available letters.
    """
    return [text for text in texts_list if can_form_string(text, letter_counts)]


possible_texts = remove_impossible_texts(letter_counts_dict, texts)

letter_counts_in_texts = {}
for text in possible_texts:
    for letter in text:
        if letter in letter_counts_in_texts:
            letter_counts_in_texts[letter] += 1
        else:
            letter_counts_in_texts[letter] = 1

# Plot to letter counts in possible texts.
plt.figure(2)
plt.bar(letter_counts_in_texts.keys(), letter_counts_in_texts.values())
plt.xlabel("Letter")
plt.ylabel("Count")
plt.title("Letters in possible texts")

# Calculate the normalized difference between the available letters
# and the letters in the possible texts.

total_available_letters = sum(letter_counts_dict.values())
total_letters_in_texts = sum(letter_counts_in_texts.values())
norm_letter_counts_dict = {
    letter: count / total_available_letters
    for letter, count in letter_counts_dict.items()
}
norm_letter_counts_in_possible_texts = {
    letter: count / total_letters_in_texts
    for letter, count in letter_counts_in_texts.items()
}

letter_difference = {}
for letter in string.ascii_uppercase:
    letter_difference[letter] = norm_letter_counts_dict.get(
        letter, 0
    ) - norm_letter_counts_in_possible_texts.get(letter, 0)

# Plot the difference between the available letters and the letters in the possible texts.
plt.figure(3)
plt.bar(letter_difference.keys(), letter_difference.values())
plt.xlabel("Letter")
plt.ylabel("available - in texts")
plt.title("Normalized diff between available letters and letters in possible texts")
plt.show()
