class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if m+n == m:
            return None
        if m+n == 0:
            return None
        
        mpointer, npointer = m-1, n-1
        pos = m+n-1
        
        while mpointer >= 0 and npointer >= 0:
            if nums1[mpointer] > nums2[npointer]:
                nums1[pos] = nums1[mpointer]
                pos -= 1
                mpointer -= 1
            else:
                nums1[pos] = nums2[npointer]
                pos -= 1
                npointer -= 1
        
        while npointer >= 0:
            nums1[pos] = nums2[npointer]
            pos -= 1
            npointer -= 1
        
        while mpointer >= 0:
            nums1[pos] = nums1[mpointer]
            pos -= 1
            mpointer -= 1