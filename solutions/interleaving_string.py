# Question number: 97
# Level: medium
# Author: Naama Tzadok
# Date: Jul 14, 2026 22:54 

#################
# Naive Solution:
###################
 
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        def f(ptr1, ptr2, ptr3):
            if ptr3 >= len(s3):
                return ptr1 == len(s1) and ptr2 == len(s2)
            x = s1[ptr1] if ptr1 < len(s1) else None
            y = s2[ptr2] if ptr2 < len(s2) else None
            if s3[ptr3] == x and s3[ptr3] == y:
                return f(ptr1 + 1, ptr2, ptr3 + 1) or f(ptr1, ptr2 + 1, ptr3 + 1)
            if s3[ptr3] == x:
                return f(ptr1 + 1, ptr2, ptr3 + 1)
            if s3[ptr3] == y:
                return f(ptr1, ptr2 + 1, ptr3 + 1)
            return False
        return f(0,0,0)
    
# Time Complexity: O(2^(n+m))
# Space Complexity: O(n+m)

###################
# smarter Solution:
#####################  

class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False

        matrix = [[False] * (len(s2) + 1) for _ in range(len(s1)+1)]
        matrix[0][0] = True
        
        for i in range(1, len(s1) + 1):
            matrix[i][0] = matrix[i-1][0] and s1[i-1] == s3[i-1]

        for j in range(1, len(s2) + 1):
            matrix[0][j] = matrix[0][j-1] and s2[j-1] == s3[j-1]
        
        for i in range(1, len(matrix)):
            for j in range(1, len(matrix[0])):
                from_up = matrix[i-1][j] and s3[i+j - 1] == s1[i - 1]
                from_left = matrix[i][j-1] and s3[i+j - 1] == s2[j - 1]
                matrix[i][j] = from_up or from_left
        
        return len(matrix) == 0 or matrix[len(s1)][len(s2)]
                
# Time Complexity: O(n*m)
# Space Complexity: O(n*m)
