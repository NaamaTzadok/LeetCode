# Question number: 434
# Level: easy
# Author: Naama Tzadok
# Date: Jun 18, 2026 07:11

class Solution:
    def countSegments(self, s: str) -> int:
        # return len(s.split()) # Its a nice solution but takes O(n) space
        segments_counter = 0
        there_is_word = False
        for i in range(len(s)):
            if s[i] == " ":
                if there_is_word:
                    segments_counter += 1
                    there_is_word = False
            else:
                there_is_word = True
        if there_is_word:
            segments_counter += 1
        return segments_counter      

# Time Complexity: O(n)
# Space Complexity: O(1)
