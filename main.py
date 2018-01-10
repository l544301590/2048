import random
import pygame.examples.cursors


class Grid:
    def __init__(self):
        # 0 stand for nothing
        # i stand for 2^i. e.g. 3 stand for 8
        self.data = [
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0]
        ]
        self.stage = 0
        self.random = [
            [1],
            [1, 1, 1, 2],
            [1, 1, 1, 1, 2, 2, 3],
            [1, 1, 1, 1, 1, 2, 2, 2, 3, 3, 4]
        ]

    def next(self):
        # random position
        zero_indexes = []
        for i in range(4):
            for j in range(4):
                if self.data[i][j] == 0:
                    zero_indexes.append((i, j))
        i, j = random.sample(zero_indexes, 1)
        # random value
        self.data[i][j] = random.sample(self.random[self.stage], 1)

    def up(self):
        for j in range(4):
            temp, res = [], []
            # extract one col into temp
            for i in range(4):
                if self.data[i][j] != 0:
                    temp.append(self.data[i][j])
            # combine the same two
            for k in range(len(temp)-1):
                if temp[k] == temp[k+1] and temp[k] != 0:
                    res.append(temp[k]+1)
                    k += 1
            # modify the origin data
            for l in range(len(res)):
                self.data[l][j] = res[l]
            while l < 4:
                self.data[l][j] = 0
                l += 1

    def down(self):
        for j in range(4):
            temp, res = [], []
            # extract one col into temp
            for i in range(4):
                if self.data[i][j] != 0:
                    temp.append(self.data[i][j])
            # combine the same two
            for k in range(len(temp)-1):
                if temp[k] == temp[k+1] and temp[k] != 0:
                    res.append(temp[k]+1)
                    k += 1
            # modify the origin data
            for l in range(3, len(res)-1, -1):
                self.data[l][j] = res[l]
            while l >= 0:
                self.data[l][j] = 0
                l -= 1

    def left(self):
        for i in range(4):
            temp, res = [], []
            # extract one row into temp
            for j in range(4):
                if self.data[i][j] != 0:
                    temp.append(self.data[i][j])
            # combine the same two
            for k in range(len(temp)-1):
                if temp[k] == temp[k+1] and temp[k] != 0:
                    res.append(temp[k]+1)
                    k += 1
            # modify the origin data
            for l in range(len(res)):
                self.data[i][l] = res[l]
            while l < 4:
                self.data[i][l] = 0
                l += 1

    def right(self):
        for i in range(4):
            temp, res = [], []
            # extract one row into temp
            for j in range(4):
                if self.data[i][j] != 0:
                    temp.append(self.data[i][j])
            # combine the same two
            for k in range(len(temp)-1):
                if temp[k] == temp[k+1] and temp[k] != 0:
                    res.append(temp[k]+1)
                    k += 1
            # modify the origin data
            for l in range(3, len(res)-1, -1):
                self.data[i][l] = res[l]
            while l >= 0:
                self.data[i][l] = 0
                l -= 1

    def show_in_cmd(self):
        for i in range(4):
            for j in range(4):
                print(2**self.data[i][j], sep=" ")
            print()


if __name__ == '__main__':
    pygame.