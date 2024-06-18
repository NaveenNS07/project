def max_num_of_palindromes(s, k):
    def is_palindrome(sub):
        return sub == sub[::-1]

    def backtrack(start, path):
        nonlocal max_count
        if start == len(s):
            max_count = max(max_count, len(path))
            return

        for end in range(start + k, len(s) + 1):
            sub = s[start:end]
            if is_palindrome(sub):
                path.append(sub)
                backtrack(end, path)
                path.pop()

    max_count = 0
    backtrack(0, [])
    return max_count

s = "abaccdbbd"
k = 3
print(max_num_of_palindromes(s, k))  #