class Solution:
    def longestCommonPrefix(self, a: List[str]) -> str:
        same = ""
        n = len(min(a, key=len))
        a.sort()

        for i in range(n):
            if a[0][i] == a[len(a) - 1][i]: # first and last word check charecter 
                same += a[0][i] 
            else:
                break

        return same

# # Another one
# prefix = a[0]

#         for i in a[1:]:
#             while not i.startswith(prefix):
#                 prefix = prefix[:-1]
#                 if not prefix:
#                     return ""

#         return prefix
