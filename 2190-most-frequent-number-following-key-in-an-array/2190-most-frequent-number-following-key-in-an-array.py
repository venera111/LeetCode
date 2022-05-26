class Solution:
    def mostFrequent(self, nums: List[int], key: int) -> int:
        obj = {} #словарь {элемент после key: кол-во вхождений}
        for i in range(len(nums)-1):
            if nums[i] == key:
                if nums[i+1] in obj:
                    obj[nums[i+1]] += 1
                else:
                    obj[nums[i+1]] = 1
        return max(obj, key=obj.get) #вернуть ключ с максимальным значением