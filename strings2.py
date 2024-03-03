# Sample string
sample_string = 'google.com'

# Initialize an empty dictionary to store character frequency
char_frequency = {}

# Iterate over each character in the string
for char in sample_string:
    if char in char_frequency:
        # If the character is already in the dictionary, increment its count
        char_frequency[char] += 1
    else:
        # If the character is not in the dictionary, add it with count 1
        char_frequency[char] = 1

# Print the character frequency dictionary
print("Character frequency in the string:", char_frequency)
