class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        res_s = s.split()

        if len(res_s) != len(pattern):
            return False

        word_to_char = {}
        char_to_word = {}

        for i,j in zip(pattern,res_s):
            if i in word_to_char and word_to_char[i] != j:
                return False
            if j in char_to_word and char_to_word[j] != i:
                return False
            word_to_char[i] = j
            char_to_word[j] = i

        return True