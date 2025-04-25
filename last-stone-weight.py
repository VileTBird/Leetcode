class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        res = []
        heapq.heapify(res)
        for stone in stones:
            heapq.heappush(res, - (stone))

        
        while len(res) > 1:
            x = -heapq.heappop(res)
            y = -heapq.heappop(res)


            
            if x < y:
                y = y - x
                heapq.heappush(res, -y)
            elif y < x:
                x = x - y
                heapq.heappush(res, -x)

        return -res[0] if res else 0

        