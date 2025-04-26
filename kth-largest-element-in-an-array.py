class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        res = []
        heapq.heapify(res)

        for num in nums:
            heapq.heappush(res, num)

        while len(res) > k:
            heapq.heappop(res)
        
        return res[0] if res else 0
        
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heapq.heapify(nums)

        while len(nums) > k:
            heapq.heappop(nums)
        
        return nums[0] if nums else 0
        
        