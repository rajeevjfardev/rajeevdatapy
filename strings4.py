def change_char(s):
    if s:
        first_char = s[0]
        updated = first_char + s[1:].replace(first_char, '$')
        return updated
    else:
        return s

sample= 'rajeev'

final = change_char(sample)
print("Original string:", sample_string)
print("Modified string:", final)
