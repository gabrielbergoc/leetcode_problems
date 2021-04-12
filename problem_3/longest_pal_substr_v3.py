# Given a string s, return the longest palindromic substring in s.

# https://leetcode.com/problems/longest-palindromic-substring/

# BAD solution (runtime: 29s)
class Solution:
    def longestPalindrome(self, s):
        longest_palindrome = s[0]
        for i in range(len(s)):
            for j in range(len(s)-1, i, -1):
                m = i
                n = j
                count = 0
                palindrome = True
                while m < n and palindrome:
                    if s[m] == s[n]:
                        m += 1
                        n -= 1
                        count += 1
                    else:
                        palindrome = False

                if palindrome:
                    if len(s[m - count : n + count + 1]) > len(longest_palindrome):
                        longest_palindrome = s[m - count: n + count + 1]

        return longest_palindrome

s = "tracecars"
print(str(Solution().longestPalindrome(s)))

s = "aacabdkacaa"
print(str(Solution().longestPalindrome(s)))