class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        count = 1
        for i in range(count, len(nums)):
            if nums[i] != nums[i-1]: #сравнение текущего и предыдущего
                nums[count] = nums[i] #копирование уникального элемента
                count += 1 #число уникальных элементов
        return count