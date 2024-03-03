# Sample dictionary
my_dict = {'name': 'Alice', 'age': 30, 'city': 'New York'}

# Method 1: Iterating through keys
print("Iterating through keys:")
for key in my_dict:
    print(key)

# Method 2: Iterating through values
print("\nIterating through values:")
for value in my_dict.values():
    print(value)

# Method 3: Iterating through key-value pairs
print("\nIterating through key-value pairs:")
for key, value in my_dict.items():
    print(f"{key}: {value}")
