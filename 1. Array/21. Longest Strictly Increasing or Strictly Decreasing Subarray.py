class Solution:
    def longestMonotonicSubarray(self, a: List[int]) -> int:
        inc = 1
        dec = 1
        length =1

        for i in range(1,len(a)):
            if a[i] >a[i-1]:
                inc +=1
                dec =1
            elif a[i] <a[i-1]:
                inc = 1
                dec +=1
            else:
                inc = dec = 1
            
            length = max(inc,dec,length)

        return length
        