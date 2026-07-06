# Question number: 12
# Level: medium
# Author: Naama Tzadok
# Date: Jul 06, 2026 11:23



class Solution:
    def intToRoman(self, num: int) -> str:
        res = []
        romans_letters = ['M','CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']
        romans_values = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        for i in range(len(romans_letters)):
            while num > 0 and num >= romans_values[i]:
                res.append(romans_letters[i])
                num -= romans_values[i]
        return "".join(res)    

# Time Complexity: O(1) (input <= 3999)
# Space Complexity: O(1) (input <= 3999)

