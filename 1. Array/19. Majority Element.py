from collections import Counter
class Solution:
    def majorityElement(self, a: List[int]) -> int:
        count = Counter(a) # return a dict
        max_num = max(count, key=count.get)
        return max_num


# Another
        # count = {}

        # for i in a:
        #     if i in count:
        #         count[i] +=1
        #     else:
        #         count[i] = 1

        # return max(count,key=count.get)