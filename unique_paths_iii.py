'''
    https://leetcode.com/problems/unique-paths-iii/

    1 = starting location
    2 = ending location
    0 = can walk on
   -1 = can not walk on

    ex1.
    Input: [[1,0,0,0],[0,0,0,0],[0,0,2,-1]]
    output: 2

    ex2.
    Input: [[1,0,0,0],[0,0,0,0],[0,0,0,2]]
    Output: 4

    ex3.
    Input: [[0,1],[2,0]]
    Output: 0
        
'''

class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        '''
        pseudo code solution:
            1. generate all possible path permutations for the grid 
            e.g. path1 = [[0,0],[0,1],[0,2],[0,3],[0,0],[0,0]]

             2. for each path, check:
                a) that each cell is not a '-1'
                b) the number of '0's sums to the total '0's
        '''
        
        # TODO: list comp for 2d list
        # TODO: return tuple of three values
        # TODO: make Index class with row and column property
        
        start, stop, num_zeros = [], [], 0
        
        # count 0's and locate 1 & 2 location
        for i, row in enumerate(grid):
            for j, item in enumerate(row):
                if grid[i][j] == 1:
                    start[0] = i; start[1] = j # start.append(i); start.append(j)
                if grid[i][j] == 2:
                    stop[0] = i; stop[1] = j 
                if grid[i][j] == 0:
                    num_zeros += 1    

        result_list = [][] # visited = [[]]
        traverse(start, grid, result_list)
        return len(result_list)
        