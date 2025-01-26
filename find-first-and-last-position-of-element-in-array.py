'''
Not the most optimized solution, this was my initial submission but then after submission I realized that worst case it could potentially be o(nlogn) i can reduce this back to logn with another binary search but i will do that after appropriate sleep.
'''

class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        l, r = 0, len(nums) - 1

        while l<=r:
            m = (l+r)//2

            if(nums[m] < target):
                l = m + 1
            elif(nums[m] > target):
                r = m - 1
            else:
                start = m
                end = m
                if len(nums) > 1:
                    while nums[start] == target:
                        if(start-1) < 0:
                            break
                        start -= 1

                    while nums[end] == target:
                        if(end + 1) > len(nums) - 1:
                            break
                        end += 1

                    if nums[start] != target:
                        start += 1
                    
                    if nums[end] != target:
                        end -= 1

                    return [start, end]
                return [0, 0]

        return [-1, -1] 