'''
The devil is in the details in a way. the question wants us to find the sqrt and if the answer is not a non-decimal integer 
then the result should be rounded down. it can be easy to get lost in details, we dont have to search for the number when squared
has the closest result to our target x. (that was my initial approach and was a miserable 20 mins)

the trick here to do binary search but when we find median we basically try to find a number where the number that follows that
has a square thats greater than x.

for example if we're trying to find the square root of 8 rounded down, the answer is around 2.82222

if we round down its 2.

in other words 1x1 = 1, 2x2 = 4, 3x3 = 9. so clearly anything past 3 is inconsequential to our result, the nearest smaller integer
is 2. so the result is 2. 

so we modify our binary search so that if our median or the middle most value when squared is greater than our target variable x
we just shift the right pointer past it ignoring it.

on the other hand if our median is lesser than x we basically store it in our res variable, by design this binary search
will run the entire loop all the way until it finds the biggest number that has a square smaller than x. 
so when the loop ends our left pointer will be at the last number that has a square lesser than x

the only extra case is when our median's square is equal to that of you know our target x, in that case which is the else conditional
we just return true
'''

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