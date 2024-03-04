def change_char(s):
    if s:
        first_char = s[0]
        modified_string = first_char + s[1:].replace(first_char, '$')
        return modified_string
    else:
        return s

sample_string = 'restart'

result = change_char(sample_string)
print("Original string:", sample_string)
print("Modified string:", result)
