class Solution:
    def replaceElements(self, a: List[int]) -> List[int]:
        max_val = -1

        for i in range(len(a)-1,-1,-1):
            current = a[i]
            a[i] = max_val
            max_val = max(current,max_val)
        return a
        