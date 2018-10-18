import sys

inputs = [10,4,5,20,2,50]
M = [[0 for x in range(6)] for y in range(6)]

for passing in range(1,6):
    for i in range(1, 6 - passing):
        j = i + passing
        M[i][j] = sys.maxsize
        for k in range(i, j):
            M[i][j] = min(M[i][j],
                          M[i][k] + M[k + 1][j] + inputs[i - 1] * inputs[k] * inputs[j])

for x in range(1,6):
    for y in range(1,6):
        print(" {0} ".format(M[x][y]),end=' ')
    print()
