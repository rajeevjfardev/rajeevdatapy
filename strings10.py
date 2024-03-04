def swap_first_last_characters(s):
    if len(s) > 1:
        return s[-1] + s[1:-1] + s[0]
    else:
        return s

sample_string = "python"

result_string = swap_first_last_characters(sample_string)

print("Original string:", sample_string)
print("String after swapping first and last characters:", result_string)
