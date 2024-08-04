# Friendship bracelet optimizer

## Introduction

This is a program that, given letters and their counts and a list of strings, finds the best strings to form using the given letters so that the remaining total letter count is minimized. In other words, it minimizes the leftover letters. The idea of this program was to help in building [friendship bracelets](https://www.theguardian.com/music/2024/feb/07/taylor-swift-eras-tour-australia-friendship-bracelets-inspiration-beads-explained) for Taylor Swift's Eras tour. My girlfriend is a huge fan and wanted to use her bought letters as efficiently as possible.

However, this turned out to be quite a tough problem and the program is still very slow for large letters counts (the test set with 61 letters and 310 bracelet text options runs in 1 minute and 15 seconds on my machine). The problem seems to be NP-complete as it can be seen as a [Knapsack problem](https://en.wikipedia.org/wiki/Knapsack_problem) with extra constraints. Now the constraint is not the carrying capacity of the knapsack, but instead the available count of each letter. So instead of one we have 26 (the count of letters in English alphabet) different constraints.

## Files
- find_bracelet_texs
