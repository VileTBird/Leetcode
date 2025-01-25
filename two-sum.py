from collections import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_map = {}
        for i in range(len(nums)):
            num_map[nums[i]] = i
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in num_map and i!=num_map[complement]:
                return list([i, num_map[complement]])



        