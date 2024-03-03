# Function to generate dictionary
def generate_dict(n):
    return {x: x*x for x in range(1, n+1)}

# Sample input
n = 5

# Generate the dictionary
result_dict = generate_dict(n)

# Print the dictionary
print("Generated dictionary:", result_dict)
