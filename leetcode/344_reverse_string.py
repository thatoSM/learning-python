from typing import List
# LeetCode #344 — Reverse String (Easy)

# Reverse a list of characters in-place.
# "In-place" means modify the original list, don't create a new one.
# O(1) memory means only use a few extra variables, not a whole new list.

# Examples:
#   ["h","e","l","l","o"] → ["o","l","l","e","h"]
#   ["H","a","n","n","a","h"] → ["h","a","n","n","a","H"]

# My approach: two pointers.
# Start one pointer at the beginning and one at the end.
# Swap the values they point to.
# Move both pointers toward the middle.
# Stop when they meet.

def reverseString(self, s: List[str]) -> None:
    """
    Do not return anything, modify s in-place instead.
    """
    left = 0
    right = len(s) - 1

    while left < right:
        s[left], s[right] = s[right], s[left]

        left += 1
        right -= 1