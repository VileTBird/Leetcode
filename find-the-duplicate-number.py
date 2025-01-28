class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        fast, slow = nums[0], nums[0]

        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if(fast == slow):
                break

        slow = nums[0]
        while True:
            if slow == fast:
                return fast

            slow = nums[slow]
            fast = nums[fast]
            