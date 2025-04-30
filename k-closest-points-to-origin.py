class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        res = []
        heapq.heapify(res)
        for point in points:
            dis = math.sqrt((point[0] * point[0]) + (point[1] * point[1]))

            heapq.heappush(res, (- dis, point))
            if len(res) > k:
                heapq.heappop(res)

        return [point for (_, point) in res]





        