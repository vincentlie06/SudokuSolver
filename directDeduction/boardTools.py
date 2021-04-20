#Solver by pure direct deduction and elimination.
#Full algorithm please see README.md file.
Locs, Matrix = tuple[int, int], list[list[int]]
def getEmptyLocs(matrix: Matrix)-> list[Locs]:
    size = len(matrix)
    locs = list()
    for x in range(size):
        for y in range(size):
            if matrix[x][y] == 0:
                locs.append((x,y))
    return locs

def makeBoxes(matrix : Matrix)-> list[Matrix]:
    size = len(matrix)
    sqrt_size = int(pow(size, 0.5))
    pre_boxes = [matrix[i:i+sqrt_size] for i in range(0,size,sqrt_size)]
    boxes = []
    for i in pre_boxes:
        for x in zip(*i):
            boxes.extend(list(x))
    preformat_boxes = [boxes[i:i+size] for i in range(0, len(boxes), size)]
    final_boxes = [preformat_boxes[i:i+sqrt_size] for i in range(0, size, sqrt_size)]
    return final_boxes

def getCrossValue(pos : Locs, matrix: Matrix)-> list:
    row = matrix[pos[0]]
    col = [a[pos[1]] for a in matrix]
    cross = set(row+col)
    return list(cross)

def getBoxValue(pos : Locs, matrix : Matrix, boxes : Matrix)-> list:
    size = int(pow(len(matrix),0.5))
    x = pos[0]//size
    y = pos[1]//size
    s = list(range(1,len(matrix)+1))
    relatedBox = boxes[x][y]
    return relatedBox

def getPossibleValue(pos : Locs, matrix : Matrix, boxes : Matrix)-> list:
    box = getBoxValue(pos, matrix, boxes)
    cross = getCrossValue(pos, matrix)
    values = set(box + cross)
    num_range = list(range(1, len(matrix)+1))
    return [num for num in num_range if num not in values]

