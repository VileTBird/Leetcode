class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashmap = defaultdict(int)

        for i in range(len(nums)):
            hashmap[nums[i]] += 1 

            if hashmap[nums[i]] == 2:
                return True

        return False