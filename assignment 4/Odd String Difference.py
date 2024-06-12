def odd_string_difference(words):
    def to_difference_array(word):
        return [ord(word[i + 1]) - ord(word[i]) for i in range(len(word) - 1)]

    difference_arrays = [to_difference_array(word) for word in words]

    difference_count = {}
    for diff_array in difference_arrays:
        diff_tuple = tuple(diff_array)  
        if diff_tuple in difference_count:
            difference_count[diff_tuple] += 1
        else:
            difference_count[diff_tuple] = 1

    odd_diff_array = None
    for diff_array in difference_arrays:
        if difference_count[tuple(diff_array)] == 1:
            odd_diff_array = diff_array
            break

    for word in words:
        if to_difference_array(word) == odd_diff_array:
            return word

words = ["abc", "bcd", "ace"]
print(odd_string_difference(words))  
