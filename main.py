"""Main program for finding the best bracelet texts."""

import pandas as pd
from bracelet_texts import taylor_texts
from find_bracelet_texts_recursive import find_best_texts_recursive
from find_bracelet_texts_ilp import find_best_texts_ilp

LETTER_COUNTS_DIR: str = "data"
LETTER_COUNTS_FILENAME: str = "letter_counts_real.xlsx"
SOLUTION_METHOD: str = "ILP"  # "ILP" or "recursive"

# Make texts upper case and remove spaces
texts: list[str] = [text.upper().replace(" ", "") for text in taylor_texts]

# Remove texts that contain characters other than A-Z
texts = [
    text
    for text in texts
    if all(letter in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" for letter in text)
]

# Read letter counts from xlsx file.
path = f"{LETTER_COUNTS_DIR}/{LETTER_COUNTS_FILENAME}"
letter_counts_df: pd.DataFrame = pd.read_excel(path, header=None)
letter_counts_dict: dict[str, int] = dict(zip(letter_counts_df[0], letter_counts_df[1]))
total_letter_count: int = sum(letter_counts_dict.values())

print(f"Number of different bracelet texts: {len(texts)}")
print("Starting letters")
for letter, count in letter_counts_dict.items():
    print(f"{letter}: {count}")
print()
print(f"Starting the algorithm with a pool of {total_letter_count} letters.")
print()

lowest_possible_letter_count, solution_texts, recursive_calls = (
    (*find_best_texts_ilp(letter_counts_dict, texts), 0)  # produces prints
    if SOLUTION_METHOD == "ILP"
    else find_best_texts_recursive(letter_counts_dict, texts)
)

print(
    f"You can decrease the letter count to {lowest_possible_letter_count}"
    " by choosing the following texts:"
)
for chosen_text in solution_texts:
    print(chosen_text)
print()

used_letters = {letter: 0 for letter in letter_counts_dict}
for text in solution_texts:
    for letter in text:
        used_letters[letter] += 1

print("Leftover letters")
for letter, count in letter_counts_dict.items():
    print(f"{letter}: {count - used_letters[letter]}")

if SOLUTION_METHOD == "recursive":
    print(f"The algorithm made {recursive_calls} recursive calls.")
