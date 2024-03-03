# Define a list with duplicates
my_list = [1, 2, 2, 3, 4, 4, 5, 6, 6, 7, 8, 8, 9]

# Convert the list to a set (which automatically removes duplicates)
my_set = set(my_list)

# Convert the set back to a list
my_list = list(my_set)

# Print the list without duplicates
print(my_list)