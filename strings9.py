def remove_nth_character(s, n):
    # Check if the string is nonempty and n is within the string's range
    if s and 0 <= n < len(s):
        # Return the string without the nth index character
        return s[:n] + s[n+1:]
    else:
        # Return original string if n is out of range or string is empty
        return s

# Sample string and index
sample_string = "Python"
n = 3

# Remove the nth index character from the string
result_string = remove_nth_character(sample_string, n)

# Print the result
print("Original string:", sample_string)
print(f"String after removing {n}th index character:", result_string)
