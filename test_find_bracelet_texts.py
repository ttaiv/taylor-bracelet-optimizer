"""
Contains a few manually engineered test cases for the
find_best_texts_recursive and find_best_texts_ilp functions.

Please note that the medium test case for the recursive algorithm
takes a few minutes to run.
"""

import unittest
import pandas as pd
from bracelet_texts import taylor_texts
from find_bracelet_texts_recursive import find_best_texts_recursive
from find_bracelet_texts_ilp import find_best_texts_ilp

# Solutions for manually engineered test letter counts.
# TODO: Add these
test_data_small_sol = ["ADD", "HERE"]
test_data_small2_sol = ["ADD", "HERE"]
test_data_medium_sol = ["ADD", "HERE"]

# Load the test letter counts from excel and preprocess the texts.

test_letter_counts: dict[str, dict[str, int]] = {
    "small": {},  # These will be replaced with dictionary of letter counts
    "small2": {},
    "medium": {},
}

for test_name in test_letter_counts:
    letter_counts_df: pd.DataFrame = pd.read_excel(
        f"data/letter_counts_test_{test_name}.xlsx", header=None
    )
    test_letter_counts[test_name] = dict(zip(letter_counts_df[0], letter_counts_df[1]))

# Make texts upper case and remove spaces
texts: list[str] = [text.upper().replace(" ", "") for text in taylor_texts]
# Remove texts that contain characters other than A-Z
texts = [
    text
    for text in texts
    if all(letter in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" for letter in text)
]

# Actual tests


class TestFindTextsRecursive(unittest.TestCase):
    """Tests for the recursive algorithm."""

    def test_small(self):
        """Test the small test case."""
        letter_counts = test_letter_counts["small"]
        _, solution_texts, _ = find_best_texts_recursive(letter_counts, texts)
        self.assertCountEqual(solution_texts, test_data_small_sol)

    def test_small2(self):
        """Test the small2 test case."""
        letter_counts = test_letter_counts["small2"]
        _, solution_texts, _ = find_best_texts_recursive(letter_counts, texts)
        self.assertCountEqual(solution_texts, test_data_small2_sol)

    def test_medium(self):
        """Test the medium test case."""
        letter_counts = test_letter_counts["medium"]
        _, solution_texts, _ = find_best_texts_recursive(letter_counts, texts)
        self.assertCountEqual(solution_texts, test_data_medium_sol)


class TestFindTextsILP(unittest.TestCase):
    """Tests for the ILP algorithm."""

    def test_small(self):
        """Test the small test case."""
        letter_counts = test_letter_counts["small"]
        _, solution_texts = find_best_texts_ilp(letter_counts, texts, False)
        self.assertCountEqual(solution_texts, test_data_small_sol)

    def test_small2(self):
        """Test the small2 test case."""
        letter_counts = test_letter_counts["small2"]
        _, solution_texts = find_best_texts_ilp(letter_counts, texts, False)
        self.assertCountEqual(solution_texts, test_data_small2_sol)

    def test_medium(self):
        """Test the medium test case."""
        letter_counts = test_letter_counts["medium"]
        _, solution_texts = find_best_texts_ilp(letter_counts, texts, False)
        self.assertCountEqual(solution_texts, test_data_medium_sol)


if __name__ == "__main__":
    unittest.main()
