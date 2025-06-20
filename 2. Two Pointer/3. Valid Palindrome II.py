class Solution:
    def validPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1
        while l < r:
            if s[l] != s[r]:
                skip_l = s[l+1:r+1]  # remove left
                skip_r = s[l:r]      # remove right
                return skip_l == skip_l[::-1] or skip_r == skip_r[::-1]
            l += 1
            r -= 1
        return True