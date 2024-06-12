def min_operations_to_sort(nums):
    n = len(nums)
    target1 = list(range(n))  
    target2 = list(range(1, n)) + [0]  

    def count_moves(target):
        copy = nums[:]
        pos = {num: i for i, num in enumerate(copy)}  
        moves = 0
        for i in range(n):
            while copy[i] != target[i]:
                empty = pos[0]
                index = pos[target[i]]
                copy[empty], copy[index] = (
                    copy[index], copy[empty])
                pos[copy[empty]] = empty
                pos[copy[index]] = index
                moves += 1
        return moves

    return min(count_moves(target1), count_moves(target2))

nums = [2, 0, 1, 3]
print(min_operations_to_sort(nums)) 
