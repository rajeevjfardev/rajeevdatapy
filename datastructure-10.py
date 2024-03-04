
#practiceagain

def words_longer_than_n(words, n):
    
    longer_words = [word for word in words if len(word) > n]
    
    return longer_words

words_list = ["Python", "Java", "C", "JavaScript", "Go", "Rust"]

long_words = words_longer_than_n(words_list, 3)

print("Words longer than 3 characters:", long_words)