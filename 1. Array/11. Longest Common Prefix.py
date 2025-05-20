class Solution:
    def longestCommonPrefix(self, a: List[str]) -> str:
        if not a:
            return ""

        a.sort()
        first = a[0]
        last = a[-1]
        i = 0
        while i < len(first) and i < len(last) and first[i] == last[i]:
            i += 1
        return first[:i]
