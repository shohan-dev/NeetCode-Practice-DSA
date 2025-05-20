class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        return len(set(s))==len(set(t))==len(set(zip(s,t)))  # check same or diff






# Another
        # s_map, t_map = {},{}

        # for i,j in zip(s,t):
        #     if (i in s_map and s_map[i] != j) or (j in t_map and t_map[j] != i):
        #         return False
        #     s_map[i] = j
        #     t_map[j] = i
        # return True
        