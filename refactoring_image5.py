import pygame
from pygame.draw import *

pygame.init()
FPS = 30
a = 1300  # width of the screen
screen = pygame.display.set_mode((a, 850))

# color palette
c_mntn1 = (160, 73, 58)  # mntn = mountain
c_mntn2 = (44, 18, 37)
c_mntn3 = (239, 156, 73)
c_sky1 = (248, 214, 169)
c_sky2 = (248, 214, 198)
c_sky3 = (248, 214, 157)
c_sky4 = (172, 136, 148)
c_sun = (250, 237, 86)
bird_color = (62, 34, 16)

# background
polygon(screen, c_sky1, [(0, 0), (a, 0), (a, 180), (0, 170)])
polygon(screen, c_sky2, [(0, 170), (a, 180), (a, 360), (0, 350)])
polygon(screen, c_sky3, [(0, 340), (a, 350), (a, 530), (0, 520)])
polygon(screen, c_sky4, [(0, 520), (a, 530), (a, 1000), (0, 1000)])
sun_size = 60  # sun radius
circle(screen, c_sun, (550, 180), sun_size)

# first mountain
cliff = [(10 + i * 8, 330 - i ** (3 / 2)) for i in range(33)]
polygon(screen, c_mntn3,
        [(0, 390), *cliff, (266, 149), (316, 169), (336, 199), (470, 320),
         (560, 312), (600, 340)])
cliff1 = [(780 + i * 9, 255 - i ** (8 / 5)) for i in range(20)]
cliff2 = [(951 + i * 7, 143.82535239422486 + i ** 2) for i in range(6)]
cliff3 = [(1086 + i * 11, 200 + i ** 2) for i in range(7)]
polygon(screen, c_mntn3,
        [(600, 340), (680, 270), (750, 280), (780, 255), *cliff1, *cliff2,
         (986, 168.8), (1036, 208), (1086, 200), *cliff3, (1152, 236),
         (1202, 216), (a, 281.6)])

# second mountain
polygon(screen, c_mntn1, [(0, 520), (0, 405), (20, 405), (45, 425), (100, 520)])
ellipse(screen, c_mntn1, (26, 335, 170, 400))
polygon(screen, c_mntn1, [(170, 525), (250, 410), (420, 525)])
polygon(screen, c_mntn1,
        [(330, 525), (430, 370), (540, 400), (610, 460), (680, 525)])
polygon(screen, c_mntn1, [(580, 450), (690, 440), (750, 525), (580, 525)])
ellipse_1 = pygame.Surface((800, 800), pygame.SRCALPHA)
ellipse(ellipse_1, c_mntn1, (500, 100, 300, 150))
ellipse_1 = pygame.transform.rotate(ellipse_1, 45)
screen.blit(ellipse_1, (190, 225))
clx4 = 875  # coords for cliff4
cly4 = 460
cliff4 = [((clx4 + 3 * i), cly4 - 100 * i ** (-0.2)) for i in range(1, 40)]
polygon(screen, c_mntn1,
        [(clx4 - 100, cly4 + 100), *cliff4, (clx4 + 200, cly4 + 100)])
polygon(screen, c_mntn1,
        [(clx4 + 200, cly4 + 100), (992, 411.94), (1060, 360), (1110, 390),
         (1160, 350), (1240, 380), (a, 300), (a, 500)])
polygon(screen, c_mntn1, [(a, 530), (a, 400), (a - 200, 530)])
polygon(screen, c_sky4, [(0, 520), (1200, 530), (1200, 1000), (0, 1000)])
polygon(screen, c_mntn1, [(0, 520), (0, 405), (20, 405), (45, 425), (100, 520)])

# third mountain
polygon(screen, c_mntn2,
        [(0, 1000), (0, 400), (150, 440), (280, 650), (360, 820)])
clx5 = 330
cly5 = 880
cliff5 = [((clx5 + 3 * i), cly5 - 100 * i ** (-0.2)) for i in range(1, 100)]
polygon(screen, c_mntn2,
        [(clx5 - 100, cly5 + 100), *cliff5, (clx5 + 200, cly5 + 100)])
polygon(screen, c_mntn2, [(530, 900), (800, 700), (860, 725), (860, 900)])
clx6 = 849
cly6 = 820
cliff6 = [((clx6 + 3 * i), cly6 - 100 * i ** (-0.05)) for i in range(1, 20)]
polygon(screen, c_mntn2, [(clx6, cly6 + 200), *cliff6, (clx6 + 60, cly6 + 200)])
clx7 = 906
cly7 = 733.7
cliff7 = [(clx7 + i * 9, cly7 - i ** (3 / 2)) for i in range(33)]
polygon(screen, c_mntn2, [(clx6 + 60, cly6 + 200), *cliff7, (1300, 800)])
ellipse_2 = pygame.Surface((800, 800), pygame.SRCALPHA)
ellipse(ellipse_2, c_mntn2, (500, 100, 300, 150))
ellipse_2 = pygame.transform.rotate(ellipse_2, 45)
screen.blit(ellipse_2, (660, 380))
polygon(screen, c_mntn2, [(a, a), (a, 600), (a - 300, 800)])


def bird(x, y, size, color):
    '''
      Функция рисует птицу на экране.
      x, y - координаты левого верхнего угла изображения
      size - относительный размер изображения
      color - цвет, заданный в формате, подходящем для pygame.Color
    '''
    bird = pygame.Surface((200 * size, 200 * size), pygame.SRCALPHA)
    subbird1 = pygame.Surface((15 * size + 1, 50 * size + 1), pygame.SRCALPHA)
    subbird2 = pygame.Surface((50 * size + 1, 15 * size + 1), pygame.SRCALPHA)
    ellipse(subbird1, color,
            (size * 15 * 7 / 15, size * 50 * 1 / 10, 15 * size, 50 * size))
    ellipse(subbird2, color,
            (size * 50 * 1 / 25, size * 15 * 2 / 15, 50 * size, 15 * size))
    subbird1 = pygame.transform.rotate(subbird1, -60)
    subbird2 = pygame.transform.rotate(subbird2, -30)
    bird.blit(subbird1, (50 * size - 12 * size, size * 27 - 25 * size))
    bird.blit(subbird2, (0, (50 - 15 - 25) * size))
    screen.blit(bird, (x, y))


bird_xy = [(450, 270, 1), (553, 280, 1), (550, 326, 1), (460, 340, 1),
           (760, 495, 1.2), (840, 570, 1), (1000, 550, 0.9), (930, 600, 1.4)]
for x, y, size in bird_xy:
    bird(x, y, size, bird_color)

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
