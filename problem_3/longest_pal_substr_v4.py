# Given a string s, return the longest palindromic substring in s.

# https://leetcode.com/problems/longest-palindromic-substring/

class Solution:
    def longestPalindrome(self, s):
        longest_palindrome = s[0]
        middle = len(s) // 2

        for i in range(middle):
            left = middle + i
            right = middle + i
            window = s[left:right + 1]
            while s[left] == s[right] and (left >=0 or right < len(s)):
                if len(window) > len(longest_palindrome):
                    longest_palindrome = window
                if len(longest_palindrome) == len(s):
                    return longest_palindrome
                if left > 0 and right < len(s) - 1:
                    left -= 1
                    right += 1
                else:
                    break
                window = s[left:right + 1]

            left = middle - i
            right = middle - i
            window = s[left:right + 1]
            while s[left] == s[right] and (left >=0 or right < len(s)):
                if len(window) > len(longest_palindrome):
                    longest_palindrome = window
                if len(longest_palindrome) == len(s):
                    return longest_palindrome
                if left > 0 and right < len(s) - 1:
                    left -= 1
                    right += 1
                else:
                    break
                window = s[left:right + 1]

            left = middle + i
            right = middle + i + 1
            if right == len(s):
                right -= 1
            window = s[left:right + 1]
            while s[left] == s[right] and (left >=0 or right < len(s)):
                if len(window) > len(longest_palindrome):
                    longest_palindrome = window
                if len(longest_palindrome) == len(s):
                    return longest_palindrome
                if left > 0 and right < len(s) - 1:
                    left -= 1
                    right += 1
                else:
                    break
                window = s[left:right + 1]

            left = middle - i - 1
            right = middle - i
            window = s[left:right + 1]
            while s[left] == s[right] and (left >=0 or right < len(s)):
                if len(window) > len(longest_palindrome):
                    longest_palindrome = window
                if len(longest_palindrome) == len(s):
                    return longest_palindrome
                if left > 0 and right < len(s) - 1:
                    left -= 1
                    right += 1
                else:
                    break
                window = s[left:right + 1]

            if len(window) == len(s):
                return longest_palindrome


        return longest_palindrome


print('Testing "tracecars"')
print('Expected: racecar')
print('Answer:', str(Solution().longestPalindrome("tracecars")))
print()

print('Testing "aacabdkacaa"')
print('Expected: aca')
print('Answer:', str(Solution().longestPalindrome('aacabdkacaa')))
print()

print('Testing "a"')
print('Expected: a')
print('Answer:', str(Solution().longestPalindrome('a')))
print()

'''print('Testing "ac"')
print('Expected: a ou c')
print('Answer:', str(Solution().longestPalindrome('ac')))
print()'''

print('Testing "aac"')
print('Expected: aac')
print('Answer:', str(Solution().longestPalindrome('aac')))
print()

print('Testing "babad"')
print('Expected: bab ou aba')
print('Answer:', str(Solution().longestPalindrome('babad')))
print()

print('Testing "cbbd"')
print('Expected: bb')
print('Answer:', str(Solution().longestPalindrome('cbbd')))
print()

print('Testing "eabcb"')
print('Expected: bcb')
print('Answer:', (Solution().longestPalindrome('eabcb')))
print()

print('Testing "abbcccbbbcaaccbababcbcabca"')
print('Expected: bbcccbb ou cbababc')
print('Answer:', str(Solution().longestPalindrome('abbcccbbbcaaccbababcbcabca')))
print()

print('Testing "abb"')
print('Expected: bb')
print('Answer:', str(Solution().longestPalindrome('abb')))
print()

print('Testing "aaabaaaa"')
print('Expected: aaabaaa')
print('Answer:', str(Solution().longestPalindrome("aaabaaaa")))
print()

print('Testing "aaaaaaaaaaaaaaaaaaaa"')
print('Expected: aaaaaaaaaaaaaaaaaaaa')
print('Answer:', str(Solution().longestPalindrome('aaaaaaaaaaaaaaaaaaaa')))
print()

print('Testing "0123456789876543210"')
print('Expected: 0123456789876543210')
print('Answer:', str(Solution().longestPalindrome('0123456789876543210')))
print()