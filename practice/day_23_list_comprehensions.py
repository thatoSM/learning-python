"""
Day 23 - List Comprehension practice

Goal: build production memory for list comprehension syntax.
Each section shows the for-loop version first (what I already know), then the list comprehension version (the new shortcut).
"""
# Exercise 1: Squares
print("Exercise 1: Squares")

numbers = [1, 2, 3, 4, 5]

squares_loop = []
for n in numbers:
    squares_loop.append(n * n)

print("For loop:     ", squares_loop)

squares_comp = [n * n for n in numbers]

print("Comprehension:", squares_comp)
print()

# Exercise 2: Doubling
print("Exercise 2: Doubling")

values = [10, 20, 30, 40]

doubled_loop = []
for a in values:
    doubled_loop.append(a * 2)

doubled_comp = [a * 2 for a in values]  # YOUR CODE HERE — replace [] with the comprehension

print("For loop:    ", doubled_loop)
print("Comprehension:", doubled_comp)
print()

# Exercise 3: Uppercase strings
print("Exercise 3: Uppercase strings")

languages = ["python", "java", "rust"]

upper_loop = []
for l in languages:
    upper_loop.append(l.upper())

upper_comp = [l.upper() for l in languages]

print("For loop: ", upper_loop)
print("Comprehension: ", upper_comp)
print()

# Exercise 4: Lengths
print("Exercise 4: Lengths")

words = ["hi", "world", "Python"]

length_loop = []
for w in words:
    length_loop.append(len(w))

length_comp = [len(w) for w in words]

print("For loop:     ", length_loop)
print("Comprehension:", length_comp)
print()

# Exercise 5: Even numbers only
print("Exercise 5: Even numbers only")

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

evens_loop = []
for n in numbers:
    if n % 2 == 0:
        evens_loop.append(n)

evens_comp = [n for n in numbers if n % 2 == 0] 

print("For loop:     ", evens_loop)
print("Comprehension:", evens_comp)
print()

# Exercise 6: Words at least 4 letters long
print("Exercise 6: Words at least 4 letters long")

words = ["hi", "world", "Python", "no", "code"]

words_loop = []
for w in words:
    if (len(w)>=4):
        words_loop.append(w)


words_comp = [w for w in words if len(w)>=4]
print("For loop:", words_loop)
print("Comprehension:", words_comp)
print()

# Exercise 7: Combine transformation and filter
print("Exercise 7: Combine transformation and filter")

numbers = [1, 2, 3, 4, 5, 6]

result_loop = []
for n in numbers:
    if n % 2 == 0:
        result_loop.append(n * n)

result_comp = [n * n for n in numbers if n % 2 == 0]
print("For loop:", result_loop)
print("Comprehension:", result_comp)
print()

# Exercise 8: Clean a string (the LeetCode #125 logic, rebuilt)
print("Exercise 8: Clean a string")

messy = "A man, a plan, a canal: Panama"

# For-loop version
cleaned_loop = ""
for c in messy.lower():
    if c.isalnum():
        cleaned_loop += c

cleaned_chars = [ c for c in messy.lower() if c.isalnum()] 

cleaned_comp = "".join(cleaned_chars)

print("For loop:     ", cleaned_loop)
print("Comprehension:", cleaned_comp)
print()