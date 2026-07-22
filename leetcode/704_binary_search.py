"""
LeetCode #704 - Binary Search (Easy)

Problem:
    Given a list of integers sorted in ascending order with no duplicates, and a
    target integer, return the index where the target sits in the list. If the
    target is not in the list at all, return -1. The problem requires the search
    to run in O(log n) time.

Examples:
    nums = [-1, 0, 3, 5, 9, 12], target = 9    ->   4
    nums = [-1, 0, 3, 5, 9, 12], target = 2    ->   -1

Constraints:
    1 <= len(nums) <= 10^4, values between -10^4 and 10^4,
    sorted ascending, all values unique.

Approach:
    Solved with a linear scan. Looped over the list with enumerate so each pass
    gives both the position and the value at that position. Compared each value
    to the target and returned the position immediately on a match. If the loop
    finishes without a match, control falls through to a return of -1 sitting
    outside the loop. This is correct but does NOT meet the O(log n) requirement
    the problem asks for - a binary search rewrite is planned.

What I learned:
    - enumerate(nums) hands back a (position, value) pair each pass; a plain
      "for x in nums" only hands back values, which is why it cannot solve an
      index-returning problem
    - The position is what gets returned; the value is what gets compared.
      Mixing these up was my main bug
    - A search loop returns ONLY on a match. Using an else with a return inside
      the loop kills it after the first element
    - The "not found" return must live outside the loop so it is only reached
      after every element has been checked
    - O(n) means work grows in lockstep with input size - proved this by
      counting steps: 10 items took 10 steps, 10000 items took 10000 steps
    - Constraints are clues, not decoration. "Sorted" plus "O(log n)" together
      point at a halving technique, which a linear scan ignores completely

Pattern: Linear search (array traversal). Intended pattern is Binary Search.
Time complexity: O(n) - worst case touches every element once
Space complexity: O(1) - only a fixed number of variables regardless of input size
"""

from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        for i, value in enumerate(nums):
            if value == target:
                return i
        return -1
    
sol = Solution()
print(sol.search([-1, 0, 3, 5, 9, 12], 9))
print(sol.search([-1, 0, 3, 5, 9, 12], 2))