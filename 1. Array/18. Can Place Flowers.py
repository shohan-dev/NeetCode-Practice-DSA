class Solution:
    def canPlaceFlowers(self, a: List[int], n: int) -> bool:
        if n == 0:
            return True
        a = [0] + a + [0]

        for i in range(1,len(a)-1):
            if a[i] == 0:
                if a[i-1] ==0 and a[i+1] ==0:
                    a[i] = 1
                    n -=1
                    if n==0:
                        return True
                    

        return False