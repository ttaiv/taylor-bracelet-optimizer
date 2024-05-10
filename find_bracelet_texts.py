# Description: This script finds texts that you can form using the letters you have so that you use as many letters as possible.
# Author: Teemu
# Version: 0.1

# Import pandas and numpy
import numpy as np
import pandas as pd
from typing import List, Dict, Tuple

texts = ['A Message From Taylor',

'A Perfectly Good Heart',

'A Place In This World',

'Afterglow',

'All Night Diner',

'All Of The Girls You Loved Before',

'All Too Well',

'All You Had To Do Was Stay',

'American Boy',

'American Girl',

'Am I Ready For Love',

'Angelina',

'Anti Hero',

'august',

'Babe',

'Back to December',

'Bad Blood',

'Beautiful Eyes',

'Beautiful Ghosts',

'Begin Again',

'Bein With My Baby',

'Bejeweled',

'Best Days Of Your Life',

'Bette Davis Eyes',

'Better Man',

'Better Off',

'Better Than Revenge',

'betty',

'Bigger Than The Whole Sky',

'Big Star',

'Birch',

'Blank Space',

'Both Of Us',

'Bother Me',

'Breathe',

'Breathless',

'Brought Up That Way',

'But Daddy I Love Him',

'By The Way',

'Bye Bye Baby',

'Call It What You Want',

'Cannon Balls',

'Cant Stop Loving You',

'cardigan',

'Carolina',

'Castles Crumbling',

'champagne problems',

'Change',

'Christmas Must Be Something More',

'Christmas Tree Farm',

'Christmases When You Were Mine',

'Clara Bow',

'Clean',

'closure',

'Cold As You',

'Come Back Be Here',

'Come In With The Rain',

'coney island',

'Cornelia Street',

'cowboy like me',

'Crazier',

'Cruel Summer',

'Dancing With Our Hands Tied',

'Dark Blue Tennessee',

'Daylight',

'Dear John',

'Dear Reader',

'Death By A Thousand Cuts',

'Delicate',

'Diary of Me',

'Didnt They',

'Dont Blame Me',

'Dont You',

'dorothea',

'Down Bad',

'Drama Queen',

'Dress',

'Drops of Jupiter',

'Electric Touch',

'Enchanted',

'End Game',

'epiphany',

'evermore',

'Everything Has Changed',

'exile',

'Eyes Open',

'False God',

'Family',

'Fearless',

'Fifteen',

'Florida',

'Foolish One',

'Forever & Always',

'Forever Winter',

'Fortnight',

'Fresh Out the Slammer',

'Gasoline',

'Getaway Car',

'Girl At Home',

'Glitch',

'gold rush',

'Gorgeous',

'Guilty as Sin',

'Half of My Heart',

'happiness',

'Haunted',

'Hey Stephen',

'High Infidelity',

'Highway Donâ€™t Care',

'Hits Different',

'hoax',

'Hold On',

'Holy Ground',

'How You Get The Girl',

'I Almost Do',

'I Bet You Think About Me',

'I Can Do It With a Broken Heart',

'I Can Fix Him',

'I Can See You',

'I Did Something Bad',

'I Dont Wanna Live Forever',

'I Forgot That You Existed',

'If This Was A Movie',

'I Heart Question Mark',

'I Knew You Were Trouble',

'I Know Places',

'illicit affairs',

'Id Lie',

'Im Every Woman',

'Im Only Me When Iâ€™m With You',

'Innocent',

'Invisible',

'invisible string',

'I Think He Knows',

'I Used to Fly',

'I Want You Back',

'Its Nice To Have A Friend',

'its time to go',

'ivy',

'I Wish You Would',

'Is It Over Now',

'Jump Then Fall',

'Just South of Knowing Why',

'Karma',

'King Of My Heart',

'Labyrinth',

'Last Christmas',

'Last Kiss',

'Lavender Haze',

'Lets Go',

'loml',

'London Boy',

'Long Live',

'long story short',

'Look What You Made Me Do',

'Lover',

'Love Is A Drug',

'Love Story',

'Lucky You',

'Macavity',

'mad woman',

'marjorie',

'Maroon',

'Marys Song',

'Mastermind',

'Matches',

'ME',

'Mean',

'Meet Me At Midnight',

'Message In A Bottle',

'Midnight Rain',

'Mine',

'mirrorball',

'Miss Americana & The Heartbreak Prince',

'Mr Perfectly Fine',

'My Boy Only Breaks His Favorite Toys',

'My Cure',

'my tears ricochet',

'Nashville',

'Need',

'Need You Now',

'Never Fade',

'Never Grow Up',

'Never Mind',

'New Romantics',

'New Years Day',

'no body no crime',

'Nothing New',

'Now That We Dont Talk',

'Only The Young',

'Ours',

'Our Song',

'Out Of The Woods',

'Paper Rings',

'Paris',

'peace',

'Permanent Marker',

'Picture To Burn',

'Question',

'Ready For It',

'Red',

'Renegade',

'REVENGE',

'right where you left me',

'Riptide',

'Ronan',

'Run',

'Sad Beautiful Tragic',

'Safe and Sound',

'Santa Baby',

'Say Dont Go',

'September',

'seven',

'Shake It Off',

'Shouldve Said No',

'Silent Night',

'Snow On The Beach',

'Slut',

'So It Goes',

'So Long London',

'Songs About You',

'Sparks Fly',

'Speak Now',

'Spinning Around',

'Starlight',

'State of Grace',

'Stay Beautiful',

'Stay Stay Stay',

'Style',

'Suburban Legends',

'Superman',

'SuperStar',

'Sweeter Than Fiction',

'Sweet Escape',

'Sweet Nothing',

'Sweet Tea and Gods Graces',

'Teardrops On My Guitar',

'Tell Me',

'Tell Me Why',

'Ten Dollars and a Six Pack',

'Tennessee',

'Thats When',

'The Albatross',

'The Alchemy',

'The Alcott',

'The Archer',

'The Best Day',

'The Bolter',

'The Great War',

'The Joker and the Queen',

'the lakes',

'the last great american dynasty',

'The Last Time',

'The Lucky One',

'The Man',

'The Manuscript',

'The Moment I Knew',

'The Other Side Of The Door',

'The Outside',

'the 1',

'The Reason Why',

'The Smallest Man Who Ever Lived',

'The Story Of Us',

'The Tortured Poets Department',

'The Very First Night',

'The Way I Loved You',

'this is me trying',

'This Is Really Happening',

'This Is What You Came For',

'This Is Why We Cant Have Nice Things',

'This Love',

'Thug Story',

'Tied Together With A Smile',

'Til Brad Pitt Comes Along',

'Tim McGraw',

'Timeless',

'tis the damn season',

'Today Was A Fairytale',

'tolerate it',

'Treacherous',

'Two Is Better Than One',

'Untouchable',

'Vigilante Shit',

'We Are Never Ever Getting Back Together',

'We Were Happy',

'Welcome Distraction',

'Welcome to New York',

'What Do You Say',

'What Hurts The Most',

'What To Wear',

'When Emma Falls In Love',

'Who Ive Always Been',

'Whos Afraid of Little Old Me',

'Wildest Dreams',

'Will You Love Me Tomorrow',

'willow',

'White Christmas',

'White Horse',

'Wonderland',

'Wouldve Couldve Shouldve',

'You All Over Me',

'You Are In Love',

'You Belong With Me',

'You Dont Have To Call',

'You Need To Calm Down',

'Youll Always Find Your Way Back Home',

'Youre Losing Me',

'Youre Not Sorry',

'Youre On Your Own, Kid',

'Your Anything',

'Your Face',

'22']

texts = [text.upper().replace(' ', '') for text in texts] # make texts upper case and remove spaces

# Read letter counts from xlsx file.
letter_counts = pd.read_excel('letter_counts2.xlsx', header=None)

letter_counts_dict = dict(zip(letter_counts[0], letter_counts[1])) # form dictionary
total_letter_count = sum(letter_counts_dict.values())

# Recursive function to choose texts so that the total letter count is minimized. 
# Returns a tuple of the lowest letter count possible and the list of texts chosen.
def choose_text(current_text_idx: int, letters_left_total: int, letters_left_base: Dict[str, int]) -> Tuple[int, List[str]]:
  if letters_left_total == 0:
    return 0, [] # we used all the letters, early return
  if current_text_idx >= len(texts):
    return letters_left_total, [] # out of texts to try
  
  # Try this text.
  text = texts[current_text_idx]
  letters_left = letters_left_base.copy() # this can be modified

  # Check if we have enough letters to form this text.
  suitable_letter_count = 0
  for letter in text:
    count = letters_left.get(letter, -1)
    if count == -1:
      print(f"Letter {letter} is not in the letter counts.")
    if count > 0: # we have this letter
      letters_left[letter] -= 1
      suitable_letter_count += 1
    else:
      break # break loop if we do not have enough letters
   
  excluded = choose_text(current_text_idx + 1, letters_left_total, letters_left_base) # recursive call without this text
  if suitable_letter_count < len(text): # cannot make text
    # return unused letters
    # for i in range(suitable_letter_count):
    #  letter_to_return = text[i]
    #  letters_left[letter_to_return] += 1
    return excluded
  # can make text
  sub_lowest_count, sub_chosen_texts = \
    choose_text(current_text_idx + 1, letters_left_total - len(text), letters_left.copy()) # recursive call
    
  included = (sub_lowest_count, [text] + sub_chosen_texts) # including this text decreases the letter count and includes this text

  if included[0] < excluded[0]: # choose the one with the lowest letter count
    return included
  else:
    return excluded
# function ends

lowest_letter_count_possible, best_texts = choose_text(0, total_letter_count, letter_counts_dict.copy()) # call recursive function

print(f"You started with {total_letter_count} letters.")
print(f"You can decrease the letter count to {lowest_letter_count_possible} by choosing the following texts:")
for text in best_texts:
  print(text)
  


    

