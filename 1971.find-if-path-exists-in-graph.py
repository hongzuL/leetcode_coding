#
# @lc app=leetcode id=1971 lang=python3
#
# [1971] Find if Path Exists in Graph
#

# @lc code=start
from re import T


class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        paths = [0] * n
        paths[source] = 1
        node_dict = dict()
        for i in range(n):
            node_dict[i] = set()
        for edge in edges:
            if paths[edge[0]] == 1:
                paths[edge[1]] == 1
            if paths[edge[1]] == 1:
                paths[edge[0]] == 1
            node_dict[edge[0]].add(edge[1])
            node_dict[edge[1]].add(edge[0])
        run_time = 0
        while paths[destination] == 0:
            run_time += 1
            changed = False
            for node in range(len(paths)):
                if paths[node] == 1:
                    for child in node_dict[node]:
                        paths[child] = 1
                        changed = True
            if not changed:
                break
            if run_time > n:
                break
        return paths[destination] == 1

# @lc code=end

