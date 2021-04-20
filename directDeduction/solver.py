#Solving a sudoku with only with direct deduction and elimination
#Full algorithm please see README.md file.
import boardTools as tool

def solve(matrix: tool.Matrix, showStatus = True)-> tool.Matrix:
    emptyLocs = tool.getEmptyLocs(matrix)
    matrix_size = len(matrix)
    prev = len(emptyLocs)
    if showStatus: print(f'Empty location length in the beginning: {prev}')
    while emptyLocs:
        boxes = tool.makeBoxes(matrix)
        possibleVals = {pos : tool.getPossibleValue(pos, matrix, boxes) for pos in emptyLocs}
        item = possibleVals.items()
        for a, b in item:
            if len(b) == 1:
                matrix[a[0]][a[1]] = b[0]
        emptyLocs = tool.getEmptyLocs(matrix)
        if len(emptyLocs) == prev:
            if showStatus: 
                print("This sudoku arrangement in unsolveable by direct deduction, this is the furthest i can do")
            return matrix
        prev = len(emptyLocs)
        if showStatus: print(f'Empty location length now: {prev}')
    return matrix
