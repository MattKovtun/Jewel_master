import copy

class SimpleMove:

    def get_move(self, gems, Game):
        moves = []
        coords = []
        for i in range(8):
            level = []
            for j in range(8):
                level.append("__")
            coords.append(level)

        for i in range(8):
            for j in range(8):
                coords[i][j] = ((j * 40) + 5 + 168, (i * 40) + 5 + 49)
        for cell in range(64):
            i = cell // 8
            j = cell - i * 8
            # print()
            #  print(i, j, self.gems[i][j])
            new_mat_lst = copy.deepcopy(gems)

            for op in Game.ops:
                n_i = i + op[0]
                n_j = j + op[1]
                # print(n_i ,n_j)
                if 0 <= n_i <= 7 and 0 <= n_j <= 7:
                    swap = new_mat_lst[i][j]
                    new_mat_lst[i][j] = new_mat_lst[n_i][n_j]
                    new_mat_lst[n_i][n_j] = swap
                    TM = SimpleMove.detect(new_mat_lst)
                    #  print(self.new_mat_lst)
                    if TM[0]:
                        if (TM[0], (n_i, n_j), (i, j)) not in moves:
                            # self.moves.append(((self.i, self.j), (self.n_i, self.n_j)))
                            moves.append((TM[1], (coords[i][j]), (coords[n_i][n_j])))

                    swap = new_mat_lst[n_i][n_j]
                    new_mat_lst[n_i][n_j] = new_mat_lst[i][j]
                    new_mat_lst[i][j] = swap

        moves = sorted(moves, reverse=True, key=lambda x: x[0])
       # print(moves)
        return (moves[0][1], moves[0][2])

    def detect(mat):
        """
        We detect here largest number of gems in row or in column
        """
        # print(len(mat))
        utility = 0

        for j in range(8):
            for i in range(1, 8):
                # if mat[j][i][0] != mat[j][i - 1][0] : #if lst[i][j] != lst[i][j + 1]:
                # continue

                if mat[j][i][0] == mat[j][i - 1][0]:
                    utility += 1

                if mat[j][i][0] != mat[j][i - 1][0]:
                    if utility >= 2:
                        return (True, utility)
                    else:
                        utility = 0

                if i == 7 and utility >= 2:
                    return (True, utility)

                if i == 7:
                    utility = 0
                    continue

        utility = 0
        for j in range(8):
            for i in range(1, 8):

                if mat[i][j][0] == mat[i - 1][j][0]:
                    utility += 1
                    #  print("Line at ", i - 1, j, mat[i - 1][j], mat[i + 1][j])
                if mat[i][j][0] != mat[i - 1][j][0]:
                    if utility >= 2:
                        return (True, utility)
                    else:
                        utility = 0
                if i == 7 and utility >= 2:
                    return (True, utility)

                if i == 7:
                    utility = 0
                    continue

        return (False, 0)



class AdvancedMove:
    def get_move(self, gems, Game):
        moves = []
        coords = []
        for i in range(8):
            level = []
            for j in range(8):
                level.append("__")
            coords.append(level)

        for i in range(8):
            for j in range(8):
                coords[i][j] = ((j * 40) + 5 + 168, (i * 40) + 5 + 49)
        for cell in range(64):
            i = cell // 8
            j = cell - i * 8
            # print()
            #  print(i, j, self.gems[i][j])
            new_mat_lst = copy.deepcopy(gems)

            for op in Game.ops:
                n_i = i + op[0]
                n_j = j + op[1]
                # print(n_i ,n_j)
                if 0 <= n_i <= 7 and 0 <= n_j <= 7:
                    swap = new_mat_lst[i][j]
                    new_mat_lst[i][j] = new_mat_lst[n_i][n_j]
                    new_mat_lst[n_i][n_j] = swap
                    TM = SimpleMove.detect(new_mat_lst)
                    #  print(self.new_mat_lst)
                    if TM[0]:
                        if (TM[0], (n_i, n_j), (i, j)) not in moves:
                            # self.moves.append(((self.i, self.j), (self.n_i, self.n_j)))
                            moves.append((TM[1], (coords[i][j]), (coords[n_i][n_j])))

                    swap = new_mat_lst[n_i][n_j]
                    new_mat_lst[n_i][n_j] = new_mat_lst[i][j]
                    new_mat_lst[i][j] = swap

        moves = sorted(moves, reverse=True, key=lambda x: x[0])
        # print(moves)
        return (moves[0][1], moves[0][2])

    def detect(mat):
        """
        We detect here largest number of gems in row or in column
        """
        # print(len(mat))
        utility = 0

        for j in range(8):
            for i in range(2, 8):
                # if mat[j][i][0] != mat[j][i - 1][0] : #if lst[i][j] != lst[i][j + 1]:
                # continue

                if mat[j][i][0] == mat[j][i - 1][0] == mat[j][i - 2][0]:
                    utility += 1
                    if 1 <= j <= 6:
                        if mat[j - 1][i][0] == mat[j + 1][i][0] == mat[j][i][0] or mat[j - 1][i][0] == mat[j + 1][i][0] == mat[j][i - 2][0]:
                            print("SNOW")
                            utility += 2

                if mat[j][i][0] != mat[j][i - 1][0]:
                    if utility >= 1:
                        return (True, utility)
                    else:
                        utility = 0

                if i == 7 and utility >= 1:
                    return (True, utility)

                if i == 7:
                    utility = 0
                    continue

        utility = 0
        for j in range(8):
            for i in range(2, 8):

                if mat[i][j][0] == mat[i - 1][j][0] == mat[i - 2][j][0]: #######################################################################
                    utility += 1
                    if 1 <= j <= 6:
                        if mat[i][j][0] == mat[i][j - 1][0] == mat[i][j - 2] or mat[i - 2][j][0] == mat[i][j - 1][0] == mat[i][j - 2]:
                            print("Snow found ")
                            utility += 2
                    #  print("Line at ", i - 1, j, mat[i - 1][j], mat[i + 1][j])
                if mat[i][j][0] != mat[i - 1][j][0]:
                    if utility >= 1:
                        return (True, utility)
                    else:
                        utility = 0
                if i == 7 and utility >= 1:
                    return (True, utility)

                if i == 7:
                    utility = 0
                    continue

        return (False, 0)