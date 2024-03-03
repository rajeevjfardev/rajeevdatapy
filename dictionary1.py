# Sample dictionary
sample_dict = {'a': 3, 'b': 1, 'c': 2, 'd': 4}

# Sort the dictionary by value in ascending order
sorted_dict_asc = dict(sorted(sample_dict.items(), key=lambda item: item[1]))

# Sort the dictionary by value in descending order
sorted_dict_desc = dict(sorted(sample_dict.items(), key=lambda item: item[1], reverse=True))

# Print the sorted dictionaries
print("Dictionary sorted in ascending order by value:", sorted_dict_asc)
print("Dictionary sorted in descending order by value:", sorted_dict_desc)
