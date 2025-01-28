# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        l, r = 1, n
        res = n
        while l<=r:
            m = (l + r)//2

            if isBadVersion(m):
                res = m
                r = m - 1
            else: 
                l = m + 1

        return res
            
                