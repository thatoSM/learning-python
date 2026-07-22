"""
Practice - Plain for loop vs enumerate()

Purpose:
    Side-by-side demo of the two ways to loop over a list in Python, written
    after getting stuck on LeetCode #704 because I used the wrong one.

What it shows:
    PART 1 - "for value in fruits" gives back only the items:
        apple / banana / cherry

    PART 2 - "for i, value in enumerate(fruits)" gives back the position and
    the item as a pair:
        0 apple / 1 banana / 2 cherry

Rule for choosing:
    - Need to know where something is (return an index, number a list, write to
      a position)  ->  use enumerate
    - Only care about the items themselves (print them, add them up)
      ->  use the plain for loop

Gotcha:
    In "for i, value in enumerate(...)" the NAMES are my choice but the ORDER is
    fixed - Python always gives position first, item second.
"""

fruits = ["apple", "banana", "cherry"]

print("--- PART 1: for value in fruits ---")
for value in fruits:
    print(value)

print()
print("--- PART 2: for i, value in enumerate(fruits) ---")
for i, value in enumerate(fruits):
    print(i, value)