class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        sub = []
        comb = 0
        def combsum(i):
            nonlocal comb

            if sum(sub) == target:
                res.append(sub.copy())
                return
            if i == len(nums) or comb > target:
                return

            sub.append(nums[i])
            comb += nums[i]
            combsum(i)

            comb -= nums[i]
            sub.pop()
            combsum(i+1)

        
        combsum(0)
        return res
