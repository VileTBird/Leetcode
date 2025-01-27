class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
 
        l, r = 0, num 
        while l<= r:
            m = (l+r)//2
            square = m * m

            if square > num:
                r = m - 1
            elif square < num:
                l = m + 1
            else:
                return True
   
            
        return False
        