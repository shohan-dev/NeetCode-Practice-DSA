class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        seen = set()
        duplicate = 0
        missing = 0
        count =0
        for i in grid:
            for j in i:
                count +=1
                if j in seen:
                    duplicate = j
                seen.add(j)

        for i in range(1,count+1):
            if i in seen:
                continue
            missing =i
            break

        return [duplicate,missing]