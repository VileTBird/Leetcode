class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        
        l, r = 0, x
        res = 0

        while l <= r:
            m = ((l + r) // 2) 
            sqm = m * m

            if (sqm > x): 
                r = m - 1
            elif sqm < x:
                res = m
                l = m + 1
            else:
                return m

        return res