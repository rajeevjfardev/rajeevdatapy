def change_char(s):
    # Check if string is not empty
    if s:
        # Get the first character
        first_char = s[0]
        # Replace all occurrences of the first character with '$', except the first character itself
        modified_string = first_char + s[1:].replace(first_char, '$')
        return modified_string
    else:
        return s

# Sample string
sample_string = 'restart'

# Apply the function and print the result
result = change_char(sample_string)
print("Original string:", sample_string)
print("Modified string:", result)
