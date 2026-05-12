"""
Dictionaries basics — lower-pressure practice.

Mapping key -> value. Faster than lists for lookups.
"""
print("Exercise 1: Create and read")

person = {
    "name": "Thato",
    "age": 19,
    "city": "Johannesburg"
}

# Print just the name
print(person["name"])

# Print just the city
print(person["city"])

print()

print("Exercise 2: Add and update")

person["country"] = "South Africa"   # add new key
person["age"] = 20                    # update existing

print(person)
print()

print("Exercise 3: Loop over keys")

for key in person:
    print(key)
print()

print("Exercise 4: Loop over key-value pairs")

for key, value in person.items():
    print(f"{key}: {value}")
print()

print("Exercise 5: Safe lookups")

print(person.get("name", "Unknown"))         # exists → Thato
print(person.get("phone", "Not provided"))   # missing → Not provided
print(person.get("country", "Unknown"))      # exists → South Africa
print()

print("Exercise 6: Counting letters")

word = "mississippi"
counts = {}

# For each letter in word, increment its count in counts
# (use .get() with default 0 to handle the "first time seeing" case)
for letter in word:
    counts[letter] = counts.get(letter, 0) + 1

print(counts)
print()