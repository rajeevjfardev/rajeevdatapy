def modify_string(s):
    # Check if string length is less than 3
    if len(s) < 3:
        return s
    # If string ends with 'ing', add 'ly'
    if s.endswith('ing'):
        return s + 'ly'
    # Otherwise, add 'ing'
    return s + 'ing'

# Sample strings
sample_strings = ['abc', 'string', 'no']

# Apply the function to each sample string and print the result
for string in sample_strings:
    result = modify_string(string)
    print(f"Original string: '{string}' - Modified string: '{result}'")
