#Solver with pure try error. By checking all the permutations of the needed number. 
#Full algorithm please see README.md file

import boardTools as tool

def solve(matrix: list[list[int]])-> list[list[int]]:
    emptyLocs = tool.getEmptyLoc(matrix)
    needs = tool.getNeeds(matrix)
    size = len(emptyLocs)
    perms = tool.getPerm(needs)
    for perm in perms:
        for i in range(size):
            x,y = emptyLocs[i]
            matrix[x][y] = perm[i]
        if tool.isValidSudoku(matrix): return matrix
