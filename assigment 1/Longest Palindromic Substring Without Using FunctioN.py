s = "babad"
def expand_around_center(s, left, right):
    while left >= 0 and right < len(s) and s[left] == s[right]:
        left -= 1
        right += 1
    return s[left + 1:right]

longest_palindrome = ""
for i in range(len(s)):
    palindrome1 = expand_around_center(s, i, i)
    palindrome2 = expand_around_center(s, i, i + 1)
    longest_palindrome = max(longest_palindrome, palindrome1, palindrome2, key=len)

print(longest_palindrome)