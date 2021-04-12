# Given a string s, return the longest palindromic substring in s.

# https://leetcode.com/problems/longest-palindromic-substring/

class Solution:
    def longestPalindrome(self, s):
        palindromes = set([])
        for i in range(len(s)):
            for j in range(len(s)-1, 0, -1):
                m = i
                n = j
                if m == n:
                    break
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
                    palindromes.add(s[m - count: n + count + 1])
            if len(palindromes) == len(s)-1:
                break

        if len(palindromes) > 0:
            longest_palindrome = palindromes.pop()
            while len(palindromes) > 0:
                comparacao = palindromes.pop()

                if len(comparacao) > len(longest_palindrome):
                    longest_palindrome = comparacao

            return longest_palindrome

        return s[0]

