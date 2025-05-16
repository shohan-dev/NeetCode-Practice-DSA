class Solution:
    def containsDuplicate(self, a: List[int]) -> bool:
        seen = set()
        for i in a:
            if i in seen:
                return True
            seen.add(i)
        return False
        