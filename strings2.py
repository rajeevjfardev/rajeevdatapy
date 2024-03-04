sample_string = 'google.com'

char_frequency = {}

for char in sample_string:
    if char in char_frequency:
        char_frequency[char] += 1
    else:
        char_frequency[char] = 1

print("frequency", char_frequency)
