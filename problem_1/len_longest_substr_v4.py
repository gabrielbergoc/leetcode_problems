# Given a string s, find the length of the longest substring without repeating characters.
# https://leetcode.com/problems/longest-substring-without-repeating-characters/

# Runtime: 84 ms
# Memory Usage: 14.3 MB

class Solution:
    def lengthOfLongestSubstring(self, s):
        s_lenght = len(s)
        window = []
        longest = len(window)

        j = 0

        for i in range(s_lenght):
            if s[j] in window:
                window = window[window.index(s[j]) + 1:]

            window.append(s[j])
            longest = max(longest, len(window))
            if j < s_lenght - 1:
                j += 1

        return longest

print(Solution().lengthOfLongestSubstring('abrkaabcdefghijjxxx'))
# 10