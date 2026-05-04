def containsDuplicate(nums):

    seen = set()

    for n in nums:
        if n in seen:
            return True     
        else:
            seen.add(n)

    return False            

print(containsDuplicate([1, 2, 3, 1]))                   # Expected: True
print(containsDuplicate([1, 2, 3, 4]))                   # Expected: False
print(containsDuplicate([1, 1, 1, 3, 3, 4, 3, 2, 4, 2])) # Expected: True    
pass