def solution(matrix):
    def map(mat):
        return "\n".join([" ".join([str(ele) for ele in sub]) for sub in mat])
    def valid(mat, elmnt):
        x, y = elmnt
        vectors = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        valmovcor=[]
        for i, j in vectors:
            if  0<=x+i<len(mat) and 0<=y+j<len(mat[0]):
               if mat[x+i][y+j] == 0:
                    valmovcor.append([x+i,y+j])
        return valmovcor
    def discal(mat):
        calculated=[[False for el in row] for row in mat]
        distance = [[None for el in row] for row in mat]
        calculated[0][0]=True
        distance[0][0]=0
        start=[0,0]
        finish=[len(mat)-1,len(mat[0])-1]
        unfinished = True
        lastcalcs = {1:[start]}
        step=1
        while True:
            step+=1
            stepchngs=[]
            for i in lastcalcs[step-1]:
                v = valid(mat, i)
                for j in v:
                    if calculated[j[0]][j[1]]:
                        continue
                    distance[j[0]][j[1]] = step
                    calculated[j[0]][j[1]] = True
                    stepchngs.append(j)
            if distance[finish[0]][finish[1]] != None:
                break
            if stepchngs == []:
                break
            lastcalcs[step]=stepchngs
        return distance[finish[0]][finish[1]]
    diswalset=[]
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 1:
                matrix[i][j] = 0
                diswalset.append(discal(matrix))
                matrix[i][j] = 1
    return min([i for i in diswalset if i is not None])
