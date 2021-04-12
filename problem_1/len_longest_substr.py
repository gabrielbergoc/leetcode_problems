# Given a string s, find the length of the longest substring without repeating characters.
# https://leetcode.com/problems/longest-substring-without-repeating-characters/

# WRONG SOLUTION

class Solution:
    def lengthOfLongestSubstring(self, s):
    # Fill this in.
        substring = ''
        substrings = []

        for i in range(len(s) - 1):
            j = i
            while s[j] != s[j + 1]:
                substring += s[j]
                j += 1
            substring += s[j + 1]
            substrings.append(substring)
            substring = ''

        for i in range(len(substrings)-1):
            pos_min = i
            for j in range(i + 1, len(substrings)):
                if len(substrings[j]) < len(substrings[i]):
                    pos_min = j
            substrings[i], substrings[pos_min] = substrings[pos_min], substrings[i]


        return len(substrings[-1])


print(Solution().lengthOfLongestSubstring('abrkaabcadcefgdefghijjxxx'))
# 10