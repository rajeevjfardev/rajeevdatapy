
#practiceagain

def replace_not_poor(s):
    not_pos = s.find('not')
    poor_pos = s.find('poor')
    
    if poor_pos > not_pos and not_pos > 0 and poor_pos > 0:
        s = s[:not_pos] + 'good' + s[poor_pos + 4:]
    return s

sample_strings = [
    'The lyrics is not that poor!',
    'The lyrics is poor!'
]

for string in sample_strings:
    result = replace_not_poor(string)
    print(f"Original string: '{string}' - Resulting string: '{result}'")
