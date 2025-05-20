import math
from typing import List

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        final = []
        for j in range(1, numRows + 1):
            res = []
            for i in range(1, j + 1):
                res.append(math.comb(j - 1, i - 1))
            final.append(res)
        return final