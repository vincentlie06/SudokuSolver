#Solver with pure try error. By checking all the permutations of the needed number. 
#Full algorithm please see README.md file

from itertools import permutations
def inRange(obj):
    return sorted(obj) == list(range(1, len(obj)+1))

def isValidSudoku(matrix : list[list[int]])-> bool:
    #Simple length test, first filter
    size = len(matrix)
    if any(len(i) != size for i in matrix): return False
    #Check rows
    if any(not inRange(obj) for obj in matrix) : return False
    #Check column
    for i in range(size):
        temp = [a[i] for a in matrix]
        if not inRange(temp): return False, 2
    #Check all boxes
    sqrt_size = int(pow(size, 0.5))
    pre_boxes = [matrix[i:i+sqrt_size] for i in range(0,size,sqrt_size)]
    boxes = []
    for i in pre_boxes:
        for x in zip(*i):
            boxes.extend(list(x))
    final_boxes = [boxes[i:i+size] for i in range(0, len(boxes), size)]
    if any(not inRange(obj) for obj in final_boxes): return False
    return True


def getNeeds(matrix : list[list[int]])-> dict:
    size = len(matrix)
    combined = []
    for i in matrix: combined += i
    needs = {i : size - combined.count(i) for i in range(1, size+1)}
    return needs

def getPerm(needs : dict)-> list:
    item = needs.items()
    sol = list()
    for num, need in item:
        sol.extend([num]*need)
    return permutations(sol)

def getEmptyLoc(matrix: list[list[int]])-> list[tuple[int, int]]:
    size = len(matrix)
    locs = []
    for x in range(size):
        for y in range(size):
            if matrix[x][y] == 0:
                locs.append((x,y))
    return locs
