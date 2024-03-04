sample = {'a': 1, 'b': 2, 'c': 3, 'd': 5}

sorted_ascending = dict(sorted(sample.items(), key=lambda item: item[1]))
sorted_descending = dict(sorted(sample.items(), key=lambda item: item[1], reverse=True))

print("ascending order:", sorted_ascending)
print("descending order:", sorted_descending)
