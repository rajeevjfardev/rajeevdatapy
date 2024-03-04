
#practiceagain

def string_manipulation(s):
    if len(s) < 2:
        return ''
    return s[:2] + s[-2:]

sample_strings = ['w3resource', 'w3', ' w']

for string in sample_strings:
    result = string_manipulation(string)
    print(f"Original string: '{string}' - Result: '{result}'")
