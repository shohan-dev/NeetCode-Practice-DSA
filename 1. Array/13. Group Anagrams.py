from collections import defaultdict
class Solution:
    def groupAnagrams(self, a: List[str]) -> List[List[str]]:
        res = defaultdict(list)

        for i in a:
            key = "".join(sorted(i))
            res[key].append(i)

        return list(res.values())