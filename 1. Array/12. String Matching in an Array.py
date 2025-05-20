class Solution:
    def stringMatching(self, a: List[str]) -> List[str]:
            a.sort(key=len)
            res = []
            for i in range(len(a)):
                for j in range(i+1,len(a)):
                    if a[i] in a[j]:
                        res.append(a[i])
                        break

            return res
