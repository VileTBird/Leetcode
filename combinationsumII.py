'''
basically the problem is the same as the previous combination sum. that is they need us to find combinations of numbers that add 
up to a target from a list of combinations, the only difference being we can't reuse each element unlimited times. by itself its not that complicated
u just switch up the backtracking rules, to not facilitate reuse & essentially generate subsets, with an element and without it then i+1. the problem 
here are duplicates which i failed to notice, my crude way to decieve the test cases was to sort something like the final subset to be added
and checking if its in an array. its a very costly operation due to the number of sorts and not in could be considered o(n) a hashmap would be better like i siad
its very crude, the common solution seems to be skipping duplicates after the first recursive call with a while loop. theoretically 
it could work yes after u sort the candidates array because duplicates would be right next to each other. very cool! i still prefer hashmap or well hashset approach
but it could be costly'''
# my initial cruder solution 
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:

        res = []

        subset = []

        def combsum(i, comb):
            if comb == target:
                copy = sorted(subset.copy())
                if copy not in res:
                    res.append(copy)
                return
            
            if len(candidates) == i or comb > target:
                return

            subset.append(candidates[i])

            combsum(i + 1, comb + candidates[i])

            subset.pop()

            combsum(i + 1, comb)

        combsum(0, 0)
        return res

# optimal
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []

        subset = []

        def combsum(i, comb):
            if comb == target:
                res.append(subset.copy())
                return
            
            if len(candidates) == i or comb > target:
                return

            subset.append(candidates[i])

            combsum(i + 1, comb + candidates[i])

            subset.pop()

            while i + 1 < len(candidates) and candidates[i] == candidates[i+1]:
                i = i + 1

            combsum(i + 1, comb)

        combsum(0, 0)
        return res

