class Solution:
    def twoSum(self, a: List[int], target: int) -> List[int]:
        seen = {}
        for i in range(len(a)):
            c = target - a[i]
            if c in seen:
                return [seen[c],i]
            seen[a[i]] = i
        
            
        