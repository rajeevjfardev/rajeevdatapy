def modify_string(s):
    if len(s) < 3:
        return s
    if s.endswith('ing'):
        return s + 'ly'
    return s + 'ing'

sample_strings = ['abc', 'string', 'no']

for string in sample_strings:
    result = modify_string(string)
    print(f"Original string: '{string}' - Modified string: '{result}'")
