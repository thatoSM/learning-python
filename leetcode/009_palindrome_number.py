class Solution:
    def isPalindrome(self, x: int) -> bool:
        # Shortcut: negative numbers can't be palindromes
        if x < 0:
            return False
        # Convert the number to a string so we can reverse it
        number_as_text = str(x)
        # Reverse the string using Python's slice trick
        reversed_text = number_as_text[::-1]
        # Compare them — if they match, it's a palindrome
        if number_as_text == reversed_text:
            return True
        else:
            return False