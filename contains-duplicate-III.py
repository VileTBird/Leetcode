'''
I wouldn't say this si the most optimal solution, technicalyl it works but the time complexity could be much better. i still 
don't understand the efficient solution for this problem, so ima just leave my inefficient solution here and come back to it later.
'''

class Solution(object):
    def containsNearbyAlmostDuplicate(self, nums, indexDiff, valueDiff):
        """
        :type nums: List[int]
        :type indexDiff: int
        :type valueDiff: int
        :rtype: bool
        """
        
        hashmap = defaultdict(int)
        l = 0

        for r in range(len(nums)):
            if abs(l - r) > indexDiff:
                l += 1
                hashmap[nums[l]] -= 1

            hashmap[nums[r]] += 1

            while i < j:
                if abs(nums[i] - nums[j]) <= valueDiff and i!=j:
                    return True
                
                i += 1
    
        return False