class Solution:
    def pivotIndex(self, a: List[int]) -> int:
        total = sum(a)
        left_sum = 0

        for i in range(len(a)):
            if left_sum == total - left_sum - a[i]:
                return i
            left_sum += a[i]
        return -1