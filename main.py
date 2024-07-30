"""Main program for finding the best bracelet texts."""

import pandas as pd
from bracelet_texts import taylor_texts
from find_bracelet_texts import find_best_texts

# Make texts upper case and remove spaces
texts: list[str] = [text.upper().replace(" ", "") for text in taylor_texts]

# Read letter counts from xlsx file.
letter_counts_df: pd.DataFrame = pd.read_excel("letter_counts_real.xlsx", header=None)
letter_counts_dict: dict[str, int] = dict(zip(letter_counts_df[0], letter_counts_df[1]))
total_letter_count: int = sum(letter_counts_dict.values())

print(f"Number of possible bracelet texts: {len(texts)}")
print("Starting letters")
for letter, count in letter_counts_dict.items():
    print(f"{letter}: {count}")
print()
print(f"Starting the algorithm with a pool of {total_letter_count} letters.")
print()

lowest_letter_count, solution_texts = find_best_texts(letter_counts_dict, texts)

print(
    f"You can decrease the letter count to {lowest_letter_count} by choosing the following texts:"
)
for chosen_text in solution_texts:
    print(chosen_text)
