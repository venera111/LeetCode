import collections
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        c = collections.Counter(nums)
        for x in c:
            if target-x in c:
                if x == target-x:
                    if c.get(target-x) == 2:
                        return [i for i, val in enumerate(nums) if val==target-x]
                    continue
                ind1 = nums.index(x)
                ind2 =  nums.index(target-x, ind1)
                return [ind1, ind2]