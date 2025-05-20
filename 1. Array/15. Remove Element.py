from typing import List

class Solution:
    def removeElement(self, a: List[int], val: int) -> int:
        k = 0 
        for i in range(len(a)):
            if a[i] != val:
                a[k] = a[i]
                k += 1
        return k
