# LeetCode #242 — Valid Anagram (Easy)

# Check if two strings are anagrams (same letters, different order).
# "listen" and "silent" are anagrams.
# "hello" and "world" are not.

# Examples:
#   "anagram", "nagaram" → True
#   "rat", "car" → False

# My approach: count letters in each string using dictionaries.
# If both dictionaries have the same letter counts, they're anagrams.

# Key concept: dictionary counting pattern.
# counts[key] = counts.get(key, 0) + 1
# This is used in hundreds of problems — memorise it.

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        count_s = {}
        for letter in s:
            count_s[letter] =  count_s.get(letter, 0) + 1

        count_t = {}
        for letter in t:
            count_t[letter] =  count_t.get(letter, 0) + 1

        return count_s == count_t