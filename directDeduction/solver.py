#Solving a sudoku with only with direct deduction and elimination
from boardTools import *

def solve(matrix: Matrix, showStatus = True)-> Matrix:
    emptyLocs = getLocState(matrix)
    matrix_size = len(matrix)
    prev = len(emptyLocs)
    if showStatus: print(f'Empty location length in the beginning: {prev}')
    while emptyLocs:
        boxes = makeBoxes(matrix)
        possibleVals = {pos : getPossibleValue(pos, matrix, boxes) for pos in emptyLocs}
        item = possibleVals.items()
        for a, b in item:
            if len(b) == 1:
                matrix[a[0]][a[1]] = b[0]
        emptyLocs = getLocState(matrix)
        if len(emptyLocs) == prev:
            print("This sudoku arrangement in unsolveable by direct deduction, this is the furthest i can do")
            return matrix
        prev = len(emptyLocs)
        if showStatus: print(f'Empty location length now: {prev}')
    return matrix
