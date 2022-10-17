#leetcode challenge to find longest string

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ss = ''                             #Empty Sub String for saving Char
        max_len = 0                  # max length substring
        i = 0                              # Starting point
        while i < len(s):
            if s[i] not in ss:          # Add char is not in sub string
                ss += s[i]
            else:
                ss = ss[ss.index(s[i])+1:] + s[i]      # Take substring from last found index of char + 1
            i += 1
            max_len = max(max_len, len(ss))     # Max length of substring
        return max_len







        