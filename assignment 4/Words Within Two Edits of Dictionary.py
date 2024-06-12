def words_within_two_edits(queries, dictionary):
    def within_two_edits(word1, word2):
        count = sum(1 for a, b in zip(word1, word2) if a != b)
        count += abs(len(word1) - len(word2))
        return count <= 2

    result = []
    
    for query in queries:
        for dict in dictionary:
            if within_two_edits(query, dict):
                result.append(query)
                break

    return result

queries = ["word", "note", "ants", "wood"]
dictionary = ["wood", "joke", "moat"]
print(words_within_two_edits(queries, dictionary))
