def swap_first_two_chars(a, b):
    # Swap the first two characters of each string
    new_a = b[:2] + a[2:]
    new_b = a[:2] + b[2:]
    # Combine the modified strings, separated by a space
    return new_a + ' ' + new_b

# Sample strings
string1 = 'abc'
string2 = 'xyz'

# Apply the function and print the result
result = swap_first_two_chars(string1, string2)
print("Result:", result)
