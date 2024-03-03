def string_manipulation(s):
    # Check if string length is less than 2
    if len(s) < 2:
        return ''
    # If string length is 2 or more, return first 2 and last 2 characters
    return s[:2] + s[-2:]

# Sample strings
sample_strings = ['w3resource', 'w3', ' w']

# Apply the function to each sample string and print the result
for string in sample_strings:
    result = string_manipulation(string)
    print(f"Original string: '{string}' - Result: '{result}'")
