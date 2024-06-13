def combinationSum2(candidates, target):
    def backtrack(start, path, target):
        if target == 0:
            result.append(path)
            return
        for i in range(start, len(candidates)):
            if i > start and candidates[i] == candidates[i - 1]:
                continue
            if candidates[i] > target:
                break
            backtrack(i + 1, path + [candidates[i]], target - candidates[i])

    candidates.sort()
    result = []
    backtrack(0, [], target)
    return result

candidates = [10, 1, 2, 7, 6, 1, 5]
target = 8
print(combinationSum2(candidates, target))