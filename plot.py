import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
# Import texts from bracelet_texts.py
from bracelet_texts import texts


# Read letter counts from xlsx file.
letter_counts = pd.read_excel('letter_counts_real.xlsx', header=None)
letter_counts_dict = dict(zip(letter_counts[0], letter_counts[1]))

# Make texts upper case and remove spaces.
texts = [text.upper().replace(' ', '') for text in texts] 

# Plot bar chart of letter counts
plt.figure(1)
plt.bar(letter_counts_dict.keys(), letter_counts_dict.values())
plt.xlabel('Letter')
plt.ylabel('Count')

def can_form_text(letter_counts_dict, text):
  for letter in text:
    letter_count = text.count(letter)
    letter_balance = letter_counts_dict.get(letter, -1)
    if letter_balance < letter_count:
      return False
  return True

def remove_impossible_texts(letter_counts_dict, texts_list):
  possible_texts = []
  for text in texts_list:
    if can_form_text(letter_counts_dict, text):
      possible_texts.append(text)
  return possible_texts

possible_texts = remove_impossible_texts(letter_counts_dict, texts)

letter_counts_in_texts = {}
for text in possible_texts:
  for letter in text:
    if letter in letter_counts_in_texts:
      letter_counts_in_texts[letter] += 1
    else:
      letter_counts_in_texts[letter] = 1

# Plot to letter counts to new figure in texts to compare.
plt.figure(2)
plt.bar(letter_counts_in_texts.keys(), letter_counts_in_texts.values())
plt.xlabel('Letter')
plt.ylabel('Count')
plt.show()
