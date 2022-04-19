class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        arr = []
        arr.append(x % 10)
        x = x // 10
        while x != 0:
            arr.append(x % 10)
            x = x // 10
        n = len(arr)
        mid = n // 2
        i = 0
        while i < mid:
            if arr[i] != arr[n-1-i]:
                return False
            i += 1
        return True