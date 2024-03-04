def modified(s):
    if len(s) < 3:
        return s
    if s.endswith('thon'):
        return s + 'av'
    return s + 'thon'

sample_strings = ['python', 'java']

for string in sample_strings:
    result = modified(string)
    print(result)
