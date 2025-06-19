class Solution:
    def check(self, nums: List[int]) -> bool:
        sort = sorted(nums)
        for i in range(len(nums)):
            roated = nums[i:] + nums[:i]
            if roated == sort:
                return True
                
        return False