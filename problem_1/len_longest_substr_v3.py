# Given a string s, find the length of the longest substring without repeating characters.
# https://leetcode.com/problems/longest-substring-without-repeating-characters/

# Runtime: 100 ms
# Memory Usage: 14.4 MB

class Solution:
    def lengthOfLongestSubstring(self, s):
        s_lenght = len(s)
        window = []
        longest = len(window)

        i = j = 0

        while i < s_lenght:
            while s[j] in window:
                window.pop(0)
                i += 1
            window.append(s[j])
            longest = max(longest, len(window))
            if j < s_lenght - 1:
                j += 1

        return longest

print(Solution().lengthOfLongestSubstring('abrkaabcdefghijjxxx'))
# 10