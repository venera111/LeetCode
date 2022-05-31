class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        strings = {}
        for i, s in enumerate(arr):
            if s not in strings:
                strings[s] = 1
            else:
                strings[s] += 1
        for key in strings:
            if k > 1:
                if strings[key] == 1:
                    k -= 1
            else:
                if strings[key] == 1:
                    return key
        return ""