def swap_first_two_chars(a, b):
    new_a = b[:2] + a[2:]
    new_b = a[:2] + b[2:]
    return new_a + ' ' + new_b

string1 = 'abc'
string2 = 'xyz'

result = swap_first_two_chars(string1, string2)
print("Result:", result)
