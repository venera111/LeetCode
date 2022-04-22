class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        temp1 = nums1[:m]
        nums1.clear()
        temp2 = nums2[:n]
        temp1.extend(temp2)
        temp1.sort()
        nums1.extend(temp1)