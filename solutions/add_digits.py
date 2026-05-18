# Question number: 258
# Level: easy
# Author: Naama Tzadok
# Date: May 18, 2026 08:49

#################
# Naive Solution:
###################
 
class Solution:
    def addDigits(self, num: int) -> int:
        while num // 10 != 0:
            copy_num = num
            num = 0
            while copy_num > 0:
                num += copy_num % 10
                copy_num = copy_num // 10
        return num
    
# Time Complexity: O(log n)
# Space Complexity: O(1)

###################
# smarter Solution:
#####################  

class Solution:
    def addDigits(self, num: int) -> int:
        if num == 0:
            return 0
        elif num % 9 == 0:
            return 9
        return num % 9

# Time Complexity: O(1)
# Space Complexity: O(1)