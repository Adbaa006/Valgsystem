"""
stemmer = [3, 5, 6, 2, 7]
flest = -1

for i in range(len(stemmer)):
    if stemmer[i] > flest:
        flest = stemmer[i]

print(flest)
"""

import random

# Your list of items
items = ['apple', 'banana', 'cherry', 'date']

# Corresponding weights (percentages) for each item.
# These don't need to sum to 100, but their relative values determine the probability.
weights = [10, 30, 50, 10] # e.g., banana is 3 times more likely than apple

# Select one item based on the weights
selected_item = random.choices(items, weights=weights, k=1)[0]

print(f"Randomly selected item: {selected_item}")
