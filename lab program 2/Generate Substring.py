def stringMatching(words):
    return [word for word in words if any(other_word.find(word) != -1 for other_word in words if word != other_word)]

words = ["mass", "as", "hero", "superhero"]
output = stringMatching(words)
print(output)