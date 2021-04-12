# There are n people that are split into some unknown number of groups. Each person is labeled with a unique ID from 0 to n - 1.
#
# You are given an integer array groupSizes, where groupSizes[i] is the size of the group that person i is in. For example, if groupSizes[1] = 3, then person 1 must be in a group of size 3.
#
# Return a list of groups such that each person i is in a group of size groupSizes[i].
#
# Each person should appear in exactly one group, and every person must be in a group. If there are multiple answers, return any of them. It is guaranteed that there will be at least one valid solution for the given input.

# https://leetcode.com/problems/group-the-people-given-the-group-size-they-belong-to/

class Solution:
    def groupThePeople(self, groupSizes: list) -> list:
        groups = []

        for i in range(len(groupSizes)):
            in_group = False
            j = 0
            while j < len(groups) and not in_group:
                if groupSizes[i] == groups[j][0]:
                    in_group = True
                j += 1
            if in_group:
                groups[j - 1].append(i)
            else:
                groups.append([groupSizes[i], i])

        resp = []
        for i in range(len(groups)):
            while len(groups[i]) > 1:
                j = 1
                group = []
                while j <= groups[i][0]:
                    group.append(groups[i].pop(1))
                    j += 1
                resp.append(group)
            
        return resp

# not my solution
    def groupThePeople2(self, groupSizes):
        res = []
        d = {}
        for i, val in enumerate(groupSizes):
            if val not in d or d.get(val)[0] == 0:
                d[val] = [val - 1, len(res)]
                res.append([i])
            else:
                d[val][0] -= 1
                res[d[val][1]].append(i)
        return res

print()
print('Testando: [3,3,3,3,3,1,3]')
print('Esperados (apenas uma possibilidade):\n'
'[[5],[0,1,2],[3,4,6]]\n'
'[[2,1,6],[5],[0,4,3]]\n'
'[[5],[0,6,2],[4,3,1]]\n')
print('Resposta:', str(Solution().groupThePeople([3,3,3,3,3,1,3])))
print()

print('Testando: [2,1,3,3,3,2]')
print('Esperado: [[1],[0,5],[2,3,4]]')
print('Resposta:', str(Solution().groupThePeople([2,1,3,3,3,2])))