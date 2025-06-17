class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        n = len(nums)
        s = set(nums)
        not_found = []
        for i in range(1,n+1):
            if i in s:
                continue
            not_found.append(i)
        return not_found
        