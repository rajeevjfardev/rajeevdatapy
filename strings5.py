def swap(a, b):
    new_a = b[:2] + a[2:]
    new_b = a[:2] + b[2:]
    return new_a + ' ' + new_b

sample1 = 'trojan'
sample2 = 'horse'

result = swap(sample1, sample2)
print(result)
