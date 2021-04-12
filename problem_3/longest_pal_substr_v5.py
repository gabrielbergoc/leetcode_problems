# Given a string s, return the longest palindromic substring in s.

# https://leetcode.com/problems/longest-palindromic-substring/

class Solution:
    def longestPalindrome(self, s):
        all_subs = self.all_subs(s)
        rev_subs = self.reverse(all_subs)
        all_pals = []
        for i in range(len(all_subs)):
            if all_subs[i] == rev_subs[i]:
                all_pals.append(all_subs[i])

        maior_pal = all_pals[0]
        for item in all_pals:
            if len(maior_pal) < len(item):
                maior_pal = item

        return maior_pal

    def all_subs(self, string):
        all_subs = []
        for i in range(len(string)):
            for j in range(i, len(string)):
                all_subs.append(string[i:j+1])
        return all_subs

    def reverse(self, string_list):
        reversed_list = []
        for string in string_list:
            reversed_list.append(string[::-1])
        return reversed_list


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