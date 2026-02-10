from typing import List

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        # Pointer for last element in nums1 
        i = m - 1
        
        # Pointer for last element in nums2
        j = n - 1
        
        # Pointer for last position in nums1
        k = m + n - 1

        # Merge from the back
        while i >= 0 and j >= 0:
            if nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                i -= 1
            else:
                nums1[k] = nums2[j]
                j -= 1
            k -= 1

        # If nums2 still has elements, copy them
        while j >= 0:
            nums1[k] = nums2[j]
            j -= 1
            k -= 1

        
