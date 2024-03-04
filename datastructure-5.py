def match_words(words):
    ctr = 0
    for word in words:
        if len(word) >= 2 and word[0] == word[-1]:
            ctr += 1
    return ctr

sample_list = ['abc', 'xyz', 'aba', '1221']
print(match_words(sample_list)) 