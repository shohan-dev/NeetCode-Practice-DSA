from typing import List

class Solution:
    def reverseString(self, a: List[str]) -> None:
        n = len(a)
        for i in range(n//2):
            a[i],a[n-1-i] = a[n-1-i],a[i]
