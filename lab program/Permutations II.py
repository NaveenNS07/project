from itertools import permutations

def permuteUnique(nums):
    unique_permutations = set()
    for perm in permutations(nums):
        if perm not in unique_permutations:
            unique_permutations.add(perm)
    return [list(perm) for perm in unique_permutations]

nums = [1, 1, 2]
print(permuteUnique(nums))