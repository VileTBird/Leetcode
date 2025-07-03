class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        subset = []
        
        def subfunc(i):
            if i == len(nums):
                res.append(subset.copy())
                return

            # its not i+1 but i, we're already getting i + 1, u gotta start with branches for both
            # 0 and 1, so u start with 0 if theres x at 0, u do both x and without x
            # next you call the function recursively with the subset being modified with x and withoutx
            # when you call it that way, you also increment i, so in the subbranch of x and withou tx
            # i+1 y will be considered it recursively generates both ends and when all subbranches
            # reach the end when len(nums) has all been looked at for all subbranches
            # we'll have exhausted all possible decisions we could make essentially storing copies
            # when we store copies we're also storing the subsets essentially solving the probelm 
            subset.append(nums[i])
            subfunc(i+1)

            subset.pop()
            subfunc(i+1)

        subfunc(0)
        return res