class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        count = Counter(arr)
        res = [key for key, value in count.items() if value == 1]
        if len(res) >= k:
            return res[k-1]
        else:
            return ""
        