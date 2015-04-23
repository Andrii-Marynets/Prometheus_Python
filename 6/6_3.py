matrix = [[1,1,1],
          [3,2,3],
          [1,0,1]]

def saddle_point(matrix):
    res = []
    resIndex = []
    for i in matrix:
        if isinstance(i, list):
            res.append(min(i))
        else:
            res.append(min(matrix))
    for i in range(0, len(matrix)):
        if isinstance(matrix[i], list):
            resIndex.append(matrix[i].index(res[i]))
        else:
            resIndex.append(matrix.index(res[i]))
    if resIndex.count(resIndex[0]) == len(resIndex):
        r = res.index(max(res), 0, len(res))
        s = resIndex[0]
        return r, s
    else:
        return False

print saddle_point(matrix)