def detect(mat):
    for j in range(8):
        for i in range(1, 8):

            if mat[j][i][0] != mat[j][i - 1][0] : #if lst[i][j] != lst[i][j + 1]:
                continue

            if i == 7:
                continue

            if mat[j][i][0] == mat[j][i - 1][0] and i == 7:
                continue

            if mat[j][i[0]] == mat[j][i - 1][0] and mat[j][i][0] == mat[j][i + 1][0]:
                print("Line at ", mat[j][i - 1], mat[j][i + 1])

