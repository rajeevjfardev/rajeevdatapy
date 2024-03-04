def remove_nth_character(s, n):
    if s and 0 <= n < len(s):
        return s[:n] + s[n+1:]
    else:
        return s

sample_string = "Python"
n = 3

result_string = remove_nth_character(sample_string, n)

print("Original string:", sample_string)
print(f"String after removing {n}th index character:", result_string)
