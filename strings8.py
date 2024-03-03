def find_longest_word(word_list):
    # Initialize variables to store the longest word and its length
    longest_word = ""
    longest_length = 0

    # Iterate through each word in the list
    for word in word_list:
        # Update the longest word and its length if the current word is longer
        if len(word) > longest_length:
            longest_word = word
            longest_length = len(word)

    return longest_word, longest_length

# Sample list of words
words = ["Python", "Exercises", "Development", "Coding", "LongestWord"]

# Find the longest word and its length
longest_word, longest_length = find_longest_word(words)

# Print the result
print("Longest word:", longest_word)
print("Length of the longest word:", longest_length)
