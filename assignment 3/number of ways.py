from functools import lru_cache
from typing import List

def numberWays(hats: List[List[int]]) -> int:
    MOD = 10**9 + 7
    n = len(hats)
    people = [set(h) for h in hats]
    hats_people = [set() for _ in range(41)]
    for i, h in enumerate(hats):
        for hat in h:
            hats_people[hat].add(i)
    def dp(assigned, mask):
        if assigned == n:
            return 1
        if mask == 0:
            return 0
        res = 0
        for i in range(1, 41):
            if mask & (1 << i) and not people[assigned] & hats_people[i]:
                res = (res + dp(assigned + 1, mask ^ (1 << i))) % MOD
        return res
    
    return dp(0, (1 << n) - 1)
if __name__ == "__main__":
    hats = [[3, 4], [4, 5], [5]]
    print(numberWays(hats))