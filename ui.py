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
        pos = self.rect[0]
        if pos == self.des_pos:  # achieve destination
            self.speed = 0, 0
            return
        pos[0] += self.speed[0]
        pos[1] += self.speed[1]
        self.rect[0] = pos


if __name__ == '__main__':
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_A, SCREEN_A))
    main_panel = pygame.Surface((M_PANEL_A, M_PANEL_A))
    main_panel.fill(M_PANEL_COLOR)

    for i in range(len(BLOCK_REGIONS)):
        for j in range(len(BLOCK_REGIONS[0])):
            pygame.draw.rect(main_panel, BLOCK_COLORS[0][0], BLOCK_REGIONS[i][j])

    blocks = pygame.sprite.Group()
    test_block = Block(1, BLOCK_REGIONS[0][0])
    blocks.add(test_block)

    while True:
        keys = pygame.key.get_pressed()
        if keys[KEYDOWN]:
            print(1)
        for event in pygame.event.get():
            if event.type == QUIT:
                exit()


        blocks.update()
        blocks.draw(main_panel)
        screen.blit(main_panel, (M_PANEL_MARGIN, M_PANEL_MARGIN))
        pygame.display.flip()

