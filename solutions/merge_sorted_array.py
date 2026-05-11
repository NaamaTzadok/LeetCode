# Question number: 88
# Level: easy
# Author: Naama Tzadok
# Date: Sep 30, 2025 16:02


class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        arr = []
        i = 0
        j = 0
        while i < m and j < n:
            if nums1[i] <= nums2[j]:
                arr.append(nums1[i])
                i += 1
            else:
                arr.append(nums2[j])
                j += 1
        if i < m:
            while i < m:
                arr.append(nums1[i])
                i += 1
        if j < n:
            while j < n:
                arr.append(nums2[j])
                j += 1  
        for i in range(n + m):
            nums1[i] = arr[i]
        return nums1     

# Time Complexity: O(n)
# Space Complexity: O(n)