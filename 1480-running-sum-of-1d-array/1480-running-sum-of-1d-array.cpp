class Solution {
public:
    vector<int> runningSum(vector<int>& nums)
    {
        int length = nums.size();
        std::vector<int> runningSum(length);
        int sum_of_arr = 0;
        for (int i = 0; i < length; i++)
        {
            sum_of_arr += nums[i];
            runningSum[i] = sum_of_arr;
        }
        return runningSum;
    }
};