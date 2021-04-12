# Given a string s, find the length of the longest substring without repeating characters.
# https://leetcode.com/problems/longest-substring-without-repeating-characters/

# Runtime: 1176 ms
# Memory Usage: 364.7 MB

class Solution:
    def lengthOfLongestSubstring(self, s):
    # Fill this in.
        substring = ''
        substrings = []

        if len(s) == 0:
            return 0

        i = j = 0

        while j < len(s):
            if s[j] not in substring:
                substring += s[j]
                j += 1
            else:
                substrings.append(substring)
                substring = ''
                i += 1
                j = i
            substrings.append(substring)

        subs_sizes = indexlen(substrings)

        return max(subs_sizes)


def indexlen(lista_str):
    lista = []
    for item in lista_str:
        lista.append(len(item))

    return lista


print(Solution().lengthOfLongestSubstring('abrkaabcdefghijjxxx'))
# 10