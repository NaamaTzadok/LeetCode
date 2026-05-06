# Question number: 13
# Level: easy
# Author: Naama Tzadok
# Date: Sep 28, 2025 17:18


class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        num = 0
        temp = 0
        rom_normal = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        for i in s:
            cur_val = rom_normal[i]
            if temp == 0:
                temp = cur_val
            elif temp < cur_val:
                num = cur_val - temp + num
                temp = 0
            else:
                num = num + temp
                temp = cur_val
        if temp > 0:
            num += temp
        return num
            
        

# Time Complexity: O(n)
# Space Complexity: O(1)