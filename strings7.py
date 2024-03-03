def replace_not_poor(s):
    # Find the first occurrence of 'not' and 'poor'
    not_pos = s.find('not')
    poor_pos = s.find('poor')
    
    # Check if 'not' comes before 'poor'
    if poor_pos > not_pos and not_pos > 0 and poor_pos > 0:
        # Replace the 'not'...'poor' substring with 'good'
        s = s[:not_pos] + 'good' + s[poor_pos + 4:]
    return s

# Sample strings
sample_strings = [
    'The lyrics is not that poor!',
    'The lyrics is poor!'
]

# Apply the function to each sample string and print the result
for string in sample_strings:
    result = replace_not_poor(string)
    print(f"Original string: '{string}' - Resulting string: '{result}'")
