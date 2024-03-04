
#practiceagain

def generate_dict(n):
    return {x: x*x for x in range(1, n+1)}

n = 5

result_dict = generate_dict(n)

print("Generated dictionary:", result_dict)
