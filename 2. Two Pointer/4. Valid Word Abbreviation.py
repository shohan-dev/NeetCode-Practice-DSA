# Premimum: https://leetcode.com/problems/valid-word-abbreviation/
# Neetcode: https://neetcode.io/problems/valid-word-abbreviation?list=allNC
# Difficulty: Easy
class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        i, j = 0, 0
        word_len = len(word)
        abbr_len = len(abbr)

        while j < abbr_len:
            if abbr[j].isdigit():
                if abbr[j] == "0":
                    return False  # ❌ Leading zeros are invalid
                num = ""
                while j < abbr_len and abbr[j].isdigit():
                    num += abbr[j]
                    j += 1
                i += int(num)
            else:
                # ✅ Fix: Check bounds before comparing characters
                if i >= word_len or word[i] != abbr[j]:
                    return False
                i += 1
                j += 1

        return i == word_len  # ✅ must consume full word
