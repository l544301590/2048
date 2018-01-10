import pygame
from const import *
from pygame.locals import *


class Block(pygame.sprite.Sprite):
    def __init__(self, ind, rect):
        pygame.sprite.Sprite.__init__(self)

        font = pygame.font.SysFont("freesansbold.ttf", 50)
        block_surface = pygame.Surface(rect[1])
        block_surface.fill(BLOCK_COLORS[ind][0])
        text_surface = font.render(str(2 ** ind), True, BLOCK_COLORS[ind][1])
        block_surface.blit(text_surface, (0, 0))

        self.image = block_surface
        self.rect = rect
        self.des_pos = rect[0]
        self.speed = 0, 0

    def move(self, des_pos):
        # prepare to move
        self.des_pos = des_pos
        org_pos = self.rect[0]
        dx = des_pos[0] - org_pos[0]
        dy = des_pos[1] - org_pos[1]
        vx = dx*5 / abs(dx) if dx != 0 else 0
        vy = dy*5 / abs(dy) if dy != 0 else 0
        self.speed = (vx, vy)

    def update(self):

        assert self.speed[0]*self.speed[1] == 0, 'Wrong direction(speed)!'
        assert self.image, 'Block with no image!'

        cur_pos = self.rect[0]

        # supervise if destination achieved
        if self.speed[0] < 0:  # head left
            if cur_pos[0] <= self.des_pos[0]:
                self.speed = 0, 0
                return
        if self.speed[0] > 0:  # head right
            if cur_pos[0] >= self.des_pos[0]:
                self.speed = 0, 0
                return
        if self.speed[1] > 0:
            if cur_pos[1] >= self.des_pos[1]:
                self.speed = 0, 0
                return
        if self.speed[1] < 0:
            if cur_pos[1] <= self.des_pos[1]:
                self.speed = 0, 0
                return

        res_pos = cur_pos[0] + self.speed[0], cur_pos[1] + self.speed[1]

        self.rect = res_pos, self.rect[1]


if __name__ == '__main__':
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_A, SCREEN_A))
    main_panel = pygame.Surface((M_PANEL_A, M_PANEL_A))
    main_panel.fill(M_PANEL_COLOR)

    for i in range(len(BLOCK_REGIONS)):
        for j in range(len(BLOCK_REGIONS[0])):
            pygame.draw.rect(main_panel, BLOCK_COLORS[0][0], BLOCK_REGIONS[i][j])

    main_bg = main_panel.copy()
    blocks = pygame.sprite.Group()
    test_block = Block(1, BLOCK_REGIONS[0][0])
    blocks.add(test_block)

    while True:
        # clear all
        main_panel.blit(main_bg, (0, 0))

        # handle events
        for event in pygame.event.get():
            if event.type == QUIT:
                exit()
            if event.type == KEYDOWN:
                if event.key == K_DOWN:
                    # TODO calculate the destination
                    test_block.move(BLOCK_REGIONS[1][0][0])

        # modify the reference variable
        blocks.update()
        blocks.draw(main_panel)

        # modify the pixels
        screen.blit(main_panel, (M_PANEL_MARGIN, M_PANEL_MARGIN))

        # render all
        pygame.display.flip()

