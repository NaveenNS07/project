def combinationSum(candidates, target):
    def backtrack(start, path, target):
        if target == 0:
            result.append(path[:])
            return
        for i in range(start, len(candidates)):
            if candidates[i] > target:
                continue
            path.append(candidates[i])
            backtrack(i, path, target - candidates[i])
            path.pop()

    result = []
    candidates.sort()
    backtrack(0, [], target)
    return result

candidates = [2, 3, 6, 7]
target = 7
print(combinationSum(candidates, target))