class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l1, r1 = 0, len(matrix) - 1

        while l1<=r1:
            m1 = int((l1+r1)/2)

            if(matrix[m1][0] > target):
                r1 = m1 - 1
            elif(matrix[m1][len(matrix[m1]) - 1] < target):
                l1 = m1 + 1
            else:
                l2, r2 = 0, len(matrix[m1]) - 1
                while l2<=r2:
                    m2 = int((l2+r2)/2)
                    if(matrix[m1][m2] < target):
                        l2 = m2 + 1
                    elif(matrix[m1][m2] > target):
                        r2 = m2 - 1
                    else:
                        return True
        
                return False
        return False
        

