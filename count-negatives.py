'''
Very easy problem. pretty cool too, my initial solution was to basically perform binary search, find the median, and if median is greater than 0
we shift left pointer past median, if not we basically loop from left until we find median, this is fine but
itll be a o(n logn) technically cus ur looping each time u find a negative number in the median. 

the better solutioon here is this, we basically perform binary search to find the first negative number, if our median is negative
we shift right pointer past it, if its the inverse then we shift left pointer past it.
this will basically happen until all 3 pointers, left, right, and median land on the final negative numbe

when that happens we basically shift right pointer to the left, going past our bounds breaking the loop leaving left pointer on the
first negative element

with that we minus from the length of the sub-array to find the count of negative numbers 

we add it to our counter and easy peasy,
'''

class Solution(object):
    def countNegatives(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        count = 0
        for i in range(len(grid)):
            l, r = 0, len(grid[i]) - 1

            while l <= r:
                m = (l + r) // 2

                if grid[i][m] < 0:
                    r = m - 1
                else:
                    l = m + 1
                
            count += len(grid[i]) - l

        return count 

        