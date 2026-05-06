"""
Re-test of LeetCode #125 - Valid Palindrome.

Cold re-attempt of a problem solved earlier this week.
Tests whether the dictionary/comprehension/cleaning patterns
are in production memory or just recognition memory.

Result: passed after one round of coaching on Step 1 (cleaning logic).
The slice [::-1] for reversal was solid from memory.
The .isalnum() filtering needed one round of structured rebuild.
"""
def clean_string(s):   
   
    cleaned = []
    for c in s:
        if c.isalnum():
            cleaned.append(c.lower())
    return "".join(cleaned)

def isPalindrome(s):
    cleaned = clean_string(s)
    return cleaned == cleaned[::-1]
    
print(isPalindrome("A man, a plan, a canal: Panama"))  # Expected: True
print(isPalindrome("race a car"))                       # Expected: False
print(isPalindrome(" "))                                # Expected: True                     # Expected: helloworld