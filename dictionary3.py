# Sample dictionaries
dic1 = {1: 10, 2: 20}
dic2 = {3: 30, 4: 40}
dic3 = {5: 50, 6: 60}

# Create a new dictionary and update it with the other dictionaries
result_dict = {}
for d in (dic1, dic2, dic3):  # Loop through each dictionary
    result_dict.update(d)  # Update the result dictionary

# Print the concatenated dictionary
print("Concatenated dictionary:", result_dict)
