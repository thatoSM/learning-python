"""
Practice - Making O(n) visible by counting steps

Purpose:
    Big-O made no sense as a definition, so this counts the actual work a
    linear search does as the input grows.

What it does:
    Runs a linear search for the last item of lists sized 10, 100, 1000 and
    10000, incrementing a counter on every element checked.

Result:
    10 items     ->  10 steps
    100 items    ->  100 steps
    1000 items   ->  1000 steps
    10000 items  ->  10000 steps

What I learned:
    - Big-O describes how work grows as input grows - it is not measured in
      seconds and does not depend on how fast the computer is
    - O(n) ("linear") means steps grow in lockstep with input size: 10x the
      input is 10x the work. The numbers above are that relationship
    - n always means the size of the input
    - Worst case here is the target being last or absent, since that forces
      the loop to check everything
    - Next: O(log n), where each step throws away half the remaining data, so
      10000 items should finish in roughly 14 steps instead of 10000
"""

def linear_search(nums, target):
    steps = 0
    for i, value in enumerate(nums):
        steps = steps + 1
        if value == target:
            print("Found at position", i, "after", steps, "steps")
            return i
    print("Not found after", steps, "steps")
    return -1

small = list(range(10))
medium = list(range(100))
big = list(range(1000))
huge = list(range(10000))

print("Searching for the last item in each list:")
linear_search(small, 9)
linear_search(medium, 99)
linear_search(big, 999)
linear_search(huge, 9999)