def sort_tuples(tuples):
    # Define a function to get the last element in a tuple
    def last_element(tuple):
        return tuple[-1]

    # Sort the tuples in increasing order based on the last element in each tuple
    sorted_tuples = sorted(tuples, key=last_element)
    return sorted_tuples

# Sample list
tuples = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]

# Sort the tuples and print the result
sorted_tuples = sort_tuples(tuples)
print(sorted_tuples)