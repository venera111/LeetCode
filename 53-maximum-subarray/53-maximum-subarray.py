class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # Sliding Window
        max_sum = nums[0]
        tmp_sum = 0
        for i in range(len(nums)):
            if tmp_sum < 0:
                tmp_sum = 0
            tmp_sum += nums[i]
            max_sum = max(tmp_sum, max_sum)
        return max_sum