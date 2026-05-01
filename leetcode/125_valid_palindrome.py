"""
LeetCode #125 - Valid Palindrome (Easy)

Problem (in my words):
    Given a string, determine whether it reads the same forward and
    backward, ignoring punctuation, spaces, and letter case. Return
    True if it is a palindrome, False otherwise.

    The cleaning rules:
    - Treat uppercase and lowercase as the same letter
    - Ignore anything that isn't a letter or number (spaces, commas,
      punctuation, etc.)
    - An empty string after cleaning counts as a palindrome

Examples:
    "A man, a plan, a canal: Panama"  ->  True
    "race a car"                      ->  False
    " "                               ->  True   (empty after cleaning)

Constraints:
    1 <= len(s) <= 200,000
    s contains only printable ASCII characters

Approach:
    Two-step solution.
    1. Clean the string: lowercase everything and keep only alphanumeric
       characters. Used a generator expression with .isalnum() to filter.
    2. Compare the cleaned string to its reverse using slice [::-1].

What I learned:
    - .lower() returns a new lowercase string (transforms)
    - .isalnum() checks if a character is letter/number (returns bool)
    - Methods that CHECK vs methods that TRANSFORM behave differently
    - "".join(iterable) glues characters back into a string
    - Generator expression: (c for c in s if c.isalnum()) - lazy, uses
      less memory than list comprehension for large inputs
    - TypeError "object is not subscriptable" means trying to slice
      something that doesn't support [] (like a bool)
"""

def isPalindrome(s):
    cleaned = "".join(c for c in s.lower() if c.isalnum())
    return cleaned == cleaned[::-1]

print(isPalindrome("A man, a plan, a canal: Panama"))  
print(isPalindrome("race a car"))                       
print(isPalindrome(" "))                                