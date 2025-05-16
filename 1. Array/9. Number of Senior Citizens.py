class Solution:
    def countSeniors(self, a: List[str]) -> int:
        count =0
        for i in a:
            if 60< int(i[11:13]):
                count +=1

        return count