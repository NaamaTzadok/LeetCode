# Question number: 151
# Level: medium
# Author: Naama Tzadok
# Date: Oct 30, 2025 11:43

#################
# Naive Solution:
###################

class Solution:
    def reverseWords(self, s: str) -> str:
        res = ""
        word = ""
        for n in s:
            if n == " ":
                if word == "":
                    continue
                if res == "":
                    res = word + res
                else:
                    res = word + " " + res
                word = ""
                continue
            word += n
        if not word == "":
            if res == "":
                res = word + res
            else:
                res = word + " " + res
        return res
    
# Time Complexity: O(n^2)
# Space Complexity: O(n)

###################
# smarter Solution:
#####################  

class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split()
        return " ".join(words[::-1])

# Time Complexity: O(n)
# Space Complexity: O(n)