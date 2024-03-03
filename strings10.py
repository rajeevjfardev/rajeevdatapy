def swap_first_last_characters(s):
    # Check if the string length is greater than 1
    if len(s) > 1:
        # Swap the first and last characters
        return s[-1] + s[1:-1] + s[0]
    else:
        # Return the original string if it's empty or has only one character
        return s

# Sample string
sample_string = "python"

# Swap the first and last characters of the string
result_string = swap_first_last_characters(sample_string)

# Print the result
print("Original string:", sample_string)
print("String after swapping first and last characters:", result_string)
