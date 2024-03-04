def find_longest_word(word_list):
    longest_word = ""
    longest_length = 0

    for word in word_list:
        if len(word) > longest_length:
            longest_word = word
            longest_length = len(word)

    return longest_word, longest_length

words = ["Python", "Exercises", "Development", "Coding", "LongestWord"]

longest_word, longest_length = find_longest_word(words)

print("Longest word:", longest_word)
print("Length of the longest word:", longest_length)
