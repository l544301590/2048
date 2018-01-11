import pygame
from const import *
from pygame.locals import *
import random
import logging


class Grid(pygame.sprite.Group):
    """container class containing blocks(sprites)

    self.data {4*4 list}:
        0 stand for nothing
        i stand for 2^i. (e.g. 3 stand for 8)
    self.spritedict {dict}:
        inherit from pygame.sprite.Group
        save blocks
    """
    def __init__(self):
        pygame.sprite.Group.__init__(self)
        # 0 stand for nothing
        # i stand for 2^i. e.g. 3 stand for 8
        self.data = [  # logically
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0]
        ]
        self.spritedict = {}  # graphically
        self.stage = 0
        self.random = [
            [1],
            [1, 1, 1, 2],
            [1, 1, 1, 1, 2, 2, 3],
            [1, 1, 1, 1, 1, 2, 2, 2, 3, 3, 4]
        ]

    def get_block(self, x, y):
        for block in self.spritedict:
            if block.gx == x and block.gy == y:
                return block
        msg = "Expected coordinate is (" + str(x) + ", " + str(y) + ") but the block is not found"
        logging.warning(msg)

    def gen_next(self):
        # random position
        zero_indexes = []
        for i in range(4):
            for j in range(4):
                if self.data[i][j] == 0:
                    zero_indexes.append((i, j))
        i, j = random.sample(zero_indexes, 1)[0]
        # random value
        ran_val = random.sample(self.random[self.stage], 1)[0]
        self.data[i][j] = ran_val
        self.add(Block(ran_val, i, j))
        msg = "New block generated, (" + str(i) + ", " + str(j) + "), " + str(2**ran_val)
        logging.info(msg)

    def up(self):
        # combine from top to bottom
        for j in range(4):
            tmp_i = 0
            for i in range(4):
                if self.data[i][j] == self.data[tmp_i][j] and self.data[i][j] != 0 and tmp_i != i:
                    block1, block2 = self.get_block(tmp_i, j), self.get_block(i, j)

                    block1.mod_num(self.data[tmp_i][j]+1)
                    block2.move_faded(tmp_i, j)

                    self.data[tmp_i][j] += 1
                    self.data[i][j] = 0

                if self.data[i][j] != 0:
                    tmp_i = i

        # draw close from top to bottom
        for j in range(4):
            tmp_i = 0
            for i in range(4):
                if self.data[i][j] != 0:
                    block = self.get_block(i, j)

                    block.move_to(tmp_i, j)

                    if tmp_i != i:
                        self.data[tmp_i][j] = self.data[i][j]
                        self.data[i][j] = 0

                    tmp_i += 1

    def down(self):
        # combine from bottom to top
        for j in range(4):
            tmp_i = 3
            for i in range(3, -1, -1):
                if self.data[i][j] == self.data[tmp_i][j] and self.data[i][j] != 0 and tmp_i != i:
                    block1, block2 = self.get_block(tmp_i, j), self.get_block(i, j)

                    block1.mod_num(self.data[tmp_i][j] + 1)
                    block2.move_faded(tmp_i, j)

                    self.data[tmp_i][j] += 1
                    self.data[i][j] = 0

                if self.data[i][j] != 0:
                    tmp_i = i

        # draw close from bottom to top
        for j in range(4):
            tmp_i = 3
            for i in range(3, -1, -1):
                if self.data[i][j] != 0:
                    block = self.get_block(i, j)

                    block.move_to(tmp_i, j)
                    if tmp_i != i:
                        self.data[tmp_i][j] = self.data[i][j]
                        self.data[i][j] = 0

                    tmp_i -= 1

    def left(self):
        # combine from left to right
        for i in range(4):
            tmp_j = 0
            for j in range(4):
                if self.data[i][j] == self.data[i][tmp_j] and self.data[i][j] != 0 and tmp_j != j:
                    block1, block2 = self.get_block(i, tmp_j), self.get_block(i, j)

                    block1.mod_num(self.data[i][tmp_j] + 1)
                    block2.move_faded(i, tmp_j)

                    self.data[i][tmp_j] += 1
                    self.data[i][j] = 0

                if self.data[i][j] != 0:
                    tmp_j = j

        # draw close from left to right
        for i in range(4):
            tmp_j = 0
            for j in range(4):
                if self.data[i][j] != 0:
                    block = self.get_block(i, j)

                    block.move_to(i, tmp_j)
                    if tmp_j != j:
                        self.data[i][tmp_j] = self.data[i][j]
                        self.data[i][j] = 0

                    tmp_j += 1

    def right(self):
        # combine from right to left
        for i in range(4):
            tmp_j = 3
            for j in range(3, -1, -1):
                if self.data[i][j] == self.data[i][tmp_j] and self.data[i][j] != 0 and tmp_j != j:
                    block1, block2 = self.get_block(i, tmp_j), self.get_block(i, j)

                    block1.mod_num(self.data[i][tmp_j] + 1)
                    block2.move_faded(i, tmp_j)

                    self.data[i][tmp_j] += 1
                    self.data[i][j] = 0

                if self.data[i][j] != 0:
                    tmp_j = j

        # draw close from right to left
        for i in range(4):
            tmp_j = 3
            for j in range(3, -1, -1):
                if self.data[i][j] != 0:
                    block = self.get_block(i, j)

                    block.move_to(i, tmp_j)
                    if tmp_j != j:
                        self.data[i][tmp_j] = self.data[i][j]
                        self.data[i][j] = 0

                    tmp_j -= 1

    def show_in_cmd(self):
        for i in range(4):
            for j in range(4):
                print(2**self.data[i][j], sep=" ")
            print()


class Block(pygame.sprite.Sprite):
    def __init__(self, ind, i, j):
        pygame.sprite.Sprite.__init__(self)

        # logically
        self.gx, self.gy = i, j

        # graphically
        font = pygame.font.SysFont("freesansbold.ttf", 50)
        block_surface = pygame.Surface((BLOCK_A, BLOCK_A))
        block_surface.fill(BLOCK_PROP[ind][0])
        text_surface = font.render(str(2 ** ind), True, BLOCK_PROP[ind][1])
        block_surface.blit(text_surface, (0, 0))

        self.image = block_surface
        self.rect = BLOCK_REGIONS[i][j]
        self.des_pos = BLOCK_REGIONS[i][j][0]
        self.speed = (0, 0)

        self.alpha = 255
        self.alpha_rate = 0

    def mod_num(self, ind):
        # graphically
        font = pygame.font.SysFont("freesansbold.ttf", 50)
        block_surface = pygame.Surface((BLOCK_A, BLOCK_A))
        block_surface.fill(BLOCK_PROP[ind][0])
        text_surface = font.render(str(2 ** ind), True, BLOCK_PROP[ind][1])
        block_surface.blit(text_surface, (0, 0))

        self.image = block_surface

    def move_to(self, i, j):
        if self.gx == i and self.gy == j:
            return
        self.des_pos = BLOCK_REGIONS[i][j][0]
        vy = (i - self.gx) * 2
        vx = (j - self.gy) * 2
        self.speed = (vx, vy)

        self.gx, self.gy = i, j

    def move_faded(self, i, j):
        self.move_to(i, j)
        self.alpha_rate = -50

    def update(self):

        assert self.speed[0]*self.speed[1] == 0, 'vx = '+str(self.speed[0])+', vy = '+str(self.speed[1])
        assert self.image, 'Block with no image!'

        cur_pos = self.rect[0]

        # supervise if destination achieved
        achieved = False
        if self.speed[0] < 0:  # head left
            if cur_pos[0] <= self.des_pos[0]:
                achieved = True
        if self.speed[0] > 0:  # head right
            if cur_pos[0] >= self.des_pos[0]:
                achieved = True
        if self.speed[1] > 0:  # head down
            if cur_pos[1] >= self.des_pos[1]:
                achieved = True
        if self.speed[1] < 0:  # head up
            if cur_pos[1] <= self.des_pos[1]:
                achieved = True

        if achieved:
            self.speed = (0, 0)
            self.rect = self.des_pos, self.rect[1]
            if self.alpha < 1:
                self.kill()
                return

        res_pos = cur_pos[0] + self.speed[0], cur_pos[1] + self.speed[1]

        self.rect = res_pos, self.rect[1]
        self.alpha += self.alpha_rate
        self.image.set_alpha(self.alpha)


if __name__ == '__main__':
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_A, SCREEN_A))
    main_panel = pygame.Surface((M_PANEL_A, M_PANEL_A))
    main_panel.fill(M_PANEL_COLOR)

    for i in range(len(BLOCK_REGIONS)):
        for j in range(len(BLOCK_REGIONS[0])):
            pygame.draw.rect(main_panel, BLOCK_PROP[0][0], BLOCK_REGIONS[i][j])

    main_bg = main_panel.copy()
    grid = Grid()
    grid.gen_next()
    grid.update()
    grid.draw(main_panel)

    while True:
        # clear all
        main_panel.blit(main_bg, (0, 0))

        # handle events
        for event in pygame.event.get():
            if event.type == QUIT:
                exit()
            if event.type == KEYDOWN:
                if event.key == K_UP:
                    grid.up()
                elif event.key == K_DOWN:
                    grid.down()
                elif event.key == K_LEFT:
                    grid.left()
                elif event.key == K_RIGHT:
                    grid.right()
                else:
                    break
                grid.gen_next()

        # modify the reference variable
        grid.update()
        grid.draw(main_panel)

        # modify the pixels
        screen.blit(main_panel, (M_PANEL_MARGIN, M_PANEL_MARGIN))

        # render all
        pygame.display.flip()

