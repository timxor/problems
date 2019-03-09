'''
author: timothy c. siwula
date: sat mar 9 2019
file: dfs.py
description: path discovery using dfs
notes:
    - ds & algo in python pg 644
'''

'''
u = starting vertex
g = graph
d = 




1. for every outgoing edge from u
2. v is an univsited vertex
3. e is the tree edge that discovered v
4. recurse



constructing path from u to v
1. build list from v to u and then reverse it

'''



class Dfs:
    def dfs(g, u, d):
        #for e in g.incident_edges(u):
        #dfs
        for i, row in enumerate(grid):
            for j, item in enumerate(row):
                visited[i][j] = True
                if grid[i][j] == 0:
                    num_zeros += 1



def count_all_zeros(self, grid: List[List[int]]) -> int:
        num_zeros = 0
        for i, row in enumerate(grid):
            for j, item in enumerate(row):
                if grid[i][j] == 0:
                    num_zeros += 1
        
        print("found " + num_zeros + " 0's in grid")
        return num_zeros