# Description: This script finds texts that you can form using the letters you have so that you use as many letters as possible.
# Author: Teemu
# Version: 0.3

# Import pandas and numpy
import numpy as np
import pandas as pd

from bracelet_texts import texts

texts = [text.upper().replace(' ', '') for text in texts] # make texts upper case and remove spaces

# Read letter counts from xlsx file.
letter_counts = pd.read_excel('letter_counts_real.xlsx', header=None)

letter_counts_dict = dict(zip(letter_counts[0], letter_counts[1])) # form dictionary
total_letter_count = sum(letter_counts_dict.values())

all_time_best = (float('inf'), []) # tuple to store the best result so far

max_letters_left = 131 # chooce what are you happy with

# Recursive function to choose texts so that the total letter count is minimized. 
# Returns a tuple of the lowest letter count possible and the list of texts chosen.
def choose_text(current_text_idx: int, letters_left_total: int, letters_left_base: Dict[str, int]) -> Tuple[int, List[str]]:
  global all_time_best

  if current_text_idx <  0:
    return letters_left_total, [] # out of texts to try
  
  # Try this text.
  text = texts[current_text_idx]
  letters_left = letters_left_base.copy() # this can be modified

  # Check if we have enough letters to form this text.
  suitable_letter_count = 0
  for letter in text:
    count = letters_left.get(letter, -1)
    #if count == -1:
      #print(f"Letter {letter} is not in the letter counts.")
    if count > 0: # we have this letter
      letters_left[letter] -= 1
      suitable_letter_count += 1
    else:
      break # break loop if we do not have enough letters
   
  if suitable_letter_count < len(text): # cannot form current text
    included = (float('inf'), []) # exclude this text
  else: # can form current text
    # search for the best texts to form with the remaining letters
    lowest_letter_count, best_texts = \
      choose_text(current_text_idx - 1, letters_left_total - len(text), letters_left) # recursive call
    
    best_texts.append(text)
    included = (lowest_letter_count, best_texts)

  if included[0] <= max_letters_left:
    return included # early return 
  else:
    excluded = choose_text(current_text_idx - 1, letters_left_total, letters_left_base) # recursive call

    if excluded[0] <= max_letters_left:
      return excluded # early return

    if included[0] < excluded[0]: # choose the one with the lowest letter count
      if included[0] < all_time_best[0]:
        all_time_best = included
        print(f"Current best count: {included[0]} and texts: {included[1]}")
      return included
    else:
      if excluded[0] < all_time_best[0]:
        all_time_best = excluded
        print(f"Current best count: {excluded[0]} and texts: {excluded[1]}")
      return excluded
# function ends

lowest_letter_count_possible, best_texts = choose_text(len(texts) - 1, total_letter_count, letter_counts_dict) # call recursive function

print(f"You started with {total_letter_count} letters.")
print(f"You can decrease the letter count to {lowest_letter_count_possible} by choosing the following texts:")
for text in best_texts:
  print(text)
print("\n")


    

