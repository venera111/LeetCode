class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # Sliding Window
        max_sum = float('-inf')
        curr = 0
        for num in nums:
            curr += num
            if max_sum < curr:
                max_sum = curr
            if curr < 0:
                curr = 0
        return max_sum