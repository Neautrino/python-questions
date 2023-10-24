def find_longest_concatenated_word(word_list):
    def can_construct(word, word_set):
        if word in word_set:
            return True
        for i in range(1, len(word)):
            prefix, suffix = word[:i], word[i:]
            if prefix in word_set and can_construct(suffix, word_set):
                return True
        return False

    word_set = set(word_list)
    word_list.sort(key=lambda x: (-len(x), x))
    
    for word in word_list:
        word_set.remove(word)
        if can_construct(word, word_set):
            return word

    return None

# Example usage:
words = ["cat", "cats", "catsdogcats", "dog", "dogcatsdog", "hippopotamuses", "rat", "ratcatsdogfish"]
result = find_longest_concatenated_word(words)
print(result)
